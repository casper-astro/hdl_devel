//============================================================================//
//                                                                            //
//      Syncronous single-port BRAM                                           //
//                                                                            //
//      Module name: bram_sync_sp                                             //
//      Desc: parameterized, syncronous, single-port block ram                //
//      Date: Dec 2011                                                        //
//      Developer: Wesley New                                                 //
//      Licence: GNU General Public License ver 3                             //
//      Notes: Developed from a combiniation of bram implmentations           //
//                                                                            //
//============================================================================//

module bram_sync_sp #(
       //=============
       // 
       //=============
       parameter ARCHITECTURE = "BEHAVIOURAL",
       
       //=============
       // Parameters
       //=============
       parameter DATA_WIDTH = 32,
       parameter ADDR_WIDTH = 4
   ) (
       //=============
       //   Ports
       //=============
       input  wire                  clk,
       input  wire                  wr,
       input  wire [ADDR_WIDTH-1:0] addr,
       input  wire [DATA_WIDTH-1:0] data_in,
       output reg  [DATA_WIDTH-1:0] data_out
   );

   //===============
   // Memory
   //===============
   reg [DATA_WIDTH-1:0] mem [(2**ADDR_WIDTH)-1:0];
   

   //=======================================
   // Generate according to implementation
   //=======================================
   generate
      case (ARCHITECTURE)

         "BEHAVIORAL" :
         begin

            //==================a
            // Read/Write Logic
            //===================
            always @(posedge clk) begin
               data_out <= mem[addr];
               if(wr) begin
                  data_out  <= data_in;
                  mem[addr] <= data_in;
               end
            end
         end

         "VIRTEX5" :
         begin
            // Instantiate V5 primitive
         end

         "VIRTEX6" :
         begin
            // Instantiate V6 primitive
         end

         default :
         begin
            // default case
         end

      endcase
   endgenerate
endmodule
