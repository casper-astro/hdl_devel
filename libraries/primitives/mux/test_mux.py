import os, shlex, subprocess
from pkg_resources import resource_filename
from myhdl import *


VPI_PATH = os.path.join(os.getenv('MYHDL'))
MOD_PATH = resource_filename(__name__, '') + os.path.sep


ICARUS_CMD = 'iverilog ' + \
    '-o {mod_path}counter_tb ' + \
    '-DMYHDL ' + \
    '-DARCHITECTURE=\\"{architecture}\\" ' + \
    '-DSELECT_LINES={select_lines} ' + \
    '{mod_path}mux_tb.v ' + \
    '{mod_path}mux.v'

VVP_CMD = "vvp -m {vpi_path} {mod_path}counter_tb"


def mux(select, data_in, data_out, 
            architecture, select_lines):
    simcmd = ICARUS_CMD.format(mod_path=MOD_PATH,
                               architecture=architecture,
                               select_lines=select_lines)
    proc = subprocess.Popen(shlex.split(simcmd))
    if proc.wait(): # wait for Icarus compiler to finish
        raise RuntimeError('Icarus compile failed (see above)!')
    return Cosimulation(VVP_CMD.format(mod_path=MOD_PATH, vpi_path=VPI_PATH), 
                        select=select, data_in=data_in, data_out=data_out)


def clean_up():
    os.remove('{mod_path}mux_tb'.format(mod_path=MOD_PATH))


def generate_cosim(architecture,
                   select_lines,
                   runtime=1024):

    select   = Signal(intbv(0))
    data_in  = Signal(intbv(0))
    data_out = Signal(intbv(0))

    dut = mux(select,
              data_in, 
              data_out, 
              architecture,
              select_lines)

    output = []

    def test(select, data_in, data_out):

        # set initial values
        @instance
        def initial():
            data_in.next = intbv(682)
            select.next = intbv(1)
            yield delay(0)

        # drive the clock
        @always(delay(10))
        def inc_select():
            select.next = select + 1

        # monitor data_out
        @instance
        def monitor():
            while True:
                yield clk.posedge
                output.append(int(data_out))

        # kill the simulation after a while
        @instance
        def stop_sim():
            yield(delay(runtime))
            raise StopSimulation

        return initial, drive_clk, monitor, stop_sim

    check =  test(select, data_in, data_out)
    sim = Simulation(dut, check)
    sim.run(quiet=True)

    clean_up()
    return output

#
#def check_output_latency(latency):
#    """ Check output latency is within specification """
#    assert latency <= 3
#
#
#def check_full_range(output, expected):
#    """ Check full output range for correctness """
#    assert output[:len(expected)] == expected
# 
#
#def check_roll_over(output, count_to, count_from):
#    """ Check roll-over at COUNT_TO """
#    last = output.index(count_to)
#    assert output[last+1] == count_from
#
#
#def test_bitwidths():
#    step = 1
#    count_from = 0
#    for bitwidth in range(2, 12):
#        count_to = 2**bitwidth-1
#        output = generate_cosim("BEHAVIORAL",
#                                select_lines)
#        latency = output.index(count_from+step) - 1
#        expected = [0]*latency + range(count_from, count_to, step)
#        yield check_output_latency, latency
#        yield check_full_range, output, expected
#        yield check_roll_over, output, count_to, count_from
#

if __name__ == "__main__":
    generate_cosim("BEHAVIOURAL", 4)
    #main()
