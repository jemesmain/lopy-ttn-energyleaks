import machine
from network import WLAN

#mac address
#import network
WLAN().mac()
#Result is in 6-byte format, not the usual MAC address with 6 hexadecimal bytes separated by ':'. To convert, use
import ubinascii
mac_adress = ubinascii.hexlify(WLAN().mac(),':').decode()
print(mac_adress)

# configure the WLAN subsystem in station mode (the default is AP)
wlan = WLAN(mode=WLAN.STA)
# go for fixed IP settings (IP, Subnet, Gateway, DNS)
#lopy red
wlan.ifconfig(config=('192.168.0.115', '255.255.255.0', '192.168.0.1', '192.168.0.1'))
wlan.scan()     # scan for available networks
#wifi home
wlan.connect(ssid='Livebox-DF06', auth=(WLAN.WPA2, 'A43F332809CAF366460A24F7E7'))
while not wlan.isconnected():
    pass
print(wlan.ifconfig())
