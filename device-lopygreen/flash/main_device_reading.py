""" OTAA Node example compatible with the LoPy Nano Gateway """

from network import LoRa
import socket
import binascii
import struct
import time
import config

#pour la lecture des valeurs
import machine
import math
numADCreadings = const(100)
current_reading = const(10)

#ADCloopMeanStdDev() fonction de lecture retournant la valeur moyenne lue
def ADCloopMeanStdDev():
    adc = machine.ADC(0)
    adcread = adc.channel(pin='P17')
    samplesADC = [0.0]*numADCreadings; meanADC = 0.0
    i = 0

    while (i < numADCreadings):
        adcint = adcread()
        samplesADC[i] = adcint
        meanADC += adcint
        i += 1
    meanADC /= numADCreadings
    varianceADC = 0.0
    for adcint in samplesADC:
        varianceADC += (adcint - meanADC)**2
    varianceADC /= (numADCreadings - 1)
    print("%u ADC readings :\n%s" %(numADCreadings, str(samplesADC)))
    print("Mean of ADC readings (0-1023) = %15.13f" % meanADC)
    print("Mean of ADC readings (0-1000 mV) = %15.13f" % (meanADC*1000/1024))
    print("Variance of ADC readings = %15.13f" % varianceADC)
    print("10**6*Variance/(Mean**2) of ADC readings = %15.13f" % ((varianceADC*10**6)//(meanADC**2)))
    print("Standard deviation of ADC readings = %15.13f" % math.sqrt(varianceADC))
    return meanADC


# mean() fonction retournant la valeur moyenne d'un tableau de chiffre
def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)

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
while not lora.has_joined():
    time.sleep(2.5)
    print('Not joined yet...')

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

#envoi de 100 valeurs moyenne
for i in range (100):
    #calcul d'une valeur moyenne
    j=1
    mean_current_reading = [] #[0.0]*current_reading
    while (j < current_reading):
        mean_current_reading.append(ADCloopMeanStdDev())
        print (mean_current_reading)
        j += 1
        time.sleep(1.0)

    moyenne=mean(mean_current_reading)
    print('valeur moyenne')
    print(moyenne)
    time.sleep(5.0)

    #envoi de la valeur moyenne
    s.send(b'PKT #' + bytes([moyenne]))
    time.sleep(4)
    rx, port = s.recvfrom(256)
    if rx:
        print('Received: {}, on port: {}'.format(rx, port))
    time.sleep(6)
