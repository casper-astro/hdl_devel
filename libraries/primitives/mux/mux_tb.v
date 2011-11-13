// mux test-bench script

module mux_tb;

   // local parameters
   localparam LOCAL_SELECT_LINES = `ifdef SELECT_LINES `SELECT_LINES `else 4 `endif;

   // declare regs
   reg [LOCAL_SELECT_LINES-1:0] select;
   reg [(2**LOCAL_SELECT_LINES)-1:0] data_in;
   
   // declare wires
   wire data_out; 

   // instance, "(d)esign (u)nder (t)est"
   mux dut (
	    .select(select), 
	    .data_in(data_in), 
	    .data_out(data_out)
	    );

   // define all of its parameters
   defparam dut.ARCHITECTURE = `ifdef ARCHITECTURE `ARCHITECTURE `else "BEHAVIORAL" `endif;
   defparam dut.SELECT_LINES = `ifdef SELECT_LINES `SELECT_LINES `else 4            `endif;

`ifdef MYHDL
      
   // define what myhdl takes over
   // only if we're running myhdl   
   initial begin
      $from_myhdl(select, data_in);
      $to_myhdl(data_out);
   end

`else

   // initial setup of ports
   initial
     begin
	select = 0;
	data_in = 682;  // 01010101010 in binary
	$display(data_out);
     end

   // loop with a delay of 10
   always #10
     begin
        select = select + 1;
        $display(data_out);
     end
   
   // finish condition
   initial #100 $finish;

`endif
   
endmodule
