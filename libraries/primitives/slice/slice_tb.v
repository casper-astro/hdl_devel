//============================================================================//
//                                                                            //
//      Slice test bench                                                      //
//                                                                            //
//      Module name: slice_tb                                                 //
//      Desc: runs and tests the slice module, and provides and interface     //
//            to test the module from Python (MyHDL)                          //
//      Date: Nov 2011                                                        //
//      Developer: Wesley New                                                 //
//      Licence: GNU General Public License ver 3                             //
//      Notes: This only tests the basic functionality of the module, more    //
//             comprehensive testing is done in the python test file          //
//                                                                            //
//============================================================================//

module slice_tb;

   //===================
   // local parameters
   //==================
   localparam LOCAL_DATA_WIDTH = `ifdef DATA_WIDTH `DATA_WIDTH `else 8 `endif;
   
   //=============
   // local regs
   //=============
   reg clk;
   reg[LOCAL_DATA_WIDTH-1:0] data_in;
   
   //==============
   // local wires
   //==============
   wire [5-1:0] data_out;

   //=====================================
   // instance, "(d)esign (u)nder (t)est"
   //=====================================
   slice # (
      .ARCHITECTURE      (`ifdef ARCHITECTURE      `ARCHITECTURE      `else "BEHAVIORAL" `endif),
      .INPUT_DATA_WIDTH  (`ifdef INPUT_DATA_WIDTH  `INPUT_DATA_WIDTH  `else 8            `endif),
      .OFFSET_REL_TO_MSB (`ifdef OFFSET_REL_TO_MSB `OFFSET_REL_TO_MSB `else 1            `endif),
      .OFFSET_1          (`ifdef OFFSET_1          `OFFSET_1          `else 1            `endif),
      .OFFSET_2          (`ifdef OFFSET_2          `OFFSET_2          `else 5            `endif)
   ) dut (
      .clk(clk), 
      .data_in(data_in), 
      .data_out(data_out)
   );

//==============
// MyHDL ports
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
      data_in = 8'b00001111;
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
   always @(posedge clk) $display(data_out);
      
   //===================
   // finish condition
   //===================
   initial #5 $finish;

`endif
   
endmodule
