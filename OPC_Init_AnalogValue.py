class OPCInitAnalogValue:
    def __init__(self,
        opc_object,
        address_space,
        ):
        self.analogvalue = opc_object
        self.address_space = address_space

    def init_opc(self):
        self.engineering_units = self.analogvalue.add_variable(self.address_space, "EngineeringUnits", "%")
        self.value = self.analogvalue.add_variable(self.address_space, "Value",0.0)
        self.value_range_object = self.analogvalue.add_object(self.address_space,"ValueRange")
        self.value_range_low = self.value_range_object.add_variable(self.address_space, "Low",0.0)
        self.value_range_high = self.value_range_object.add_variable(self.address_space, "High",100.0)
        self.bad_quality = self.analogvalue.add_variable(self.address_space, "BadQuality",False)
        self.alarm_lowlow = self.analogvalue.add_variable(self.address_space, "AlarmLowLow",False)
        self.warning_low = self.analogvalue.add_variable(self.address_space, "WarningLow", False)
        self.warning_high = self.analogvalue.add_variable(self.address_space, "WarningHigh", False)
        self.alarm_highhigh = self.analogvalue.add_variable(self.address_space,"AlarmHighHigh",False)
        self.limit_lowlow = self.analogvalue.add_variable(self.address_space,"LimitLowLow",False)
        self.limit_low = self.analogvalue.add_variable(self.address_space, "LimitLow", False)
        self.limit_high = self.analogvalue.add_variable(self.address_space, "LimitHigh", False)
        self.limit_highhigh = self.analogvalue.add_variable(self.address_space, "LimitHighHigh",False)
        self.display_name = self.analogvalue.add_variable(self.address_space,"DisplayName", "Name")
        self.description = self.analogvalue.add_variable(self.address_space,"Description", "Description")
        self.logging_enabled = self.analogvalue.add_variable(self.address_space,"LoggingEnabled", False)

        self.engineering_units.set_writable()
        self.value.set_writable()
        self.value_range_low.set_writable()
        self.value_range_high.set_writable()
        self.bad_quality.set_writable()
        self.alarm_lowlow.set_writable()
        self.warning_low.set_writable()
        self.warning_high.set_writable()
        self.alarm_highhigh.set_writable()
        self.limit_lowlow.set_writable()
        self.limit_low.set_writable()
        self.limit_high.set_writable()
        self.limit_highhigh.set_writable()
        self.display_name.set_writable()
        self.description.set_writable()
        self.logging_enabled.set_writable()
