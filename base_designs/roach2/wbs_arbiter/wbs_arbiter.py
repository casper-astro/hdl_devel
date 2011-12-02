from myhdl import *

def clk_gen_wrapper(block_name,
            clk_100,
            rst,
            clk0,
	    clk180,
	    clk270,
	    clkdiv2,
	    pll_lock
            ):

   @always(clk100.posedge)
   def logic():
      if (rst == 0 and out < COUNT_TO):
         if (en == 1):
            out == out + STEP
      else:
         out = COUNT_FROM

   __verilog__ = \
   """
   clk_gen 
   #(
   ) counter_%(block_name)s (
      .clk      (%(clk)s),
      .rst      (%(rst)s),
      .clk0     (%(clk0)s),
      .clk180   (%(clk180)s),
      .clk270   (%(clk270)s),
      .clkdiv2  (%(clkdiv2)s),
      .pll_lock (%(pll_lock)s)
   );
   """

   return logic

if __name__ == "__main__":
   convert()

