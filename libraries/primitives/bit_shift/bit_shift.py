#==============================================================================#
#                                                                              # 
#      Bit shift wrapper and simulation model                                  # 
#                                                                              # 
#      Module name: bit_shift_wrapper                                          # 
#      Desc: wraps the verilog bit shift and provides a model for simulation   # 
#      Date: Nov 2011                                                          # 
#      Developer: Wesley New                                                   # 
#      Licence: GNU General Public License ver 3                               # 
#      Notes:                                                                  # 
#                                                                              # 
#==============================================================================#

from myhdl import *

def bit_shift_wrapper(block_name,
      #==================
      # Ports
      #==================
      clk,
      data_in,
      data_out,
      
      #==================
      # Parameters
      #==================
      ARCHITECTURE="BEHAVIORAL",
      INPUT_DATA_WIDTH=8,
      SHIFT_DIRECTION=1,
      NUMBER_OF_BITS=1,
      WRAP=0
   ):

   #====================
   # Simulation Logic
   #====================  
   @always(clk.posedge)
   def logic():
      if WRAP == 0:
         data_out.next[8:] = (data_in[:]*2**NUMBER_OF_BITS)
      else:
         data_out.next = (data_in[:]*2**NUMBER_OF_BITS)


   return logic


#==================================
# Bit Shift Verilog Instantiation
#==================================
bit_shift_wrapper.verilog_code = \
"""
bit_shift
#(
   .ARCHITECTURE      ($ARCHITECTURE),
   .INPUT_DATA_WIDTH  ($INPUT_DATA_WIDTH),
   .SHIFT_DIRECTION   ($SHIFT_DIRECTION),
   .NUMBER_OF_BITS    ($NUMBER_OF_BITS),
   .WRAP              ($WRAP)
) bit_shift_$block_name (
   .clk      ($clk),
   .data_in  ($data_in),
   .data_out ($data_out)
);
"""

#======================================= 
# For testing of conversion to verilog 
#======================================= 
def convert(): 
 
   clk, data_in, data_out = [Signal(bool(0)) for i in range(3)] 
     
   toVerilog(bit_shift_wrapper, block_name="inst", clk=clk, data_in=data_in, data_out=data_out) 


if __name__ == "__main__":
   convert()

