import os
from datetime import datetime
from pythonosc import dispatcher
from pythonosc import osc_server
from dotenv import load_dotenv, dotenv_values 
load_dotenv() 

ip = os.getenv("IP_ADDRESS")
port = int(os.getenv("PORT"))

def eeg_handler(address: str,*args):
    print(len(args))
    print(args)
    
def eeg_handler2(address: str,*args):
    print(len(args))
    print(args)
    
if __name__ == "__main__":
    dispatcher = dispatcher.Dispatcher()
    dispatcher.map("/muse/elements/alpha_absolute", eeg_handler)
    # dispatcher.map("/muse/elements/alpha_absolute", eeg_handler)

    server = osc_server.ThreadingOSCUDPServer((ip, port), dispatcher)
    print("Listening on UDP port "+str(port))
    server.serve_forever()