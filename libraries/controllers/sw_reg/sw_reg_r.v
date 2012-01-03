//=====================================================
//             _________
//       read |         | write
//   SW <-----|   Reg   |<----- Fabric
//            |_________|
//
//=====================================================


module sw_reg_r #(
      //================
      // parameters
      //================
      parameter C_BASEADDR      = 32'h00000000,
      parameter C_HIGHADDR      = 32'h0000000F,
      parameter C_WB_DATA_WIDTH = 32,
      parameter C_WB_ADDR_WIDTH = 1,
      parameter C_BYTE_EN_WIDTH = 4
   ) (
      //================
      // fabric ports
      //================
      input         fabric_clk,
      input         fabric_data_in,
      
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
      output        wb_err_o
   );
 
   wire a_match = wb_adr_i >= C_BASEADDR && wb_adr_i <= C_HIGHADDR;
 
   reg [31:0] fabric_data_in_reg;
   
   //================
   // register buffer 
   //================
   reg [31:0] reg_buffer;
 
   //================
   // wb control
   //================
   reg wb_ack_reg;
   assign wb_ack_o = wb_ack_reg;
   always @(posedge wb_clk_i)
   begin
      wb_ack_reg <= 1'b0;
      if (wb_rst_i)
      begin
         //
      end
      else
      begin
         if (wb_stb_i && wb_cyc_i)
         begin
            wb_ack_reg <= 1'b1;
         end
      end
   end
 
   //================
   // wb read
   //================
   reg [31:0] wb_dat_o_reg;
   assign wb_dat_o = wb_dat_o_reg;
 
   always @(*)
   begin
      if (wb_rst_i)
      begin
         register_request <= 1'b0;
      end
      if(~wb_we_i)
      begin
         case (wb_adr_i[6:2])
            5'h0:   
            begin   
               wb_dat_o_reg <= reg_buffer;
            end
            default:
            begin
               wb_dat_o_reg <= 32'b0;
            end
         endcase
      end
      if (register_readyRR)
      begin
         register_request <= 1'b0;
      end
      if (register_readyRR && register_request)
      begin
         reg_buffer <= fabric_data_in_reg;
      end
 
      if (!register_readyRR)
      begin
         /* always request the buffer */
         register_request <= 1'b1;
      end
   end
   
   //================
   // fabric write
   //================
   
   /* Handshake signal from wb to application indicating new data should be latched */
   reg register_request;
   reg register_requestR;
   reg register_requestRR;
   /* Handshake signal from application to wb indicating data has been latched */
   reg register_ready;
   reg register_readyR;
   reg register_readyRR;
   
   always @(posedge fabric_clk)
   begin
      register_requestR  <= register_request;
      register_requestRR <= register_requestR;
 
      if (register_requestRR)
      begin
         register_ready <= 1'b1;
      end
 
      if (!register_requestRR)
      begin
         register_ready <= 1'b0;
      end
 
      if (register_requestRR && !register_ready)
      begin
         register_ready <= 1'b1;
         fabric_data_in_reg <= fabric_data_in;
      end
   end
endmodule
