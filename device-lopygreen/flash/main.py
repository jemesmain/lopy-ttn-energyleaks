""" OTAA Node example compatible with the LoPy Nano Gateway """

from network import LoRa
import socket
import binascii
import struct
import time
import config

# initialize LoRa in LORAWAN mode.
lora = LoRa(mode=LoRa.LORAWAN)


# create an OTA authentication params
#setting found in ttn device / name of device with activation method OTAA
#ttn dev_eui 70B3D54995E573F7
#const char *appEui = "70B3D59BA0000004";
#const char *appKey = "65240933ADE876AB9AD5990DB004C2E9";
print('ttn config')
dev_eui = binascii.unhexlify('70B3D54995E573F7'.replace(' ','')) # these settings can be found from TTN
app_eui = binascii.unhexlify('70B3D59BA0000004'.replace(' ','')) # these settings can be found from TTN
app_key = binascii.unhexlify('65240933ADE876AB9AD5990DB004C2E9'.replace(' ','')) # these settings can be found from TTN



# set the 3 default channels to the same frequency (must be before sending the OTAA join request)
lora.add_channel(0, frequency=config.LORA_FREQUENCY, dr_min=0, dr_max=5)
lora.add_channel(1, frequency=config.LORA_FREQUENCY, dr_min=0, dr_max=5)
lora.add_channel(2, frequency=config.LORA_FREQUENCY, dr_min=0, dr_max=5)

# join a network using OTAA
lora.join(activation=LoRa.OTAA, auth=(dev_eui, app_eui, app_key), timeout=0, dr=config.LORA_NODE_DR)

# wait until the module has joined the network
i=1
while not lora.has_joined():
    time.sleep(2.5)
    print('Not joined yet...')
    print(i)
    i+=1

print('device connected')
# remove all the non-default channels
for i in range(3, 16):
    lora.remove_channel(i)

# create a LoRa socket
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

# set the LoRaWAN data rate
s.setsockopt(socket.SOL_LORA, socket.SO_DR, config.LORA_NODE_DR)

# make the socket blocking
s.setblocking(False)

time.sleep(5.0)

for i in range (200):
    value = 2048
    # Nombre mis dans un tableau de flottants et on l'affiche avec formattage
    myArrayOfFloat = bytes(struct.pack("f", value))
    print('myArrayOfFloat')
    print(myArrayOfFloat)
    print([ "0x%02x" % item for item in myArrayOfFloat ])
    s.send(b'0001' + myArrayOfFloat)
    #s.send(b'PKT #' + myArrayOfFloat)
    #s.send(b'PKT #' + bytes([i]))
    time.sleep(4)
    rx, port = s.recvfrom(256)
    if rx:
        print('Received: {}, on port: {}'.format(rx, port))
    time.sleep(6)
