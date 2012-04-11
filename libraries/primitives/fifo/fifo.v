//============================================================================//
//                                                                            //
//      FIFO                                                                  //
//                                                                            //
//      Module name: fifo                                                     //
//      Desc: parameterized fifo                                              //
//      Date: Dec 2011                                                        //
//      Developer: Wesley New                                                 //
//      Licence: GNU General Public License ver 3                             //
//      Notes: Uses the dual port BRAM module                                 //
//                                                                            //
//============================================================================//

module fifo #(
      //=======================
      //   fifo parameters
      //=======================
      parameter DATA_WIDTH = 16;
      parameter FIFO_DEPTH = 1024;
      parameter ADDR_BITS  = 10;
   ) (
      //=======================
      //   input ports
      //=======================
      input                  wr_clk;
      input                  rd_clk;
      input                  en;
      input                  rst;
      input                  wr_req;
      input                  rd_req;
      input [DATA_WIDTH-1:0] data_in;
      
      //=======================
      //   output ports
      //=======================
      output     [DATA_WIDTH-1:0] data_out;
      output                      perc_full;
      output                      full;
      output                      empty;
      output reg [ADDR_BITS-1:0]  usedw;
   );

   
   //=======================
   //   internal variables
   //=======================
   reg [DATA_WIDTH-1:0] mem [0:FIFO_DEPTH-1];
   reg [ADDR_BITS-1:0] 	rd_ptr;
   reg [ADDR_BITS-1:0] 	wr_ptr;
   
//`ifdef rd_req
   reg [DATA_WIDTH-1:0]    data_out;
//`else
   //wire [DATA_WIDTH-1:0]   data_out;
//`endif
   
   integer i;
   
   always @(rst)
      begin
         wr_ptr <= #1 0;
         rd_ptr <= #1 0;
         for(i=0;i<FIFO_DEPTH;i=i+1)
            mem[i] <= 0;
     end
   
   always @(posedge wr_clk or posedge wr_reg)
      if (wr_req)
         begin
            wr_ptr <= wr_ptr+1;
            mem[wr_ptr] <= data_in;
         end
     
   always @(posedge rd_clk)
      if (rd_req)
         begin
            rd_ptr <= rd_ptr+1;
//`ifdef rd_req
            data_out <= mem[rd_ptr];
//`endif
         end
   
//`ifdef rd_req
//`else
//   assign data_out = mem[rdptr];
//`endif
   
   // Fix these
   //always @(posedge clk)
   //   usedw <= wrptr - rdptr;
   
   //assign empty = (usedw == 0);
   //assign full =  (usedw == FIFO_DEPTH-1);
   
endmodule //fifo
