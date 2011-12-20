module sw_reg_tb;


   reg         wb_clk_i;
   reg         wb_rst_i;
   reg         wb_cyc_i;
   reg         wb_stb_i;
   reg         wb_we_i;
   reg   [3:0] wb_sel_i;
   reg  [31:0] wb_adr_i;
   reg  [31:0] wb_dat_i;
   wire [31:0] wb_dat_o;
   wire        wb_ack_o;
   wire        wb_err_o;

   sw_reg #(
      .C_BASEADDR (32'h00000000),
      .C_HIGHADDR (32'h0000FFFF)
   ) dut (
      .wb_clk_i   (wb_clk_i),
      .wb_rst_i   (wb_rst_i),
      .wb_cyc_i   (wb_cyc_i),
      .wb_stb_i   (wb_stb_i),
      .wb_we_i    (wb_we_i),
      .wb_sel_i   (wb_sel_i),
      .wb_adr_i   (wb_adr_i),
      .wb_dat_i   (wb_dat_i),
      .wb_dat_o   (wb_dat_o),
      .wb_ack_o   (wb_ack_o),
      .wb_err_o   (wb_err_o)
   );

   initial
      begin
         $dumpvars;

         wb_clk_i = 0;
         wb_sel_i = 4'h4;
         wb_stb_i = 1;
         wb_cyc_i = 1;
         wb_we_i = 1;
         wb_adr_i = 32'h00000000;
         wb_dat_i = 32'hEEEEEEEE;
      
         #100 $finish;
      end

   always #1
      wb_clk_i = ~wb_clk_i;



endmodule
