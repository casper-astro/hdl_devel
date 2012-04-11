from myhdl import *

def clk_infrastructure_wrapper(block_name,
      sys_clk_n, sys_clk_p,
      sys_clk, sys_clk90, sys_clk180, sys_clk270,
      sys_clk_lock, op_power_on_rst,
      sys_clk2x, sys_clk2x90, sys_clk2x180, sys_clk2x270,
      #dly_clk_n, dly_clk_p,
      #dly_clk,
      epb_clk_in,
      epb_clk,
      aux_clk_n, aux_clk_p,
      aux_clk, aux_clk90, aux_clk180, aux_clk270,
      aux_clk2x, aux_clk2x90, aux_clk2x180, aux_clk2x270,
      idelay_rst,
      idelay_rdy,
      ARCHITECTURE="BEHAVIORAL",
      CLK_FREQ="100"
   ):

   @always(sys_clk_n.posedge)
   def logic():
      sys_clk_p = sys_clk_n

   __verilog__ = \
   """
   clk_infrastructure 
   #(
      .ARCHITECTURE     ("%(ARCHITECTURE)s"),
      .CLK_FREQ         (%(CLK_FREQ)s)
   ) clk_infrustructure_%(block_name)s (
      .sys_clk_n        (%(sys_clk_n)s),
      .sys_clk_p        (%(sys_clk_p)s),
      .sys_clk          (%(sys_clk)s), 
      .sys_clk90        (%(sys_clk90)s), 
      .sys_clk180       (%(sys_clk180)s), 
      .sys_clk270       (%(sys_clk270)s),
      .sys_clk_lock     (%(sys_clk_lock)s), 
      .op_power_on_rst  (%(op_power_on_rst)s),
      .sys_clk2x        (%(sys_clk2x)s), 
      .sys_clk2x90      (%(sys_clk2x90)s), 
      .sys_clk2x180     (%(sys_clk2x180)s), 
      .sys_clk2x270     (%(sys_clk2x270)s),
      .epb_clk_in       (%(epb_clk_in)s),
      .epb_clk          (%(epb_clk)s),
      .aux_clk_n        (%(aux_clk_n)s), 
      .aux_clk_p        (%(aux_clk_p)s),
      .aux_clk          (%(aux_clk)s), 
      .aux_clk90        (%(aux_clk90)s), 
      .aux_clk180       (%(aux_clk180)s), 
      .aux_clk270       (%(aux_clk270)s),
      .aux_clk2x        (%(aux_clk2x)s), 
      .aux_clk2x90      (%(aux_clk2x90)s), 
      .aux_clk2x180     (%(aux_clk2x180)s), 
      .aux_clk2x270     (%(aux_clk2x270)s),
      .idelay_rst       (%(idelay_rst)s),
      .idelay_rdy       (%(idelay_rdy)s)
   );
   """

   sys_clk.driven         = "wire"
   sys_clk90.driven       = "wire"
   sys_clk180.driven      = "wire"
   sys_clk270.driven      = "wire"
   sys_clk_lock.driven    = "wire"
   op_power_on_rst.driven = "wire"
   sys_clk2x.driven       = "wire"
   sys_clk2x90.driven     = "wire"
   sys_clk2x180.driven    = "wire"
   sys_clk2x270.driven    = "wire"
   epb_clk.driven         = "wire"
   
   aux_clk.driven      = "wire"
   aux_clk90.driven    = "wire"
   aux_clk180.driven   = "wire"
   aux_clk270.driven   = "wire"
   aux_clk2x.driven    = "wire"
   aux_clk2x90.driven  = "wire"
   aux_clk2x180.driven = "wire"
   aux_clk2x270.driven = "wire"

   #idelay_rdy.driven   = "wire"

   return logic

def convert():
   
   sys_clk_n, sys_clk_p, sys_clk, sys_clk90, sys_clk180, sys_clk270, sys_clk_lock, op_power_on_rst, sys_clk2x, sys_clk2x90, sys_clk2x180, sys_clk2x270, epb_clk_in, epb_clk, aux_clk_n, aux_clk_p, aux_clk, aux_clk90, aux_clk180, aux_clk270, aux_clk2x, aux_clk2x90, aux_clk2x180, aux_clk2x270, idelay_rst, idelay_rdy = [Signal(bool(0)) for i in range(26)] 
   
   
   toVerilog(clk_infrastructure_wrapper, "1", sys_clk_n, sys_clk_p, sys_clk, sys_clk90, sys_clk180, sys_clk270, sys_clk_lock, op_power_on_rst, sys_clk2x, sys_clk2x90, sys_clk2x180, sys_clk2x270, epb_clk_in, epb_clk, aux_clk_n, aux_clk_p, aux_clk, aux_clk90, aux_clk180, aux_clk270, aux_clk2x, aux_clk2x90, aux_clk2x180, aux_clk2x270, idelay_rst, idelay_rdy, ARCHITECTURE="VIRTEX6")

if __name__ == "__main__":
   convert()

