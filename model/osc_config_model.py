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

eeg_data = { 
            '_alpha_readings': {}, 
            '_beta_readings': {}, 
            '_delta_readings': {}, 
            '_gamma_readings': {}, 
            '_theta_readings': {},
            '_gyroscope_readings': {},
            '_accelerometer_readings': {},
            '_is_blink_detected': False}

def alpha_absolute_eeg_handler(address: int,*args):
    _alpha_readings = {
        'TP9': args[0],
        'AF7': args[1],
        'AF8': args[2],
        'TP10': args[3],
    }
    eeg_data['_alpha_readings'] = _alpha_readings

def beta_absolute_eeg_handler(address: int,*args):
    _beta_readings = {
        'TP9': args[0],
        'AF7': args[1],
        'AF8': args[2],
        'TP10': args[3],
    }
    eeg_data['_beta_readings'] = _beta_readings

def delta_absolute_eeg_handler(address: int,*args):
    _delta_readings = {
        'TP9': args[0],
        'AF7': args[1],
        'AF8': args[2],
        'TP10': args[3],
    }
    eeg_data['_delta_readings'] = _delta_readings

def gamma_absolute_eeg_handler(address: int,*args):
    _gamma_readings = {
        'TP9': args[0],
        'AF7': args[1],
        'AF8': args[2],
        'TP10': args[3],
    }
    eeg_data['_gamma_readings'] = _gamma_readings

def theta_absolute_eeg_handler(address: int,*args):
    _theta_readings = {
        'TP9': args[0],
        'AF7': args[1],
        'AF8': args[2],
        'TP10': args[3],
    }
    eeg_data['_theta_readings'] = _theta_readings

def gyroscope_values_handler(address: int,*args):
    _gyroscope_readings = {
        'X': args[0],
        'Y': args[1],
        'Z': args[2]
    }
    eeg_data['_gyroscope_readings'] = _gyroscope_readings

def accelerometer_values_handler(address: float,*args):
    _accelerometer_readings = {
        'X': args[0],
        'Y': args[1],
        'Z': args[2]
    }
    eeg_data['_accelerometer_readings'] = _accelerometer_readings

def blink_detection_handler (address: str,*args):
    if args[0] == 1:
        eeg_data['_is_blink_detected'] = True
        # global _is_blink_detected
        # _is_blink_detected = True

async def send_data(websocket, path):
    # initial values
    while True:
        if True:
            await websocket.send(json.dumps(eeg_data))
            eeg_data['_is_blink_detected'] = False
        await asyncio.sleep(0.1)

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