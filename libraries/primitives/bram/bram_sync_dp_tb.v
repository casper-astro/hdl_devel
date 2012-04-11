//============================================================================//
//                                                                            //
//      BRAM dual port test bench                                             //
//                                                                            //
//      Module name: bram_sync_dp_tb                                          //
//      Desc: runs and tests the BRAM dual port module, and provides and      //
//            interface to test the module from Python (MyHDL)                //
//      Date: Dec 2011                                                        //
//      Developer: Wesley New                                                 //
//      Licence: GNU General Public License ver 3                             //
//      Notes: This only tests the basic functionality of the module, more    //
//             comprehensive testing is done in the python test file          //
//                                                                            //
//============================================================================//

module bram_sync_dp_tb;

   //===================
   // local parameters
   //===================
   localparam LOCAL_DATA_WIDTH = 2;
   localparam LOCAL_ADDR_WIDTH = 4;
   localparam LOCAL_DATA_DEPTH = 2**LOCAL_ADDR_WIDTH;

   //=============
   // local regs
   //=============
   reg                        clk;
   reg                        a_wr;
   reg [LOCAL_ADDR_WIDTH-1:0] a_addr;
   reg [LOCAL_DATA_WIDTH-1:0] a_data_in;
   reg                        b_wr;
   reg [LOCAL_ADDR_WIDTH-1:0] b_addr;
   reg [LOCAL_DATA_WIDTH-1:0] b_data_in;

   //==============
   // local wires 
   //==============
   wire [LOCAL_DATA_WIDTH-1:0] a_data_out;
   wire [LOCAL_DATA_WIDTH-1:0] b_data_out;

   
   //=====================================
   // instance, "(d)esign (u)nder (t)est"
   //=====================================
   bram_sync_dp #(
      .DATA_WIDTH (`ifdef DATA_WIDTH `DATA_WIDTH `else 2 `endif),
      
      .DATA_DEPTH (`ifdef DATA_DEPTH `DATA_DEPTH `else 2 `endif)
   ) dut (

      .a_clk      (clk),
      .a_wr       (a_wr),
      .a_addr     (a_addr),
      .a_data_in  (a_data_in),
      .a_data_out (a_data_out),
      
      .b_clk      (clk),
      .b_wr       (b_wr),
      .b_addr     (b_addr),
      .b_data_in  (b_data_in),
      .b_data_out (b_data_out)
   );

//==============
// MyHDL ports
//==============
`ifdef MYHDL
   // define what myhdl takes over
   // only if we're running myhdl   
   initial begin
      $from_myhdl(clk, en, rst);
      $to_myhdl(out);
   end
`else

   //=============
   // initialize
   //=============
   initial
      begin
         $dumpvars;
         clk = 0;
         a_addr = 4'b0110; 
         a_data_in = 32'b1010101010101;
         a_wr = 1;
         
         #5 a_wr = 0;

         #10 b_wr = 0;
         #10 b_addr = 4'b0110;

      end

   //=====================
   // simulate the clock
   //=====================
   always #1
      begin
         clk = ~clk;
      end

   //===============
   // print output
   //===============
   always
      #1 $display(b_data_out);

   //===================
   // finish condition 
   //===================
   // 2 time units = 1 clock cycle
   initial #100 $finish;

`endif

endmodule

