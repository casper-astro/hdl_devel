//============================================================================//
//                                                                            //
//      Parameterize Sync Delay                                               //
//                                                                            //
//      Module name: sync_delay                                               //
//      Desc: parameterized sync delay, using generate statements to create a //
//            varible length delay of variable width                          //
//      Date: April 2012                                                      //
//      Developer: Wesley New                                                 //
//      Licence: GNU General Public License ver 3                             //
//      Notes:                                                                //
//                                                                            //
//============================================================================//

module sync_delay #(
      //=============
      // parameters
      //=============
      parameter DATA_WIDTH = 32,
      parameter DELAY_CYCLES = 1
   ) (
      //=====================
      // input/output ports
      //=====================
      input  clk,
      //input  en,
      //input  rst,
      input  [DATA_WIDTH-1:0] din,
      output [DATA_WIDTH-1:0] dout,
      output data_valid
   );

   //TODO: Set the size of count correctly
   reg [DELAY_CYCLES-1:0] count;
   reg [DATA_WIDTH-1:0] data_in;
   reg [DATA_WIDTH-1:0] data_out;
   
   initial count = 0;

   // increment counter and set the data out to the data in
   // when count = DELAY_CYCLESalways @(posedge clk)
   always @ (posedge clk)
   begin
      if (count == 0)
      begin
         data_in <= din;
      end
      if (count == DELAY_CYCLES)
      begin
         data_out <= data_in;
         count <= 0;
      end
      else
      begin
         count = count + 1;
      end
   end

   // assign output to output reg 
   assign dout = data_out;
endmodule   
