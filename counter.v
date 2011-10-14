module counter(
	       clk,
	       en,
	       rst,
	       out
	       );

   // Diagram positioning parameters
   parameter BLOCK_NAME = "counter"; // hierarchical block name
   parameter X = 0; // x location within sub-block
   parameter Y = 0; // y location within sub-block
   parameter DX = 0; // x length
   parameter DY = 0; // y lenghth
   
   // Top level block parameters
   parameter ARCHITECTURE = "BEHAVIORAL"; // BEHAVIORAL, VIRTEX5, VIRTEX6
   parameter DATA_WIDTH = 8; // number of bits in counter
   parameter COUNT_FROM = 0; // start with this number   
   parameter COUNT_TO = 2^(DATA_WIDTH-1); // value to count to in CL case
   parameter STEP = 1; // negative or positive, sets direction

   // Input
   input clk;
   input en;
   input rst;

   // Output
   output reg [DATA_WIDTH-1:0] out;

   // Generate according to implementation
   generate
   case (ARCHITECTURE)
     "BEHAVIORAL" : 
       begin

	  // Synchronous logic
	  always @(posedge clk)
	    begin
	       
	       if (rst == 0 && out < COUNT_TO)
		 begin
		    
		    if (en == 1)
		      begin
			 out <= out + STEP;
		      end

		 end
	       else
		 begin

		    out <= COUNT_FROM;

		 end // else: !if(rst == 0)
	    end
	  
       end // case "BEHAVIORAL"

     "VIRTEX5" : 
       begin
	  // Instantiate V5 counter primitive
       end
	
     "VIRTEX6" : 
       begin
	  // Instantiate V6 counter primitive
       end
	
     endcase 
   endgenerate
   
endmodule

