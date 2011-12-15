module ibram_sync_dp_tb;

   localparam LOCAL_A_DATA_WIDTH = 2;
   localparam LOCAL_A_ADDR_WIDTH = 4;
   localparam LOCAL_A_DATA_DEPTH = 2**LOCAL_A_ADDR_WIDTH;
   localparam LOCAL_B_DATA_WIDTH = 2;
   localparam LOCAL_B_ADDR_WIDTH = 4;
   localparam LOCAL_B_DATA_DEPTH = 2**LOCAL_B_ADDR_WIDTH;

   reg clk;
   
   reg a_wr;
   reg [LOCAL_A_ADDR_WIDTH-1:0] a_addr;
   reg [LOCAL_A_DATA_WIDTH-1:0] a_data_in;

   reg b_wr;
   reg [LOCAL_B_ADDR_WIDTH-1:0] b_addr;
   reg [LOCAL_B_DATA_WIDTH-1:0] b_data_in;

   wire [LOCAL_A_DATA_WIDTH-1:0] a_data_out;
   wire [LOCAL_B_DATA_WIDTH-1:0] b_data_out;

   bram_dp dut(

      .a_clk      (clk),
      .a_wr       (a_wr),
      .a_addr     (a_addr),
      .a_data_in  (a_data_in),
      .a_data_out (a_data_out),
      
      .b_clk      (clk),
      .b_wr       (b_wr),
      .b_addr     (b_addr),
      .b_data_in  (b_data_in),
      .b_data_out (b_data_out)
   );

   defparam dut.A_DATA_WIDTH = 2;
   defparam dut.A_ADDR_WIDTH = 4;
   defparam dut.A_DATA_DEPTH = 2**LOCAL_A_ADDR_WIDTH;
   defparam dut.B_DATA_WIDTH = 2;
   defparam dut.B_ADDR_WIDTH = 4;
   defparam dut.B_DATA_DEPTH = 2**LOCAL_B_ADDR_WIDTH;
   
   initial
      begin
         $dumpvars;
         clk = 0;
         a_addr = 4'b0110; 
         a_data_in = 32'b1010101010101;
         a_wr = 1;
         
         #5 a_wr = 0;

         #10 b_wr = 0;
         #10 b_addr = 4'b0110;

      end

   always #1
      begin
         clk = ~clk;
      end

   // print the output
   always
      #1 $display(b_data_out);

   // run for 30 time units = 15 clock cycles
   initial #100 $finish;

endmodule

