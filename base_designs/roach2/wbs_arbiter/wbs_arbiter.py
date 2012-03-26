from myhdl import *

def wbs_arbiter_wrapper(block_name,
   # generic wb signals
   wb_clk_i, wb_rst_i,
   # wbm signals
   wbm_cyc_i, wbm_stb_i, wbm_we_i, wbm_sel_i,
   wbm_adr_i, wbm_dat_i, wbm_dat_o,
   wbm_ack_o, wbm_err_o,
   # wbs signals
   wbs_cyc_o, wbs_stb_o, wbs_we_o, wbs_sel_o,
   wbs_adr_o, wbs_dat_o, wbs_dat_i,
   wbs_ack_i,

   ARCHITECTURE="BEHAVIOURAL",
   NUM_SLAVES=1,
   SLAVE_ADDR=0,
   SLAVE_HIGH=65535,
   TIMEOUT=1024
   ):

   @always(wb_clk_i.posedge)
   def logic():
      wb_dat_o = 0
   

   __verilog__ = \
   """
   wbs_arbiter
   #(
      .ARCHITECTURE ("%(ARCHITECTURE)s"),
      .NUM_SLAVES   (%(NUM_SLAVES)s),
      .SLAVE_ADDR   (%(SLAVE_ADDR)s),
      .SLAVE_HIGH   (%(SLAVE_HIGH)s),
      .TIMEOUT      (%(TIMEOUT)s)
   ) wbs_arbiter_%(block_name)s (
      .wb_clk_i (%(wb_clk_i)s), .wb_rst_i (%(wb_rst_i)s), 
      
      .wbm_cyc_i (%(wbm_cyc_i)s), .wbm_stb_i (%(wbm_stb_i)s), .wbm_we_i  (%(wbm_we_i)s), .wbm_sel_i (%(wbm_sel_i)s), 
      .wbm_adr_i (%(wbm_adr_i)s), .wbm_dat_i (%(wbm_dat_i)s), .wbm_dat_o (%(wbm_dat_o)s), 
      .wbm_ack_o (%(wbm_ack_o)s),
      
      .wbs_cyc_o (%(wbs_cyc_o)s), .wbs_stb_o (%(wbs_stb_o)s), .wbs_we_o  (%(wbs_we_o)s), .wbs_sel_o (%(wbs_sel_o)s), 
      .wbs_adr_o (%(wbs_adr_o)s), .wbs_dat_o (%(wbs_dat_o)s), .wbs_dat_i (%(wbs_dat_i)s), 
      .wbs_ack_i (%(wbs_ack_i)s)
   );
   """

   wbm_dat_o.driven = "wire"
   wbm_ack_o.driven = "wire"
   wbm_err_o.driven = "wire"
   wbs_cyc_o.driven = "wire"
   wbs_stb_o.driven = "wire"
   wbs_we_o.driven  = "wire"
   wbs_sel_o.driven = "wire"
   wbs_adr_o.driven = "wire"
   wbs_dat_o.driven = "wire"
   
   return logic

def convert():
   wb_clk_i, wb_rst_i, wbm_cyc_i, wbm_stb_i, wbm_we_i, wbm_sel_i, wbm_adr_i, wbm_dat_i, wbm_dat_o, wbm_ack_o, wbm_err_o, wbs_cyc_o, wbs_stb_o, wbs_we_o, wbs_sel_o, wbs_adr_o, wbs_dat_o, wbs_dat_i, wbs_ack_i = [Signal(bool(0))for i in range(19)]

   toVerilog(wbs_arbiter_wrapper, "inst", wb_clk_i, wb_rst_i, wbm_cyc_i, wbm_stb_i, wbm_we_i, wbm_sel_i, wbm_adr_i, wbm_dat_i, wbm_dat_o, wbm_ack_o, wbm_err_o, wbs_cyc_o, wbs_stb_o, wbs_we_o, wbs_sel_o, wbs_adr_o, wbs_dat_o, wbs_dat_i, wbs_ack_i, "BEHAVIOURAL", 14, 100, 150, 10)

if __name__ == "__main__":
   convert()

