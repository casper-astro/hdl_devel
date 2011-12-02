from myhdl import *

def slice_wrapper(block_name,
            clk,
	    data_in,
            data_out,
            ARCHITECTURE="BEHAVIORAL",
            INPUT_DATA_WIDTH=8,
            OFFSET_REL_TO_MSB=1,
            OFFSET_1=0,
            OFFSET_2=7
            ):

   @always(clk.posedge)
   def logic():
      if OFFSET_REL_TO_MSB:
         data_out.next = data_in[OFFSET_2:OFFSET_1]
      else:
         data_out.next = data_in[OFFSET_1:OFFSET_2]


   __verilog__ = \
   """
   slice 
   #(
      .ARCHITECTURE      (%(ARCHITECTURE)s),
      .INPUT_DATA_WIDTH  (%(INPUT_DATA_WIDTH)s),
      .OFFSET_REL_TO_MSB (%(OFFSET_REL_TO_MSB)s),
      .OFFSET_1          (%(OFFSET_1)s),
      .OFFSET_2          (%(OFFSET_2)s)
   ) counter_%(block_name)s (
      .clk      (%(clk)s),
      .data_in  (%(data_in)s),
      .data_out (%(data_out)s)
   );
   """

   data_in.driven = "wire"
   data_out.driven = "wire"

   return logic


def convert():

  clk, data_in, data_out = [Signal(bool(0)) for i in range(3)]

  toVerilog(slice_wrapper, block_name="slice2", clk=clk, data_in=data_in, data_out=data_out)


if __name__ == "__main__":
   convert()

