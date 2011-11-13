// slice test-bench script

module slice_tb;

   // local parameters
   localparam LOCAL_DATA_WIDTH = `ifdef DATA_WIDTH `DATA_WIDTH `else 8 `endif;

   // declare regs
   reg clk;
   reg[LOCAL_DATA_WIDTH-1:0] data_in;
   //reg data_out;
   
   // declare wires
   wire [LOCAL_DATA_WIDTH-1:0] data_out;

   // instance, "(d)esign (u)nder (t)est"
   slice dut (
            .clk(clk), 
            .data_in(data_in), 
            .data_out(data_out)
	   );

   // define all of its parameters
   defparam dut.ARCHITECTURE      = `ifdef ARCHITECTURE      `ARCHITECTURE      `else "BEHAVIORAL" `endif;
   defparam dut.INPUT_DATA_WIDTH  = `ifdef INPUT_DATA_WIDTH  `INPUT_DATA_WIDTH  `else 8            `endif;
   defparam dut.OFFSET_REL_TO_MSB = `ifdef OFFSET_REL_TO_MSB `OFFSET_REL_TO_MSB `else 1            `endif;
   defparam dut.OFFSET_1          = `ifdef OFFSET_1          `OFFSET_1          `else 0            `endif;
   defparam dut.OFFSET_2          = `ifdef OFFSET_2          `OFFSET_2          `else 7            `endif;

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
	 = 0;
     end

   // simulate the clock
   always #1
     begin
	clk = ~clk;
     end

   // print the output
   always @(posedge clk) $display(data_out);
   
   // finish after 100 clocks
   initial #200 $finish;

`endif
   
endmodule
