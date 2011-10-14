// counter test-bench script

`include "counter.v"

module counter_tb;

   // local parameters
   localparam CLK_COUNT = 0;
   localparam DATA_WIDTH = 8;

   // declate regs
   reg clk;
   reg en;
   reg rst;
   reg count;
   
   // declare wires
   wire [DATA_WIDTH-1:0] out;

   // counter
   counter
     #(
       .ARCHITECTURE("BEHAVIORAL"),
       .DATA_WIDTH(DATA_WIDTH),
       .COUNT_FROM(20),
       .COUNT_TO(2**DATA_WIDTH),
       .STEP(1)
       ) counter_inst
       (
	.clk(clk), 
	.en(en), 
	.rst(rst), 
	.out(out)
	);

   // initial
   initial
     begin
	clk = 0;
	en = 1;
	rst = 0;
        count = 0;
     end

   always #10 
     begin
	clk = ~clk;
        $display(out);
     end

   always @(posedge clk) count = count+1;

endmodule
