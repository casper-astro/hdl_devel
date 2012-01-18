#==============================================================================#
#                                                                              # 
#      Bit Shift python testing                                                # 
#                                                                              # 
#      Module name: test_bit_shift                                             # 
#      Desc: The MyHDL code that test the bit_shift module using co-simulation # 
#      Date: Nov 2011                                                          # 
#      Developer: Wesley New                                                   # 
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
    '-o {mod_path}bit_shift_tb ' + \
    '-DMYHDL ' + \
    '-DARCHITECTURE=\\"{architecture}\\" ' + \
    '-DDATA_WIDTH={data_width} ' + \
    '-DSHIFT_DIRECTION={shift_direction} ' + \
    '-DNUMBER_BITS={number_bits} ' + \
    '-DWRAP={wrap} ' + \
    '{mod_path}bit_shift_tb.v ' + \
    '{mod_path}bit_shift.v'

VVP_CMD = "vvp -m {vpi_path} {mod_path}bit_shift_tb"

#================================
# Call to the Bit Shift Wrapper
#================================
def bit_shift_wrapper(clk, data_in, data_out, 
            architecture, data_width, shift_direction, number_bits, wrap):
    simcmd = ICARUS_CMD.format(mod_path=MOD_PATH,
                               architecture=architecture,
                               data_width=data_width,
                               shift_direction=shift_direction,
                               number_bits=number_bits,
                               wrap=wrap)
    proc = subprocess.Popen(shlex.split(simcmd))
    if proc.wait(): # wait for Icarus compiler to finish
        raise RuntimeError('Icarus compile failed (see above)!')
    return Cosimulation(VVP_CMD.format(mod_path=MOD_PATH, vpi_path=VPI_PATH), 
                        clk=clk, data_in=data_in, data_out=data_out)


def clean_up():
    os.remove('{mod_path}bit_shift_tb'.format(mod_path=MOD_PATH))


def generate_cosim(architecture,
                   data_width,
                   shift_direction,
                   number_bits,
                   wrap,
                   runtime=1024):

    clk      = Signal(intbv(0))
    data_in  = Signal(intbv(0))
    data_out = Signal(intbv(0))

    dut = bit_shift_wrapper(clk,
                    data_in, 
                    data_out, 
                    architecture,
                    data_width,
                    shift_direction,
                    number_bits,
                    wrap)

    output = []

    def test(clk, data_in, data_out):

        # set initial values
        @instance
        def initial():
            clk.next = intbv(0)
            data_in.next = intbv(682)
            yield delay(0)

        # drive the clock
        @always(delay(1))
        def drive_clk():
            clk.next = not clk

        # monitor bit_shift output
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

    check =  test(clk, data_in, data_out)
    sim = Simulation(dut, check)
    sim.run(quiet=True)

    clean_up()
    return output


# TODO: create a set of tests for the bit_shift block
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


#def test_bitwidths():
#    data_width = 16
#    shift_direction = 0
#    number_bits = 1
#    wrap = 0
#    output = generate_cosim("BEHAVIORAL",
#                            data_width,
#			    shift_direction, 
#                            number_bits,
#                            wrap)
#    latency = output.index(count_from+step) - 1
#    expected = [0]*latency + range(count_from, count_to, step)
#    yield check_output_latency, latency
#    yield check_full_range, output, expected
#    yield check_roll_over, output, count_to, count_from


if __name__ == "__main__":
    main()
