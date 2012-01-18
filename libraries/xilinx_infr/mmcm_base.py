#==============================================================================#
#                                                                              #
#      mmcm_base wrapper and simulation model                                  #
#                                                                              #
#      Module name: mmcm_base_wrapper                                          #
#      Desc: wraps the xilinx mmcm_base in Python and provides a model for     #
#            simulation                                                        #
#            MMCM_BASE: The MMCM primitive in Virtex-6 parts is used to        #
#            generate multiple clocks with defined phase and frequency         #
#            relationships to a given input clock. The MMCM module is a        #
#            wrapper around the MMCM_ADV primitive that allows the MMCM to be  #
#            used in the EDK tool suite. The MMCM (V6) replaces the DCM (V5)   #
#      Date: Dec 2011                                                          #
#      Developer: Wesley New                                                   #
#      Licence: GNU General Public License ver 3                               #
#      Notes:                                                                  #
#                                                                              #
#==============================================================================#

from myhdl import *

def mmcm_base_wrapper (block_name,
      #========
      # Ports
      #========
      clk_in_1,
      clk_fb_in,
      
      clk_out_0, clk_out_0B,
      clk_out_1, clk_out_1B,
      clk_out_2, clk_out_2B,
      clk_out_3, clk_out_3B,
      clk_out_4, clk_out_4B,
      clk_out_5, clk_out_5B,
      clk_out_6, clk_out_6B,
      
      clk_fb_out, clk_fb_outb,

      locked,
      pwr_down,
      rst,

      #=============
      # Parameters 
      #=============
      BANDWIDTH,
      CLKFBOUT_MULT_F,
      CLKFBOUT_PHASE,
      CLKIN1_PERIOD,
      CLKOUT0_DIVIDE_F,
      CLKOUT0_DUTY_CYCLE,
      CLKOUT1_DUTY_CYCLE,
      CLKOUT2_DUTY_CYCLE,
      CLKOUT3_DUTY_CYCLE,
      CLKOUT4_DUTY_CYCLE,
      CLKOUT5_DUTY_CYCLE,
      CLKOUT6_DUTY_CYCLE,
      CLKOUT0_PHASE,
      CLKOUT1_PHASE,
      CLKOUT2_PHASE,
      CLKOUT3_PHASE,
      CLKOUT4_PHASE,
      CLKOUT5_PHASE,
      CLKOUT6_PHASE,
      CLKOUT1_DIVIDE,
      CLKOUT2_DIVIDE,
      CLKOUT3_DIVIDE,
      CLKOUT4_DIVIDE,
      CLKOUT5_DIVIDE,
      CLKOUT6_DIVIDE,
      CLKOUT4_CASCADE,
      CLOCK_HOLD,
      DIVCLK_DIVIDE,
      REF_JITTER1,
      STARTUP_WAIT
   ):

   #===================
   # TODO: Simulation Logic
   #===================
   @always(clk_n.posedge)
   def logic():
      clk_out_0.next = clk_in_1


   # removes warning when converting to hdl   
   clk_ds.driven = "wire"

   return logic

   
#==========================
# MMCM_BASE Instantiation
#==========================
mmcm_base_wrapper.verilog_code = \
"""
MMCM_BASE
#(
   .BANDWIDTH          ($BANDWIDTH),         // Jitter programming ("HIGH","LOW","OPTIMIZED")
   .CLKFBOUT_MULT_F    ($CLKFBOUT_MULT_F),   // Multiply value for all CLKOUT (5.0-64.0).
   .CLKFBOUT_PHASE     ($CLKFBOUT_PHASE),
   .CLKIN1_PERIOD      ($CLKIN1_PERIOD),
   .CLKOUT0_DIVIDE_F   ($CLKOUT0_DIVIDE_F),  // Divide amount for CLKOUT0 (1.000-128.000).
   .CLKOUT0_DUTY_CYCLE ($CLKOUT0_DUTY_CYCLE),
   .CLKOUT1_DUTY_CYCLE ($CLKOUT1_DUTY_CYCLE),
   .CLKOUT2_DUTY_CYCLE ($CLKOUT2_DUTY_CYCLE),
   .CLKOUT3_DUTY_CYCLE ($CLKOUT3_DUTY_CYCLE),
   .CLKOUT4_DUTY_CYCLE ($CLKOUT4_DUTY_CYCLE),
   .CLKOUT5_DUTY_CYCLE ($CLKOUT5_DUTY_CYCLE),
   .CLKOUT6_DUTY_CYCLE ($CLKOUT6_DUTY_CYCLE),
   .CLKOUT0_PHASE      ($CLKOUT0_PHASE),
   .CLKOUT1_PHASE      ($CLKOUT1_PHASE),
   .CLKOUT2_PHASE      ($CLKOUT2_PHASE),
   .CLKOUT3_PHASE      ($CLKOUT3_PHASE),
   .CLKOUT4_PHASE      ($CLKOUT4_PHASE),
   .CLKOUT5_PHASE      ($CLKOUT5_PHASE),
   .CLKOUT6_PHASE      ($CLKOUT6_PHASE),
   .CLKOUT1_DIVIDE     ($CLKOUT1_DIVIDE),
   .CLKOUT2_DIVIDE     ($CLKOUT2_DIVIDE),
   .CLKOUT3_DIVIDE     ($CLKOUT3_DIVIDE),
   .CLKOUT4_DIVIDE     ($CLKOUT4_DIVIDE),
   .CLKOUT5_DIVIDE     ($CLKOUT5_DIVIDE),
   .CLKOUT6_DIVIDE     ($CLKOUT6_DIVIDE),
   .CLKOUT4_CASCADE    ($CLKOUT4_CASCADE),
   .CLOCK_HOLD         ($CLOCK_HOLD),
   .DIVCLK_DIVIDE      ($DIVCLK_DIVIDE),     // Master division value (1-80)
   .REF_JITTER1        ($REF_JITTER1),
   .STARTUP_WAIT       ($STARTUP_WAIT)
) MMCM_BASE_$block_name (
   .CLKIN1    ($clk_in_1),
   .CLKFBIN   ($clk_fb_in),

   .CLKOUT0   ($clk_out_0),
   .CLKOUT0B  ($clk_out_0b),
   .CLKOUT1   ($clk_out_1),
   .CLKOUT1B  ($clk_out_1b),
   .CLKOUT2   ($clk_out_2),
   .CLKOUT2B  ($clk_out_2b),
   .CLKOUT3   ($clk_out_3),
   .CLKOUT3B  ($clk_out_3b),
   .CLKOUT4   ($clk_out_4),
   .CLKOUT5   ($clk_out_5),
   .CLKOUT6   ($clk_out_6),
   .LOCKED    ($locked),

   .CLKFBOUT  ($clk_fb_out),
   .CLKFBOUTB ($clk_fb_outb),

   .PWRDWN    ($pwr_down),
   .RST       ($rst)

);
"""

# incomplete
def convert():
   clk_n, clk_p, clk_ds = [Signal(bool(0)) for i in range(3)]
   #toVerilog(mmcm_base_wrapper, "1", clk_n, clk_p, clk_ds)

if __name__ == "__main__":
   convert()
