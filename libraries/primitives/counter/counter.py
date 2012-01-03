#==============================================================================#
#                                                                              # 
#      Counter wrapper and simulation model                                    # 
#                                                                              # 
#      Module name: counter_wrapper                                            # 
#      Desc: wraps the verilog counter and provides a model for simulation     # 
#      Date: Oct 2011                                                          # 
#      Developer: Rurik Primiani & Wesley New                                  # 
#      Licence: GNU General Public License ver 3                               # 
#      Notes:                                                                  # 
#                                                                              # 
#==============================================================================#

from myhdl import *

def counter_wrapper(block_name,
      #========
      # Ports
      #========
      clk,
      en,
      rst,
      out,

      #=============
      # Parameters
      #=============
      ARCHITECTURE="BEHAVIORAL",
      DATA_WIDTH=8,
      COUNT_FROM=0,
      COUNT_TO=256,  # should be 2^(DATAWIDTH-1)
      STEP=1
   ):

   #===================
   # Simulation Logic
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

