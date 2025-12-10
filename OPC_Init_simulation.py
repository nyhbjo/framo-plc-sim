import asyncio

class OPCInitSimulation:
    def __init__(self,
        opc_object,
        address_space
        ):
        self.opc_object = opc_object
        self.address_space = address_space

    async def init_opc(self):
        self.dc_undervoltage_error = await self.opc_object.add_variable(self.address_space,"DCUndervoltageError",False)
        self.drive_error = await self.opc_object.add_variable(self.address_space,"DriveError",False)
        self.drive_not_in_remote = await self.opc_object.add_variable(self.address_space,"DriveNotInRemote",False)
        self.drive_communication_error = await self.opc_object.add_variable(self.address_space,"DriveCommunication",False)
        self.emergency_stop = await self.opc_object.add_variable(self.address_space,"EmergencyStop",False)
        self.motor_temperature = await self.opc_object.add_variable(self.address_space,"MotorTemperature", False)
        self.ups_supply_error = await self.opc_object.add_variable(self.address_space,"UPSSupplyError",False)

        await self.dc_undervoltage_error.set_writable()
        await self.drive_error.set_writable()
        await self.drive_not_in_remote.set_writable()
        await self.drive_communication_error.set_writable()
        await self.emergency_stop.set_writable()
        await self.motor_temperature.set_writable()
        await self.ups_supply_error.set_writable()
        
    