//============================================================================//
//                                                                            //
//      Multilexer test bench                                                 //
//                                                                            //
//      Module name: mux_tb                                                   //
//      Desc: runs and tests the mux module, and provides and interface       //
//            to test the module from Python (MyHDL)                          //
//      Date: Oct 2011                                                        //
//      Developer: Rurik Primiani & Wesley New                                //
//      Licence: GNU General Public License ver 3                             //
//      Notes: This only tests the basic functionality of the module, more    //
//             comprehensive testing is done in the python test file          //
//                                                                            //
//============================================================================//

module mux_tb;

   //===================
   // local parameters
   //===================
   localparam LOCAL_SELECT_LINES = `ifdef SELECT_LINES `SELECT_LINES `else 4 `endif;
   localparam LOCAL_DATA_WIDTH   = `ifdef DATA_WIDTH   `DATA_WIDTH   `else 2 `endif;

   //=============
   // local regs
   //=============
   reg [LOCAL_SELECT_LINES-1:0] select;
   reg [LOCAL_DATA_WIDTH*(2**LOCAL_SELECT_LINES)-1:0] data_in;
   
   //==============
   // local wires
   //==============
   wire [LOCAL_DATA_WIDTH-1:0] data_out; 

   //======================================
   // instance, "(d)esign (u)nder (t)est"
   //======================================
   mux #(
      .ARCHITECTURE (`ifdef ARCHITECTURE `ARCHITECTURE `else "BEHAVIORAL" `endif),
      .SELECT_LINES (`ifdef SELECT_LINES `SELECT_LINES `else 4            `endif),
      .DATA_WIDTH   (`ifdef DATA_WIDTH   `DATA_WIDTH   `else 2            `endif)
   ) dut (
	    .select   (select), 
	    .data_in  (data_in), 
	    .data_out (data_out)
	 );


//==============
// MyHDL ports
//==============
`ifdef MYHDL
    
   // define what myhdl takes over
   // only if we're running myhdl   
   initial begin
      $from_myhdl(select, data_in);
      $to_myhdl(data_out);
   end

`else

   //=========================
   // initial setup of ports
   //=========================
   initial
     begin
      select = 0;
      data_in = 32'b0101010101;  // 01010101010 in binary
      $display(data_out);
     end


   //==========================
   // loop with a delay of 10
   //==========================
   always #10
     begin
        select = select + 1;
        $display(data_out);
     end
   
   //===================
   // finish condition
   //===================
   initial #100 $finish;

`endif
   
endmodule
