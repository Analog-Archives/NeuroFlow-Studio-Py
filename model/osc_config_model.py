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
import random
from pythonosc import udp_client
from pythonosc.osc_message_builder import OscMessageBuilder

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

# Initialize OSC client
# Configuration
target_ip = "192.168.1.208"  # Replace with your target IP address
target_port = 5001       # Replace with your target port number
osc_address = "/example" # OSC address pattern
client = udp_client.SimpleUDPClient(target_ip, target_port)
from osc_server_model import control_server
async def send_data(websocket, path):    
    # initial values
    while True:
        if True:
            db = TinyDB('data/data_layer.json')
            db.truncate()
            db.insert({ 'data': eeg_data })

            # print(db.all()[0]['data']['_gyroscope_readings'])
            
            await websocket.send(json.dumps(eeg_data))
            eeg_data['_is_blink_detected'] = False
            # OSC out
            # msg_builder = OscMessageBuilder(address=osc_address)
            # msg_builder.add_arg(random.randint(0, 100))  # Random integer
            # msg_builder.add_arg(random.uniform(0, 10))   # Random float
            # msg_builder.add_arg(random.choice(["A", "B", "C"]))  # Random string from list
            # msg_builder.add_arg(random.choice([True, False]))    # Random boolean
            # msg_builder.add_arg([random.randint(0, 10) for _ in range(3)])  # Random list of integers

            # msg = msg_builder.build()
            # client.send(msg)

            control_server(db.all()[0]['data'])
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