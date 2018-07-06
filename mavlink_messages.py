from dronekit import connect
import time

vehicle = connect('/dev/serial0', wait_ready=True, baud=921600)

def send_PARAM_SET(param_id, param_value):
    #encode PARAM_SET mavlink message
    msg = vehicle.message_factory.param_set_encode(
        0,0, #target_system, target_component
        param_id,
        param_value,
        1)   #param_type: 8-bit unsigned integer 

    #send command
    vehicle.send_mavlink(msg)

print vehicle.parameters['FLTMODE1'] #read previous 'FLTMODE1' parameter

send_PARAM_SET('FLTMODE1', 0) #0: MANUAL for plane
'''
Another way of setting parameter is directly assing it to a value:
vehicle.parameters['FLTMODE1'] = 0
'''
time.sleep(0.1)

print vehicle.parameters['FLTMODE1']

