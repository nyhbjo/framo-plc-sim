import asyncio
from asyncua import ua

class OPCInitAnalogValue:
    def __init__(self,
        opc_object,
        address_space,
        ):
        self.opc_object = opc_object
        self.address_space = address_space

    async def init_opc(self):
        self.engineering_units = await self.opc_object.add_variable(self.address_space, "EngineeringUnits", "%", ua.VariantType.String)
        self.value = await self.opc_object.add_variable(self.address_space, "Value",0.0, ua.VariantType.Double)
        self.value_range_object = await self.opc_object.add_object(self.address_space,"ValueRange")
        self.value_range_low = await self.value_range_object.add_variable(self.address_space, "Low",0.0, ua.VariantType.Double)
        self.value_range_high = await self.value_range_object.add_variable(self.address_space, "High",100.0, ua.VariantType.Double)
        self.bad_quality = await self.opc_object.add_variable(self.address_space, "BadQuality",False, ua.VariantType.Boolean)
        self.alarm_lowlow = await self.opc_object.add_variable(self.address_space, "AlarmLowLow",False, ua. VariantType.Boolean)
        self.warning_low = await self.opc_object.add_variable(self.address_space, "WarningLow", False, ua.VariantType.Boolean)
        self.warning_high = await self.opc_object.add_variable(self.address_space, "WarningHigh", False, ua.VariantType.Boolean)
        self.alarm_highhigh = await self.opc_object.add_variable(self.address_space,"AlarmHighHigh",False, ua.VariantType.Boolean)
        self.limit_lowlow = await self.opc_object.add_variable(self.address_space,"LimitLowLow",False, ua.VariantType.Boolean)
        self.limit_low = await self.opc_object.add_variable(self.address_space, "LimitLow", False, ua.VariantType.Boolean)
        self.limit_high = await self.opc_object.add_variable(self.address_space, "LimitHigh", False, ua.VariantType.Boolean)
        self.limit_highhigh = await self.opc_object.add_variable(self.address_space, "LimitHighHigh",False, ua.VariantType.Boolean)
        self.display_name = await self.opc_object.add_variable(self.address_space,"DisplayName", "Name", ua.VariantType.Boolean)
        self.description = await self.opc_object.add_variable(self.address_space,"Description", "Description", ua.VariantType.Boolean)
        self.logging_enabled = await self.opc_object.add_variable(self.address_space,"LoggingEnabled", False, ua.VariantType.Boolean)

        await self.engineering_units.set_writable()
        await self.value.set_writable()
        await self.value_range_low.set_writable()
        await self.value_range_high.set_writable()
        await self.bad_quality.set_writable()
        await self.alarm_lowlow.set_writable()
        await self.warning_low.set_writable()
        await self.warning_high.set_writable()
        await self.alarm_highhigh.set_writable()
        await self.limit_lowlow.set_writable()
        await self.limit_low.set_writable()
        await self.limit_high.set_writable()
        await self.limit_highhigh.set_writable()
        await self.display_name.set_writable()
        await self.description.set_writable()
        await self.logging_enabled.set_writable()
