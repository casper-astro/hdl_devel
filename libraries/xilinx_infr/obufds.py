#==============================================================================#
#                                                                              #
#      obufds wrapper and simulation model                                     #
#                                                                              #
#      Module name: obufds_wrapper                                             #
#      Desc: wraps the xilinx obufds in Python and provides a model for        #
#            simulation                                                        #
#            OBUGDS:This design element is a single output buffer that         #
#            supports low-voltage, differential signaling (1.8 v CMOS).        #
#            OBUFDS isolates the internal circuit and provides drive current   #
#            for signals leaving the chip. Its output is represented as two    #
#            distinct ports (O and OB), one deemed the "master" and the other  #
#            the "slave." The master and the slave are opposite phases of the  #
#            same logical signal (for example, MYNET and MYNETB).              #
#      Date: Dec 2011                                                          #
#      Developer: Wesley New                                                   #
#      Licence: GNU General Public License ver 3                               #
#      Notes:                                                                  #
#                                                                              #
#==============================================================================#

from myhdl import *

def obufds_wrapper (block_name,
      #========
      # Ports
      #========
      i,
      o,
      ob,
      
      #=============
      # Parameters
      #=============
      IOSTANDARD="LVDS_25"
   ):

   #===================
   # Simulation Logic
   #===================
   @always(i.posedge and i.negedge)
   def logic():
      o.next = i
      ob.next = i

   # removes warning when converting to hdl
   o.driven  = "wire"
   ob.driven = "wire"

   return logic
   

#========================
# OBUFDS Instantiation
#========================
obufds_wrapper.verilog_code = \
"""
OBUFDS
#(
   .IOSTANDARD ($IOSTANDARD)
) OBUFDS_$block_name (
   .I  ($i),
   .O  ($o),
   .OB ($ob)
);
"""


#=======================================
# For testing of conversion to verilog
#=======================================
def convert():
   i, o, ob = [Signal(bool(0)) for i in range(3)]
   toVerilog(obufds_wrapper, "buf", i, o, ob)

if __name__ == "__main__":
   convert()
