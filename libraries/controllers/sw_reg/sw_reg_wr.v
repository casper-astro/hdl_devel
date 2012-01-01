//=====================================================
//                    _________
//      read & write |         | read only
//   SW <----------> |   Reg   | --------> Fabric
//                   |_________|
//
//=====================================================


module sw_reg_wr #(
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
    // wb inputs
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
    // wb outputs
    //================
    output [31:0] wb_dat_o,
    output        wb_ack_o,
    output        wb_err_o,

    //================
    // fabric ports
    //================
    input         fabric_clk,
    output        fabric_data_out
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
    register_doneR  <= register_done;
    register_doneRR <= register_doneR;
    // reset
    if (wb_rst_i) begin
      reg_buffer <= 32'd0;
      register_ready <= 1'b0;
    end else begin
      if (a_match && wb_stb_i && wb_cyc_i && wb_we_i) begin
        register_ready <= 1'b1;
        case (wb_adr_i[6:2])
          // byte enables
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
    if (register_doneRR) begin
       register_ready <= 1'b0;
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
      5'h0:   
        wb_dat_o_reg <= reg_buffer;
      default:
        wb_dat_o_reg <= 32'b0;
    endcase
  end

  
  //================
  // fabric read
  //================
  reg [31:0] fabric_data_out_reg; 
  /* Handshake signal from OPB to application indicating data is ready to be latched */
  reg register_ready;
  reg register_readyR; 
  reg register_readyRR; 
  /* Handshake signal from application to OPB indicating data has been latched */
  reg register_done;
  reg register_doneR;
  reg register_doneRR;
  assign fabric_data_out = fabric_data_out_reg; 
 
  always @(posedge fabric_clk) begin 
    // registering for clock domain crossing  
    register_readyR  <= register_ready; 
    register_readyRR <= register_readyR; 
 
    if (!register_readyRR) begin 
      register_done <= 1'b0; 
    end 
 
    if (register_readyRR) begin 
      register_done <= 1'b1; 
      fabric_data_out_reg <= reg_buffer; 
    end 
  end

endmodule
