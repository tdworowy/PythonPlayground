import myhdl
def add_gate(a,b,c, clk):
    @myhdl.always(clk.posedge)
    def logic():
        c.next = a and b
    return logic

def convert_to_vhd():
    a,b,c, clk = [myhdl.Signal(bool(0))for i in range(4)]
    myhdl.toVHDL(add_gate,a,b,c,clk)

