from myhdl import *
import clk_infrastructure.clk_infrastructure as clk_infrastructure
import epb_infrastructure.epb_infrastructure as epb_infrastructure
import epb_wb_bridge.epb_wb_bridge           as epb_wb_bridge
import reset_block.reset_block               as reset_block
import sys_block.sys_block                   as sys_block
import wbs_arbiter.wbs_arbiter               as wbs_arbiter       


def toplevel(
    sys_clk_n,
    sys_clk_p,

    aux_clk_n,
    aux_clk_p,
    #aux_synci_n,
    #aux_synci_p,
    #aux_synco_n,
    #aux_synco_p,

    v6_gpio,     #[15:0]
                       
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
   
   sys_clk, sys_clk90, sys_clk180, sys_clk270, sys_clk_lock, op_power_on_rst, sys_clk2x, sys_clk2x90, sys_clk2x180, sys_clk2x270, epb_clk_in, epb_clk, aux_clk, aux_clk90, aux_clk180, aux_clk270, aux_clk2x, aux_clk2x90, aux_clk2x180, aux_clk2x270 = [Signal(bool(0)) for i in range(20)]

   clk_infr = clk_infrastructure.clk_infrastructure_wrapper("1", sys_clk_n, sys_clk_p, sys_clk, sys_clk90, sys_clk180, sys_clk270, sys_clk_lock, op_power_on_rst, sys_clk2x, sys_clk2x90, sys_clk2x180, sys_clk2x270, epb_clk_in, epb_clk, aux_clk_n, aux_clk_p, aux_clk, aux_clk90, aux_clk180, aux_clk270, aux_clk2x, aux_clk2x90, aux_clk2x180, aux_clk2x270)

   rst_blk = reset_block.reset_block_wrapper("1", sys_clk, Signal(bool(0)), Signal(bool(0)), op_power_on_rst) # maybe change clock to slower epb clock

   wb_clk_i, wb_rst_i, wb_cyc_o, wb_stb_o, wb_we_o, wb_sel_o, wb_adr_o, wb_dat_o, wb_dat_i, wb_ack_i, wb_err_i, epb_clk, epb_data_i, epb_data_o, epb_data_oe_n = [Signal(bool(0)) for i in range(15)]
   
   epb_wb_brdg = epb_wb_bridge.epb_wb_bridge_wrapper("1", wb_clk_i, wb_rst_i,wb_cyc_o, wb_stb_o, wb_we_o, wb_sel_o, wb_adr_o, wb_dat_o, wb_dat_i, wb_ack_i, wb_err_i, epb_clk, ppc_pcsn, ppc_poen, ppc_pwrn, ppc_pben, ppc_paddr, epb_data_i, epb_data_o, epb_data_oe_n, ppc_prdy, ppc_doen)

   epb_infr = epb_infrastructure.epb_infrastructure_wrapper("1", ppc_pdata, epb_data_oe_n, epb_data_o, epb_data_i, ppc_per_clk, epb_clk)

   return clk_infr, rst_blk, epb_wb_brdg, epb_infr

   #sys_block.sys_block_wrapper("1", )
   #wbs_arbiter.wbs_arbiter_wrapper("1", )


def convert():
   sys_clk_n, sys_clk_p, aux_clk_n, aux_clk_p = [Signal(bool(0)) for i in range(4)]
   ppc_per_clk, ppc_poen, ppc_pwrn, ppc_pblastn, ppc_prdy, ppc_doen, v6_irqn = [Signal(bool(0)) for i in range(7)]
   ppc_paddr = Signal(intbv(0)[29:5])   #[5:29]
   ppc_pcsn  = Signal(intbv(0)[1:])     #[1:0]
   ppc_pdata = Signal(intbv(0)[31:])   #[0:31]
   ppc_pben  = Signal(intbv(0)[3:])     #[0:3]

   gpio = Signal(intbv(0)[16:])
   toVerilog(toplevel, sys_clk_n, sys_clk_p, aux_clk_n, aux_clk_p, gpio, ppc_per_clk, ppc_paddr, ppc_pcsn, ppc_pdata, ppc_pben, ppc_poen, ppc_pwrn, ppc_pblastn, ppc_prdy, ppc_doen, v6_irqn)


if __name__ == "__main__":
   convert()

