module tb_mux_wrapper;

wire select;
wire data_in;
wire data_out;

initial begin
    $to_myhdl(
        select,
        data_in,
        data_out
    );
end

mux_wrapper dut(
    select,
    data_in,
    data_out
);

endmodule
