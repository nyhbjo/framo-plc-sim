class OPCInitConfig:
    def __init__(self,
        opc_object,
        address_space
        ):
        self.opc_object = opc_object
        self.address_space = address_space

    def init_opc(self):
        self.number_of_inlet_pumps = self.opc_object.add_variable(self.address_space,"NumberOfInletPumps",True)
        self.number_of_oxygenators = self.opc_object.add_variable(self.address_space,"NumberOfOxygenators",False)
        self.number_of_oxygen_sensors = self.opc_object.add_variable(self.address_space,"NumberOfOxygenSensors",False)
        self.number_of_level_sensors = self.opc_object.add_variable(self.address_space,"NumberOfLevelSensors",False)
        self.pump_plc_ip_address = self.opc_object.add_variable(self.address_space,"PumpPLCIP_IPaddress",False)
        self.oxygen_sensor_range_low = self.opc_object.add_variable(self.address_space,"OxygenSensorRangeLow",False)
        self.oxygen_sensor_range_high = self.opc_object.add_variable(self.address_space,"OxygenSensorRangeHigh",False)
        self.level_sensor_range_low = self.opc_object.add_variable(self.address_space,"LevelSensorRangeLow",False)
        self.level_sensor_range_high = self.opc_object.add_variable(self.address_space,"LevelSensorRangeHigh",False)
        
        self.number_of_inlet_pumps.set_writable()
        self.number_of_oxygenators.set_writable()
        self.number_of_oxygen_sensors.set_writable()
        self.number_of_level_sensors.set_writable()
        self.pump_plc_ip_address.set_writable()
        self.oxygen_sensor_range_low.set_writable()
        self.oxygen_sensor_range_high.set_writable()
        self.level_sensor_range_low.set_writable()
        self.level_sensor_range_high.set_writable()

    