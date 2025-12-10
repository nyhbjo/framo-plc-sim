import asyncio

class OPCInitEvent:
    def __init__(self,
        opc_object,
        address_space,
        default_value
        ):
        self.opc_object = opc_object
        self.address_space = address_space
        self.default_value = default_value

    async def init_opc(self):
        self.active = await self.opc_object.add_variable(self.address_space,"Active",self.default_value)
        
        await self.active.set_writable()
        