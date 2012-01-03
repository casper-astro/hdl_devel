//============================================================================//
//                                                                            //
//      Syncronous dual-port BRAM                                             //
//                                                                            //
//      Module name: bram_sync_dp                                             //
//      Desc: parameterized, syncronous, inferable, true dual-port,           //
//            dual clock block ram                                            //
//      Date: Dec 2011                                                        //
//      Developer: Wesley New                                                 //
//      Licence: GNU General Public License ver 3                             //
//      Notes: Developed from a combiniation of bram implmentations           //
//                                                                            //
//============================================================================//

module bram_sync_dp #(
      //==============
      // Parameters
      //==============
      parameter DATA_WIDTH = 2,             // width of the data
      parameter ADDR_WIDTH = 4,             // number of address bits
      parameter DATA_DEPTH = 2**ADDR_WIDTH  // depth of the ram, this is tied to the number of address bits
   ) (
      //==============
      // Port A
      //==============
      input  wire                  a_clk,
      input  wire                  a_wr,       // pulse a 1 to write and 0 reads
      input  wire [ADDR_WIDTH-1:0] a_addr, 
      input  wire [DATA_WIDTH-1:0] a_data_in,
      output reg  [DATA_WIDTH-1:0] a_data_out,
      
      //==============
      // Port B
      //==============
      input  wire                  b_clk,
      input  wire                  b_wr,       // pulse a 1 to write and 0 reads
      input  wire [ADDR_WIDTH-1:0] b_addr,
      input  wire [DATA_WIDTH-1:0] b_data_in,
      output reg  [DATA_WIDTH-1:0] b_data_out
   );
   //==============
   // Shared memory
   //==============
   reg [DATA_WIDTH-1:0] mem [DATA_DEPTH-1:0];
   
   //==============
   // Port A
   //==============
   always @(posedge a_clk)
   begin
      a_data_out <= mem[a_addr];
      if(a_wr)
      begin
         a_data_out  <= a_data_in;
         mem[a_addr] <= a_data_in;
      end
   end
   
   //==============
   // Port B
   //==============
   always @(posedge b_clk)
   begin
      b_data_out <= mem[b_addr];
      if(b_wr)
      begin
         b_data_out  <= b_data_in;
         mem[b_addr] <= b_data_in;
      end
   end
endmodule
