module delay(
	       clk,
	       en,
	       rst,
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
   parameter DELAY_TYPE = "SYNC";         // SYNC, DATA, COUNTER, REGISTERS(FIFO)
   parameter DATA_WIDTH = 8;              // number of bits in counter
   parameter LATENCY = 1;                 // delay in number of clock cycles

   // Input
   input clk;
   input en;
   input rst;
   input [DATA_WIDTH-1:0] data_in;

   // Output
   output reg [DATA_WIDTH-1:0] data_out;

   // Generate according to implementation
   generate
   case (ARCHITECTURE)
     "BEHAVIORAL" : 
       begin
          case (DELAY_TYPE)
	         "COUNTER" :
	           begin
                      //
	           end
	         "FIFO" :
	           begin
                      //
	           end
	         "SYNC" :
	           begin
	              //
              end

          endcase
	  
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

