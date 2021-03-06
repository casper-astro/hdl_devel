#==============================================================================#
#                                                                              #
#      iobuf wrapper and simulation model                                      #
#                                                                              #
#      Module name: iobuf_wrapper                                              #
#      Desc: wraps the xilinx iobuf in Python and provides a model for         #
#            simulation                                                        #
#            IOBUF: The design element is a bidirectional single-ended I/O     #
#            Buffer used to connect internal logic to an external              #
#            bidirectional pin.                                                #
#      Date: Dec 2011                                                          #
#      Developer: Wesley New                                                   #
#      Licence: GNU General Public License ver 3                               #
#      Notes:                                                                  #
#                                                                              #
#==============================================================================#

from myhdl import *

def iobuf_wrapper (block_name,
      #========
      # Ports
      #========
      t,   # selects whether io is an input or an output
      i,   # input
      o,   # output
      io,  # inout
  
      #=============
      # Parameters
      #=============
      DRIVE      = 12,        # output drive strength
      IOSTANDARD = "DEFAULT", # I/O standard
      SLEW       = "SLOW"     # output slew rate
   ):

   #===================
   # Simulation Logic
   #===================
   @always(i.posedge and i.negedge)
   def logic():
      o.next = i
      #TODO: get this logic correct


   # removes warning when converting to hdl
   o.driven = "wire"

   return logic
   

#======================
# IOBUF Instantiation
#======================
iobuf_wrapper.verilog_code = \
"""
IOBUF
#(
   .DRIVE      ($DRIVE),
   .IOSTANDARD ($IOSTANDARD),
   .SLEW       ($SLEW)

) IOBUF_$block_name (
   .T  ($t)
   .I  ($i),
   .O  ($o)
   .IO ($io)
);
"""


#=======================================
# For testing of conversion to verilog
#=======================================
def convert():
   t, i, o, io = [Signal(bool(0)) for i in range(4)]
   toVerilog(iobuf_wrapper, "buf", t, i, o, io)

if __name__ == "__main__":
   convert()
