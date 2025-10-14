from opcua import Server
from opcua import ua
from opcua.common.type_dictionary_buider import get_ua_class
from OPC_Init_AnalogValue import OPCInitAnalogValue
from OPC_Init_alarm import OPCInitAlarm
from OPC_Init_event import OPCInitEvent
from OPC_Init_simulation import OPCInitSimulation
import time

def main():
    server = Server()
    server.set_security_policy([ua.SecurityPolicyType.NoSecurity])

    # get the BaseObjectType to create new object type
    base_object_type = server.nodes.base_object_type

    url = "opc.tcp://10.20.1.240:4841"
    server.set_endpoint(url)
    address_space = server.register_namespace("FramoPLS_1")

    motor_frequency_object = server.nodes.objects.add_object(address_space, "MotorFrequency")
    motor_velocity_object = server.nodes.objects.add_object(address_space, "MotorVelocity")
    motor_current_object = server.nodes.objects.add_object(address_space, "MotorCurrent")
    motor_power_object = server.nodes.objects.add_object(address_space, "MotorPower")
    motor_voltage_object = server.nodes.objects.add_object(address_space, "MotorVoltage")
    motor_torque_object = server.nodes.objects.add_object(address_space, "MotorTorque")

    power_consumption_counter_object = server.nodes.objects.add_object(address_space, "PowerConsumptionCounter")
    dc_link_voltage_object = server.nodes.objects.add_object(address_space, "DCLinkVoltage")
    vsd_heatsink_temperature_object = server.nodes.objects.add_object(address_space, "VSDHeatSinkTemperature")
    vsd_operating_days_object = server.nodes.objects.add_object(address_space, "VSDOperatingDays")
    motor_running_days_object = server.nodes.objects.add_object(address_space, "MotorRunningDays")
    drive_error_object = server.nodes.objects.add_object(address_space, "DriveError")
    drive_communication_object = server.nodes.objects.add_object(address_space, "DriveCommunication")
    drive_not_in_remote_object = server.nodes.objects.add_object(address_space, "DriveNotInRemote")
    motor_temperature_object = server.nodes.objects.add_object(address_space, "MotorTemperature")
    emergency_stop_object = server.nodes.objects.add_object(address_space, "EmergencyStop")
    dc_undervoltage_error_object = server.nodes.objects.add_object(address_space, "DCUnderVoltageError")
    pump_stopped_object = server.nodes.objects.add_object(address_space, "PumpStopped")
    UPS_supply_error_object = server.nodes.objects.add_object(address_space, "UPSSupplyError")
    emergency_run_mode_object = server.nodes.objects.add_object(address_space, "EmergencyRunMode")
    low_power_object = server.nodes.objects.add_object(address_space, "LowPower")
    high_power_object = server.nodes.objects.add_object(address_space, "HighPower")
    
    pump_state_unavailable_object = server.nodes.objects.add_object(address_space,"PumpStateUnavailable")
    pump_state_available_object = server.nodes.objects.add_object(address_space,"PumpStateAvailable")
    pump_state_start_object = server.nodes.objects.add_object(address_space, "PumpStateStart")
    pump_state_stop_object = server.nodes.objects.add_object(address_space, "PumpStateStop")
    pump_state_remote_object = server.nodes.objects.add_object(address_space, "PumpStateRemote")
    pump_state_hold_object = server.nodes.objects.add_object(address_space, "PumpStateHold")
    pump_state_lockdown_object = server.nodes.objects.add_object(address_space,"PumpStateLockdown")

    start_object = server.nodes.objects.add_object(address_space, "Start")
    stop_object = server.nodes.objects.add_object(address_space, "Stop")
    reset_object = server.nodes.objects.add_object(address_space, "Reset")
    speed_sp_object = server.nodes.objects.add_object(address_space, "SpeedSetpoint")
    heartbeat_toggle_object = server.nodes.objects.add_object(address_space,"HeartbeatToggle")

    pressure_compressed_air_object = server.nodes.objects.add_object(address_space, "PressureCompressedAir")
    level_switch_lsl_object = server.nodes.objects.add_object(address_space, "LevelSwitchLSL01")
    level_switch_lsh_object = server.nodes.objects.add_object(address_space, "LevelSwitchLSH02")
    status_v001_object = server.nodes.objects.add_object(address_space, "StatusV001")
    status_v002_object = server.nodes.objects.add_object(address_space, "StatusV002")

    simulation_object = server.nodes.objects.add_object(address_space, "Simulation")

    motor_frequency = OPCInitAnalogValue(motor_frequency_object, address_space)
    motor_frequency.init_opc()
    motor_velocity = OPCInitAnalogValue(motor_velocity_object, address_space)
    motor_velocity.init_opc()
    motor_current = OPCInitAnalogValue(motor_current_object, address_space)
    motor_current.init_opc()
    motor_power = OPCInitAnalogValue(motor_power_object, address_space)
    motor_power.init_opc()
    motor_voltage = OPCInitAnalogValue(motor_voltage_object, address_space)
    motor_voltage.init_opc()
    motor_torque = OPCInitAnalogValue(motor_torque_object, address_space)
    motor_torque.init_opc()
    power_consumption_counter = OPCInitAnalogValue(power_consumption_counter_object, address_space)
    power_consumption_counter.init_opc()
    dc_link_voltage = OPCInitAnalogValue(dc_link_voltage_object, address_space)
    dc_link_voltage.init_opc()
    vsd_heatsink_temperature = OPCInitAnalogValue(vsd_heatsink_temperature_object, address_space)
    vsd_heatsink_temperature.init_opc()
    vsd_operating_days = OPCInitAnalogValue(vsd_operating_days_object, address_space)
    vsd_operating_days.init_opc()
    motor_running_days = OPCInitAnalogValue(motor_running_days_object, address_space)
    motor_running_days.init_opc()
    drive_error = OPCInitAlarm(drive_error_object, address_space)
    drive_error.init_opc()
    drive_communication = OPCInitAlarm(drive_communication_object, address_space)
    drive_communication.init_opc()
    drive_not_in_remote = OPCInitAlarm(drive_not_in_remote_object, address_space)
    drive_not_in_remote.init_opc()
    motor_temperature = OPCInitAlarm(motor_temperature_object, address_space)
    motor_temperature.init_opc()
    emergency_stop = OPCInitAlarm(emergency_stop_object, address_space)
    emergency_stop.init_opc()
    dc_undervoltage_error = OPCInitAlarm(dc_undervoltage_error_object, address_space)
    dc_undervoltage_error.init_opc()
    pump_stopped = OPCInitAlarm(pump_stopped_object, address_space)
    pump_stopped.init_opc()
    UPS_supply_error = OPCInitAlarm(UPS_supply_error_object, address_space)
    UPS_supply_error.init_opc()
    emergency_run_mode = OPCInitAlarm(emergency_run_mode_object, address_space)
    emergency_run_mode.init_opc()
    low_power = OPCInitAlarm(low_power_object, address_space)
    low_power.init_opc()
    high_power = OPCInitAlarm(high_power_object, address_space)
    high_power.init_opc()
    
    pump_state_unavailable = OPCInitEvent(pump_state_unavailable_object, address_space, False)
    pump_state_unavailable.init_opc()
    pump_state_available = OPCInitEvent(pump_state_available_object, address_space, True)
    pump_state_available.init_opc()
    pump_state_start = OPCInitEvent(pump_state_start_object, address_space,False)
    pump_state_start.init_opc()
    pump_state_stop = OPCInitEvent(pump_state_stop_object, address_space,False)
    pump_state_stop.init_opc()    
    pump_state_remote = OPCInitEvent(pump_state_remote_object, address_space,False)
    pump_state_remote.init_opc()
    pump_state_hold = OPCInitEvent(pump_state_hold_object, address_space,False)
    pump_state_hold.init_opc()
    pump_state_lockdown = OPCInitEvent(pump_state_lockdown_object, address_space,False)
    pump_state_lockdown.init_opc()

    start = OPCInitEvent(start_object, address_space, False)
    start.init_opc()
    stop = OPCInitEvent(stop_object, address_space,False)
    stop.init_opc()
    reset = OPCInitEvent(reset_object, address_space, False)
    reset.init_opc()
    speed_sp = OPCInitAnalogValue(speed_sp_object, address_space)
    speed_sp.init_opc()
    toggle = OPCInitEvent(heartbeat_toggle_object, address_space,False)
    toggle.init_opc()

    pressure_compressed_air = OPCInitAnalogValue(pressure_compressed_air_object, address_space)
    pressure_compressed_air.init_opc()
    level_switch_lsl = OPCInitEvent(level_switch_lsl_object, address_space,True)
    level_switch_lsl.init_opc()
    level_switch_lsh = OPCInitEvent(level_switch_lsh_object, address_space, False)
    level_switch_lsh.init_opc()
    status_v001 = OPCInitEvent(status_v001_object, address_space,True)
    status_v001.init_opc()
    status_v002 = OPCInitEvent(status_v002_object, address_space,True)
    status_v002.init_opc()

    simulation = OPCInitSimulation(simulation_object, address_space)
    simulation.init_opc()

    server.start()
    print("OPC UA server started at", url)

    inletpump_sequence_step = "available"
    inletpump_data_written = False
    toggle_last = not toggle.active.get_value()
    heartbeat_timeout = False
    minimum_pump_velocity = 32
    minimum_pump_frequency = 10
    minimum_pump_current = 15
    minimum_pump_power = 8
    minimum_pump_torque = 7
    minimum_pump_voltage = 400
    startup_pump_velocity = 42

    try:
        while True:
            if not toggle.active.get_value() == toggle_last: # HeartBeat
                toggle_last = toggle.active.get_value()
                toggle.active.set_value(not toggle_last)
            time.sleep(2)
            print(f"frequency = {motor_frequency.value.get_value()}")
            match inletpump_sequence_step:
                case "unavailable":
                    ## Pump unavailable
                    print("case : unavailble")
                    if not inletpump_data_written:
                        ## Pump
                        motor_frequency.value.set_value(0.0)
                        motor_current.value.set_value(0.0)
                        motor_power.value.set_value(0.0)
                        motor_torque.value.set_value(0.0)
                        motor_velocity.value.set_value(0.0)
                        motor_voltage.value.set_value(0.0)
                        motor_temperature.active.set_value(False)
                        dc_link_voltage.value.set_value(0.0)
                        dc_undervoltage_error.active.set_value(False)
                        vsd_heatsink_temperature.set_value(0.0)
                        drive_communication.active.set_value(True)
                        drive_not_in_remote.active.set_value(False)
                        drive_error.active.set_value(False)
                        pump_stopped.active.set_value(False)
                        UPS_supply_error.active.set_value(False)
                        emergency_run_mode.active.set_value(False)
                        low_power.active.set_value(False)
                        high_power.active.set_value(False)
                        pump_state_unavailable.active.set_value(False)
                        pump_state_available.active.set_value(True)
                        pump_state_remote.active.set_value(False)
                        pump_state_start.active.set_value(False)
                        pump_state_stop.active.set_value(False)
                        pump_state_hold.active.set_value(False)
                        pump_state_lockdown.active.set_value(False)
                        ## Vacuum system
                        pressure_compressed_air.value.set_value(0.0)
                        level_switch_lsl.active.set_value(True)
                        level_switch_lsh.active.set_value(False)
                        status_v001.active.set_value(False)
                        status_v002.active.set_value(True)
                        
                        inletpump_data_written = True
                                         
                    dc_undervoltage_error.active.set_value(simulation.dc_undervoltage_error.get_value())
                    drive_communication.active.set_value(simulation.drive_communication_error.get_value())
                    drive_not_in_remote.active.set_value(simulation.drive_not_in_remote.get_value())
                    emergency_stop.active.set_value(simulation.emergency_stop.get_value())
                    motor_temperature.active.set_value(simulation.motor_temperature.get_value())
                    UPS_supply_error.active.set_value(simulation.ups_supply_error.get_value())

                    if  not dc_undervoltage_error.active.get_value() \
                            and not drive_communication.active.get_value() \
                            and not drive_not_in_remote.active.get_value() \
                            and not emergency_stop.active.get_value() \
                            and not motor_temperature.active.get_value() \
                            and not UPS_supply_error.active.get_value():
                        inletpump_data_written = False
                        inletpump_sequence_step = "available"

                case "available":
                    print("case : available")
                    ## Pump available, not running
                    if not inletpump_data_written:
                        pump_state_unavailable.active.set_value(False)
                        pump_state_available.active.set_value(True)
                        print(f"pump state available = {pump_state_available.active.get_value()}")
                        pump_state_remote.active.set_value(False)
                        pump_state_start.active.set_value(False)
                        pump_state_stop.active.set_value(False)
                        pump_state_hold.active.set_value(False)
                        pump_state_lockdown.active.set_value(False)
                        ## Pump
                        motor_frequency.value.set_value(0.0)
                        motor_current.value.set_value(0.0)
                        motor_power.value.set_value(0.0)
                        motor_torque.value.set_value(0.0)
                        motor_velocity.value.set_value(0.0)
                        motor_voltage.value.set_value(0.0)
                        motor_temperature.active.set_value(False)
                        dc_link_voltage.value.set_value(0.0)
                        dc_undervoltage_error.active.set_value(False)
                        vsd_heatsink_temperature.value.set_value(15)
                        drive_communication.active.set_value(True)
                        drive_not_in_remote.active.set_value(False)
                        drive_error.active.set_value(False)
                        pump_stopped.active.set_value(False)
                        UPS_supply_error.active.set_value(False)
                        emergency_run_mode.active.set_value(False)
                        low_power.active.set_value(False)
                        high_power.active.set_value(False)
                        ## Vacuum system
                        pressure_compressed_air.value.set_value(0.0)
                        level_switch_lsl.active.set_value(True)
                        level_switch_lsh.active.set_value(False)
                        status_v001.active.set_value(False)
                        status_v002.active.set_value(True)
                        print("vacuum")                        
                        inletpump_data_written = True
                    #time.sleep(120)
                    tmp = simulation.dc_undervoltage_error.get_value()
                    print(f"dc undervoltage error = {tmp}")
                    dc_undervoltage_error.active.set_value(tmp)
                    print(f"dc undervoltage error = {dc_undervoltage_error.active.get_value()}")
                    drive_communication.active.set_value(simulation.drive_communication_error.get_value())
                    drive_not_in_remote.active.set_value(simulation.drive_not_in_remote.get_value())
                    emergency_stop.active.set_value(simulation.emergency_stop.get_value())
                    motor_temperature.active.set_value(simulation.motor_temperature.get_value())
                    UPS_supply_error.active.set_value(simulation.ups_supply_error.get_value())

                    if  dc_undervoltage_error.active.get_value() \
                            or drive_communication.active.get_value() \
                            or drive_not_in_remote.active.get_value() \
                            or emergency_stop.active.get_value() \
                            or motor_temperature.active.get_value() \
                            or UPS_supply_error.active.get_value():
                        inletpump_data_written = False
                        inletpump_sequence_step = "unavailable"
                    elif start.active.get_value():
                        print(f"Pump start = True, speed SP = {startup_pump_velocity}")
                        inletpump_data_written = False
                        inletpump_sequence_step = "start"

                case "start":
                    ## Starting - Run pump at minimum speed
                    print("Case - start")
                    if not inletpump_data_written:
                        pump_state_unavailable.active.set_value(False)
                        pump_state_available.active.set_value(False)
                        pump_state_remote.active.set_value(False)
                        pump_state_start.active.set_value(True)
                        pump_state_stop.active.set_value(False)
                        pump_state_hold.active.set_value(False)
                        pump_state_lockdown.active.set_value(False)
                    motor_frequency.value.set_value(minimum_pump_frequency)
                    motor_velocity.value.set_value(minimum_pump_velocity)
                    motor_current.value.set_value(minimum_pump_current)
                    motor_power.value.set_value(minimum_pump_power)
                    motor_voltage.value.set_value(minimum_pump_voltage)
                    motor_torque.value.set_value(minimum_pump_torque)
                    time.sleep(2)

                    # Vacuum system simulation
                    status_v001.active.set_value(True)
                    status_v002.active.set_value(False)
                    pressure_compressed_air.value.set_value(6.55)
                    time.sleep(3)
                    level_switch_lsl.active.set_value(False)
                    level_switch_lsh.active.set_value(False)
                    
                    dc_undervoltage_error.active.set_value(simulation.dc_undervoltage_error.get_value())
                    drive_communication.active.set_value(simulation.drive_communication_error.get_value())
                    drive_not_in_remote.active.set_value(simulation.drive_not_in_remote.get_value())
                    emergency_stop.active.set_value(simulation.emergency_stop.get_value())
                    motor_temperature.active.set_value(simulation.motor_temperature.get_value())
                    UPS_supply_error.active.set_value(simulation.ups_supply_error.get_value())

                    if  drive_error.active.get_value() \
                        or motor_temperature.active.get_value() \
                        or emergency_stop.active.get_value() \
                        or UPS_supply_error.active.get_value() \
                        or dc_undervoltage_error.active.get_value():
                            inletpump_data_written = False
                            inletpump_sequence_step = "lockdown"
                    else:
                        inletpump_data_written = False
                        inletpump_sequence_step = "ramp_up_speed"

                case "ramp_up_speed":
                ## Starting - ramp up speed
                    print("Ramp up speed")
                    if not inletpump_data_written:
                        pump_state_start.active.set_value(True)
                        inletpump_speed = 0.0
                        start_time = int(time.time())
                        inletpump_data_written = True
                    new_time = int(time.time())

                    if new_time-start_time >= 1:
                        inletpump_speed = inletpump_speed + 1   ## increase 1 rpm per second
                        print(f"Starting - rpm = {inletpump_speed} - Ref = {startup_pump_velocity:.3f}")
                        motor_frequency.value.set_value(50/15*inletpump_speed)
                        motor_current.value.set_value(4*inletpump_speed)
                        motor_power.value.set_value(120/15*inletpump_speed)
                        motor_torque.value.set_value(7.0)
                        motor_velocity.value.set_value(inletpump_speed)
                        motor_voltage.value.set_value(400.0)

                    drive_error.active.set_value(simulation.drive_error.get_value())
                    dc_undervoltage_error.active.set_value(simulation.dc_undervoltage_error.get_value())
                    drive_communication.active.set_value(simulation.drive_communication_error.get_value())
                    drive_not_in_remote.active.set_value(simulation.drive_not_in_remote.get_value())
                    emergency_stop.active.set_value(simulation.emergency_stop.get_value())
                    motor_temperature.active.set_value(simulation.motor_temperature.get_value())
                    UPS_supply_error.active.set_value(simulation.ups_supply_error.get_value())
                    print(f"ramp1 - speed = {inletpump_speed}")                    
                    if  drive_error.active.get_value() \
                            or motor_temperature.active.get_value() \
                            or emergency_stop.active.get_value() \
                            or UPS_supply_error.active.get_value() \
                            or dc_undervoltage_error.active.get_value():
                        inletpump_data_written = False
                        inletpump_sequence_step = 90
                    elif inletpump_speed >= startup_pump_velocity:
                        inletpump_data_written = False
                        inletpump_sequence_step = "remote"

                case "remote":
                ## Ramped up to reference speed
                    print("Case - remote")
                    if not inletpump_data_written:
                        pump_state_unavailable.active.set_value(False)
                        pump_state_available.active.set_value(False)
                        pump_state_remote.active.set_value(True)
                        pump_state_start.active.set_value(False)
                        pump_state_stop.active.set_value(False)
                        pump_state_hold.active.set_value(False)
                        pump_state_lockdown.active.set_value(False)
                        start_time = int(time.time())
                        inletpump_data_written = True

                    new_time = int(time.time())
                    inletpump_speed = motor_velocity.value.get_value()
                    inletpump_speed_sp = speed_sp.value.get_value()

                    if new_time-start_time >= 1:
                        start_time = int(time.time())
                        if inletpump_speed > inletpump_speed_sp + 1:
                            inletpump_speed = inletpump_speed - 1   ## change 1 rpm per second
                        elif inletpump_speed < inletpump_speed_sp - 1:
                            inletpump_speed = inletpump_speed - 1   ## change 1 rpm per second
                        motor_frequency.value.set_value(50/15*inletpump_speed)
                        motor_current.value.set_value(4*inletpump_speed)
                        motor_power.value.set_value(120/15*inletpump_speed)
                        motor_torque.value.set_value(12/15*inletpump_speed)
                        motor_velocity.value.set_value(inletpump_speed)
                        motor_voltage.value.set_value(399)

                    drive_error.active.set_value(simulation.drive_error.get_value())
                    dc_undervoltage_error.active.set_value(simulation.dc_undervoltage_error.get_value())
                    drive_communication.active.set_value(simulation.drive_communication_error.get_value())
                    drive_not_in_remote.active.set_value(simulation.drive_not_in_remote.get_value())
                    emergency_stop.active.set_value(simulation.emergency_stop.get_value())
                    motor_temperature.active.set_value(simulation.motor_temperature.get_value())
                    UPS_supply_error.active.set_value(simulation.ups_supply_error.get_value())
                    
                    if  drive_error.active.get_value() \
                            or motor_temperature.active.get_value() \
                            or emergency_stop.active.get_value() \
                            or UPS_supply_error.active.get_value() \
                            or dc_undervoltage_error.active.get_value():
                        inletpump_data_written = False
                        inletpump_sequence_step = "lockdown"
                    elif stop.active.get_value():
                        inletpump_data_written = False
                        inletpump_sequence_step = "stop"
                    elif heartbeat_timeout:
                        inletpump_data_written = False
                        inletpump_sequence_step = "hold"

                case "hold":
                ## Loss of comm. to PLC - keep current speed
                    if not inletpump_data_written:
                        pump_state_unavailable.active.set_value(False)
                        pump_state_available.active.set_value(False)
                        pump_state_remote.active.set_value(False)
                        pump_state_start.active.set_value(False)
                        pump_state_stop.active.set_value(False)
                        pump_state_hold.active.set_value(True)
                        pump_state_lockdown.active.set_value(False)                                                          
                        inletpump_data_written = True
                    if  drive_error.active.get_value() \
                            or motor_temperature.active.get_value() \
                            or emergency_stop.active.get_value() \
                            or UPS_supply_error.active.get_value() \
                            or dc_undervoltage_error.active.get_value:
                        inletpump_data_written = False
                        inletpump_sequence_step = "lockdown"
                    elif not heartbeat_timeout:
                        inletpump_data_written = False
                        inletpump_sequence_step = "remote"
                
                case "stop":
                    # stop the pump - ramp down speed
                    if not inletpump_data_written:
                        pump_state_unavailable.active.set_value(False)
                        pump_state_available.active.set_value(False)
                        pump_state_remote.active.set_value(False)
                        pump_state_start.active.set_value(False)
                        pump_state_stop.active.set_value(True)
                        pump_state_hold.active.set_value(False)
                        pump_state_lockdown.active.set_value(False)
                        inletpump_speed = motor_velocity.value.get_value()
                        start_time = int(time.time())
                        inletpump_data_written = True

                    new_time = int(time.time())

                    if new_time-start_time >= 1:
                        inletpump_speed = inletpump_speed - 0.5   ## decrease 0.5 rpm per second
                        if inletpump_speed < 0:
                            inletpump_speed = 0
                        print(f"Stopping : rpm = {inletpump_speed}")
                        motor_frequency.value.set_value(50/15*inletpump_speed)
                        motor_current.value.set_value(4*inletpump_speed)
                        motor_power.value.set_value(120/15*inletpump_speed)
                        motor_torque.value.set_value(7.0/15*inletpump_speed)
                        motor_velocity.value.set_value(inletpump_speed)
                        motor_voltage.value.set_value(400.0)

                    drive_error.active.set_value(simulation.drive_error.get_value())
                    dc_undervoltage_error.active.set_value(simulation.dc_undervoltage_error.get_value())
                    drive_communication.active.set_value(simulation.drive_communication_error.get_value())
                    drive_not_in_remote.active.set_value(simulation.drive_not_in_remote.get_value())
                    emergency_stop.active.set_value(simulation.emergency_stop.get_value())
                    motor_temperature.active.set_value(simulation.motor_temperature.get_value())
                    UPS_supply_error.active.set_value(simulation.ups_supply_error.get_value())
                    
                    if  drive_error.active.get_value() \
                            or motor_temperature.active.get_value() \
                            or emergency_stop.active.get_value() \
                            or UPS_supply_error.active.get_value() \
                            or dc_undervoltage_error.active.get_value():
                        inletpump_data_written = False
                        inletpump_sequence_step = "lockdown"
                    elif inletpump_speed <= 0.0:
                        inletpump_data_written = False
                        inletpump_sequence_step = "available"

                case "lockdown":
                        inletpump_data_written = False
                        inletpump_sequence_step = "available"

                case _:
                    print("Breaking out of while loop")
                    break
                                   
                
            
    except KeyboardInterrupt:
        print("Server keyboard interrupt")
        server.stop()
    except Exception:
        print("Exception stop")
        server.stop()
    finally:
        server.stop()
        print("Quitting - Server stopped")
        
if __name__ == "__main__":
    main()
