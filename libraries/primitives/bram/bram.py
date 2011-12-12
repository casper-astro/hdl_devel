from myhdl import *

def bram(block_name,
            clk,
            en,
            rst,
            out,
            ARCHITECTURE="BEHAVIORAL",
            DATA_WIDTH=8,
            COUNT_FROM=0,
            COUNT_TO=256,  # should be 2^(DATAWIDTH-1)
            STEP=1
            ):

   @always(clk.posedge)
   def logic():
      if (rst == 0 and out < COUNT_TO):
         if (en == 1):
            out == out + STEP
      else:
         out = COUNT_FROM

   __verilog__ = \
   """
   counter 
   #(
      .ARCHITECTURE ("%(ARCHITECTURE)s"),
      .DATA_WIDTH   (%(DATA_WIDTH)s),
      .COUNT_FROM   (%(COUNT_FROM)s),
      .COUNT_TO     (%(COUNT_TO)s),
      .STEP         (%(STEP)s)
   ) counter_%(block_name)s (
      .clk  (%(clk)s),
      .en   (%(en)s),
      .rst  (%(rst)s),
      .out  (%(out)s)
   );
   """

   out.driven = "wire"

   return logic


def convert():

   clk, en, rst, out = [Signal(bool(0)) for i in range(4)]

   toVerilog(counter_wrapper, block_name="cntr2", clk=clk, en=en, rst=rst, out=out)


if __name__ == "__main__":
   convert()

