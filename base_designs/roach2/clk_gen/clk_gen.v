module clk_gen #(
     parameter ARCHITECTURE = "VIRTEX6",
     parameter CLK_FREQ = 200
   ) (
     input  clk100,
     input  rst,
     output clk0,
     output clk180,
     output clk270,
     output clkdiv2,
     output pll_lock
   );
   /********** Clock Generation ***********/
 
   wire dcm_clk;
   wire dcm_clk_lock;
 
   localparam FX_MULT = CLK_FREQ == 150 ?  6 :
                        CLK_FREQ == 200 ?  8 :
                        CLK_FREQ == 250 ? 10 :
                        CLK_FREQ == 266 ?  8 :
                        CLK_FREQ == 300 ?  9 :
                        CLK_FREQ == 333 ? 10 :
                        CLK_FREQ == 350 ?  7 :
                                           8;
 
   localparam FX_DIV  = CLK_FREQ == 150 ? 4 :
                        CLK_FREQ == 200 ? 4 :
                        CLK_FREQ == 250 ? 4 :
                        CLK_FREQ == 266 ? 3 :
                        CLK_FREQ == 300 ? 3 :
                        CLK_FREQ == 333 ? 3 :
                        CLK_FREQ == 350 ? 2 :
                                          4;
 
   wire clk0_int;
   wire clk180_int;
   wire clk270_int;
   wire clkdiv2_int;
   wire fb_clk;
 
   // Generate according to implementation
   generate
   case (ARCHITECTURE)
      "VIRTEX6" :
      begin
         MMCM_BASE #(
            .BANDWIDTH          ("OPTIMIZED"), // Jitter programming ("HIGH","LOW","OPTIMIZED")
            .CLKFBOUT_MULT_F    (FX_MULT), // Multiply value for all CLKOUT (5.0-64.0).
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
            .CLKOUT4_PHASE      (180),
            .CLKOUT5_PHASE      (0.0),
            .CLKOUT6_PHASE      (0.0),
            .CLKOUT1_DIVIDE     (FX_DIV),
            .CLKOUT2_DIVIDE     (FX_DIV),
            .CLKOUT3_DIVIDE     (FX_DIV*2),
            .CLKOUT4_DIVIDE     (FX_DIV),
            .CLKOUT5_DIVIDE     (FX_DIV),
            .CLKOUT6_DIVIDE     (FX_DIV),
            .CLKOUT4_CASCADE    ("FALSE"),
            .CLOCK_HOLD         ("FALSE"),
            .DIVCLK_DIVIDE      (1), // Master division value (1-80)
            .REF_JITTER1        (0.0),
            .STARTUP_WAIT       ("FALSE")
         ) MMCM_BASE_inst (
            .CLKIN1   (clk100),
            .CLKFBIN  (fb_clk),
 
            .CLKFBOUT  (fb_clk),
            .CLKFBOUTB (),
 
            .CLKOUT0  (),
            .CLKOUT0B (),
            .CLKOUT1  (clk0_int),
            .CLKOUT1B (),
            .CLKOUT2  (clk270_int),
            .CLKOUT2B (),
            .CLKOUT3  (clkdiv2_int),
            .CLKOUT3B (),
            .CLKOUT4  (clk180_int),
            .CLKOUT5  (),
            .CLKOUT6  (),
            .LOCKED   (pll_lock),
 
            .PWRDWN   (1'b0),
            .RST      (rst)
 
         );
 
         BUFG bufg_arr[3:0](
           .I({clk0_int, clk180_int, clk270_int, clkdiv2_int}),
           .O({clk0,     clk180,     clk270,     clkdiv2})
         );
      end
   endcase
   endgenerate
endmodule
