import asyncio
from asyncua import Server, ua, Client, Node
from asyncua.common.methods import uamethod
#from opcua.common.type_dictionary_buider import get_ua_class
from OPC_Init_AnalogValue import OPCInitAnalogValue
from OPC_Init_alarm import OPCInitAlarm
from OPC_Init_event import OPCInitEvent
from OPC_Init_simulation import OPCInitSimulation
import time

async def main():
    server = Server()
    await server.init()

    url = "opc.tcp://10.20.1.240:4841"
    server.set_endpoint(url)
    server.set_security_policy([ua.SecurityPolicyType.NoSecurity])
    server.set_server_name("FramoPLS_1")

    address_space = await server.register_namespace("FramoPLS_2")

    motor_frequency_object = await server.nodes.objects.add_object(address_space, "MotorFrequency")
    motor_velocity_object = await server.nodes.objects.add_object(address_space, "MotorVelocity")
    motor_current_object = await server.nodes.objects.add_object(address_space, "MotorCurrent")
    motor_power_object = await server.nodes.objects.add_object(address_space, "MotorPower")
    motor_voltage_object = await server.nodes.objects.add_object(address_space, "MotorVoltage")
    motor_torque_object = await server.nodes.objects.add_object(address_space, "MotorTorque")

    power_consumption_counter_object = await server.nodes.objects.add_object(address_space, "PowerConsumptionCounter")
    dc_link_voltage_object = await server.nodes.objects.add_object(address_space, "DCLinkVoltage")
    vsd_heatsink_temperature_object = await server.nodes.objects.add_object(address_space, "VSDHeatSinkTemperature")
    vsd_operating_days_object = await server.nodes.objects.add_object(address_space, "VSDOperatingDays")
    motor_running_days_object = await server.nodes.objects.add_object(address_space, "MotorRunningDays")
    drive_error_object = await server.nodes.objects.add_object(address_space, "DriveError")
    drive_communication_object = await server.nodes.objects.add_object(address_space, "DriveCommunication")
    drive_not_in_remote_object = await server.nodes.objects.add_object(address_space, "DriveNotInRemote")
    motor_temperature_object = await server.nodes.objects.add_object(address_space, "MotorTemperature")
    emergency_stop_object = await server.nodes.objects.add_object(address_space, "EmergencyStop")
    dc_undervoltage_error_object = await server.nodes.objects.add_object(address_space, "DCUnderVoltageError")
    pump_stopped_object = await server.nodes.objects.add_object(address_space, "PumpStopped")
    UPS_supply_error_object = await server.nodes.objects.add_object(address_space, "UPSSupplyError")
    emergency_run_mode_object = await server.nodes.objects.add_object(address_space, "EmergencyRunMode")
    low_power_object = await server.nodes.objects.add_object(address_space, "LowPower")
    high_power_object = await server.nodes.objects.add_object(address_space, "HighPower")
    
    pump_state_unavailable_object = await server.nodes.objects.add_object(address_space,"PumpStateUnavailable")
    pump_state_available_object = await server.nodes.objects.add_object(address_space,"PumpStateAvailable")
    pump_state_start_object = await server.nodes.objects.add_object(address_space, "PumpStateStart")
    pump_state_stop_object = await server.nodes.objects.add_object(address_space, "PumpStateStop")
    pump_state_remote_object = await server.nodes.objects.add_object(address_space, "PumpStateRemote")
    pump_state_hold_object = await server.nodes.objects.add_object(address_space, "PumpStateHold")
    pump_state_lockdown_object = await server.nodes.objects.add_object(address_space,"PumpStateLockdown")

    start_object = await server.nodes.objects.add_object(address_space, "Start")
    stop_object = await server.nodes.objects.add_object(address_space, "Stop")
    reset_object = await server.nodes.objects.add_object(address_space, "Reset")
    speed_sp_object = await server.nodes.objects.add_object(address_space, "SpeedSetpoint")
    heartbeat_toggle_object = await server.nodes.objects.add_object(address_space,"HeartbeatToggle")

    pressure_compressed_air_object = await server.nodes.objects.add_object(address_space, "PressureCompressedAir")
    level_switch_lsl_object = await server.nodes.objects.add_object(address_space, "LevelSwitchLSL01")
    level_switch_lsh_object = await server.nodes.objects.add_object(address_space, "LevelSwitchLSH02")
    status_v001_object = await server.nodes.objects.add_object(address_space, "StatusV001")
    status_v002_object = await server.nodes.objects.add_object(address_space, "StatusV002")

    simulation_object = await server.nodes.objects.add_object(address_space, "Simulation")

    motor_frequency = OPCInitAnalogValue(motor_frequency_object, address_space)
    await motor_frequency.init_opc()
    motor_velocity = OPCInitAnalogValue(motor_velocity_object, address_space)
    await motor_velocity.init_opc()
    motor_current = OPCInitAnalogValue(motor_current_object, address_space)
    await motor_current.init_opc()
    motor_power = OPCInitAnalogValue(motor_power_object, address_space)
    await motor_power.init_opc()
    motor_voltage = OPCInitAnalogValue(motor_voltage_object, address_space)
    await motor_voltage.init_opc()
    motor_torque = OPCInitAnalogValue(motor_torque_object, address_space)
    await motor_torque.init_opc()
    power_consumption_counter = OPCInitAnalogValue(power_consumption_counter_object, address_space)
    await power_consumption_counter.init_opc()
    dc_link_voltage = OPCInitAnalogValue(dc_link_voltage_object, address_space)
    await dc_link_voltage.init_opc()
    vsd_heatsink_temperature = OPCInitAnalogValue(vsd_heatsink_temperature_object, address_space)
    await vsd_heatsink_temperature.init_opc()
    vsd_operating_days = OPCInitAnalogValue(vsd_operating_days_object, address_space)
    await vsd_operating_days.init_opc()
    motor_running_days = OPCInitAnalogValue(motor_running_days_object, address_space)
    await motor_running_days.init_opc()
    drive_error = OPCInitAlarm(drive_error_object, address_space)
    await drive_error.init_opc()
    drive_communication = OPCInitAlarm(drive_communication_object, address_space)
    await drive_communication.init_opc()
    drive_not_in_remote = OPCInitAlarm(drive_not_in_remote_object, address_space)
    await drive_not_in_remote.init_opc()
    motor_temperature = OPCInitAlarm(motor_temperature_object, address_space)
    await motor_temperature.init_opc()
    emergency_stop = OPCInitAlarm(emergency_stop_object, address_space)
    await emergency_stop.init_opc()
    dc_undervoltage_error = OPCInitAlarm(dc_undervoltage_error_object, address_space)
    await dc_undervoltage_error.init_opc()
    pump_stopped = OPCInitAlarm(pump_stopped_object, address_space)
    await pump_stopped.init_opc()
    UPS_supply_error = OPCInitAlarm(UPS_supply_error_object, address_space)
    await UPS_supply_error.init_opc()
    emergency_run_mode = OPCInitAlarm(emergency_run_mode_object, address_space)
    await emergency_run_mode.init_opc()
    low_power = OPCInitAlarm(low_power_object, address_space)
    await low_power.init_opc()
    high_power = OPCInitAlarm(high_power_object, address_space)
    await high_power.init_opc()
    
    pump_state_unavailable = OPCInitEvent(pump_state_unavailable_object, address_space, False)
    await pump_state_unavailable.init_opc()
    pump_state_available = OPCInitEvent(pump_state_available_object, address_space, True)
    await pump_state_available.init_opc()
    pump_state_start = OPCInitEvent(pump_state_start_object, address_space,False)
    await pump_state_start.init_opc()
    pump_state_stop = OPCInitEvent(pump_state_stop_object, address_space,False)
    await pump_state_stop.init_opc()    
    pump_state_remote = OPCInitEvent(pump_state_remote_object, address_space,False)
    await pump_state_remote.init_opc()
    pump_state_hold = OPCInitEvent(pump_state_hold_object, address_space,False)
    await pump_state_hold.init_opc()
    pump_state_lockdown = OPCInitEvent(pump_state_lockdown_object, address_space,False)
    await pump_state_lockdown.init_opc()

    start = OPCInitEvent(start_object, address_space, False)
    await start.init_opc()
    stop = OPCInitEvent(stop_object, address_space,False)
    await stop.init_opc()
    reset = OPCInitEvent(reset_object, address_space, False)
    await reset.init_opc()
    speed_sp = OPCInitAnalogValue(speed_sp_object, address_space)
    await speed_sp.init_opc()
    toggle = OPCInitEvent(heartbeat_toggle_object, address_space,False)
    await toggle.init_opc()

    pressure_compressed_air = OPCInitAnalogValue(pressure_compressed_air_object, address_space)
    await pressure_compressed_air.init_opc()
    level_switch_lsl = OPCInitEvent(level_switch_lsl_object, address_space,True)
    await level_switch_lsl.init_opc()
    level_switch_lsh = OPCInitEvent(level_switch_lsh_object, address_space, False)
    await level_switch_lsh.init_opc()
    status_v001 = OPCInitEvent(status_v001_object, address_space,True)
    await status_v001.init_opc()
    status_v002 = OPCInitEvent(status_v002_object, address_space,True)
    await status_v002.init_opc()

    simulation = OPCInitSimulation(simulation_object, address_space)
    await simulation.init_opc()

    #await server.start()
    print("OPC UA server started at", url)

    inletpump_sequence_step = "available"
    inletpump_data_written = False
    toggle_last = not await toggle.active.get_value()
    heartbeat_timeout = False
    minimum_pump_velocity = 38
    minimum_pump_frequency = 10
    minimum_pump_current = 15
    minimum_pump_power = 3
    minimum_pump_torque = 7
    minimum_pump_voltage = 400
    startup_pump_velocity = 40
    max_pump_velocity = 80

    try:
        async with server:
            while True:
                await asyncio.sleep(2)
                if not await toggle.active.get_value() == toggle_last: # HeartBeat
                    toggle_last = await toggle.active.get_value()
                    await toggle.active.write_value(not toggle_last)
                
                match inletpump_sequence_step:
                    case "unavailable":
                        ## Pump unavailable
                        #print("case : unavailble")
                        if not inletpump_data_written:
                            ## Pump
                            await motor_frequency.value.write_value(0.0,ua.VariantType.Double)
                            await motor_current.value.write_value(0.0,ua.VariantType.Double)
                            await motor_power.value.write_value(0.0,ua.VariantType.Double)
                            await motor_torque.value.write_value(0.0,ua.VariantType.Double)
                            await motor_velocity.value.write_value(0.0,ua.VariantType.Double)
                            await motor_voltage.value.write_value(0.0,ua.VariantType.Double)
                            await motor_temperature.active.write_value(False)
                            await dc_link_voltage.value.write_value(0.0,ua.VariantType.Double)
                            await dc_undervoltage_error.active.write_value(False)
                            await vsd_heatsink_temperature.write_value(0.0,ua.VariantType.Double)
                            await drive_communication.active.write_value(True)
                            await drive_not_in_remote.active.write_value(False)
                            await drive_error.active.write_value(False)
                            await pump_stopped.active.write_value(True)
                            await UPS_supply_error.active.write_value(False)
                            await emergency_run_mode.active.write_value(False)
                            await low_power.active.write_value(False)
                            await high_power.active.write_value(False)
                            await pump_state_unavailable.active.write_value(False)
                            await pump_state_available.active.write_value(True)
                            await pump_state_remote.active.write_value(False)
                            await pump_state_start.active.write_value(False)
                            await pump_state_stop.active.write_value(False)
                            await pump_state_hold.active.write_value(False)
                            await pump_state_lockdown.active.write_value(False)
                            ## Vacuum system
                            await pressure_compressed_air.value.write_value(0.0,ua.VariantType.Double)
                            await level_switch_lsl.active.write_value(True)
                            await level_switch_lsh.active.write_value(False)
                            await status_v001.active.write_value(True)
                            await status_v002.active.write_value(False)
                            
                            inletpump_data_written = True
                                            
                        await drive_error.active.write_value(simulation.drive_error.get_value())
                        await dc_undervoltage_error.active.write_value(simulation.dc_undervoltage_error.get_value())
                        await drive_communication.active.write_value(simulation.drive_communication_error.get_value())
                        await drive_not_in_remote.active.write_value(simulation.drive_not_in_remote.get_value())
                        await emergency_stop.active.write_value(simulation.emergency_stop.get_value())
                        await motor_temperature.active.write_value(simulation.motor_temperature.get_value())
                        await UPS_supply_error.active.write_value(simulation.ups_supply_error.get_value())

                        if  not await drive_error.active.get_value() \
                                and not await motor_temperature.active.get_value() \
                                and not await emergency_stop.active.get_value() \
                                and not await dc_undervoltage_error.active.get_value() \
                                and not await UPS_supply_error.active.get_value():
                            inletpump_data_written = False
                            inletpump_sequence_step = "available"

                    case "available":
                        #print("case : available")
                        ## Pump available, not running
                        if not inletpump_data_written:
                            await pump_state_unavailable.active.write_value(False)
                            await pump_state_available.active.write_value(True)
                            await pump_state_remote.active.write_value(False)
                            await pump_state_start.active.write_value(False)
                            await pump_state_stop.active.write_value(False)
                            await pump_state_hold.active.write_value(False)
                            await pump_state_lockdown.active.write_value(False)
                            ## Pump
                            await motor_frequency.value.write_value(0.0,ua.VariantType.Double)
                            await motor_current.value.write_value(0.0,ua.VariantType.Double)
                            await motor_power.value.write_value(0.0,ua.VariantType.Double)
                            await motor_torque.value.write_value(0.0,ua.VariantType.Double)
                            await motor_velocity.value.write_value(0.0,ua.VariantType.Double)
                            await motor_voltage.value.write_value(0.0,ua.VariantType.Double)
                            await motor_temperature.active.write_value(False)
                            await dc_link_voltage.value.write_value(0.0,ua.VariantType.Double)
                            await dc_undervoltage_error.active.write_value(False)
                            await vsd_heatsink_temperature.value.write_value(15,ua.VariantType.Double)
                            await drive_communication.active.write_value(True)
                            await drive_not_in_remote.active.write_value(False)
                            await drive_error.active.write_value(False)
                            await pump_stopped.active.write_value(True)
                            await UPS_supply_error.active.write_value(False)
                            await emergency_run_mode.active.write_value(False)
                            await low_power.active.write_value(False)
                            await high_power.active.write_value(False)
                            ## Vacuum system
                            await pressure_compressed_air.value.write_value(0.0,ua.VariantType.Double)
                            await level_switch_lsl.active.write_value(True)
                            await level_switch_lsh.active.write_value(False)
                            await status_v001.active.write_value(True)
                            await status_v002.active.write_value(False)
                            #print("vacuum")                        
                            inletpump_data_written = True
                        #time.sleep(120)
                        tmp = await simulation.dc_undervoltage_error.get_value()
                        #print(f"dc undervoltage error = {tmp}")
                        await dc_undervoltage_error.active.write_value(tmp)
                        #print(f"dc undervoltage error = {dc_undervoltage_error.active.get_value()}")
                        await drive_communication.active.write_value(await simulation.drive_communication_error.get_value())
                        await drive_not_in_remote.active.write_value(await simulation.drive_not_in_remote.get_value())
                        await emergency_stop.active.write_value(await simulation.emergency_stop.get_value())
                        await motor_temperature.active.write_value(await simulation.motor_temperature.get_value())
                        await UPS_supply_error.active.write_value(await simulation.ups_supply_error.get_value())
                        if  await dc_undervoltage_error.active.get_value() \
                                or await drive_communication.active.get_value() \
                                or await drive_not_in_remote.active.get_value() \
                                or await emergency_stop.active.get_value() \
                                or await motor_temperature.active.get_value() \
                                or await UPS_supply_error.active.get_value():
                            inletpump_data_written = False
                            inletpump_sequence_step = "unavailable"
                        elif await start.active.get_value():
                            print(f"Pump start = True, speed SP = {startup_pump_velocity}")
                            inletpump_data_written = False
                            inletpump_sequence_step = "start"

                    case "start":
                        ## Starting - Run pump at minimum speed
                        #print("Case - start")
                        if not inletpump_data_written:
                            await pump_state_unavailable.active.write_value(False)
                            await pump_state_available.active.write_value(False)
                            await pump_state_remote.active.write_value(False)
                            await pump_state_start.active.write_value(True)
                            await pump_state_stop.active.write_value(False)
                            await pump_state_hold.active.write_value(False)
                            await pump_state_lockdown.active.write_value(False)
                            await start.active.write_value(False)
                        await motor_frequency.value.write_value(minimum_pump_frequency,ua.VariantType.Double)
                        await motor_velocity.value.write_value(minimum_pump_velocity,ua.VariantType.Double)
                        await motor_current.value.write_value(minimum_pump_current,ua.VariantType.Double)
                        await motor_power.value.write_value(minimum_pump_power,ua.VariantType.Double)
                        await motor_voltage.value.write_value(minimum_pump_voltage,ua.VariantType.Double)
                        await motor_torque.value.write_value(minimum_pump_torque,ua.VariantType.Double)
                        await pump_stopped.active.write_value(False)
                        asyncio.sleep(2)

                        # Vacuum system simulation
                        await status_v001.active.write_value(False)
                        await status_v002.active.write_value(True)
                        await pressure_compressed_air.value.write_value(6.55,ua.VariantType.Double)
                        await pressure_compressed_air.engineering_units.write_value("bar")
                        asyncio.sleep(3)
                        await level_switch_lsl.active.write_value(False)
                        await level_switch_lsh.active.write_value(False)
                        
                        await dc_undervoltage_error.active.write_value(simulation.dc_undervoltage_error.get_value())
                        await drive_communication.active.write_value(simulation.drive_communication_error.get_value())
                        await drive_not_in_remote.active.write_value(simulation.drive_not_in_remote.get_value())
                        await emergency_stop.active.write_value(simulation.emergency_stop.get_value())
                        await motor_temperature.active.write_value(simulation.motor_temperature.get_value())
                        await UPS_supply_error.active.write_value(simulation.ups_supply_error.get_value())

                        if  await drive_error.active.get_value() \
                            or await motor_temperature.active.get_value() \
                            or await emergency_stop.active.get_value() \
                            or await UPS_supply_error.active.get_value() \
                            or await dc_undervoltage_error.active.get_value():
                                inletpump_data_written = False
                                inletpump_sequence_step = "lockdown"
                        else:
                            inletpump_data_written = False
                            inletpump_sequence_step = "ramp_up_speed"

                    case "ramp_up_speed":
                    ## Starting - ramp up speed
                        #print("Ramp up speed")
                        if not inletpump_data_written:
                            await pump_state_start.active.write_value(True)
                            inletpump_speed = 0.0
                            await pump_stopped.active.write_value(False)
                            start_time = int(time.time())
                            inletpump_data_written = True
                        new_time = int(time.time())

                        if new_time-start_time >= 1:
                            inletpump_speed = inletpump_speed + 2   ## increase 2 rpm per second
                            #print(f"Starting - rpm = {inletpump_speed} - Ref = {startup_pump_velocity:.3f}")
                            await motor_frequency.value.write_value(50/80*inletpump_speed,ua.VariantType.Double)
                            await motor_current.value.write_value(4*inletpump_speed,ua.VariantType.Double)
                            await motor_power.value.write_value(120/15*inletpump_speed,ua.VariantType.Double)
                            await motor_torque.value.write_value(7.0,ua.VariantType.Double)
                            await motor_velocity.value.write_value(inletpump_speed,ua.VariantType.Double)
                            await motor_voltage.value.write_value(400.0,ua.VariantType.Double)

                        await drive_error.active.write_value(simulation.drive_error.get_value())
                        await dc_undervoltage_error.active.write_value(simulation.dc_undervoltage_error.get_value())
                        await drive_communication.active.write_value(simulation.drive_communication_error.get_value())
                        await drive_not_in_remote.active.write_value(simulation.drive_not_in_remote.get_value())
                        await emergency_stop.active.write_value(simulation.emergency_stop.get_value())
                        await motor_temperature.active.write_value(simulation.motor_temperature.get_value())
                        await UPS_supply_error.active.write_value(simulation.ups_supply_error.get_value())
                        #print(f"ramp1 - speed = {inletpump_speed}")                    
                        if  await drive_error.active.get_value() \
                                or await motor_temperature.active.get_value() \
                                or await emergency_stop.active.get_value() \
                                or await UPS_supply_error.active.get_value() \
                                or await dc_undervoltage_error.active.get_value():
                            inletpump_data_written = False
                            inletpump_sequence_step = "lockdown"
                        elif await stop.active.get_value():
                            inletpump_data_written = False
                            inletpump_sequence_step = "stop"    
                        elif inletpump_speed >= startup_pump_velocity:
                            inletpump_data_written = False
                            inletpump_sequence_step = "remote"

                    case "remote":
                    ## Ramped up to reference speed
                        #print("Case - remote")
                        if not inletpump_data_written:
                            await pump_state_unavailable.active.write_value(False)
                            await pump_state_available.active.write_value(False)
                            await pump_state_remote.active.write_value(True)
                            await pump_state_start.active.write_value(False)
                            await pump_state_stop.active.write_value(False)
                            await pump_state_hold.active.write_value(False)
                            await pump_state_lockdown.active.write_value(False)
                            await pump_stopped.active.write_value(False)
                            start_time = int(time.time())
                            inletpump_data_written = True

                        new_time = int(time.time())
                        inletpump_speed = await motor_velocity.value.get_value()
                        inletpump_speed_sp = await speed_sp.value.get_value()

                        if new_time-start_time >= 1:
                            start_time = int(time.time())
                            if inletpump_speed > inletpump_speed_sp + 2:
                                inletpump_speed = inletpump_speed - 2   ## change 2 rpm per second
                            elif inletpump_speed < inletpump_speed_sp - 2:
                                inletpump_speed = inletpump_speed + 2   ## change 2 rpm per second
                            else:
                                inletpump_speed = inletpump_speed + (inletpump_speed_sp-inletpump_speed)/2
                            await motor_frequency.value.write_value(50/15*inletpump_speed,ua.VariantType.Double)
                            await motor_current.value.write_value(4*inletpump_speed,ua.VariantType.Double)
                            await motor_power.value.write_value(120/15*inletpump_speed,ua.VariantType.Double)
                            await motor_torque.value.write_value(12/15*inletpump_speed,ua.VariantType.Double)
                            await motor_velocity.value.write_value(inletpump_speed,ua.VariantType.Double)
                            await motor_voltage.value.write_value(399,ua.VariantType.Double)

                        await drive_error.active.write_value(simulation.drive_error.get_value())
                        await dc_undervoltage_error.active.write_value(simulation.dc_undervoltage_error.get_value())
                        await drive_communication.active.write_value(simulation.drive_communication_error.get_value())
                        await drive_not_in_remote.active.write_value(simulation.drive_not_in_remote.get_value())
                        await emergency_stop.active.write_value(simulation.emergency_stop.get_value())
                        await motor_temperature.active.write_value(simulation.motor_temperature.get_value())
                        await UPS_supply_error.active.write_value(simulation.ups_supply_error.get_value())
                        
                        if  await drive_error.active.get_value() \
                                or await motor_temperature.active.get_value() \
                                or await emergency_stop.active.get_value() \
                                or await UPS_supply_error.active.get_value() \
                                or await dc_undervoltage_error.active.get_value():
                            inletpump_data_written = False
                            inletpump_sequence_step = "lockdown"
                        elif await stop.active.get_value():
                            inletpump_data_written = False
                            inletpump_sequence_step = "stop"
                        elif heartbeat_timeout:
                            inletpump_data_written = False
                            inletpump_sequence_step = "hold"

                    case "hold":
                    ## Loss of comm. to PLC - keep current speed
                        if not inletpump_data_written:
                            await pump_state_unavailable.active.write_value(False)
                            await pump_state_available.active.write_value(False)
                            await pump_state_remote.active.write_value(False)
                            await pump_state_start.active.write_value(False)
                            await pump_state_stop.active.write_value(False)
                            await pump_state_hold.active.write_value(True)
                            await pump_state_lockdown.active.write_value(False)
                            await pump_stopped.active.write_value(False)                                                          
                            inletpump_data_written = True
                        if  await drive_error.active.get_value() \
                                or await motor_temperature.active.get_value() \
                                or await emergency_stop.active.get_value() \
                                or await UPS_supply_error.active.get_value() \
                                or await dc_undervoltage_error.active.get_value:
                            inletpump_data_written = False
                            inletpump_sequence_step = "lockdown"
                        elif not heartbeat_timeout:
                            inletpump_data_written = False
                            inletpump_sequence_step = "remote"
                    
                    case "stop":
                        # stop the pump - ramp down speed
                        #print("Case - stop")
                        if not inletpump_data_written:
                            await start.active.write_value(False)
                            await stop.active.write_value(False)
                            await pump_state_unavailable.active.write_value(False)
                            await pump_state_available.active.write_value(False)
                            await pump_state_remote.active.write_value(False)
                            await pump_state_start.active.write_value(False)
                            await pump_state_stop.active.write_value(True)
                            await pump_state_hold.active.write_value(False)
                            await pump_state_lockdown.active.write_value(False)
                            await pump_stopped.active.write_value(False)
                            inletpump_speed = await motor_velocity.value.get_value()
                            start_time = int(time.time())
                            inletpump_data_written = True

                        new_time = int(time.time())

                        if new_time-start_time >= 1:
                            inletpump_speed = inletpump_speed - 2   ## decrease 2 rpm per second
                            if inletpump_speed < 0:
                                inletpump_speed = 0
                            #print(f"Stopping : rpm = {inletpump_speed}")
                            await motor_frequency.value.write_value(50/15*inletpump_speed,ua.VariantType.Double)
                            await motor_current.value.write_value(4*inletpump_speed,ua.VariantType.Double)
                            await motor_power.value.write_value(120/15*inletpump_speed,ua.VariantType.Double)
                            await motor_torque.value.write_value(7.0/15*inletpump_speed,ua.VariantType.Double)
                            await motor_velocity.value.write_value(inletpump_speed,ua.VariantType.Double)
                            await motor_voltage.value.write_value(400.0,ua.VariantType.Double)

                        await drive_error.active.write_value(simulation.drive_error.get_value())
                        await dc_undervoltage_error.active.write_value(simulation.dc_undervoltage_error.get_value())
                        await drive_communication.active.write_value(simulation.drive_communication_error.get_value())
                        await drive_not_in_remote.active.write_value(simulation.drive_not_in_remote.get_value())
                        await emergency_stop.active.write_value(simulation.emergency_stop.get_value())
                        await motor_temperature.active.write_value(simulation.motor_temperature.get_value())
                        await UPS_supply_error.active.write_value(simulation.ups_supply_error.get_value())
                        
                        if  await drive_error.active.get_value() \
                                or await motor_temperature.active.get_value() \
                                or await emergency_stop.active.get_value() \
                                or await UPS_supply_error.active.get_value() \
                                or await dc_undervoltage_error.active.get_value():
                            inletpump_data_written = False
                            inletpump_sequence_step = "lockdown"
                        elif inletpump_speed <= 0.0:
                            inletpump_data_written = False
                            inletpump_sequence_step = "available"

                    case "lockdown":
                            #print("Case - lockdown")
                            asyncio.sleep(5)
                            await motor_frequency.value.write_value(0,ua.VariantType.Double)
                            await motor_current.value.write_value(0,ua.VariantType.Double)
                            await motor_power.value.write_value(0,ua.VariantType.Double)
                            await motor_torque.value.write_value(0,ua.VariantType.Double)
                            await motor_velocity.value.write_value(0,ua.VariantType.Double)
                            await motor_voltage.value.write_value(0,ua.VariantType.Double)
                            await pump_stopped.active.write_value(True)
                            await status_v001.active.write_value(True)
                            await status_v002.active.write_value(False)
                            inletpump_data_written = False
                            inletpump_sequence_step = "unavailable"

                    case _:
                        print("Unknown case - Breaking out of while loop")
                        break
                
            
    except KeyboardInterrupt:
        print("Server keyboard interrupt")
        #server.stop()
    except Exception:
        print("Exception stop")
        #server.stop()
    finally:
        server.stop()
        print("Server stopped")
        
if __name__ == "__main__":
    asyncio.run(main())