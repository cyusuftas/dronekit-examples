from dronekit import connect, VehicleMode
from math import pi
import time

connection_string = '/dev/serial0'
print 'Connecting to vehicle on: %s' % connection_string

#connect to vehicle
vehicle = connect(connection_string, wait_ready=True, baud=921600)

'''
#Set some attribute values
vehicle.mode = VehicleMode('QSTABILIZE')
vehicle.airspeed = 10
time.sleep(0.01)

#Get some vehicle attribute values
print 'Airspeed: %s' % vehicle.airspeed
print 'Mode: %s' % vehicle.mode.name
print 'System Status: %s' % vehicle.system_status.state
print 'GPS: %s' % vehicle.gps_0
print 'Last Heartbeat: %s' % vehicle.last_heartbeat

#Vehicle Capabilities
print vehicle.capabilities.set_actuator_target
print vehicle.capabilities.flight_termination
print vehicle.capabilities.compass_calibration
'''

'''
while True:
    ####Getting and setting attribute and parameter values 
    #print 'Pitch: %s, Yaw: %s, Roll: %s' % (vehicle.attitude.pitch*180/pi, vehicle.attitude.yaw*180/pi, vehicle.attitude.roll*180/pi)
    #print 'Heading: %s, Yaw: %s' % (vehicle.heading, vehicle.attitude.yaw*180/pi)
    #Check-Enable Quadplane
    if vehicle.parameters['Q_ENABLE'] == 0:
        print 'Quadplane is not activated.'
        print 'Activating Quadplane'
        vehicle.parameters['Q_ENABLE'] = 1
    else:
        print 'Quadplane is already activated.'
        break
    time.sleep(0.1)
'''

#close vehicle object before exiting script
vehicle.close()
