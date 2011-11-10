// mux test-bench script

module mux_tb;

   // local parameters
   localparam LOCAL_SELECT_LINES = `ifdef SELECT_LINES `SELECT_LINES `else 2 `endif;

   // declare regs
   reg [LOCAL_SELECT_LINES-1:0] select;
   reg [(2**LOCAL_SELECT_LINES)-1:0] in;
   
   // declare wires
   wire out; 

   // instance, "(d)esign (u)nder (t)est"
   mux dut (
	    .select(select), 
	    .in(in), 
	    .out(out)
	    );

   // define all of its parameters
   defparam dut.ARCHITECTURE = `ifdef ARCHITECTURE `ARCHITECTURE `else "BEHAVIORAL" `endif;
   defparam dut.SELECT_LINES = `ifdef SELECT_LINES `SELECT_LINES `else 2            `endif;

`ifdef MYHDL
      
   // define what myhdl takes over
   // only if we're running myhdl   
   initial begin
      $from_myhdl(select, in);
      $to_myhdl(out);
   end

`else

   // initial
   initial
     begin
	select= 0;
	in = 2;
	$display(out);
     end

   // set select differently
   initial #10 
     begin
        select = 1;
        $display(out);
     end

`endif
   
endmodule
