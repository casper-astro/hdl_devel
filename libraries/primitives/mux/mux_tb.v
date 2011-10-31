// mux test-bench script

`include "mux.v"

module mux_tb;

   // local parameters
   localparam SELECT_LINES = 8;

   // declare regs
   reg [SELECT_LINES-1:0]select;
   reg [(2**SELECT_LINES)-1:0]in;
   
   // declare wires
   wire out; 

   mux
     #(
       .ARCHITECTURE("BEHAVIORAL"),
       .SELECT_LINES(SELECT_LINES)
       ) mux_inst
       (
	.select(select), 
	.in(in), 
	.out(out)
       );

   // initial
   initial
     begin
	select= 1;
	in = 0;
        //out = 0;
     end

   always #10 
     begin
        select = 3;
        in = 0;
        $display(out);
     end

endmodule
