import machine
import math
numADCreadings = const(100)
current_reading = const(10)


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

#ADCloopMeanStdDev()

def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)

#retour de 10 valeurs moyenne
for i in range (10):
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
