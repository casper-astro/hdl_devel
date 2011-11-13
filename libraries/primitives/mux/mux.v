module mux(
          select,
          data_in,
          data_out
          );

   // Diagram positioning parameters
   parameter BLOCK_NAME = "mux";      // hierarchical block name
   parameter X = 0;                   // x location within sub-block
   parameter Y = 0;                   // y location within sub-block
   parameter DX = 0;                  // x length
   parameter DY = 0;                  // y lenghth
   
   // Top level block parameters
   parameter ARCHITECTURE = "BEHAVIORAL";  // BEHAVIORAL, VIRTEX5, VIRTEX6
   parameter SELECT_LINES = 4;             // number of inputs into mux, must be a power of 2.

   input[SELECT_LINES-1:0] select;
   input[(2**SELECT_LINES)-1:0] data_in;

   output data_out;

   wire data_out;
   wire[SELECT_LINES-1:0] select;
   wire[(2**SELECT_LINES)-1:0] data_in;

   // Generate according to implementation
   generate
   case (ARCHITECTURE)
     "BEHAVIORAL" : 
       begin
          assign data_out = data_in[select];
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

