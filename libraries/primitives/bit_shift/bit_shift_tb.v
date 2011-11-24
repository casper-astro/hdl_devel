// bit_shift test-bench script

module bit_shift_tb;

   // local parameters
   localparam LOCAL_DATA_WIDTH = `ifdef DATA_WIDTH `DATA_WIDTH `else 8 `endif;

   // declare regs
   reg clk;
   reg[LOCAL_DATA_WIDTH-1:0] data_in;
   //reg data_out;
   
   // declare wires
   wire [LOCAL_DATA_WIDTH-1:0] data_out;

   // instance, "(d)esign (u)nder (t)est"
   bit_shift dut (
            .clk(clk), 
            .data_in(data_in), 
            .data_out(data_out)
	   );

   // define all of its parameters
   defparam dut.ARCHITECTURE      = `ifdef ARCHITECTURE      `ARCHITECTURE      `else "BEHAVIORAL" `endif;
   defparam dut.DATA_WIDTH        = `ifdef DATA_WIDTH        `DATA_WIDTH        `else 8            `endif;
   defparam dut.SHIFT_DIRECTION   = `ifdef SHIFT_DIRECTION   `SHIFT_DIRECTION   `else 0            `endif;
   defparam dut.NUMBER_BITS       = `ifdef NUMBER_BITS       `NUMBER_BITS       `else 1            `endif;
   defparam dut.WRAP              = `ifdef WRAP              `WRAP              `else 0            `endif;

`ifdef MYHDL
      
   // define what myhdl takes over
   // only if we're running myhdl   
   initial begin
      $from_myhdl(clk, data_in, data_out);
      $to_myhdl(data_out);
   end

`else

   // initialize
   initial
     begin
	clk = 0;
	data_in = 16'b0101010101010101;
     end

   // simulate the clock
   always #1
     begin
	clk = ~clk;
     end

   // print the output
   always @(posedge clk) $display(data_out);
   
   // finish after 3 clocks
   initial #3 $finish;

`endif
   
endmodule
