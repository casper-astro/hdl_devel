from myhdl import *

def bit_shift_wrapper(block_name,
            clk,
            data_in,
            data_out,
            ARCHITECTURE="BEHAVIORAL",
            INPUT_DATA_WIDTH=8,
            SHIFT_DIRECTION=1,
            NUMBER_OF_BITS=1,
            WRAP=0
            ):

   @always(clk.posedge)
   def logic():
      if WRAP == 0:
         data_out.next[8:] = (data_in[:]*2**NUMBER_OF_BITS)
      else:
         data_out.next = (data_in[:]*2**NUMBER_OF_BITS)

   __verilog__ = \
   """
   bit_shift
   #(
      .ARCHITECTURE      (%(ARCHITECTURE)s),
      .INPUT_DATA_WIDTH  (%(INPUT_DATA_WIDTH)s),
      .SHIFT_DIRECTION   (%(SHIFT_DIRECTION)s),
      .NUMBER_OF_BITS    (%(NUMBER_OF_BITS)s),
      .WRAP              (%(WRAP)s)
   ) bit_shift_%(block_name)s (
      .clk      (%(clk)s),
      .data_in  (%(data_in)s),
      .data_out (%(data_out)s)
   );
   """

   return logic


if __name__ == "__main__":
   convert()

