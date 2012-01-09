//============================================================================//
//                                                                            //
//      BRAM single port test bench                                           //
//                                                                            //
//      Module name: bram_sync_sp_tb                                          //
//      Desc: runs and tests the BRAM single port module, and provides and    //
//            interface to test the module from Python (MyHDL)                //
//      Date: Dec 2011                                                        //
//      Developer: Wesley New                                                 //
//      Licence: GNU General Public License ver 3                             //
//      Notes: This only tests the basic functionality of the module, more    //
//             comprehensive testing is done in the python test file          //
//                                                                            //
//============================================================================//

module bram_sync_sp_tb;

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
   reg                        wr;
   reg [LOCAL_ADDR_WIDTH-1:0] addr;
   reg [LOCAL_DATA_WIDTH-1:0] data_in;

   //==============
   // local wires 
   //==============
   wire [LOCAL_DATA_WIDTH-1:0] data_out;

   //=====================================
   // instance, "(d)esign (u)nder (t)est"
   //=====================================
   bram_sync_sp #(
      .DATA_WIDTH (`ifdef DATA_WIDTH `DATA_WIDTH `else 2 `endif),
      .ADDR_WIDTH (`ifdef ADDR_WIDTH `ADDR_WIDTH `else 4 `endif)
   ) dut (

      .clk      (clk),
      .wr       (wr),
      .addr     (addr),
      .data_in  (data_in),
      .data_out (data_out)
   );

   //=============
   // initialize
   //=============   
   initial
      begin
         $dumpvars;
         clk = 0;
         addr = 4'b0110; 
         data_in = 32'b1010101010101;
         wr = 1;
         
         #5 wr = 0;

         #10 wr = 0;
         #10 addr = 4'b0110;

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
      #1 $display(data_out);

   //===================
   // finish condition 
   //===================
   // 2 time units = 1 clock cycle
   initial #100 $finish;

endmodule

