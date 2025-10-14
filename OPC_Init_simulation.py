class OPCInitSimulation:
    def __init__(self,
        opc_object,
        address_space
        ):
        self.simulation = opc_object
        self.address_space = address_space

    def init_opc(self):
        self.dc_undervoltage_error = self.simulation.add_variable(self.address_space,"DCUndervoltageError",False)
        self.drive_error = self.simulation.add_variable(self.address_space,"DriveError",False)
        self.drive_not_in_remote = self.simulation.add_variable(self.address_space,"DriveNotInRemote",False)
        self.drive_communication_error = self.simulation.add_variable(self.address_space,"DriveCommunication",False)
        self.emergency_stop = self.simulation.add_variable(self.address_space,"EmergencyStop",False)
        self.motor_temperature = self.simulation.add_variable(self.address_space,"MotorTemperature", False)
        self.ups_supply_error = self.simulation.add_variable(self.address_space,"UPSSupplyError",False)

        self.dc_undervoltage_error.set_writable()
        self.drive_error.set_writable()
        self.drive_not_in_remote.set_writable()
        self.drive_communication_error.set_writable()
        self.emergency_stop.set_writable()
        self.motor_temperature.set_writable()
        self.ups_supply_error.set_writable()
        
    