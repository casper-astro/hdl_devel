module fifo_tb;

   localparam LOCAL_DATA_WIDTH = 32;
   localparam LOCAL_ADDR_BITS  = 10;

   reg wr_clk;
   reg rd_clk;
   reg en;
   reg rst;
   reg wr_req;
   reg rd_req;

   reg  [LOCAL_DATA_WIDTH-1:0] data_in;

   wire [LOCAL_DATA_WIDTH-1:0] data_out;
   wire [LOCAL_ADDR_BITS-1:0]  usedw;

   fifo dut(
      .wr_clk  (wr_clk),
      .rd_clk  (rd_clk),
      .en      (en),
      .rst     (rst),
      .wr_req  (wr_req),
      .rd_req  (rd_req),
      .data_in (data_in),

      .data_out  (data_out),
      .perc_full (perc_full),
      .full      (full),
      .empty     (empty),
      .usedw     (usedw)
   );

   defparam dut.DATA_WIDTH = 32;
   defparam dut.FIFO_DEPTH = 16;
   defparam dut.ADDR_BITS  = 10;

   initial
      begin
         $dumpvars;
         wr_clk = 0;
         rd_clk = 0;
         rst = 0;
	      en = 1;
         wr_req = 0;
         rd_req = 0;
         data_in = 32'b1010101010101;
         #1 rst = 1;
         #2 rst = 0;
         
         #3 wr_req = 1;
         #3 wr_req = 0;

         #5 data_in = 32'b101010101010;

         #5 wr_req = 1;
         #5 wr_req = 0;
         
         #7 rd_req = 1;
         #8 rd_req = 0;

         #9 rd_req = 1;
         #10 rd_req = 0;


      end
   
   always #1
      begin
         wr_clk = ~wr_clk;
         rd_clk = ~rd_clk;
      end

   //always #40
   //   begin
   //      rst = ~rst;
   //   end

   // print the output
   always
      #1 $display(data_out);
  
   // run for 30 time units = 15 clock cycles
   initial #100 $finish;

endmodule

