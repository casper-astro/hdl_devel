module reset_block(
    clk, async_rst_i, rst_i, rst_o
  );
  parameter DELAY = 10;
  parameter WIDTH = 50;
  input  clk;
  input  async_rst_i;
  input  rst_i;
  output rst_o;

  reg [31:0] delay_counter;
  reg [31:0] width_counter;

  reg rst_o;

  always @(posedge clk or posedge async_rst_i) begin
    if (async_rst_i) begin
      delay_counter<=32'b0;
      width_counter<=32'b0;
      rst_o <= 1'b0;
`ifdef DEBUG
      $display("rb: got async rst");
`endif
    end else begin
      rst_o <= (width_counter < WIDTH && delay_counter >= DELAY);
`ifdef SIMULATION
      /* fake initialization */
      if (delay_counter === 32'hxxxx_xxxx) begin
        delay_counter <= 32'b0;
      end else if (width_counter === 32'hxxxx_xxxx) begin
        width_counter <= 32'b0;
      end else
`endif
      if (delay_counter < DELAY) begin
        delay_counter<=delay_counter + 1;
      end else if (width_counter < WIDTH) begin
        width_counter<=width_counter + 1;
      end else if (rst_i == 1'b1) begin
        delay_counter<=32'b0;
        width_counter<=32'b0;
      end
    end
  end

endmodule

