#==============================================================================#
#                                                                              #
#      bufg wrapper and simulation model                                       #
#                                                                              #
#      Module name: bufg_wrapper                                               #
#      Desc: wraps the xilinx bufg in Python and provides a model for          #
#            simulation                                                        #
#            BUFG: This design element is a high-fanout buffer that connects   #
#                  signals to the global routing resources for low skew        #
#                  distribution of the signal. BUFGs are typically used on     #
#                  clock nets as well other high fanout nets like sets/resets  #
#                  and clock enables.                                          #
#      Date: Dec 2011                                                          #
#      Developer: Wesley New                                                   #
#      Licence: GNU General Public License ver 3                               #
#      Notes:                                                                  #
#                                                                              #
#==============================================================================#

from myhdl import *

def bufg_wrapper (block_name,
      #========
      # Ports
      #========
      i, # input
      o, # output
   ):

   #===================
   # Simulation Logic
   #===================
   @always(i.posedge and i.negedge)
   def logic():
      o.next = i

   #======================
   # BUFG Instantiation
   #======================
   __verilog__ = \
   """
   BUFG
   #(
   ) BUFG_%(block_name)s (
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
   toVerilog(bufg_wrapper, "buf", i, o)

if __name__ == "__main__":
   convert()
