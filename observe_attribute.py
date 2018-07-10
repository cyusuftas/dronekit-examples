from dronekit import connect, VehicleMode
import time

#connection_string = '/dev/serial0'      #raspberry pi
connection_string = '127.0.0.1:14552'    #simulation

#connect to the vehicle
#vehicle = connect(connection_string, wait_ready = True, baud=921600)
vehicle = connect(connection_string, wait_ready = True)

#use decorator to observe changes in mode
@vehicle.on_attribute('mode')
def callback(self, attr_name, value):
    print '%s Value: %s' % (attr_name, value)

#use decorator to observe changes in any parameter
@vehicle.parameters.on_attribute('*')
def parameter_callback(self, attr_name, value):
    print '%s Value: %s' % (attr_name, value)
    
mode_changed = False
vehicle.mode = VehicleMode('STABILIZE')

time_start = time.time()
while True:    
    time_now = time.time()
    if 3 < time_now - time_start < 5 and not mode_changed:
        vehicle.mode = VehicleMode('GUIDED')
        mode_changed = True
    if time_now - time_start > 15:  #observe changes in 15 seconds then quit
        print 'exiting'
        break
    time.sleep(0.1)


#close vehicle
vehicle.close()
