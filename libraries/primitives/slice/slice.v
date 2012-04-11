//============================================================================//
//                                                                            //
//      Bit Slicer                                                            //
//                                                                            //
//      Module name: slice                                                    //
//      Desc: parameterized, bit slicer, outputs the remaining bits           //
//      Date: Nov 2011                                                        //
//      Developer: Wesley New                                                 //
//      Licence: GNU General Public License ver 3                             //
//      Notes:                                                                //
//                                                                            //
//============================================================================//

module slice #(
      //===================
      // Slice Parameters
      //===================
      parameter ARCHITECTURE = "BEHAVIORAL",   // BEHAVIORAL, VIRTEX5, VIRTEX6
      parameter INPUT_DATA_WIDTH = 8,          // number of input bits
      parameter OFFSET_REL_TO_MSB = 1,         // 1 = MSB, 0 = LSB
      parameter OFFSET_1 = 0,                  // position of first offset
      parameter OFFSET_2 = INPUT_DATA_WIDTH-1  // position of second offest
   ) (
      //===========
      // IO Ports
      //===========
      input  wire                        clk,
      input  wire [INPUT_DATA_WIDTH-1:0] data_in,
      output reg  [OFFSET_1-OFFSET_2:0]  data_out
   );

   //=======================================
   // Generate according to implementation
   //=======================================
   generate
      case (ARCHITECTURE)
         "BEHAVIORAL" : 
         begin
            // Synchronous logic
            always @(posedge clk)
            begin
               if (OFFSET_REL_TO_MSB) // (MSB)
               begin
                  data_out <= data_in[OFFSET_2:OFFSET_1];
               end
               else // OFFSET_RELATIVE_TO_MSB = 0 (LSB)
               begin
                  data_out <= data_in[(INPUT_DATA_WIDTH-1'd1)-OFFSET_1:(INPUT_DATA_WIDTH-1'd1)-OFFSET_2];
               end
            end
         end // case "BEHAVIORAL"
         
         "VIRTEX5" : 
         begin
            // Instantiate primitive for V5
         end
         
         "VIRTEX6" : 
         begin
            // Instantiate primitive for V6
         end
   
      endcase 
   endgenerate
endmodule

