from myhdl import *

def delay_wrapper(block_name,
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


   out.driven = "wire"

   return logic

   
delay_wrapper.verilog_code = \
"""
delay 
#(
   .ARCHITECTURE ("$ARCHITECTURE"),
   .DATA_WIDTH   ($DATA_WIDTH),
   .COUNT_FROM   ($COUNT_FROM),
   .COUNT_TO     ($COUNT_TO),
   .STEP         ($STEP)
) counter_$block_name (
   .clk  ($clk),
   .en   ($en),
   .rst  ($rst),
   .out  ($out)
);
"""

def convert():

   clk, en, rst, out = [Signal(bool(0)) for i in range(4)]

   toVerilog(counter_wrapper, block_name="cntr2", clk=clk, en=en, rst=rst, out=out)


if __name__ == "__main__":
   convert()

