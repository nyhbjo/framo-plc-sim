class OPCInitController:
    def __init__(self,
        controller,
        address_space
        ):
        self.controller = controller
        self.address_space = address_space

    def init_opc(self):
        self.pv = self.controller.add_variable(self.address_space,"pv",0.0)
        self.sp = self.controller.add_variable(self.address_space,"sp",0.0)
        self.out = self.controller.add_variable(self.address_space,"out",0.0)
        self.man = self.controller.add_variable(self.address_space,"man",True)
        self.kp = self.controller.add_variable(self.address_space,"kp",1.0)
        self.ti = self.controller.add_variable(self.address_space,"ti",10.0)
        self.td = self.controller.add_variable(self.address_space,"td",0.0)
        self.out_low = self.controller.add_variable(self.address_space,"out_low",0.0)
        self.out_high = self.controller.add_variable(self.address_space,"out_high",100.0)
        self.man_value = self.controller.add_variable(self.address_space,"man_value",0.0)

        self.sp.set_writable()
        self.pv.set_writable()
        self.out.set_writable()
        self.man.set_writable()
        self.kp.set_writable()
        self.ti.set_writable()
        self.td.set_writable()
        self.out_low.set_writable()
        self.out_high.set_writable()
        self.man_value.set_writable()

    