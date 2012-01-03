#==============================================================================#
#                                                                              # 
#      Multiplexer wrapper and simulation model                                # 
#                                                                              # 
#      Module name: mux_wrapper                                                # 
#      Desc: wraps the verilog counter and provides a model for simulation     # 
#      Date: Oct 2011                                                          # 
#      Developer: Rurik Primiani & Wesley New                                  # 
#      Licence: GNU General Public License ver 3                               # 
#      Notes:                                                                  # 
#                                                                              # 
#==============================================================================#

from myhdl import *

def mux_wrapper(block_name,
      #========
      # Ports
      #========
      select,
      data_in,
      data_out,
      
      #============
      # Parameter 
      #============
      ARCHITECTURE="BEHAVIORAL",
      SELECT_LINES=8,
      DATA_WIDTH=1
   ):


   #===================
   # Simulation Logic
   #===================
   #TODO: rework model so that it takes into account the DATA_WIDTH, It may just work as is though?
   @always(delay(1))
   def logic():
      data_out.next = data_in[select]
   
   
   #====================
   # Mux Instantiation 
   #====================
   __verilog__ = \
   """
   mux
   #(
      .ARCHITECTURE ("%(ARCHITECTURE)s"),
      .SELECT_LINES (%(SELECT_LINES)s),
      .DATA_WIDTH   (%(DATA_WIDTH)s)
   ) mux_%(block_name)s (
      .select   (%(select)s),
      .data_in  (%(data_in)s),
      .data_out (%(data_out)s)
   );
   """

   # prevent warnings when converting to hdl
   select.driven   = "wire"
   data_in.driven  = "wire"
   data_out.driven = "wire"


   return logic


#=======================================
# For testing of conversion to verilog
#=======================================
def convert():

  select, data_in, data_out = [Signal(bool(0)) for i in range(3)]

  toVerilog(mux_wrapper, block_name="mux1", select=srelect, data_in=data_in, data_out=data_out)


if __name__ == "__main__":
   convert()

