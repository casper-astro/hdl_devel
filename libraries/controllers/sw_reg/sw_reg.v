module sw_reg #(
    //================
    // parameters
    //================
    parameter C_BASEADDR      = 32'h00000000,
    parameter C_HIGHADDR      = 32'h0000000F,
    parameter C_WB_DATA_WIDTH = 32,
    parameter C_WB_ADDR_WIDTH = 1,
    parameter C_BYTE_EN_WIDTH = 4
  )  (
    //================
    // inputs
    //================
    input         wb_clk_i,
    input         wb_rst_i,
    input         wb_cyc_i,
    input         wb_stb_i,
    input         wb_we_i,
    input   [3:0] wb_sel_i,
    input  [31:0] wb_adr_i,
    input  [31:0] wb_dat_i,
    
    //================
    // outputs
    //================
    output [31:0] wb_dat_o,
    output        wb_ack_o,
    output        wb_err_o
  );

  wire a_match = wb_adr_i >= C_BASEADDR && wb_adr_i <= C_HIGHADDR;

  //================
  // register buffer 
  //================
  reg [31:0] reg_buffer;

  //================
  // wb control
  //================
  reg wb_ack_reg;
  assign wb_ack_o = wb_ack_reg;
  always @(posedge wb_clk_i) begin
    wb_ack_reg <= 1'b0;
    if (wb_rst_i) begin
    end else begin
      if (wb_stb_i && wb_cyc_i) begin
        wb_ack_reg <= 1'b1;
      end
    end
  end

  //================
  // wb write
  //================
  always @(posedge wb_clk_i) begin
    if (wb_rst_i) begin
      reg_buffer <= 32'd0;
    end else begin
      if (a_match && wb_stb_i && wb_cyc_i && wb_we_i) begin
        case (wb_adr_i[6:2])
          /* TODO: add byte enables to test */
          5'h0: begin
            if (wb_sel_i[0])
              reg_buffer[7:0] <= wb_dat_i[7:0];
            if (wb_sel_i[1])
              reg_buffer[15:8] <= wb_dat_i[15:8];
            if (wb_sel_i[2])
              reg_buffer[23:16] <= wb_dat_i[23:16];
            if (wb_sel_i[3])
              reg_buffer[31:24] <= wb_dat_i[31:24];
          end
        endcase
      end
    end
  end

  //================
  // wb read
  //================
  reg [31:0] wb_dat_o_reg;
  assign wb_dat_o = wb_dat_o_reg;

  always @(*) begin
    if(~wb_we_i)
    case (wb_adr_i[6:2])
      5'h0:   wb_dat_o_reg <= reg_buffer;
      default:
        wb_dat_o_reg <= 32'b0;
    endcase
  end
endmodule
