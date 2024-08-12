import asyncio
import time
import os
from datetime import datetime
from pythonosc import dispatcher
from pythonosc import osc_server
import websockets
import json
from dotenv import load_dotenv, dotenv_values 
load_dotenv() 
from tinydb import TinyDB, Query


# env values
ip = os.getenv("IP_ADDRESS")
port = int(os.getenv("PORT"))

# initial values
eeg_data = { 
            '_alpha_readings': {}, 
            '_beta_readings': {}, 
            '_delta_readings': {}, 
            '_gamma_readings': {}, 
            '_theta_readings': {},
            '_gyroscope_readings': {},
            '_accelerometer_readings': {},
            '_is_blink_detected': False}

_default_values_1 = {'TP9': 0.0, 'AF7': 0.0, 'AF8': 0.0, 'AF10': 0.0}
_default_values_2 = {'X': 0.0, 'Y': 0.0, 'Z': 0.0}

# array option
_alpha_readings = _default_values_1
_beta_readings = _default_values_1
_delta_readings = _default_values_1
_gamma_readings = _default_values_1
_theta_readings = _default_values_1
_gyroscope_readings = _default_values_2
_accelerometer_readings = _default_values_2
_is_blink_detected = False

def alpha_absolute_eeg_handler(address: int,*args):
    _alpha_readings['TP9'] = args[0]
    _alpha_readings['AF7'] = args[1]
    _alpha_readings['AF8'] = args[2]
    _alpha_readings['AF10'] = args[3]
    # print(_alpha_readings)

def beta_absolute_eeg_handler(address: int,*args):
    _beta_readings['TP9'] = args[0]
    _beta_readings['AF7'] = args[1]
    _beta_readings['AF8'] = args[2]
    _beta_readings['AF10'] = args[3]
    # print(_beta_readings)

def delta_absolute_eeg_handler(address: int,*args):
    _delta_readings['TP9'] = args[0]
    _delta_readings['AF7'] = args[1]
    _delta_readings['AF8'] = args[2]
    _delta_readings['AF10'] = args[3]
    # print(_delta_readings)

def gamma_absolute_eeg_handler(address: int,*args):
    _gamma_readings['TP9'] = args[0]
    _gamma_readings['AF7'] = args[1]
    _gamma_readings['AF8'] = args[2]
    _gamma_readings['AF10'] = args[3]
    # print(_gamma_readings)

def theta_absolute_eeg_handler(address: int,*args):
    _theta_readings['TP9'] = args[0]
    _theta_readings['AF7'] = args[1]
    _theta_readings['AF8'] = args[2]
    _theta_readings['AF10'] = args[3]
    # print(_theta_readings)

def gyroscope_values_handler(address: int,*args):
    _gyroscope_readings['X'] = args[0]
    _gyroscope_readings['Y'] = args[1]
    _gyroscope_readings['Z'] = args[2]

def accelerometer_values_handler(address: int,*args):
    _accelerometer_readings['X'] = args[0]
    _accelerometer_readings['Y'] = args[1]
    _accelerometer_readings['Z'] = args[2]

def blink_detection_handler (address: str,*args):
    if args[0] == 1:
        global _is_blink_detected
        _is_blink_detected = True

async def send_data(websocket, path):
    while True:
        if True:
            global eeg_data
            eeg_data['_alpha_readings'] = _alpha_readings
            eeg_data['_beta_readings'] = _beta_readings
            eeg_data['_delta_readings'] = _delta_readings
            eeg_data['_gamma_readings'] = _gamma_readings
            eeg_data['_theta_readings'] = _theta_readings
            eeg_data['_gyroscope_readings'] = _gyroscope_readings
            eeg_data['_accelerometer_readings'] = _accelerometer_readings
            global _is_blink_detected
            eeg_data['_is_blink_detected'] = _is_blink_detected
            # print(eeg_data)
            
            await websocket.send(json.dumps(eeg_data))
            # global _is_blink_detected
            _is_blink_detected = False
        await asyncio.sleep(0.1 * 1)
        

if __name__ == "__main__":    
    dispatcher = dispatcher.Dispatcher()
    dispatcher.map("/muse/elements/alpha_absolute", alpha_absolute_eeg_handler)
    dispatcher.map("/muse/elements/beta_absolute", beta_absolute_eeg_handler)
    dispatcher.map("/muse/elements/delta_absolute", delta_absolute_eeg_handler)
    dispatcher.map("/muse/elements/gamma_absolute", gamma_absolute_eeg_handler)
    dispatcher.map("/muse/elements/theta_absolute", theta_absolute_eeg_handler)
    dispatcher.map("/muse/gyro", gyroscope_values_handler)
    dispatcher.map("/muse/acc", accelerometer_values_handler)
    dispatcher.map("/muse/elements/blink", blink_detection_handler)
    

    server = osc_server.ThreadingOSCUDPServer((ip, port), dispatcher)
    print("Listening on UDP port "+str(port))

    # websocket
    start_web_socket_server = websockets.serve(send_data, "localhost", 6789)
    
    asyncio.get_event_loop().run_in_executor(None, server.serve_forever)
    asyncio.get_event_loop().run_until_complete(start_web_socket_server)
    asyncio.get_event_loop().run_forever()