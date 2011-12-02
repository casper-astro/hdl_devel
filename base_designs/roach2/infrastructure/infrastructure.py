from myhdl import *

def infrastructure_wrapper(block_name,
                   sys_clk_buf_n,
                   sys_clk_buf_p,

                   sys_clk0,
                   sys_clk180,
                   sys_clk270,
                   
                   clk_200,
                   sys_rst,
                   idelay_rdy,
                   ARCHITECTURE="BEHAVIORAL"
                   ):

   @always(sys_clk0.posedge)
   def logic():
      if (rst == 0 and out < COUNT_TO):
         if (en == 1):
            out == out + STEP
      else:
         out = COUNT_FROM

   __verilog__ = \
   """
   infrastructure 
   #(
      .ARCHITECTURE ("%(ARCHITECTURE)s")
   ) infrustructure_%(block_name)s (
      .sys_clk_buf_n (%(sys_clk_buf_n)s),
      .sys_clk_buf_p (%(sys_clk_buf_p)s),

      .sys_clk0      (%(sys_clk0)s),
      .sys_clk180    (%(sys_clk180)s),
      .sys_clk270    (%(sys_clk270)s),
      
      .clk_200       (%(clk_200)s),
      .sys_rst       (%(sys_rst)s),
      .idelay_rdy    (%(idelay_rdy)s)
   );
   """

   return logic

def convert():
   
   sys_clk_buf_n, sys_clk_buf_p, sys_clk0, sys_clk180, sys_clk270, clk_200, sys_rst, idelay_rdy = [Signal(bool(0)) for i in range(8)]
   toVerilog(infrastructure_wrapper, "1", sys_clk_buf_n, sys_clk_buf_p, sys_clk0, sys_clk180, sys_clk270, clk_200, sys_rst, idelay_rdy, ARCHITECTURE="VIRTEX6")

if __name__ == "__main__":
   convert()

