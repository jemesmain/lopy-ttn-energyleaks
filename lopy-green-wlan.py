import machine
from network import WLAN

#mac address
#import network
WLAN().mac()
#Result is in 6-byte format, not the usual MAC address with 6 hexadecimal bytes separated by ':'. To convert, use
import ubinascii
mac_adress = ubinascii.hexlify(WLAN().mac(),':').decode()
print('mac adress lopy-green')
print(mac_adress)

#wifi_home_settings
wlan = WLAN(mode=WLAN.STA)
nets = wlan.scan()

for net in nets:
    if net.ssid == 'Livebox-DF06':
        wlan.connect(net.ssid, auth=(net.sec, 'A43F332809CAF366460A24F7E7'), timeout=5000)
        while not wlan.isconnected():
            machine.idle()
            print('lopy-green is connected')
        break
