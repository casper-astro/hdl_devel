module sys_block #(
    parameter     BOARD_ID = 32'h0,
    parameter     REV_MAJ  = 32'h0,
    parameter     REV_MIN  = 32'h0,
    parameter     REV_RCS  = 32'h0
  )  (
    input         wb_clk_i,
    input         wb_rst_i,
    input         wb_cyc_i,
    input         wb_stb_i,
    input         wb_we_i,
    input   [3:0] wb_sel_i,
    input  [31:0] wb_adr_i,
    input  [31:0] wb_dat_i,
    output [31:0] wb_dat_o,
    output        wb_ack_o,
    output        wb_err_o,

    input         debug_clk,
    input  [31:0] regin_0,
    input  [31:0] regin_1,
    input  [31:0] regin_2,
    input  [31:0] regin_3,
    input  [31:0] regin_4,
    input  [31:0] regin_5,
    input  [31:0] regin_6,
    input  [31:0] regin_7,

    output [31:0] regout_0,
    output [31:0] regout_1,
    output [31:0] regout_2,
    output [31:0] regout_3,
    output [31:0] regout_4,
    output [31:0] regout_5,
    output [31:0] regout_6,
    output [31:0] regout_7
  );

  /* latch data in */
  reg [31:0] regin_0_R;
  reg [31:0] regin_1_R;
  reg [31:0] regin_2_R;
  reg [31:0] regin_3_R;
  reg [31:0] regin_4_R;
  reg [31:0] regin_5_R;
  reg [31:0] regin_6_R;
  reg [31:0] regin_7_R;
  reg [31:0] regin_0_RR;
  reg [31:0] regin_1_RR;
  reg [31:0] regin_2_RR;
  reg [31:0] regin_3_RR;
  reg [31:0] regin_4_RR;
  reg [31:0] regin_5_RR;
  reg [31:0] regin_6_RR;
  reg [31:0] regin_7_RR;

  always @(posedge wb_clk_i) begin
    regin_0_R <= regin_0;
    regin_1_R <= regin_1;
    regin_2_R <= regin_2;
    regin_3_R <= regin_3;
    regin_4_R <= regin_4;
    regin_5_R <= regin_5;
    regin_6_R <= regin_6;
    regin_7_R <= regin_7;
    regin_0_RR<= regin_0_R;
    regin_1_RR<= regin_1_R;
    regin_2_RR<= regin_2_R;
    regin_3_RR<= regin_3_R;
    regin_4_RR<= regin_4_R;
    regin_5_RR<= regin_5_R;
    regin_6_RR<= regin_6_R;
    regin_7_RR<= regin_7_R;
  end

  /* latch data out */
  reg [31:0] regout_0_reg;
  reg [31:0] regout_1_reg;
  reg [31:0] regout_2_reg;
  reg [31:0] regout_3_reg;
  reg [31:0] regout_4_reg;
  reg [31:0] regout_5_reg;
  reg [31:0] regout_6_reg;
  reg [31:0] regout_7_reg;

  reg [31:0] regout_0_R;
  reg [31:0] regout_1_R;
  reg [31:0] regout_2_R;
  reg [31:0] regout_3_R;
  reg [31:0] regout_4_R;
  reg [31:0] regout_5_R;
  reg [31:0] regout_6_R;
  reg [31:0] regout_7_R;
  reg [31:0] regout_0_RR;
  reg [31:0] regout_1_RR;
  reg [31:0] regout_2_RR;
  reg [31:0] regout_3_RR;
  reg [31:0] regout_4_RR;
  reg [31:0] regout_5_RR;
  reg [31:0] regout_6_RR;
  reg [31:0] regout_7_RR;

  always @(posedge debug_clk) begin
    regout_0_R <= regout_0_reg;
    regout_1_R <= regout_1_reg;
    regout_2_R <= regout_2_reg;
    regout_3_R <= regout_3_reg;
    regout_4_R <= regout_4_reg;
    regout_5_R <= regout_5_reg;
    regout_6_R <= regout_6_reg;
    regout_7_R <= regout_7_reg;

    regout_0_RR<= regout_0_R;
    regout_1_RR<= regout_1_R;
    regout_2_RR<= regout_2_R;
    regout_3_RR<= regout_3_R;
    regout_4_RR<= regout_4_R;
    regout_5_RR<= regout_5_R;
    regout_6_RR<= regout_6_R;
    regout_7_RR<= regout_7_R;
  end

  assign regout_0 = regout_0_RR;
  assign regout_1 = regout_1_RR;
  assign regout_2 = regout_2_RR;
  assign regout_3 = regout_3_RR;
  assign regout_4 = regout_4_RR;
  assign regout_5 = regout_5_RR;
  assign regout_6 = regout_6_RR;
  assign regout_7 = regout_7_RR;

  reg [31:0] scratchpad [3:0];

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

  /* wb write */
  always @(posedge wb_clk_i) begin
    if (wb_rst_i) begin
      regout_0_reg <= 32'd0;
      regout_1_reg <= 32'd0;
      regout_2_reg <= 32'd0;
      regout_3_reg <= 32'd0;
      regout_4_reg <= 32'd0;
      regout_5_reg <= 32'd0;
      regout_6_reg <= 32'd0;
      regout_7_reg <= 32'd0;
    end else begin
      if (wb_stb_i && wb_cyc_i && wb_we_i) begin
        case (wb_adr_i[6:2])
          /* TODO: add byte enables to test */
          5'h4: begin
            if (wb_sel_i[0])
              scratchpad[0][7:0] <= wb_dat_i[7:0];
            if (wb_sel_i[1])
              scratchpad[0][15:8] <= wb_dat_i[15:8];
            if (wb_sel_i[2])
              scratchpad[0][23:16] <= wb_dat_i[23:16];
            if (wb_sel_i[3])
              scratchpad[0][31:24] <= wb_dat_i[31:24];
          end
          5'h5: begin
            if (wb_sel_i[0])
              scratchpad[1][7:0] <= wb_dat_i[7:0];
            if (wb_sel_i[1])
              scratchpad[1][15:8] <= wb_dat_i[15:8];
            if (wb_sel_i[2])
              scratchpad[1][23:16]<= wb_dat_i[23:16];
            if (wb_sel_i[3])
              scratchpad[1][31:24] <= wb_dat_i[31:24];
          end
          5'h6: begin
            if (wb_sel_i[0])
              scratchpad[2][7:0] <= wb_dat_i[7:0];
            if (wb_sel_i[1])
              scratchpad[2][15:8] <= wb_dat_i[15:8];
            if (wb_sel_i[2])
              scratchpad[2][23:16] <= wb_dat_i[23:16];
            if (wb_sel_i[3])
              scratchpad[2][31:24] <= wb_dat_i[31:24];
          end
          5'h7: begin
            if (wb_sel_i[0])
              scratchpad[3][7:0] <= wb_dat_i[7:0];
            if (wb_sel_i[1])
              scratchpad[3][15:8] <= wb_dat_i[15:8];
            if (wb_sel_i[2])
              scratchpad[3][23:16] <= wb_dat_i[23:16];
            if (wb_sel_i[3])
              scratchpad[3][31:24] <= wb_dat_i[31:24];
          end
          5'h10: regout_0_reg <= wb_dat_i;
          5'h11: regout_1_reg <= wb_dat_i;
          5'h12: regout_2_reg <= wb_dat_i;
          5'h13: regout_3_reg <= wb_dat_i;
          5'h14: regout_4_reg <= wb_dat_i;
          5'h15: regout_5_reg <= wb_dat_i;
          5'h16: regout_6_reg <= wb_dat_i;
          5'h17: regout_7_reg <= wb_dat_i;
        endcase
      end
    end
  end

  /* wb read */

  reg [31:0] wb_dat_o_reg;
  assign wb_dat_o = wb_dat_o_reg;

  always @(*) begin
    case (wb_adr_i[6:2])
      5'h0:   wb_dat_o_reg <= BOARD_ID;
      5'h1:   wb_dat_o_reg <= REV_MAJ;
      5'h2:   wb_dat_o_reg <= REV_MIN;
      5'h3:   wb_dat_o_reg <= REV_RCS;
      5'h4:   wb_dat_o_reg <= scratchpad[0];
      5'h5:   wb_dat_o_reg <= scratchpad[1];
      5'h6:   wb_dat_o_reg <= scratchpad[2];
      5'h7:   wb_dat_o_reg <= scratchpad[3];
      5'h8:   wb_dat_o_reg <= regin_0_RR;
      5'h9:   wb_dat_o_reg <= regin_1_RR;
      5'ha:   wb_dat_o_reg <= regin_2_RR;
      5'hb:   wb_dat_o_reg <= regin_3_RR;
      5'hc:   wb_dat_o_reg <= regin_4_RR;
      5'hd:   wb_dat_o_reg <= regin_5_RR;
      5'he:   wb_dat_o_reg <= regin_6_RR;
      5'hf:   wb_dat_o_reg <= regin_7_RR;
      5'h10:  wb_dat_o_reg <= regout_0_reg;
      5'h11:  wb_dat_o_reg <= regout_1_reg;
      5'h12:  wb_dat_o_reg <= regout_2_reg;
      5'h13:  wb_dat_o_reg <= regout_3_reg;
      5'h14:  wb_dat_o_reg <= regout_4_reg;
      5'h15:  wb_dat_o_reg <= regout_5_reg;
      5'h16:  wb_dat_o_reg <= regout_6_reg;
      5'h17:  wb_dat_o_reg <= regout_7_reg;
      default:
              wb_dat_o_reg <= 32'b0;
        
    endcase
  end

endmodule
