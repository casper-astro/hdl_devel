from myhdl import *

def mux_wrapper(block_name,
            clk,
            inputs,
            out,
            ARCHITECTURE="BEHAVIORAL",
            SELECT_LINES=8
            ):

   @always(clk.posedge)
   def logic():
      if (rst == 0 and out < COUNT_TO):
         if (en == 1):
            out == out + STEP
      else:
         out = COUNT_FROM

   __verilog__ = \
   """
   mux
   #(
      .ARCHITECTURE (%(ARCHITECTURE)s),
      .SELECT_LINES (%(SELECT_LINES)s)
   ) mux_%(block_name)s (
      .clk  (%(clk)s),
      .in   (%(inputs)s),
      .out  (%(out)s)
   );
   """

   inputs.driven = "wire"
   out.driven = "wire"

   return logic


def convert():

  clk, inputs, out = [Signal(bool(0)) for i in range(3)]

  toVerilog(mux_wrapper, block_name="mux1", clk=clk, inputs=inputs, out=out)


if __name__ == "__main__":
   convert()

