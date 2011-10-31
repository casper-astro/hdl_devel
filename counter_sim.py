import shlex, subprocess
from unittest import TestCase, main
from myhdl import *


cmd = 'iverilog -o counter_tb ' + \
    '-DMYHDL ' + \
    '-DARCHITECTURE=\\"{architecture}\\" ' + \
    '-DDATA_WIDTH={data_width} ' + \
    '-DCOUNT_FROM={count_from} ' + \
    '-DCOUNT_TO={count_to} ' + \
    '-DSTEP={step} ' + \
    'counter_tb.v' 


def counter(clk, en, rst, out, 
            architecture, data_width, count_from, count_to, step):
    simcmd = cmd.format(architecture=architecture,
                        data_width=data_width,
                        count_from=count_from,
                        count_to=count_to,
                        step=step)
    subprocess.Popen(shlex.split(simcmd))
    return Cosimulation("vvp -m ./myhdl.vpi counter_tb", clk=clk, en=en, rst=rst, out=out)


class TestCounterProperties(TestCase):

    def test_output(self):
        """ Check that the counter increments """
        architecture = 'BEHAVIORAL'
        data_width = 8
        count_from = 0
        count_to = 255
        step = 1
        output = []

        def test(clk, en, rst, out, 
                 architecture=architecture,
                 data_width=data_width,
                 count_from=count_from,
                 count_to=count_to,
                 step=step):
            
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

            # stop the simulation after
            # certain number of clocks
            @instance
            def stop_sim():
                while True:
                    yield clk.posedge
                    if out == count_to:
                        raise StopSimulation

            return initial, drive_clk, monitor, stop_sim

        clk = Signal(intbv(0))
        en = Signal(intbv(0))
        rst = Signal(intbv(0))
        out = Signal(intbv(0))
        dut = counter(clk, en, rst, out, 
                      architecture, data_width, count_from, count_to, step)
        check =  test(clk, en, rst, out)
        sim = Simulation(dut, check)
        sim.run(quiet=True)
        self.assertEqual(output, [0]+range(count_to+1))


main()
