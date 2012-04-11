#==============================================================================#
#                                                                              # 
#      Delay wrapper and simulation model                                      # 
#                                                                              # 
#      Module name: delay_wrapper                                              # 
#      Desc: wraps the verilog delaymodule and provides a model for simulation # 
#      Date: April 2012                                                        # 
#      Developer: Wesley New                                                   # 
#      Licence: GNU General Public License ver 3                               # 
#      Notes:                                                                  # 
#                                                                              # 
#==============================================================================#

from myhdl import *

def delay_wrapper(block_name,
      #========
      # Ports
      #========
      clk,
      en,
      rst,
      din,
      dout,
      data_valid,
      
      #=============
      # Parameters
      #=============
      ARCHITECTURE = "BEHAVIORAL",
      DELAY_TYPE   = "FIFO",
      DATA_WIDTH   = 32,
      DELAY_CYCLES = 1
   ):

   #===================
   # Simulation Logic
   #===================

   @always(clk.posedge)
   def logic():
      pass

   dout.driven       = "wire"
   data_valid.driven = "wire"

   return logic

   
delay_wrapper.verilog_code = \
"""
delay 
#(
   .ARCHITECTURE ("$ARCHITECTURE"),
   .DELAY_TYPE   ("$DELAY_TYPE"),
   .DATA_WIDTH   ($DATA_WIDTH),
   .DELAY_CYCLES ($DELAY_CYCLES)
) counter_$block_name (
   .clk        ($clk),
   .en         ($en),
   .rst        ($rst),
   .din        ($din)
   .dout       ($dout),
   .data_valid ($data_valid)
);
"""

def convert():

   clk, en, rst, din, dout, data_valid = [Signal(bool(0)) for i in range(6)]

   toVerilog(delay_wrapper, block_name="inst", clk=clk, en=en, rst=rst, din=din, dout=dout, data_valid=data_valid)


if __name__ == "__main__":
   convert()

