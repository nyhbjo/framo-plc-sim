from opcua import Server
from opcua import ua
from opcua.common.type_dictionary_buider import get_ua_class
from OPC_Init_Pump import OPCInitPump
from OPC_Init_Controller import OPCInitController
from OPC_Init_Pen import OPCInitPen
from OPC_Init_VacuumSystem import OPCInitVacuumSystem
from OPC_Init_Oxygenator import OPCInitOxygenator
from OPC_Init_Config import OPCInitConfig
import time


def main():
    server = Server()
    server.set_security_policy([ua.SecurityPolicyType.NoSecurity])

    #url = "opc.tcp://127.0.0.1:4840/test/"
    url = "opc.tcp://10.20.1.240:4840"
    server.set_endpoint(url)

    address_space = server.register_namespace("CASNamespace")

    ##PumpClass = get_ua_class('PumpClassType')
    #inletpump1 = PumpClass()
    #inletpump2 = PumpClass()
    #inletpump3 = PumpClass()

    inletpump1_object = server.nodes.objects.add_object(address_space, "Pump1")
    inletpump2_object = server.nodes.objects.add_object(address_space, "Pump2")
    inletpump3_object = server.nodes.objects.add_object(address_space, "Pump3")

    oxypump1_object = server.nodes.objects.add_object(address_space, "OxyPump1")
    oxypump2_object = server.nodes.objects.add_object(address_space, "OxyPump2")
    oxypump3_object = server.nodes.objects.add_object(address_space, "OxyPump3")

    oxy_controller_object = server.nodes.objects.add_object(address_space, "OxyController")
    oxy_flow_controller_object = server.nodes.objects.add_object(address_space, "OxyFlowController")
    level_controller_object = server.nodes.objects.add_object(address_space, "LevelController")

    pen_sim_object = server.nodes.objects.add_object(address_space, "Pen")
    vacuum_system_object = server.nodes.objects.add_object(address_space, "VacuumSystem")

    oxygenator1_object = server.nodes.objects.add_object(address_space, "Oxygenator1")
    oxygenator2_object = server.nodes.objects.add_object(address_space, "Oxygenator2")
    oxygenator3_object = server.nodes.objects.add_object(address_space, "Oxygenator3")

    config_object = server.nodes.objects.add_object(address_space, "Config")

    #inletpump = OPCInitPump(inletpump1_object, address_space)
    #inletpump.init_opc()
    inletpump = [OPCInitPump(inletpump1_object, address_space),
            OPCInitPump(inletpump2_object, address_space),
            OPCInitPump(inletpump3_object, address_space)
        ]
    inletpump[0].init_opc()
    inletpump[1].init_opc()
    inletpump[2].init_opc()

    oxypump = [OPCInitPump(oxypump1_object, address_space),
               OPCInitPump(oxypump2_object, address_space),
               OPCInitPump(oxypump3_object, address_space)
        ]
    oxypump[0].init_opc()
    oxypump[1].init_opc()
    oxypump[2].init_opc()

    oxycontroller = OPCInitController(oxy_controller_object, address_space)
    oxycontroller.init_opc()

    oxyflowcontroller = OPCInitController(oxy_flow_controller_object, address_space)
    oxyflowcontroller.init_opc()

    levelcontroller = OPCInitController(level_controller_object, address_space)
    levelcontroller.init_opc()

    pen_sim = OPCInitPen(pen_sim_object, address_space)
    pen_sim.init_opc()

    vacuum_system = OPCInitVacuumSystem(vacuum_system_object, address_space)
    vacuum_system.init_opc()

    oxygenator1 = OPCInitOxygenator(oxygenator1_object, address_space)
    oxygenator1.init_opc()
    oxygenator2 = OPCInitOxygenator(oxygenator2_object, address_space)
    oxygenator2.init_opc()
    oxygenator3 = OPCInitOxygenator(oxygenator3_object, address_space)
    oxygenator3.init_opc()

    config = OPCInitConfig(config_object, address_space)
    config.init_opc()

    server.start()
    print("OPC UA server started at", url)



    try:
        while True:
            time.sleep(2)
            print(f"Pump1 frequency = {inletpump[0].frequency.get_value()}")
    except KeyboardInterrupt:
        print("Server keyboard interrupt")
        server.stop()
    except Exception:
        print("Exception stop")
        server.stop()
    finally:
        print("Server stopped")
        
if __name__ == "__main__":
    main()
