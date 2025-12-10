import asyncio

class OPCInitAlarm:
    def __init__(self,
        opc_object,
        address_space
        ):
        self.alarm = opc_object
        self.address_space = address_space

    async def init_opc(self):
        self.active = await self.alarm.add_variable(self.address_space,"Active",False)
        self.id = await self.alarm.add_variable(self.address_space,"Id",1)

        await self.active.set_writable()
        await self.id.set_writable()
        
    