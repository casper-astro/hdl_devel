from myhdl import *

def ibufgds_wrapper (block_name,
   clk_n,
   clk_p,
   clk_ds,
   IOSTANDARD="LVDS_25",
   DIFF_TERM="TRUE"
   ):

   @always(clk_n.posedge)
   def logic():
      clk_ds.next = clk_n


   __verilog__ = \
   """
   IBUFGDS
   #(
      .IOSTANDARD (%(IOSTANDARD)s),
      .DIFF_TERM  (%(DIFF_TERM)s)
   ) IBUFGDS_%(block_name)s (
      .I  (%(clk_n)s),
      .IB (%(clk_p)s),
      .O  (%(clk_ds)s)
   );
   """

   clk_ds.driven = "wire"

   return logic


def convert():
   clk_n, clk_p, clk_ds = [Signal(bool(0)) for i in range(3)]
   toVerilog(ibufgds_wrapper, "1", clk_n, clk_p, clk_ds)

if __name__ == "__main__":
   convert()
