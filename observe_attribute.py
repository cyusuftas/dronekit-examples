from dronekit import connect, VehicleMode
import time

connection_string = '/dev/serial0'

#connect to the vehicle
vehicle = connect(connection_string, wait_ready = True, baud=921600)

def callback(self, attr_name, value):
    print '%s Value: %s' % (attr_name, value)

def parameter_callback(self, attr_name, value):
    print '%s Value: %s' % (attr_name, value)
    
#vehicle.add_attribute_listener('*', callback)  
vehicle.add_attribute_listener('mode', callback)
mode_changed = False
#time.sleep(3)

#observe parameter changes
vehicle.parameters.add_attribute_listener('*', parameter_callback)

time_start = time.time()
while True:    
    time_now = time.time()
    if 3 < time_now - time_start < 5 and not mode_changed:
        vehicle.mode = VehicleMode('MANUAL')
        mode_changed = True
    if time_now - time_start > 15:
        print 'exiting'
        break
    time.sleep(0.1)


#close vehicle
vehicle.close()
