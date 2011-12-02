module bit_shift(clk,
             data_in,
	     data_out
            );

   // Diagram positioning parameters
   parameter BLOCK_NAME = "counter"; // hierarchical block name
   parameter X = 0;                  // x location within sub-block
   parameter Y = 0;                  // y location within sub-block
   parameter DX = 0;                 // x length
   parameter DY = 0;                 // y lenghth
   
   // Top level block parameters
   parameter ARCHITECTURE = "BEHAVIORAL"; // BEHAVIORAL, VIRTEX5, VIRTEX6
   parameter INPUT_DATA_WIDTH = 8;        // number of input bits
   parameter SHIFT_DIRECTION = 1;         // 1 = shift right, 0 = shift left
   parameter NUMBER_BITS = 1;             // number of bits to shift
   parameter WRAP = 0;                    // whether to wrap the shift or not

   // Input
   input clk;
   input[INPUT_DATA_WIDTH-1:0] data_in;

   // Output
   output reg [INPUT_DATA_WIDTH-1:0] data_out;

   // Generate according to implementation
   generate
   case (ARCHITECTURE)
     "BEHAVIORAL" : 
       begin

	  // Synchronous logic
	  always @(posedge clk)
	    begin
	      if (WRAP == 0) // (WRAP)
	        begin
                  if (SHIFT_DIRECTION)  // right shift
                    begin
	              data_out <= data_in >> NUMBER_BITS;
	            end
	          else  // left shift
	            begin
                      data_out <= data_in << NUMBER_BITS;
	            end
	        end
              // TODO: make this code wrap 
              if (WRAP)  // (WRAP)
	        begin
                  if (SHIFT_DIRECTION)  // right shift
                    begin
	              data_out <= data_in >> NUMBER_BITS;
	            end
	          else  // left shift
	            begin
                      data_out <= data_in << NUMBER_BITS;
	            end
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

