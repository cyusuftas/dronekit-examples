from dronekit import connect
from pymavlink import mavutil
import time

#connect to the vehicle
#vehicle = connect('/dev/serial0', wait_ready=True, baud=921600)    #raspberry pi
vehicle = connect('udp:127.0.0.1:14552', wait_ready=True)           #simulation

def param_set(param_id, param_value):
    msg = vehicle.message_factory.param_set_encode(
        0,0,            #target_system, target_component        
        param_id,       
        param_value,
        mavutil.mavlink.MAV_PARAM_TYPE_INT64)                       #64 bit signed int
    vehicle.send_mavlink(msg)

#observe any changed parameter
@vehicle.parameters.on_attribute('*')
def param_callback(self, name, value):
    print '%s: %s' %(name, value)

def send_param_request_read(param_id):
    msg = vehicle.message_factory.param_request_read_encode(
        0,0,
        param_id,
        -1)
    vehicle.send_mavlink(msg)

def send_param_request_list():
    vehicle.send_mavlink(vehicle.message_factory.param_request_list_encode(0,0))

#observe parameter values emitted by vehicle
@vehicle.on_message('PARAM_VALUE')
def parameter_callback(self, name, message):
    print '%s value: %s' % (name, message)

vehicle.parameters['FLTMODE1'] = 1                                  #parameters can be set by using vehicle.parameters attribute
print 'param:FLTMODE1 value:%s' % vehicle.parameters['FLTMODE1']    #parameters can be read by using vehicle.parameters attribute
param_set('FLTMODE1', 2)                                            #parameters can also be set by using PARAM_SET mavlink message
time.sleep(0.1)                                                     
send_param_request_read('FLTMODE1')                                 #individual parameters can also be read by listening the PARAM_VALUE  
                                                                    #mavlink message emitted by the vehicle after sending PARAM_REQUEST_READ
send_param_request_read('FLTMODE1')
#send_param_request_list()
time.sleep(0.1)

#close
vehicle.close()
