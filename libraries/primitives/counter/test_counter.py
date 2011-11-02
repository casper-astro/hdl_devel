import os, shlex, subprocess
from unittest import TestCase, main
from myhdl import *


VPI_PATH = os.path.join(os.getenv('MYHDL'), 'cosimulation', 'icarus', 'myhdl.vpi')
MOD_PATH = os.path.abspath(os.path.dirname(__file__))

ICARUS_CMD = 'iverilog ' + \
    '-o {mod_path}/counter_tb ' + \
    '-DMYHDL ' + \
    '-DARCHITECTURE=\\"{architecture}\\" ' + \
    '-DDATA_WIDTH={data_width} ' + \
    '-DCOUNT_FROM={count_from} ' + \
    '-DCOUNT_TO={count_to} ' + \
    '-DSTEP={step} ' + \
    '{mod_path}/counter_tb.v ' + \
    '{mod_path}/counter.v'

VVP_CMD = "vvp -m {vpi_path} {mod_path}/counter_tb"


def counter(clk, en, rst, out, 
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


class TestCounterProperties(TestCase):

    def setUp(self):
        self.architecture = 'BEHAVIORAL'
        self.data_width = 8
        self.count_from = 0
        self.count_to = 255
        self.step = 1

        self.clk = Signal(intbv(0))
        self.en = Signal(intbv(0))
        self.rst = Signal(intbv(0))
        self.out = Signal(intbv(0))

        self.dut = counter(self.clk, self.en, self.rst, self.out, 
                           self.architecture, self.data_width, 
                           self.count_from, self.count_to, self.step)

    def test_output(self):
        """ Check that the counter increments """

        output = []

        def test(clk, en, rst, out, 
                 architecture=self.architecture,
                 data_width=self.data_width,
                 count_from=self.count_from,
                 count_to=self.count_to,
                 step=self.step):
            
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

        check =  test(self.clk, self.en, self.rst, self.out)
        sim = Simulation(self.dut, check)
        sim.run(quiet=True)
        self.assertEqual(output, [0]+range(self.count_to+1))

    def tearDown(self):
        os.remove('{mod_path}/counter_tb'.format(mod_path=MOD_PATH))


if __name__ == "__main__":
    main()
