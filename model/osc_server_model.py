import random
from pythonosc import udp_client
from pythonosc.osc_message_builder import OscMessageBuilder
import time

# Configuration
target_ip = "192.168.1.208"  # Replace with your target IP address
target_port = 5001       # Replace with your target port number
osc_address = "/example" # OSC address pattern

# Initialize OSC client
client = udp_client.SimpleUDPClient(target_ip, target_port)

try:
    while True:
        # Create and send an OSC message
        msg_builder = OscMessageBuilder(address=osc_address)
        msg_builder.add_arg(random.randint(0, 100))  # Random integer
        msg_builder.add_arg(random.uniform(0, 10))   # Random float
        msg_builder.add_arg(random.choice(["A", "B", "C"]))  # Random string from list
        msg_builder.add_arg(random.choice([True, False]))    # Random boolean
        msg_builder.add_arg([random.randint(0, 10) for _ in range(3)])  # Random list of integers

        msg = msg_builder.build()
        client.send(msg)

        time.sleep(0.1)

        # time.sleep(0.1)  # Sleep to avoid flooding the network (adjust as needed)

except KeyboardInterrupt:
    print("OSC streaming stopped by user.")
