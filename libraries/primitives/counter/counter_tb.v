//============================================================================//
//                                                                            //
//      Counter test bench                                                    //
//                                                                            //
//      Module name: counter_tb                                               //
//      Desc: runs and tests the counter module, and provides and interface   //
//            to test the module from Python (MyHDL)                          //
//      Date: Oct 2011                                                        //
//      Developer: Rurik Primiani & Wesley New                                //
//      Licence: GNU General Public License ver 3                             //
//      Notes: This only tests the basic functionality of the module, more    //
//             comprehensive testing is done in the python test file          //
//                                                                            //
//============================================================================//

module counter_tb;

   //===================
   // local parameters
   //===================
   localparam LOCAL_DATA_WIDTH = `ifdef DATA_WIDTH `DATA_WIDTH `else 8 `endif;

   //=============
   // local regs
   //=============
   reg clk;
   reg en;
   reg rst;
   
   //==============
   // local wires
   //==============
   wire [LOCAL_DATA_WIDTH-1:0] out;

   //=====================================
   // instance, "(d)esign (u)nder (t)est"
   //=====================================
   counter #(
       .ARCHITECTURE (`ifdef ARCHITECTURE `ARCHITECTURE `else "BEHAVIORAL" `endif),
       .DATA_WIDTH   (`ifdef DATA_WIDTH   `DATA_WIDTH   `else 8            `endif),
       .COUNT_FROM   (`ifdef COUNT_FROM   `COUNT_FROM   `else 0            `endif),
       .COUNT_TO     (`ifdef COUNT_TO     `COUNT_TO     `else 255          `endif),
       .STEP         (`ifdef STEP         `STEP         `else 1            `endif)
    ) dut (
		   .clk (clk), 
		   .en  (en), 
		   .rst (rst), 
		   .out (out)
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
      clk = 0;
      en = 1;
      rst = 0;
   end

   //====================
   // simulate the clock
   //====================
   always #1
   begin
	    clk = ~clk;
   end

   //===============
   // print output
   //===============
   always @(posedge clk) $display(out);
   
   //===============================
   // finish after 100 clock cycles
   //===============================
   initial #200 $finish;

`endif
   
endmodule
