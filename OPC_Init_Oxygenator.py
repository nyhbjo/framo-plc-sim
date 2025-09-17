class OPCInitOxygenator:
    def __init__(self,
        opc_object,
        address_space
        ):
        self.opc_object = opc_object
        self.address_space = address_space

    def init_opc(self):
        self.ready = self.opc_object.add_variable(self.address_space,"ready",True)
        self.running = self.opc_object.add_variable(self.address_space,"running",False)
        self.fault = self.opc_object.add_variable(self.address_space,"fault",False)
        self.valve_pos = self.opc_object.add_variable(self.address_space,"valve_pos",False)
        self.oxygen_flow = self.opc_object.add_variable(self.address_space,"oxygen_flow",0.0)

        self.ready.set_writable()
        self.running.set_writable()
        self.fault.set_writable()
        self.valve_pos.set_writable()
        self.oxygen_flow.set_writable()
    