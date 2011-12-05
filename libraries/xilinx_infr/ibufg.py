from myhdl import *

def ibufg_wrapper (block_name,
   clk_i,
   clk_o,
   IOSTANDARD="LVDS_25",
   DIFF_TERM="TRUE"
   ):

   @always(clk_i.posedge)
   def logic():
      clk_o.next = clk_i


   __verilog__ = \
   """
   IBUFGDS
   #(
      .IOSTANDARD (%(IOSTANDARD)s),
      .DIFF_TERM  (%(DIFF_TERM)s)
   ) IBUFGDS_%(block_name)s (
      .I  (%(clk_i)s),
      .O  (%(clk_o)s)
   );
   """

   clk_o.driven = "wire"

   return logic



def convert():
   clk_i, clk_o = [Signal(bool(0)) for i in range(2)]
   toVerilog(ibufg_wrapper, "1", clk_i, clk_o)

if __name__ == "__main__":
   convert()
