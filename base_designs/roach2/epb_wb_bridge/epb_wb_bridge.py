from myhdl import *

def epb_wb_bridge_wrapper(block_name,
    wb_clk_i, wb_rst_i,
    wb_cyc_o, wb_stb_o, wb_we_o, wb_sel_o,
    wb_adr_o, wb_dat_o, wb_dat_i,
    wb_ack_i, wb_err_i,

    epb_clk,
    epb_cs_n, epb_oe_n, epb_r_w_n, epb_be_n,
    epb_addr,
    epb_data_i, epb_data_o,
    epb_data_oe_n,
    epb_rdy,
    epb_doen,

    ARCHITECTURE="BEHAVIORAL"
    ):

   @always(wb_clk_i.posedge)
   def logic():
      if (rst == 0 and out < COUNT_TO):
         if (en == 1):
            out == out + STEP
      else:
         out = COUNT_FROM

   __verilog__ = \
   """
   epb_wb_bridge
   #(
      .ARCHITECTURE ("%(ARCHITECTURE)s")
   ) epb_wb_bridge_%(block_name)s (
      .wb_clk_i (%(wb_clk_i)s), .wb_rst_i (%(wb_rst_i)s),
      .wb_cyc_o (%(wb_cyc_o)s), .wb_stb_o (%(wb_stb_o)s), .wb_we_o  (%(wb_we_o)s), .wb_sel_o (%(wb_sel_o)s),
      .wb_adr_o (%(wb_adr_o)s), .wb_dat_o (%(wb_dat_o)s), .wb_dat_i (%(wb_dat_i)s),
      .wb_ack_i (%(wb_ack_i)s), .wb_err_i (%(wb_err_i)s),

      .epb_clk       (%(epb_clk)s),
      .epb_cs_n      (%(epb_cs_n)s),      .epb_oe_n   (%(epb_oe_n)s),   .epb_r_w_n (%(epb_r_w_n)s), .epb_be_n (%(epb_be_n)s),
      .epb_addr      (%(epb_addr)s),
      .epb_data_i    (%(epb_data_i)s),    .epb_data_o (%(epb_data_o)s),
      .epb_data_oe_n (%(epb_data_oe_n)s),
      .epb_rdy       (%(epb_rdy)s),
      .epb_doen      (%(epb_doen)s)
   );
   """

   wb_cyc_o.driven  = "wire"
   wb_stb_o.driven  = "wire"
   wb_we_o.driven   = "wire"
   wb_sel_o.driven  = "wire"
   wb_adr_o.driven  = "wire"
   wb_dat_o.driven  = "wire"

   epb_data_o.driven    = "wire"
   epb_data_oe_n.driven = "wire"
   epb_rdy.driven       = "wire"
   epb_doen.driven      = "wire"

   return logic




def convert():

    wb_clk_i, wb_rst_i, wb_cyc_o, wb_stb_o, wb_we_o, wb_sel_o, wb_adr_o, wb_dat_o, wb_dat_i, wb_ack_i, wb_err_i, epb_clk, epb_cs_n, epb_oe_n, epb_r_w_n, epb_be_n, epb_addr, epb_data_i, epb_data_o, epb_data_oe_n, epb_rdy, epb_doen = [Signal(bool(0))for i in range(22)]

    ARCHITECTURE="BEHAVIORAL"

    toVerilog(epb_wb_bridge_wrapper, 
    "inst",
    wb_clk_i, wb_rst_i,
    wb_cyc_o, wb_stb_o, wb_we_o, wb_sel_o,
    wb_adr_o, wb_dat_o, wb_dat_i,
    wb_ack_i, wb_err_i,

    epb_clk,
    epb_cs_n, epb_oe_n, epb_r_w_n, epb_be_n,
    epb_addr,
    epb_data_i, epb_data_o,
    epb_data_oe_n,
    epb_rdy,
    epb_doen)



if __name__ == "__main__":
   convert()
