from myhdl import *

def mux_wrapper(block_name,
            select,
            data_in,
            data_out,
            ARCHITECTURE="BEHAVIORAL",
            SELECT_LINES=8
            ):


   @instance
   def initial():
      data_out = data_in[select]
      yield data_out
   
   
   
   __verilog__ = \
   """
   mux
   #(
      .ARCHITECTURE ("%(ARCHITECTURE)s"),
      .SELECT_LINES (%(SELECT_LINES)s)
   ) mux_%(block_name)s (
      .select   (%(select)s),
      .data_in  (%(data_in)s),
      .data_out (%(data_out)s)
   );
   """

   return initial


#def convert():

  #select, data_in, data_out = [Signal(bool(0)) for i in range(3)]

  #toVerilog(mux_wrapper, block_name="mux1", select=select, data_in=data_in, data_out=data_out)


if __name__ == "__main__":
   convert()

