module delay #(
      //=============
      // parameters
      //=============
      parameter ARCHITECTURE = "BEHAVIORAL", // BEHAVIORAL, VIRTEX5, VIRTEX6
      parameter DELAY_TYPE   = "FIDO",       // SYNC (COUNTER), REGISTERS(FIFO)
      parameter DATA_WIDTH   = 32,           // number of bits in counter
      parameter DELAY_CYCLES = 1             // delay in number of clock cycles
   ) (
      //=====================
      // input/output ports
      //=====================
      input                   clk,
      input                   en,
      input                   rst,
      input  [DATA_WIDTH-1:0] din,
      output [DATA_WIDTH-1:0] dout,
      output                  data_valid
   );

   // Generate according to implementation
   generate
      // Generate counter type
      case (DELAY_TYPE)
         //=======================
         // Implement Sync delay
         //=======================
         "SYNC" :   // outputs the input data after the desired amount of clock cycles have passed
         begin
            sync_delay #(
               .DATA_WIDTH   (DATA_WIDTH),
               .DELAY_CYCLES (DELAY_CYCLES)
            ) dut (
               .clk        (clk),
               .din        (din),
               .dout       (dout),
               .data_valid (data_valid)
            );
         end
         //=======================
         // Implement FIFO delay
         //=======================
         "FIFO" :  // shifts the input data through a FIFO
         begin
            fifo_delay #(
               .DATA_WIDTH   (DATA_WIDTH),
               .DELAY_CYCLES (DELAY_CYCLES)
            ) dut (
               .clk        (clk),
               .din        (din),
               .dout       (dout),
               .data_valid (data_valid)
            );
         end
      endcase
   endgenerate
endmodule

