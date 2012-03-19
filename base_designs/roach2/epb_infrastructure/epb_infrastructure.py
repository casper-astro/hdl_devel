from myhdl import *

def epb_infrastructure_wrapper(block_name,
			       epb_data_buf,
                               epb_data_oe_n,
                               epb_data_in,
                               epb_data_out,
                               per_clk,
                               epb_clk,
			       ARCHITECTURE="VIRTEX6"
                               ):

   @always(epb_clk.posedge)
   def logic():
      if (rst == 0 and out < COUNT_TO):
         if (en == 1):
            out == out + STEP
      else:
         out = COUNT_FROM

   __verilog__ = \
   """
   epb_infrastructure
   #(
      .ARCHITECTURE ("%(ARCHITECTURE)s")
   ) epb_infrastructure_%(block_name)s (
      .epb_data_buf  (%(epb_data_buf)s),
      .epb_data_oe_n (%(epb_data_oe_n)s),
      .epb_data_in   (%(epb_data_in)s),
      .epb_data_out  (%(epb_data_out)s),
      .per_clk       (%(per_clk)s),
      .epb_clk       (%(epb_clk)s)
   );
   """

   epb_clk.driven  = "wire"
   
   return logic

def convert():

   epb_data_buf, epb_data_oe_n, epb_data_in, epb_data_out, per_clk, epb_clk = [Signal(bool(0)) for i in range(6)]

   toVerilog(epb_infrastructure_wrapper, block_name="cntr2", epb_data_buf=epb_data_buf, epb_data_oe_n=epb_data_oe_n, epb_data_in=epb_data_in, epb_data_out=epb_data_out, per_clk=per_clk, epb_clk=epb_clk)


if __name__ == "__main__":
   convert()

