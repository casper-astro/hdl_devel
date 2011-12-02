module epb_infrastructure(
     epb_data_buf,
     epb_data_oe_n,
     epb_data_in,
     epb_data_out,
     per_clk,
     epb_clk
   );
   
   parameter ARCHITECTURE = "VIRTEX6";
   
   inout  [0:31] epb_data_buf;
   input  epb_data_oe_n;
   input  [0:31] epb_data_in;
   output [0:31] epb_data_out;
   input  per_clk;
   output epb_clk;
 
     // Generate according to implementation
   generate
   case (ARCHITECTURE)
     
     "BEHAVIORAL" :
        begin
           // 
        end

     "VIRTEX5" : 
        begin
           // Instantiate V5 counter primitive
        end
     
     "VIRTEX6" :
        begin 
           IOBUF #(
             .IOSTANDARD("DEFAULT")
           ) iobuf_data [0:31] (
             .O  (epb_data_out),
             .IO (epb_data_buf),
             .I  (epb_data_in),
             .T  (epb_data_oe_n)
           );
         
           BUFG bufg_perclk(
             .I (per_clk),
             .O (epb_clk)
           );
        end
    
   endcase
   endgenerate

endmodule
