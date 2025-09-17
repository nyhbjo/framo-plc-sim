class OPCInitPump:
    def __init__(self,
        opc_object,
        address_space
        ):
        self.pump = opc_object
        self.address_space = address_space

    def init_opc(self):
        self.frequency = self.pump.add_variable(self.address_space, "frequency", 0.0)
        self.speed_sp = self.pump.add_variable(self.address_space, "speed_sp",0.0)
        self.freq_man = self.pump.add_variable(self.address_space,"man_freq",0.0)
        self.current = self.pump.add_variable(self.address_space, "current",0.0)
        self.power = self.pump.add_variable(self.address_space, "power",0.0)
        self.available = self.pump.add_variable(self.address_space, "available", True)
        self.starting = self.pump.add_variable(self.address_space, "starting", True)
        self.running = self.pump.add_variable(self.address_space,"running",True)
        self.warning = self.pump.add_variable(self.address_space,"warning",True)
        self.trip = self.pump.add_variable(self.address_space, "trip", False)
        self.fault_reset = self.pump.add_variable(self.address_space, "fault_reset", False)
        self.remote = self.pump.add_variable(self.address_space, "remote",False)
        self.manual = self.pump.add_variable(self.address_space,"manual", True)
        self.manual = self.pump.add_variable(self.address_space,"auto", True)
        self.start = self.pump.add_variable(self.address_space,"start", False)
        self.stop = self.pump.add_variable(self.address_space,"stop", True)
        self.speed_rpm = self.pump.add_variable(self.address_space,"speed_rpm",0.0)
        self.sim_fault = self.pump.add_variable(self.address_space,"sim_fault",False)
        self.sim_remote = self.pump.add_variable(self.address_space,"sim_remote",True)
        self.sim_speed_sp = self.pump.add_variable(self.address_space,"sim_speed_sp",True)
        self.sim_start = self.pump.add_variable(self.address_space,"sim_start",True)
        self.sim_stop = self.pump.add_variable(self.address_space,"sim_stop",True)

        self.frequency.set_writable()
        self.speed_sp.set_writable()
        self.freq_man.set_writable()
        self.current.set_writable()
        self.power.set_writable()
        self.available.set_writable()
        self.starting.set_writable()
        self.running.set_writable()
        self.warning.set_writable()
        self.trip.set_writable()
        self.fault_reset.set_writable()
        self.remote.set_writable()
        self.manual.set_writable()
        self.start.set_writable()
        self.stop.set_writable()
        self.speed_rpm.set_writable()
        self.sim_fault.set_writable()
        self.sim_remote.set_writable()
        self.sim_speed_sp.set_writable()
        self.sim_start.set_writable()
        self.sim_stop.set_writable()