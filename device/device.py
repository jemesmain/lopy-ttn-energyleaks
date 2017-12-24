#get device EUI
from network import LoRa
import binascii
lora = LoRa(mode=LoRa.LORAWAN)
print(binascii.hexlify(lora.mac()).upper().decode('utf-8'))

#OTAA
from network import LoRa
import time
import binascii

lora = LoRa(mode=LoRa.LORAWAN)
#energyleaks2 app_eui
#70B3D59BA0000004

#on obtient les éléments suivants en faisant device register dans la console ttn
#energyleaks2 app_key for lopy-green
#B9A2907480D9EFE386B6EFE38B72651E
#deveui lopy1/lopy-green
#70B3D54995E573F7
app_eui = binascii.unhexlify('70B3D59BA0000004')
app_key = binascii.unhexlify('B9A2907480D9EFE386B6EFE38B72651E')

lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0)

# wait until the module has joined the network
while not lora.has_joined():
    time.sleep(2.5)
    print('Not joined yet...')

print('Network joined!')


#send a message
import socket
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)
s.setblocking(False)
s.send(bytes([1, 2, 3]))
