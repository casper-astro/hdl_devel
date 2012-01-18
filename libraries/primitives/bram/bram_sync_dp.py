#==============================================================================#
#                                                                              # 
#      BRAM dual port wrapper and simulation model                             # 
#                                                                              # 
#      Module name: bram_sp_wrapper                                            # 
#      Desc: wraps the verilog bram_dp and provides a model for simulation     # 
#      Date: Jan 2012                                                          # 
#      Developer: Wesley New                                                   # 
#      Licence: GNU General Public License ver 3                               # 
#      Notes:                                                                  # 
#                                                                              # 
#==============================================================================#

from myhdl import *

def bram_sync_dp_wrapper(block_name,
      #========
      # Ports
      #========
      a_clk,
      a_wr,
      a_addr,
      a_data_in,
      a_data_out,
      b_clk,
      b_wr,
      b_addr,
      b_data_in,
      b_data_out,

      #=============
      # Parameters
      #=============
      ARCHITECTURE="BEHAVIORAL",
      DATA_WIDTH=32,
      ADDR_WIDTH=4
   ):

   #========================
   # TODO:Simulation Logic
   #========================
   @always(a_clk.posedge)
   def logic():
      #if (rst == 0 and a_data_out < COUNT_TO):
      #   if (en == 1):
      #      data_out == data_out + STEP
      #else:
      a_data_out = 0


   # removes warning when converting to hdl
   a_data_out.driven = "wire"
   b_data_out.driven = "wire"

   return logic

   
#=============================
# BRAM Verilog Instantiation
#=============================
bram_sync_dp_wrapper.verilog_code = \
"""
bram_sync_dp
#(
   .ARCHITECTURE ("$ARCHITECTURE"),
   .DATA_WIDTH   ($DATA_WIDTH),
   .ADDR_WIDTH   ($ADDR_WIDTH)
) bram_sync_dp_$block_name (
   .a_clk      ($a_clk),
   .a_wr       ($a_wr),
   .a_addr     ($a_addr),
   .a_data_in  ($a_data_in),
   .a_data_out ($a_data_out)
   .b_clk      ($b_clk),
   .b_wr       ($b_wr),
   .b_addr     ($b_addr),
   .b_data_in  ($b_data_in),
   .b_data_out ($b_data_out)
);
"""


#=======================================
# For testing of conversion to verilog
#=======================================
def convert():

   a_clk, a_wr, a_addr, a_data_in, a_data_out, b_clk, b_wr, b_addr, b_data_in, b_data_out = [Signal(bool(0)) for i in range(10)]

   toVerilog(bram_sync_dp_wrapper, block_name="inst", a_clk=a_clk, a_wr=a_wr, a_addr=a_addr, a_data_in=a_data_in, a_data_out=a_data_out, b_clk=b_clk, b_wr=b_wr, b_addr=b_addr, b_data_in=b_data_in, b_data_out=b_data_out)


if __name__ == "__main__":
   convert()

