#==============================================================================#
#                                                                              #
#      ibufgds wrapper and simulation model                                    #
#                                                                              #
#      Module name: ibufgds_wrapper                                            #
#      Desc: wraps the xilinx ibufgds in Python and provides a model for       #
#            simulation                                                        #
#            IBUFGDS: This design element is a dedicated differential          #
#            signaling input buffer for connection to the clock buffer (BUFG)  #
#            or MMCM. In IBUFGDS, a design-level interface signal is           #
#            represented as two distinct ports (I and IB), one deemed the      #
#            "master" and the other the "slave." The master and the slave are  #
#            opposite phases of the same logical signal (for example, MYNET_P  #
#            and MYNET_N). Optionally, a programmable differential termination #
#            feature is available to help improve signal integrity and reduce  #
#            external components. Also available is a programmable delay is to #
#            assist in the capturing of incoming data to the device.           #
#      Date: Dec 2011                                                          #
#      Developer: Wesley New                                                   #
#      Licence: GNU General Public License ver 3                               #
#      Notes:                                                                  #
#                                                                              #
#==============================================================================#

from myhdl import *

def ibufgds_wrapper (block_name,
      #========
      # Ports
      #========
      i,  # input 
      ib, # input b
      o,  # output
      
      #=============
      # Parameters
      #=============
      DIFF_TERM    = "TRUE",    # Differential Termination
      IBUF_LOW_PWR = "TRUE",    # Low power (TRUE) vs. performance (FALSE) setting for refernced I/O standards 
      IOSTANDARD   = "LVDS_25"  # Specify the input I/O standard
   ):

   #===================
   # Simulation Logic
   #===================
   @always(i.posedge and i.negedge)
   def logic():
      o.next = i


   # removes warning when converting to hdl
   o.driven  = "wire"

   return logic

#========================
# IBUFGDS Instantiation
#========================
ibufgds_wrapper.verilog_code = \
"""
IBUFGDS
#(
   .DIFF_TERM    ($DIFF_TERM),
   .IBUF_LOW_PWR ($IBUF_LOW_PWR),
   .IOSTANDARD   ($IOSTANDARD)
) IBUFGDS_$block_name (
   .I  ($i),
   .IB ($ib),
   .O  ($o)
);
"""


#=======================================
# For testing of conversion to verilog
#=======================================
def convert():
   i, ib, o = [Signal(bool(0)) for i in range(3)]
   toVerilog(ibufgds_wrapper, "buf", i, ib, o)

if __name__ == "__main__":
   convert()
