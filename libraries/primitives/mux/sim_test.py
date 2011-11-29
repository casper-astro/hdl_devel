from myhdl import *
import mux

out = bool(0)

inst = mux.mux_wrapper("mux_inst_0",3,intbv(12),out)
sim = Simulation(inst)
sim.run(10)

print out

