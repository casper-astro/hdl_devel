from myhdl import *
import clk_infrastructure.clk_infrastructure as clk_infrastructure
import epb_infrastructure.epb_infrastructure as epb_infrastructure
import epb_wb_bridge.epb_wb_bridge           as epb_wb_bridge
import reset_block.reset_block               as reset_block
import sys_block.sys_block                   as sys_block
import wbs_arbiter.wbs_arbiter               as wbs_arbiter       
import counter.counter                       as counter

def toplevel(
    sys_clk_n,
    sys_clk_p,

    aux_clk_n,
    aux_clk_p,
    #aux_synci_n,
    #aux_synci_p,
    #aux_synco_n,
    #aux_synco_p,

    gpio,     #[15:0]
                       
    ppc_per_clk, # is this the epb clock?       
    ppc_paddr,   #[5:29]
                  
    ppc_pcsn,     #[1:0]
    ppc_pdata,   #[0:31]
    ppc_pben,     #[0:3]
    ppc_poen,          
    ppc_pwrn,          
    ppc_pblastn,       
    ppc_prdy,          
    ppc_doen,          

    v6_irqn
):
   
   

   sys_rst, sys_clk, sys_clk90, sys_clk180, sys_clk270, sys_clk_lock, power_on_rst, sys_clk2x, sys_clk2x90, sys_clk2x180, sys_clk2x270, aux_clk, aux_clk90, aux_clk180, aux_clk270, aux_clk2x, aux_clk2x90, aux_clk2x180, aux_clk2x270, idelay_rdy = [Signal(bool(0)) for i in range(20)]

   wbm_clk_i, wbm_rst_i, wbm_cyc_o, wbm_stb_o, wbm_we_o, wbm_sel_o, wbm_adr_o, wbm_dat_o, wbm_dat_i, wbm_ack_i, wbm_err_i, epb_clk, epb_data_i, epb_data_o, epb_data_oe_n = [Signal(bool(0)) for i in range(15)]
   
   clk_infr = clk_infrastructure.clk_infrastructure_wrapper(
      block_name      = "1", 
      sys_clk_n       = sys_clk_n, 
      sys_clk_p       = sys_clk_p, 
      sys_clk         = sys_clk, 
      sys_clk90       = sys_clk90, 
      sys_clk180      = sys_clk180, 
      sys_clk270      = sys_clk270, 
      sys_clk_lock    = sys_clk_lock, 
      op_power_on_rst = power_on_rst, 
      sys_clk2x       = sys_clk2x, 
      sys_clk2x90     = sys_clk2x90, 
      sys_clk2x180    = sys_clk2x180, 
      sys_clk2x270    = sys_clk2x270, 
      epb_clk_in      = ppc_per_clk, 
      epb_clk         = epb_clk, 
      aux_clk_n       = aux_clk_n, 
      aux_clk_p       = aux_clk_p, 
      aux_clk         = aux_clk, 
      aux_clk90       = aux_clk90, 
      aux_clk180      = aux_clk180, 
      aux_clk270      = aux_clk270, 
      aux_clk2x       = aux_clk2x, 
      aux_clk2x90     = aux_clk2x90, 
      aux_clk2x180    = aux_clk2x180, 
      aux_clk2x270    = aux_clk2x270, 
      idelay_rst      = power_on_rst, 
      idelay_rdy      = idelay_rdy
   )

   # maybe change clock to slower epb clock
   rst_blk = reset_block.reset_block_wrapper(
      block_name  = "1", 
      clk         = sys_clk, 
      async_rst_i = power_on_rst, 
      rst_i       = power_on_rst, 
      rst_o       = sys_rst
   ) 

  
   wbm_clk_i = epb_clk
 
   epb_wb_brdg = epb_wb_bridge.epb_wb_bridge_wrapper(
      block_name = "1", 
      wb_clk_i      = wbm_clk_i, 
      wb_rst_i      = wbm_rst_i, 
      wb_cyc_o      = wbm_cyc_o, 
      wb_stb_o      = wbm_stb_o, 
      wb_we_o       = wbm_we_o, 
      wb_sel_o      = wbm_sel_o, 
      wb_adr_o      = wbm_adr_o, 
      wb_dat_o      = wbm_dat_o, 
      wb_dat_i      = wbm_dat_i, 
      wb_ack_i      = wbm_ack_i, 
      wb_err_i      = wbm_err_i, 
      epb_clk       = epb_clk, 
      epb_cs_n      = ppc_pcsn, 
      epb_oe_n      = ppc_poen, 
      epb_r_w_n     = ppc_pwrn, 
      epb_be_n      = ppc_pben, 
      epb_addr      = ppc_paddr, 
      epb_data_o    = epb_data_o, 
      epb_data_i    = epb_data_i, 
      epb_data_oe_n = epb_data_oe_n, 
      epb_rdy       = ppc_prdy, 
      epb_doen      = ppc_doen
   )

   wbs_cyc_o, wbs_stb_o, wbs_we_o, wbs_sel_o, wbs_adr_o, wbs_dat_o, wbs_dat_i, wbs_ack_i, wbs_err_i = [Signal(bool(0)) for i in range(9)]
   
   epb_infr = epb_infrastructure.epb_infrastructure_wrapper(
      block_name    = "1", 
      epb_data_buf  = ppc_pdata, 
      epb_data_oe_n = epb_data_oe_n, 
      epb_data_i    = epb_data_i, 
      epb_data_o    = epb_data_o
   )

   wbs_arb = wbs_arbiter.wbs_arbiter_wrapper(
      block_name = "1", 
      wb_clk_i   = wbm_clk_i, 
      wb_rst_i   = wbm_rst_i, 
      wbm_cyc_i  = wbm_cyc_o, 
      wbm_stb_i  = wbm_stb_o, 
      wbm_we_i   = wbm_we_o, 
      wbm_sel_i  = wbm_sel_o, 
      wbm_adr_i  = wbm_adr_o, 
      wbm_dat_i  = wbm_dat_o, 
      wbm_dat_o  = wbm_dat_i, 
      wbm_ack_o  = wbm_ack_i, 
      wbm_err_o  = wbm_err_i, 
      wbs_cyc_o  = wbs_cyc_o, 
      wbs_stb_o  = wbs_stb_o, 
      wbs_we_o   = wbs_we_o, 
      wbs_sel_o  = wbs_sel_o, 
      wbs_adr_o  = wbs_adr_o, 
      wbs_dat_o  = wbs_dat_o, 
      wbs_dat_i  = wbs_dat_i, 
      wbs_ack_i  = wbs_ack_i
   )

   sys_blk = sys_block.sys_block_wrapper(
      block_name = "1", 
      wb_clk_i   = wbm_clk_i, 
      wb_rst_i   = wbm_rst_i, 
      wb_cyc_i   = wbs_cyc_o, 
      wb_stb_i   = wbs_stb_o, 
      wb_we_i    = wbs_we_o, 
      wb_sel_i   = wbs_sel_o, 
      wb_adr_i   = wbs_adr_o, 
      wb_dat_i   = wbs_dat_o, 
      wb_dat_o   = wbs_dat_i, 
      wb_ack_o   = wbs_ack_i, 
      wb_err_o   = wbs_err_i
   )


   count_out = Signal(intbv(0)[32:])
   
   cntr = counter.counter_wrapper(
      block_name = "1", 
      clk        = sys_clk, 
      en         = 1, 
      rst        = 0, 
      out        = count_out
   )

   @always_comb
   def logic():
      gpio.next = count_out[32:16]

   return clk_infr, rst_blk, epb_wb_brdg, epb_infr, wbs_arb, sys_blk, cntr, logic





def convert():
   sys_clk_n, sys_clk_p, aux_clk_n, aux_clk_p = [Signal(bool(0)) for i in range(4)]
   ppc_per_clk, ppc_poen, ppc_pwrn, ppc_pblastn, ppc_prdy, ppc_doen, v6_irqn = [Signal(bool(0)) for i in range(7)]
   ppc_paddr = Signal(intbv(0)[29:5])   #[5:29]
   ppc_pcsn  = Signal(intbv(0)[1:])     #[1:0]
   ppc_pben  = Signal(intbv(0)[3:])     #[0:3]

   ppc_pdata = TristateSignal(intbv(0)[31:])   #[0:31]
   gpio = Signal(intbv(0)[16:])
   
   toVerilog(
      toplevel, 
      sys_clk_n, 
      sys_clk_p, 
      aux_clk_n, 
      aux_clk_p, 
      gpio, 
      ppc_per_clk, 
      ppc_paddr, 
      ppc_pcsn, 
      ppc_pdata, 
      ppc_pben, 
      ppc_poen, 
      ppc_pwrn, 
      ppc_pblastn, 
      ppc_prdy, 
      ppc_doen, 
      v6_irqn
   )


if __name__ == "__main__":
   convert()

