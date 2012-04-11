from myhdl import *

def sys_block_wrapper(block_name,
      wb_clk_i,
      wb_rst_i,
      wb_cyc_i,
      wb_stb_i,
      wb_we_i,
      wb_sel_i,
      wb_adr_i,
      wb_dat_i,
      wb_dat_o,
      wb_ack_o,
      wb_err_o,
      BOARD_ID="0",
      REV_MAJ="0",
      REV_MIN="0",
      REV_RCS="0"
   ):

   @always(wb_clk_i.posedge)
   def logic():
      pass 

   __verilog__ = \
   """
   sys_block
   #(
      .BOARD_ID (%(BOARD_ID)s),
      .REV_MAJ  (%(REV_MAJ)s),
      .REV_MIN  (%(REV_MIN)s),
      .REV_RCS  (%(REV_RCS)s)
   ) sys_block_%(block_name)s (
      .wb_clk_i (%(wb_clk_i)s), 
      .wb_rst_i (%(wb_rst_i)s),
      .wb_cyc_i (%(wb_cyc_i)s),
      .wb_stb_i (%(wb_stb_i)s),
      .wb_we_i  (%(wb_we_i)s),
      .wb_sel_i (%(wb_sel_i)s),
      .wb_adr_i (%(wb_adr_i)s),
      .wb_dat_i (%(wb_dat_i)s),
      .wb_dat_o (%(wb_dat_o)s),
      .wb_ack_o (%(wb_ack_o)s),
      .wb_err_o (%(wb_err_o)s)
   );
   """
   
   wb_dat_o.driven  = "wire"
   wb_ack_o.driven  = "wire"
   wb_err_o.driven  = "wire"

   return logic

def convert():
   wb_clk_i, wb_rst_i, wbm_cyc_i, wbm_stb_i, wbm_we_i, wbm_sel_i, wbm_adr_i, wbm_dat_i, wbm_dat_o, wbm_ack_o, wbm_err_o, = [Signal(bool(0))for i in range(11)]

   toVerilog(sys_block_wrapper, "inst", wb_clk_i, wb_rst_i, wbm_cyc_i, wbm_stb_i, wbm_we_i, wbm_sel_i, wbm_adr_i, wbm_dat_i, wbm_dat_o, wbm_ack_o, wbm_err_o)

if __name__ == "__main__":
   convert()

