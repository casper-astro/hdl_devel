#==============================================================================#
#                                                                              # 
#      Software Register wrapper and simulation model                          # 
#                                                                              # 
#      Module name: sw_reg_wrapper                                             # 
#      Desc: wraps the verilog sw_reg and provides a model for simulation      # 
#      Date: Jan 2012                                                          # 
#      Developer: Wesley New                                                   # 
#      Licence: GNU General Public License ver 3                               # 
#      Notes:                                                                  # 
#                                                                              # 
#==============================================================================#

from myhdl import *

def sw_reg_r_wrapper(block_name,
      #===============
      # fabric ports
      #===============
      fabric_clk,
      fabric_data_in,

      #============
      # wb inputs
      #============
      wb_clk_i,
      wb_rst_i,
      wb_cyc_i,
      wb_stb_i,
      wb_we_i,
      wb_sel_i,
      wb_adr_i,
      wb_dat_i,

      #=============
      # wb outputs
      #=============
      wb_dat_o,
      wb_ack_o,
      wb_err_o,

      #=============
      # Parameters
      #=============
      C_BASEADDR      = 0,
      C_HIGHADDR      = 32,
      C_WB_DATA_WIDTH = 32,
      C_WB_ADDR_WIDTH = 1,
      C_BYTE_EN_WIDTH = 4
   ):

   #========================
   # TODO:Simulation Logic
   #========================
   @always(wb_clk_i.posedge)
   def logic():
      if (rst == 0 and out < COUNT_TO):
         if (en == 1):
            out == out + STEP
      else:
         out = COUNT_FROM


   # removes warning when converting to hdl
   fabric_data_in.driven = "wire"
   wb_dat_o.driven = "wire"
   wb_ack_o.driven = "wire"
   wb_err_o.driven = "wire"

   return logic


#=====================================
# Software Reg Verilog Instantiation
#=====================================
sw_reg_r_wrapper.verilog_code = \
"""
sw_reg_r
#(
   .C_BASEADDR      ($C_BASEADDR), 
   .C_HIGHADDR      ($C_HIGHADDR), 
   .C_WB_DATA_WIDTH ($C_WB_DATA_WIDTH), 
   .C_WB_ADDR_WIDTH ($C_WB_ADDR_WIDTH), 
   .C_BYTE_EN_WIDTH ($C_BYTE_EN_WIDTH)  
) sw_reg_r_$block_name (
  
   .fabric_clk     ($fabric_clk),
   .fabric_data_in ($fabric_data_in),
                                    
   .wb_clk_i       ($wb_clk_i),
   .wb_rst_i       ($wb_rst_i),
   .wb_cyc_i       ($wb_cyc_i),
   .wb_stb_i       ($wb_stb_i),
   .wb_we_i        ($wb_we_i),
   .wb_sel_i       ($wb_sel_i),
   .wb_adr_i       ($wb_adr_i),
   .wb_dat_i       ($wb_dat_i),
                                    
   .wb_dat_o       ($wb_dat_o),
   .wb_ack_o       ($wb_ack_o),
   .wb_err_o       ($wb_err_o)
);
"""


#=======================================
# For testing of conversion to verilog
#=======================================
def convert():

   fabric_clk,fabric_data_in,wb_clk_i,wb_rst_i,wb_cyc_i,wb_stb_i,wb_we_i,wb_sel_i,wb_adr_i,wb_dat_i,wb_dat_o,wb_ack_o,wb_err_o = [Signal(bool(0)) for i in range(13)]

   toVerilog(sw_reg_r_wrapper, block_name="sw_reg", fabric_clk=fabric_clk,fabric_data_in=fabric_data_in,wb_clk_i=wb_clk_i,wb_rst_i=wb_rst_i,wb_cyc_i=wb_cyc_i,wb_stb_i=wb_stb_i,wb_we_i=wb_we_i,wb_sel_i=wb_sel_i,wb_adr_i=wb_adr_i,wb_dat_i=wb_dat_i,wb_dat_o=wb_dat_o,wb_ack_o=wb_ack_o,wb_err_o=wb_err_o)


if __name__ == "__main__":
   convert()

