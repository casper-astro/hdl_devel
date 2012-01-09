from myhdl import *

def mmcm_base_wrapper (block_name,
   clk_in_1,
   clk_fb_in,
   
   clk_out_0,
   clk_out_0B,
   clk_out_1,
   clk_out_1B,
   clk_out_2,
   clk_out_2B,
   clk_out_3,
   clk_out_3B,
   clk_out_4,
   clk_out_4B,
   clk_out_5,
   clk_out_5B,
   clk_out_6,
   clk_out_6B,
   
   clk_fb_out,
   clk_fb_outb,

   locked,
   pwr_down,
   rst,

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

   @always(clk_n.posedge)
   def logic():
      clk_ds.next = clk_n


   __verilog__ = \
   """
   MMCM_BASE
   #(
      .BANDWIDTH          ("OPTIMIZED"), // Jitter programming ("HIGH","LOW","OPTIMIZED")
      .CLKFBOUT_MULT_F    (6), // Multiply value for all CLKOUT (5.0-64.0).
      .CLKFBOUT_PHASE     (0.0),
      .CLKIN1_PERIOD      (10.0),
      .CLKOUT0_DIVIDE_F   (1.0), // Divide amount for CLKOUT0 (1.000-128.000).
      .CLKOUT0_DUTY_CYCLE (0.5),
      .CLKOUT1_DUTY_CYCLE (0.5),
      .CLKOUT2_DUTY_CYCLE (0.5),
      .CLKOUT3_DUTY_CYCLE (0.5),
      .CLKOUT4_DUTY_CYCLE (0.5),
      .CLKOUT5_DUTY_CYCLE (0.5),
      .CLKOUT6_DUTY_CYCLE (0.5),
      .CLKOUT0_PHASE      (0.0),
      .CLKOUT1_PHASE      (0.0),
      .CLKOUT2_PHASE      (270),
      .CLKOUT3_PHASE      (0.0),
      .CLKOUT4_PHASE      (0.0),
      .CLKOUT5_PHASE      (0.0),
      .CLKOUT6_PHASE      (0.0),
      .CLKOUT1_DIVIDE     (6),
      .CLKOUT2_DIVIDE     (6),
      .CLKOUT3_DIVIDE     (3),
      .CLKOUT4_DIVIDE     (1),
      .CLKOUT5_DIVIDE     (1),
      .CLKOUT6_DIVIDE     (1),
      .CLKOUT4_CASCADE    ("FALSE"),
      .CLOCK_HOLD         ("FALSE"),
      .DIVCLK_DIVIDE      (1), // Master division value (1-80)
      .REF_JITTER1        (0.0),
      .STARTUP_WAIT       ("FALSE")
   ) MMCM_BASE_%(block_name)s (
      .CLKIN1     (%(clk_in_1)s),
      .CLKFBIN    (%(clk_fb_in)s),

      .CLKOUT0    (%(clk_out_0)s),
      .CLKOUT0B   (%(clk_out_0b)s),
      .CLKOUT1    (%(clk_out_1)s),
      .CLKOUT1B   (%(clk_out_1b)s),
      .CLKOUT2    (%(clk_out_2)s),
      .CLKOUT2B   (%(clk_out_2b)s),
      .CLKOUT3    (%(clk_out_3)s),
      .CLKOUT3B   (%(clk_out_3b)s),
      .CLKOUT4    (%(clk_out_4)s),
      .CLKOUT5    (%(clk_out_5)s),
      .CLKOUT6    (%(clk_out_6)s),
      .LOCKED     (%(locked)s),

      .CLKFBOUT   (%(clk_fb_out)s),
      .CLKFBOUTB  (%(clk_fb_outb)s),

      .PWRDWN     (%(pwr_down)s),
      .RST        (%(rst)s)

   );
   """
   
   clk_ds.driven = "wire"

   return logic



def convert():
   clk_n, clk_p, clk_ds = [Signal(bool(0)) for i in range(3)]
   toVerilog(ibufgds_wrapper, "1", clk_n, clk_p, clk_ds)

if __name__ == "__main__":
   convert()
