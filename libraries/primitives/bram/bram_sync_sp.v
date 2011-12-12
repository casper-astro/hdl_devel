// A parameterized, inferable, true dual-port, dual-clock block RAM in Verilog.

module bram_sp #(
    parameter DATA_WIDTH = 72,
    parameter ADDR_WIDTH = 10
) (
    //=============
    //   Ports
    //=============
    input  wire                  clk,
    input  wire                  wr,
    input  wire [ADDR_WIDTH-1:0] addr,
    input  wire [DATA_WIDTH-1:0] din,
    output reg  [DATA_WIDTH-1:0] dout
);

//===============
// Shared memory
//===============
reg [DATA_WIDTH-1:0] mem [(2**ADDR_WIDTH)-1:0];

always @(posedge clk) begin
    dout <= mem[addr];
    if(wr) begin
        dout      <= din;
        mem[addr] <= din;
    end
end

endmodule
