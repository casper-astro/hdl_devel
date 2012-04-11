module delay_line_tb;

   reg        clk;
   reg  [7:0] din;
   wire [7:0] dout;
   wire       data_valid;

   delay #(
      .DELAY_TYPE   ("FIFO"),
      .DATA_WIDTH   (8),
      .DELAY_CYCLES (4) 
   ) dut (
      .clk  (clk),
      .din  (din),
      .dout (dout),
      .data_valid (data_valid)
   );

   initial
   begin
      $dumpvars;
      clk = 1;
      din = 8'hAB;
      #3
      din = 8'h11;
   end

   always #1
   begin
      clk = ~clk;
   end


   always @(posedge clk) $display(dout);

   //===============================
   // finish after 100 clock cycles
   //===============================
   initial #40 $finish;

endmodule
