import machine
from network import WLAN

#mac address
#import network
WLAN().mac()
#Result is in 6-byte format, not the usual MAC address with 6 hexadecimal bytes separated by ':'. To convert, use
import ubinascii
mac_adress = ubinascii.hexlify(WLAN().mac(),':').decode()
print('mac adress lopy-red')
print(mac_adress)

#wifi_home_settings
wlan = WLAN(mode=WLAN.STA)
nets = wlan.scan()

#wifi home/bavg _settings settings
SSID = ('Livebox-DF06','Livebox-0081')
PWD = ('A43F332809CAF366460A24F7E7','64AC31F80AF42F46672E21C886')

i=0
for i in range (2):
    for net in nets:
        #print (nets)
        print (net.ssid)
        print (SSID[i])
        if net.ssid ==SSID[i] :
            wlan.connect(net.ssid, auth=(net.sec,PWD[i] ), timeout=5000)
            while not wlan.isconnected():
                machine.idle()
                print('lopy-red is connected to')
                print(SSID[i])
            break
    i+=1
