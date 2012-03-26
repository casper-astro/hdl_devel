from myhdl import *

def epb_infrastructure_wrapper(block_name,
      epb_data_buf,
      epb_data_oe_n,
      epb_data_i,
      epb_data_o,
      #per_clk,
      #epb_clk,
      ARCHITECTURE="VIRTEX6"
   ):

   @always(epb_data_i.posedge)
   def logic():
      pass

   __verilog__ = \
   """
   epb_infrastructure
   #(
      .ARCHITECTURE ("%(ARCHITECTURE)s")
   ) epb_infrastructure_%(block_name)s (
      .epb_data_buf  (%(epb_data_buf)s),
      .epb_data_oe_n (%(epb_data_oe_n)s),
      .epb_data_i    (%(epb_data_i)s),
      .epb_data_o    (%(epb_data_o)s)
   );
   """

   #epb_data_o.driven = "wire"
   
   return logic

def convert():

   epb_data_buf = TristateSignal(bool(0))
   epb_data_oe_n, epb_data_i, epb_data_o, per_clk, epb_clk = [Signal(bool(0)) for i in range(5)]

   toVerilog(epb_infrastructure_wrapper, block_name="inst", epb_data_buf=epb_data_buf, epb_data_oe_n=epb_data_oe_n, epb_data_i=epb_data_i, epb_data_o=epb_data_o, per_clk=per_clk, epb_clk=epb_clk)


if __name__ == "__main__":
   convert()

