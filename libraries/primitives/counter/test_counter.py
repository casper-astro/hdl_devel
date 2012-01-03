#==============================================================================#
#                                                                              # 
#      Counter python testing                                                  # 
#                                                                              # 
#      Module name: test_counter                                               # 
#      Desc: The MyHDL code that test the counter module using co-simulation   # 
#      Date: Oct 2011                                                          # 
#      Developer: Rurik Primiani & Wesley New                                  # 
#      Licence: GNU General Public License ver 3                               # 
#      Notes:                                                                  # 
#                                                                              # 
#==============================================================================#

import os, shlex, subprocess
from pkg_resources import resource_filename
from myhdl import *

#============================
# Paths to Co-sim and MyHDL
#============================
VPI_PATH = os.path.join(os.getenv('MYHDL'))
MOD_PATH = resource_filename(__name__, '') + os.path.sep

#========================
# Builds Icarus Command
#========================
ICARUS_CMD = 'iverilog ' + \
    '-o {mod_path}counter_tb ' + \
    '-DMYHDL ' + \
    '-DARCHITECTURE=\\"{architecture}\\" ' + \
    '-DDATA_WIDTH={data_width} ' + \
    '-DCOUNT_FROM={count_from} ' + \
    '-DCOUNT_TO={count_to} ' + \
    '-DSTEP={step} ' + \
    '{mod_path}counter_tb.v ' + \
    '{mod_path}counter.v'

VVP_CMD = "vvp -m {vpi_path} {mod_path}counter_tb"

#=============================
# Call to the Counter Wrapper
#=============================
def counter_wrapper(clk, en, rst, out, 
            architecture, data_width, count_from, count_to, step):
    simcmd = ICARUS_CMD.format(mod_path=MOD_PATH,
                               architecture=architecture,
                               data_width=data_width,
                               count_from=count_from,
                               count_to=count_to,
                               step=step)
    proc = subprocess.Popen(shlex.split(simcmd))
    if proc.wait(): # wait for Icarus compiler to finish
        raise RuntimeError('Icarus compile failed (see above)!')
    return Cosimulation(VVP_CMD.format(mod_path=MOD_PATH, vpi_path=VPI_PATH), 
                        clk=clk, en=en, rst=rst, out=out)


def clean_up():
    os.remove('{mod_path}counter_tb'.format(mod_path=MOD_PATH))


def generate_cosim(architecture,
                   data_width,
                   count_from,
                   count_to,
                   step,
                   runtime=1024):

    clk = Signal(intbv(0))
    en = Signal(intbv(0))
    rst = Signal(intbv(0))
    out = Signal(intbv(0))

    dut = counter_wrapper(clk,
                  en, 
                  rst,
                  out, 
                  architecture,
                  data_width,
                  count_from,
                  count_to,
                  step)

    output = []

    def test(clk, en, rst, out):

        # set initial values
        @instance
        def initial():
            rst.next = intbv(0)
            en.next = intbv(1)
            yield delay(0)

        # drive the clock
        @always(delay(1))
        def drive_clk():
            clk.next = not clk

        # monitor counter output
        @instance
        def monitor():
            while True:
                yield clk.posedge
                output.append(int(out))

        # kill the simulation after a while
        @instance
        def stop_sim():
            yield(delay(runtime))
            raise StopSimulation

        return initial, drive_clk, monitor, stop_sim

    check =  test(clk, en, rst, out)
    sim = Simulation(dut, check)
    sim.run(quiet=True)

    clean_up()
    return output


def check_output_latency(latency):
    """ Check output latency is within specification """
    assert latency <= 3


def check_full_range(output, expected):
    """ Check full output range for correctness """
    assert output[:len(expected)] == expected
 

def check_roll_over(output, count_to, count_from):
    """ Check roll-over at COUNT_TO """
    last = output.index(count_to)
    assert output[last+1] == count_from


def test_bitwidths():
    step = 1
    count_from = 0
    for bitwidth in range(2, 12):
        count_to = 2**bitwidth-1
        output = generate_cosim("BEHAVIORAL",
                                bitwidth, 
                                count_from,
                                count_to,
                                step,
                                count_to*4+4)
        latency = output.index(count_from+step) - 1
        expected = [0]*latency + range(count_from, count_to, step)
        yield check_output_latency, latency
        yield check_full_range, output, expected
        yield check_roll_over, output, count_to, count_from


if __name__ == "__main__":
    main()
