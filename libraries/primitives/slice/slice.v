module slice(
      clk,
      data_in,
      data_out
   );

   // Diagram positioning parameters
   parameter BLOCK_NAME = "slice"; // hierarchical block name
   parameter X = 0;                  // x location within sub-block
   parameter Y = 0;                  // y location within sub-block
   parameter DX = 0;                 // x length
   parameter DY = 0;                 // y lenghth
   
   // Top level block parameters
   parameter ARCHITECTURE = "BEHAVIORAL";   // BEHAVIORAL, VIRTEX5, VIRTEX6
   parameter INPUT_DATA_WIDTH = 8;          // number of input bits
   parameter OFFSET_REL_TO_MSB = 1;         // 1 = MSB, 0 = LSB
   parameter OFFSET_1 = 0;                  // position of first offset
   parameter OFFSET_2 = INPUT_DATA_WIDTH-1; // position of second offest

   // Input
   input clk;
   input[INPUT_DATA_WIDTH-1:0] data_in;

   // Output
   output reg [OFFSET_1-OFFSET_2:0] data_out;

   // Generate according to implementation
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

