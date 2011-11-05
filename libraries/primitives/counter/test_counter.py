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

    @classmethod
    def setUpClass(cls):
        """ Generating the Cosimulation instance """
        cls.architecture = 'BEHAVIORAL'
        cls.data_width = 8
        cls.count_from = 0
        cls.count_to = 255
        cls.step = 1

        cls.clk = Signal(intbv(0))
        cls.en = Signal(intbv(0))
        cls.rst = Signal(intbv(0))
        cls.out = Signal(intbv(0))

        cls.dut = counter(cls.clk, cls.en, cls.rst, cls.out, 
                          cls.architecture, cls.data_width, 
                          cls.count_from, cls.count_to, cls.step)
        cls.output = []

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
                    cls.output.append(int(out))

            return initial, drive_clk, monitor

        check =  test(cls.clk, cls.en, cls.rst, cls.out)
        sim = Simulation(cls.dut, check)
        sim.run(1024, quiet=True)
        cls.latency = cls.output.index(cls.count_from+cls.step) - 1
        cls.expected = [0]*cls.latency + range(cls.count_from, cls.count_to, cls.step)

    @classmethod
    def tearDownClass(cls):
        os.remove('{mod_path}/counter_tb'.format(mod_path=MOD_PATH))

    def test_output_latency(self):
        """ Check output latency is within specification """
        self.assertLessEqual(self.latency, 3)

    def test_full_range(self):
        """ Check full output range for correctness """
        self.assertEqual(self.output[:len(self.expected)], self.expected)

    def test_roll_over(self):
        """ Check roll-over at COUNT_TO """
        last = self.output.index(self.count_to)
        self.assertEqual(self.output[last+1], self.count_from)


if __name__ == "__main__":
    main()
