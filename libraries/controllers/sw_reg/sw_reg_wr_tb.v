//============================================================================//
//                                                                            //
//      Software Reg test bench                                               //
//                                                                            //
//      Module name: sw_reg_tb                                                //
//      Desc: runs and tests the sw_reg module, and provides and interface    //
//            to test the module from Python (MyHDL)                          //
//      Date: Dec 2011                                                        //
//      Developer: Wesley New                                                 //
//      Licence: GNU General Public License ver 3                             //
//      Notes: This only tests the basic functionality of the module, more    //
//             comprehensive testing is done in the python test file          //
//                                                                            //
//============================================================================//

module sw_reg_wr_tb;

   //=====================
   // local wires & regs
   //=====================
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

   reg         fabric_clk;
   wire        fabric_data_out;


   //=====================================
   // instance, "(d)esign (u)nder (t)est"
   //=====================================
   sw_reg_wr #(
      .C_BASEADDR (32'h00000000),
      .C_HIGHADDR (32'h0000FFFF)
   ) dut (
      
      .wb_rst_i   (wb_rst_i),
      .wb_cyc_i   (wb_cyc_i),
      .wb_stb_i   (wb_stb_i),
      .wb_we_i    (wb_we_i),
      .wb_sel_i   (wb_sel_i),
      .wb_adr_i   (wb_adr_i),
      .wb_dat_i   (wb_dat_i),
      .wb_dat_o   (wb_dat_o),
      .wb_ack_o   (wb_ack_o),
      .wb_err_o   (wb_err_o),
   
      .fabric_clk      (fabric_clk),
      .fabric_data_out (fabric_data_out)
   
   );

//==============
// MyHDL hooks
//==============
`ifdef MYHDL
   // define what myhdl takes over
   // only if we're running myhdl   
   initial begin
      $from_myhdl(fabric_clk, wb_clk_i, wb_rst_i, wb_cyc_i, wb_stb_i, wb_we_i, wb_sel_i, wb_adr_i, wb_dat_i);
      $to_myhdl(fabric_data_in, wb_dat_o,wb_ack_o,wb_err_o);
   end
`else

   //==============
   // Initialize
   //==============
   initial
      begin
         $dumpvars;

         wb_clk_i = 0;
         wb_sel_i = 4'hE;
         wb_stb_i = 1;
         wb_cyc_i = 1;
         wb_we_i  = 1;
         wb_adr_i = 32'h00000000;
         wb_dat_i = 32'hEEEEEEEE;

         #5 
         
         wb_stb_i = 0;
         wb_cyc_i = 0;
      
         #5
         
         wb_adr_i = 32'h00000000;
         wb_stb_i = 1;
         wb_cyc_i = 1;
         wb_we_i = 0;
         
         #20 $finish;
      end

   //=====================
   // Simulate the Clock
   //=====================
   always #1
      wb_clk_i = ~wb_clk_i;

`endif

endmodule
