""" OTAA Node example compatible with the LoPy Nano Gateway """

from network import LoRa
import socket
import binascii
import struct
import time
#import config

# for EU868
LORA_FREQUENCY = 868100000
LORA_GW_DR = "SF7BW125" # DR_5
LORA_NODE_DR = 5

# initialize LoRa in LORAWAN mode.
lora = LoRa(mode=LoRa.LORAWAN)

# create an OTA authentication params
#setting found in ttn device / name of device with activation method OTAA
dev_eui = binascii.unhexlify('70B3D54995E573F7'.replace(' ','')) # these settings can be found from TTN
app_eui = binascii.unhexlify('70B3D59BA0000004'.replace(' ','')) # these settings can be found from TTN
app_key = binascii.unhexlify('3792D626DBA69EA929E3CA5EB403CACD'.replace(' ','')) # these settings can be found from TTN

# set the 3 default channels to the same frequency (must be before sending the OTAA join request)
#lora.add_channel(0, frequency=config.LORA_FREQUENCY, dr_min=0, dr_max=5)
#lora.add_channel(1, frequency=config.LORA_FREQUENCY, dr_min=0, dr_max=5)
#lora.add_channel(2, frequency=config.LORA_FREQUENCY, dr_min=0, dr_max=5)

#without import config working
lora.add_channel(0, frequency=LORA_FREQUENCY, dr_min=0, dr_max=5)
lora.add_channel(1, frequency=LORA_FREQUENCY, dr_min=0, dr_max=5)
lora.add_channel(2, frequency=LORA_FREQUENCY, dr_min=0, dr_max=5)

# join a network using OTAA
#lora.join(activation=LoRa.OTAA, auth=(dev_eui, app_eui, app_key), timeout=0, dr=config.LORA_NODE_DR)

#without import config working
lora.join(activation=LoRa.OTAA, auth=(dev_eui, app_eui, app_key), timeout=0, dr=LORA_NODE_DR)

# wait until the module has joined the network
while not lora.has_joined():
    time.sleep(2.5)
    print('Not joined yet...')

# remove all the non-default channels
for i in range(3, 16):
    lora.remove_channel(i)

# create a LoRa socket
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

# set the LoRaWAN data rate
#s.setsockopt(socket.SOL_LORA, socket.SO_DR, config.LORA_NODE_DR)

#without import config working
s.setsockopt(socket.SOL_LORA, socket.SO_DR, LORA_NODE_DR)

# make the socket blocking
s.setblocking(False)

time.sleep(5.0)

for i in range (200):
    s.send(b'PKT #' + bytes([i]))
    send_message = bytes([i])
    print(send_message)

    time.sleep(4)
    rx, port = s.recvfrom(256)
    if rx:
        print('Received: {}, on port: {}'.format(rx, port))
    time.sleep(6)
