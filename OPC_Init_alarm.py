class OPCInitAlarm:
    def __init__(self,
        opc_object,
        address_space
        ):
        self.alarm = opc_object
        self.address_space = address_space

    def init_opc(self):
        self.active = self.alarm.add_variable(self.address_space,"Active",False)
        self.id = self.alarm.add_variable(self.address_space,"Id",1)

        self.active.set_writable()
        self.id.set_writable()
        
    