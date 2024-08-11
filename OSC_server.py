import asyncio
import os
from datetime import datetime
from pythonosc import dispatcher
from pythonosc import osc_server
import websockets
import json
from dotenv import load_dotenv, dotenv_values 
load_dotenv() 
from tinydb import TinyDB, Query


ip = os.getenv("IP_ADDRESS")
port = int(os.getenv("PORT"))

alpha_data = {}
beta_data = {}
db = TinyDB('config/_alpha_readings.json')

User = Query()
db.insert({'name': 'John', 'age': 22})


# def alpha_absolute_eeg_handler(address: str,*args):
#     print(str(len(args) )+ " - __alpha values")
#     global alpha_data
#     alpha_data = {
#         "ch1": args[0] * 1, 
#         "ch2": args[1] * 1 , 
#         "ch3": args[2] * 1, 
#         "ch4": args[3] * 1
#         }

# def beta_absolute_eeg_handler(address: str,*args):
#     print(str(len(args) ) + " - __beta values")
#     global beta_data
#     beta_data = {
#         "ch1": args[0] * 1, 
#         "ch2": args[1] * 1 , 
#         "ch3": args[2] * 1, 
#         "ch4": args[3] * 1
#     }
    
# # async def send_data(websocket, path):
# #     while True:
# #         if True:
# #             # eeg_data.append(alpha_data)
# #             # eeg_data.append(beta_data)
# #             # print(eeg_data)
# #             json.loads(eeg_data)["__alpha"]
# #             await websocket.send(json.dumps(eeg_data))
# #         await asyncio.sleep(0.1)
        

# if __name__ == "__main__":
#     dispatcher = dispatcher.Dispatcher()
#     dispatcher.map("/muse/elements/alpha_absolute", alpha_absolute_eeg_handler)
#     dispatcher.map("/muse/elements/beta_absolute", beta_absolute_eeg_handler)

#     server = osc_server.ThreadingOSCUDPServer((ip, port), dispatcher)
#     print("Listening on UDP port "+str(port))

#     # websocket
#     # start_web_socket_server = websockets.serve(send_data, "localhost", 6789)
    
#     asyncio.get_event_loop().run_in_executor(None, server.serve_forever)
#     # asyncio.get_event_loop().run_until_complete(start_web_socket_server)
#     # asyncio.get_event_loop().run_forever()