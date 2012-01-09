#==============================================================================#
#                                                                              # 
#      BRAM single port wrapper and simulation model                           # 
#                                                                              # 
#      Module name: bram_sp_wrapper                                            # 
#      Desc: wraps the verilog bram_sp and provides a model for simulation     # 
#      Date: Jan 2012                                                          # 
#      Developer: Wesley New                                                   # 
#      Licence: GNU General Public License ver 3                               # 
#      Notes:                                                                  # 
#                                                                              # 
#==============================================================================#

from myhdl import *

def bram_sync_sp_wrapper(block_name,
      #========
      # Ports
      #========
      clk,
      wr,
      addr,
      data_in,
      data_out,

      #=============
      # Parameters
      #=============
      ARCHITECTURE="BEHAVIORAL",
      DATA_WIDTH=32,
      ADDR_WIDTH=4
   ):

   #===================
   # TODO:Simulation Logic
   #===================
   @always(clk.posedge)
   def logic():
      if (rst == 0 and out < COUNT_TO):
         if (en == 1):
            out == out + STEP
      else:
         out = COUNT_FROM

   #========================
   # Counter Instantiation
   #========================
   __verilog__ = \
   """
   bram_sync_sp
   #(
      .ARCHITECTURE ("%(ARCHITECTURE)s"),
      .DATA_WIDTH   (%(DATA_WIDTH)s),
      .ADDR_WIDTH   (%(ADDR_WIDTH)s)
   ) counter_%(block_name)s (
      .clk      (%(clk)s),
      .wr       (%(wr)s),
      .addr     (%(addr)s),
      .data_in  (%(data_in)s),
      .data_out (%(data_out)s)
   );
   """

   # removes warning when converting to hdl
   out.driven = "wire"

   return logic


#=======================================
# For testing of conversion to verilog
#=======================================
def convert():

   clk, en, rst, out = [Signal(bool(0)) for i in range(4)]

   toVerilog(counter_wrapper, block_name="cntr2", clk=clk, en=en, rst=rst, out=out)


if __name__ == "__main__":
   convert()

