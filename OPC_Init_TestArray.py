from opcua import ua


class OPCInitTestArray:
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
        self.tank_level_high = self.opc_object.add_variable(self.address_space,"TankLevelHigh",False)
        self.tank_level_low = self.opc_object.add_variable(self.address_space,"TankLevelLow",False)
        self.cooling_flow_low = self.opc_object.add_variable(self.address_space,"CoolingFlowLow",False)
        self.cooling_tank_level_low = self.opc_object.add_variable(self.address_space,"CoolingTankLevelLow",False)
        self.anti_siphon_valve_open = self.opc_object.add_variable(self.address_space,"AntiSiphonValveOpen",False)

        self.ready.set_writable()
        self.running.set_writable()
        self.fault.set_writable()
        self.tank_level_high.set_writable()
        self.tank_level_low.set_writable()
        self.cooling_flow_low.set_writable()
        self.cooling_tank_level_low.set_writable()
        self.anti_siphon_valve_open.set_writable()

    