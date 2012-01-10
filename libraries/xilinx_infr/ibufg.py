#==============================================================================#
#                                                                              #
#      ibufg wrapper and simulation model                                      #
#                                                                              #
#      Module name: ibufg_wrapper                                              #
#      Desc: wraps the xilinx ibufg in Python and provides a model for         #
#            simulation                                                        #
#      Date: Dec 2011                                                          #
#      Developer: Wesley New                                                   #
#      Licence: GNU General Public License ver 3                               #
#      Notes:                                                                  #
#                                                                              #
#==============================================================================#

from myhdl import *

def ibufg_wrapper (block_name,
      #========
      # Ports
      #========
      i, # input
      o, # output
  
      #=============
      # Parameters
      #=============
      IBUF_LOW_PWR = "TRUE",    # Low power (TRUE) vs. performance (FALSE) setting for refernced I/O standards 
      IOSTANDARD   = "LVDS_25"  # Specify the input I/O standard
   ):

   #===================
   # Simulation Logic
   #===================
   @always(i.posedge and i.negedge)
   def logic():
      o.next = i

   #======================
   # IBUFG Instantiation
   #======================
   __verilog__ = \
   """
   IBUFG
   #(
      .IBUF_LOW_PWR (%(IBUF_LOW_PWR)s),
      .IOSTANDARD   (%(IOSTANDARD)s)
   ) IBUFG_%(block_name)s (
      .I  (%(i)s),
      .O  (%(o)s)
   );
   """

   # removes warning when converting to hdl
   o.driven = "wire"

   return logic


#=======================================
# For testing of conversion to verilog
#=======================================
def convert():
   i, o = [Signal(bool(0)) for i in range(2)]
   toVerilog(ibufg_wrapper, "buf", i, o)

if __name__ == "__main__":
   convert()
