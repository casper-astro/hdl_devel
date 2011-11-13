from myhdl import *

def mux_wrapper(block_name,
            select,
            data_in,
            data_out,
            ARCHITECTURE="BEHAVIORAL",
            SELECT_LINES=8
            ):

   @always(select.posedge)
   def logic():
      if (rst == 0 and out < COUNT_TO):
         if (en == 1):
            data_out == data_out + STEP
      else:
         data_out = COUNT_FROM

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

   select.driven = "wire"
   data_in.driven = "wire"
   data_out.driven = "wire"

   return logic


def convert():

  select, data_in, data_out = [Signal(bool(0)) for i in range(3)]

  toVerilog(mux_wrapper, block_name="mux1", select=select, data_in=data_in, data_out=data_out)


if __name__ == "__main__":
   convert()

