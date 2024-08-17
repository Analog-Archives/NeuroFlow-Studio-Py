import random
from pythonosc import udp_client
from pythonosc.osc_message_builder import OscMessageBuilder
import time
from tinydb import TinyDB, Query

# Configuration
target_ip = "192.168.1.208"  # Replace with your target IP address
target_port = 5001       # Replace with your target port number
osc_address = "/example" # OSC address pattern

# Initialize OSC client
client = udp_client.SimpleUDPClient(target_ip, target_port)

def control_server(data):
    print(data['_gyroscope_readings']['X'])
    # while True:
        # Create and send an OSC message
    msg_builder = OscMessageBuilder(address=osc_address)

    # _alpha_readings
    msg_builder.add_arg(data['_alpha_readings']['TP9'])
    msg_builder.add_arg(data['_alpha_readings']['AF7'])
    msg_builder.add_arg(data['_alpha_readings']['AF8'])
    msg_builder.add_arg(data['_alpha_readings']['TP10'])

    # _beta_readings
    msg_builder.add_arg(data['_beta_readings']['TP9'])
    msg_builder.add_arg(data['_beta_readings']['AF7'])
    msg_builder.add_arg(data['_beta_readings']['AF8'])
    msg_builder.add_arg(data['_beta_readings']['TP10'])

    # _delta_readings
    msg_builder.add_arg(data['_delta_readings']['TP9'])
    msg_builder.add_arg(data['_delta_readings']['AF7'])
    msg_builder.add_arg(data['_delta_readings']['AF8'])
    msg_builder.add_arg(data['_delta_readings']['TP10'])

     # _gamma_readings
    msg_builder.add_arg(data['_gamma_readings']['TP9'])
    msg_builder.add_arg(data['_gamma_readings']['AF7'])
    msg_builder.add_arg(data['_gamma_readings']['AF8'])
    msg_builder.add_arg(data['_gamma_readings']['TP10'])

    # _theta_readings
    msg_builder.add_arg(data['_theta_readings']['TP9'])
    msg_builder.add_arg(data['_theta_readings']['AF7'])
    msg_builder.add_arg(data['_theta_readings']['AF8'])
    msg_builder.add_arg(data['_theta_readings']['TP10'])
    
    # _gyroscope_readings
    msg_builder.add_arg(data['_gyroscope_readings']['X'])
    msg_builder.add_arg(data['_gyroscope_readings']['Y'])
    msg_builder.add_arg(data['_gyroscope_readings']['Z'])

    # # _accelerometer_readings
    msg_builder.add_arg(data['_accelerometer_readings']['X'])
    msg_builder.add_arg(data['_accelerometer_readings']['Y'])
    msg_builder.add_arg(data['_accelerometer_readings']['Z'])

    # # blink detection
    # if data['_is_blink_detected']:
    #     msg_builder.add_arg(1)
    # else :
    #     msg_builder.add_arg(0)

        
    msg = msg_builder.build()
    client.send(msg)
    # time.sleep(0.1)























# try:
#     while run_server:
#         # Create and send an OSC message
#         msg_builder = OscMessageBuilder(address=osc_address)
#         msg_builder.add_arg(random.randint(0, 100))  # Random integer
#         msg_builder.add_arg(random.uniform(0, 10))   # Random float
#         msg_builder.add_arg(random.choice(["A", "B", "C"]))  # Random string from list
#         msg_builder.add_arg(random.choice([True, False]))    # Random boolean
#         msg_builder.add_arg([random.randint(0, 10) for _ in range(3)])  # Random list of integers

#         msg = msg_builder.build()
#         client.send(msg)
#         time.sleep(0.1)

#     except KeyboardInterrupt:
#       print("OSC streaming stopped by user.")

