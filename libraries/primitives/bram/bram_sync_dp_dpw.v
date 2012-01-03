//============================================================================//
//                                                                            //
//      Syncronous dual-port with different port widths BRAM                  //
//                                                                            //
//      Module name: bram_sync_dp_dpw                                         //
//      Desc: parameterized, syncronous, inferable, true dual-port,           //
//            dual clock with different port widths block ram                 //
//      Date: Dec 2011                                                        //
//      Developer: Wesley New                                                 //
//      Licence: GNU General Public License ver 3                             //
//      Notes: Developed from a combiniation of bram implmentations           //
//             Uses the multiplexer module                                    //
//                                                                            //
//============================================================================//

//==============================================================================
// Note: this module is incomplete, due to its nature it will be easier to 
// generate the core using vendor tools as many devices have hard cores for
// dual port different data width brams.
//==============================================================================

module bram_sync_dp_dpw #(
    
      //====================
      // Port B Parameters
      //====================
      parameter A_DATA_WIDTH = 4,
      parameter A_ADDR_WIDTH = 3,
      parameter A_DATA_DEPTH = 2**A_ADDR_WIDTH,
      
      //====================
      // Port B Parameters
      //====================
      parameter B_DATA_WIDTH = 2,
      parameter B_ADDR_WIDTH = 4,
      parameter B_DATA_DEPTH = 2**B_ADDR_WIDTH
   ) (
      //====================
      // Port A
      //====================
      input  wire                    a_clk,
      input  wire                    a_wr,
      input  wire [A_ADDR_WIDTH-1:0] a_addr,
      input  wire [A_DATA_WIDTH-1:0] a_data_in,
      output reg  [A_DATA_WIDTH-1:0] a_data_out,
      
      //====================
      // Port B
      //====================
      input  wire                    b_clk,
      input  wire                    b_wr,
      input  wire [B_ADDR_WIDTH-1:0] b_addr,
      input  wire [B_DATA_WIDTH-1:0] b_data_in,
      output wire [B_DATA_WIDTH-1:0] b_data_out
   );
   //====================
   // Local variables
   //====================
   reg [(A_DATA_WIDTH-B_DATA_WIDTH)-1:0] b_be;
   
   //====================
   // Shared memory
   //====================
   reg [A_DATA_WIDTH-1:0] mem [A_DATA_DEPTH-1:0];
   
   //====================
   // Port A
   //====================
   always @(posedge a_clk)
   begin
      a_data_out <= mem[a_addr];
      if(a_wr)
      begin
         a_data_out  <= a_data_in;
         mem[a_addr] <= a_data_in;
      end
   end
   
   //====================
   // Port B
   //====================
   always @(posedge b_clk)
   begin
      //b_data_out <= mem [b_addr%A_DATA_DEPTH] [b_addr/A_DATA_DEPTH:(b_addr/A_DATA_DEPTH)-B_DATA_WIDTH];
      if(b_wr)
      begin
         //b_data_out <= b_data_in;
         //mem [b_addr%A_DATA_DEPTH] [b_addr/A_DATA_DEPTH:(b_addr/A_DATA_DEPTH)-B_DATA_WIDTH] <= b_data_in;
      end
   end

   //====================
   // Read Port B Mux 
   //====================
   mux 
   #(
      .SELECT_LINES ((A_DATA_WIDTH/B_DATA_WIDTH)-1),
      .DATA_WIDTH   (B_DATA_WIDTH)
   ) slice_mux (
      .select   (b_addr/A_DATA_DEPTH),
      .data_in  (mem [b_addr%A_DATA_DEPTH]),
      .data_out (b_data_out)
   );

   //===================
   // TODO: Implement writing on port b
   //===================

endmodule
