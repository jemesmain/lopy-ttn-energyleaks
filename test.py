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
