from myhdl import *

def clk_gen_wrapper(block_name,
            clk100,
            rst,
            clk0,
	    clk180,
	    clk270,
	    clkdiv2,
	    pll_lock,
	    ARCHITECTURE="BEHAVIORAL"
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
      .ARCHITECTURE ("%(ARCHITECTURE)s")
   ) clk_gen_%(block_name)s (
      .clk100   (%(clk100)s),
      .rst      (%(rst)s),
      .clk0     (%(clk0)s),
      .clk180   (%(clk180)s),
      .clk270   (%(clk270)s),
      .clkdiv2  (%(clkdiv2)s),
      .pll_lock (%(pll_lock)s)
   );
   """

   clk0.driven     = "wire"
   rst.driven      = "wire"
   clk180.driven   = "wire"
   clk270.driven   = "wire"
   clkdiv2.driven  = "wire"
   pll_lock.driven = "wire"

   return logic

def convert():
   block_name, clk100, rst, clk0, clk180, clk270, clkdiv2, pll_lock = [Signal(bool(0)) for i in range(8)]
   toVerilog(clk_gen_wrapper, block_name="1", clk100=clk100, rst=rst, clk0=clk0, clk180=clk180, clk270=clk270, clkdiv2=clkdiv2, pll_lock=pll_lock, ARCHITECTURE="VIRTEX6")
   

if __name__ == "__main__":
   convert()

