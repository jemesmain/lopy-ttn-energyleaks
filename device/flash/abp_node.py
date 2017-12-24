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

# create an ABP authentication params
# these settings can be found from TTN device / device name with activation method APB
dev_addr = struct.unpack(">l", binascii.unhexlify('26011BFA'.replace(' ','')))[0] # these settings can be found from TTN
nwk_swkey = binascii.unhexlify('19688FC64C700099D456FA6CFEC66510'.replace(' ','')) # these settings can be found from TTN
app_swkey = binascii.unhexlify('DD0E9563117A7A5BA1BCC0C8A180E663'.replace(' ','')) # these settings can be found from TTN

# remove all the non-default channels
for i in range(3, 16):
    lora.remove_channel(i)

# set the 3 default channels to the same frequency
#lora.add_channel(0, frequency=config.LORA_FREQUENCY, dr_min=0, dr_max=5)
#lora.add_channel(1, frequency=config.LORA_FREQUENCY, dr_min=0, dr_max=5)
#lora.add_channel(2, frequency=config.LORA_FREQUENCY, dr_min=0, dr_max=5)

#without import config working
lora.add_channel(0, frequency=LORA_FREQUENCY, dr_min=0, dr_max=5)
lora.add_channel(1, frequency=LORA_FREQUENCY, dr_min=0, dr_max=5)
lora.add_channel(2, frequency=LORA_FREQUENCY, dr_min=0, dr_max=5)

# join a network using ABP (Activation By Personalization)
lora.join(activation=LoRa.ABP, auth=(dev_addr, nwk_swkey, app_swkey))

# create a LoRa socket
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

# set the LoRaWAN data rate
#s.setsockopt(socket.SOL_LORA, socket.SO_DR, config.LORA_NODE_DR)

#without import config working
s.setsockopt(socket.SOL_LORA, socket.SO_DR, LORA_NODE_DR)

# make the socket blocking
s.setblocking(False)

for i in range (200):
    s.send(b'PKT #' + bytes([i]))
    time.sleep(4)
    rx, port = s.recvfrom(256)
    if rx:
        print('Received: {}, on port: {}'.format(rx, port))
    time.sleep(6)
