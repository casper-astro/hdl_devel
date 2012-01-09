//============================================================================//
//                                                                            //
//      Bit shift test bench                                                  //
//                                                                            //
//      Module name: bit_shift_tb                                             //
//      Desc: runs and tests the counter module, and provides and interface   //
//            to test the module from Python (MyHDL)                          //
//      Date: Nov 2011                                                        //
//      Developer: Wesley New                                                 //
//      Licence: GNU General Public License ver 3                             //
//      Notes: This only tests the basic functionality of the module, more    //
//             comprehensive testing is done in the python test file          //
//                                                                            //
//============================================================================//

module bit_shift_tb;

   //===================
   // local parameters
   //===================
   localparam LOCAL_DATA_WIDTH = `ifdef DATA_WIDTH `DATA_WIDTH `else 8 `endif;

   //===============
   // declare regs
   //===============
   reg clk;
   reg[LOCAL_DATA_WIDTH-1:0] data_in;
   
   //================
   // declare wires
   //================
   wire [LOCAL_DATA_WIDTH-1:0] data_out;

   //======================================
   // instance, "(d)esign (u)nder (t)est"
   //======================================
   bit_shift #(
      .ARCHITECTURE    (`ifdef ARCHITECTURE      `ARCHITECTURE      `else "BEHAVIORAL" `endif), 
      .DATA_WIDTH      (`ifdef DATA_WIDTH        `DATA_WIDTH        `else 8            `endif),
      .SHIFT_DIRECTION (`ifdef SHIFT_DIRECTION   `SHIFT_DIRECTION   `else 0            `endif),
      .NUMBER_BITS     (`ifdef NUMBER_BITS       `NUMBER_BITS       `else 1            `endif),
      .WRAP            (`ifdef WRAP              `WRAP              `else 0            `endif)
   ) dut (
      .clk     (clk), 
      .data_in (data_in), 
      .data_out(data_out)
	 );


//==============
// MyHDL Ports
//==============
`ifdef MYHDL
      
   // define what myhdl takes over
   // only if we're running myhdl   
   initial begin
      $from_myhdl(clk, data_in, data_out);
      $to_myhdl(data_out);
   end

`else

   //=============
   // initialize
   //=============
   initial
   begin
     clk = 0;
     data_in = 16'b0101010101010101;
   end

   //=====================
   // simulate the clock
   //=====================
   always #1
   begin
      clk = ~clk;
   end

   //===================
   // print the output
   //===================
   always @(posedge clk) $display(data_out);
   
   //========================
   // finish after 3 clocks
   //========================
   initial #3 $finish;

`endif
   
endmodule
