from network import WLAN
import binascii
wl = WLAN()
gate_id = binascii.hexlify(wl.mac())[:6] + 'FFFE' + binascii.hexlify(wl.mac())[6:]
print(gate_id)
