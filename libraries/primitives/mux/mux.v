module mux(
          select,
          in,
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
   parameter SELECT_LINES = 8; // number of inputs into mux, must be a power of 2.

   input[SELECT_LINES-1:0] select;
   input[(2**SELECT_LINES)-1:0] in;

   output out;

   wire out;
   wire[SELECT_LINES-1:0] select;
   wire[(2**SELECT_LINES)-1:0] in;

   // Generate according to implementation
   generate
   case (ARCHITECTURE)
     "BEHAVIORAL" : 
       begin
          assign out = in[select];
       end // case "BEHAVIORAL"

     "VIRTEX5" : 
       begin
	  // Instantiate V5 mux primitive
       end
	
     "VIRTEX6" : 
       begin
	  // Instantiate V6 mux primitive
       end
	
     endcase 
   endgenerate
   
endmodule

