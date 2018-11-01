import pycom # we need this module to control the LED
pycom.heartbeat(False) # disable the blue blinking
pycom.rgbled(0x00ffff) # make the LED light up green in colour

#varialble assignment
variable = "Hello World"
print(variable)

#conditional
temperature = 15
target = 10
if temperature > target:
    print("Too High!")
elif temperature < target:
    print("Too Low!")
else:
    print("Just right!")

#for loop
x = 0
for y in range(0,9):
    x += 1
print(x)

#while loop
x = 0
while x < 9:
    x += 1
print(x)

#function
def add(number1, number2):
    return number1 + number2

print(add(1,2)) # expect a result of 3

def welcome(name):
    welcome_phrase = "Hello, " + name + "!"
    print(welcome_phrase)

welcome("Alex") # expect "Hello, Alex!"

#lists
networks = ['lora', 'sigfox', 'wifi', 'bluetooth', 'lte-m']
print(networks[2]) # expect 'wifi'

#dictionnary
address_book = {'Alex':'2604 Crosswind Drive','Joe':'1301 Hillview Drive','Chris':'3236 Goldleaf Lane'}
print(address_book['Alex']) # expect '2604 Crosswind Drive'

#tuple
pycom_devices = ('wipy', 'lopy', 'sipy', 'gpy', 'fipy')
print(pycom_devices[0]) # expect 'wipy'

#calcul d'une moyenne
def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)
print('moyenne')
print(mean([1,2,3,4]))

#les listes
liste = []
print (liste)
liste.append(1)
liste.append(2)
print(mean(liste))

#mean_current_reading=[]
#mean_current_reading.append(j)
#print (mean_current_reading)
#print (mean(mean_current_reading))
#j += 1
#time.sleep(1.0)

#byte problems
#moyenne=3196.736
#moyenne_arr=int(round(moyenne,0))
#print('moyenne arrondi')
#print(moyenne_arr)
#print('bytes([moyenne_arr])')
#print(bytes([moyenne_arr]))

#bytes sending
#s.send(b'PKT #' + bytes([i]))
for i in range (256):
    print('bytes message sent')
    print(b'PKT #' + bytes([i]))

#for i in range (4095):
    #print('int message sent')
    #print('i')
    #print(i)
    #print('text'+ i)
    #print(b'PKT #' + i)

import struct

# Nombre "flottant" à tester

value = 4095

# Nombre mis dans un tableau de flottants et on l'affiche avec formattage

myArrayOfFloat = bytes(struct.pack("f", value))
print('myArrayOfFloat')
print(myArrayOfFloat)
print([ "0x%02x" % item for item in myArrayOfFloat ])

# Nombre mis dans un tableau de double (a priori solution préférée)

myArrayOfDouble = bytes(struct.pack("d", value))
print('myArrayOfDouble')
print(myArrayOfDouble)
print([ "0x%02x" % item for item in myArrayOfDouble ])

print('array of float message sent')
print(b'PKT #' + myArrayOfFloat)

#réponse utilisateur
#Command line inputs are in sys.argv. Try this in your script:
#import sys
#print (sys.argv)
#text = raw_input("prompt")  # Python 2
text = input("choose wifi settings: home / bavg ")  # Python 3
print (text)

import sys
chr = sys.stdin.read(1)
print (chr)
