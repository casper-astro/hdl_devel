from myhdl import *

def reset_block_wrapper(block_name,
   clk,
   async_rst_i,
   rst_i,
   rst_o,
   ARCHITECTURE="BEHAVIORAL",
   DELAY="10",
   WIDTH="50"
):

   @always(clk.posedge)
   def logic():
      pass

   __verilog__ = \
   """
   reset_block
   #(
      .ARCHITECTURE ("%(ARCHITECTURE)s"),
      .DELAY        ("%(DELAY)s"),
      .WIDTH        ("%(WIDTH)s")
   ) reset_block_%(block_name)s (
      .clk         (%(clk)s),
      .async_rst_i (%(async_rst_i)s),
      .rst_i       (%(rst_i)s),
      .rst_o       (%(rst_o)s)
   );
   """

   rst_o.driven = "wire"

   return logic

def convert():
   clk, rst_i, rst_o, async_rst_i = [Signal(bool(0)) for i in range(4)]
   toVerilog(reset_block_wrapper, block_name="1", clk=clk, rst_i=rst_i, rst_o=rst_o, async_rst_i=async_rst_i, ARCHITECTURE="VIRTEX6")
   

if __name__ == "__main__":
   convert()

