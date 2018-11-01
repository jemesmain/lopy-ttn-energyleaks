#https://docs.pycom.io/chapter/firmwareapi/pycom/machine/Pin.html
#from machine import Pin

# initialize ``P9`` in gpio mode and make it an output
#p_out = Pin('P9', mode=Pin.OUT)
#p_out.value(1)
#p_out.value(0)
#p_out.toggle()
#p_out(True)

# make ``P1`` an input with the pull-up enabled
#p_in = Pin('P1', mode=Pin.IN, pull=Pin.PULL_UP)
#p_in() # get value, 0 or 1

#pin([value])
#Pin objects are callable. The call method provides a (fast) shortcut to set and get the value of the pin.
#Example:
#from machine import Pin
#pin = Pin('P12', mode=Pin.IN, pull=Pin.PULL_UP)
#pin_reading = pin()   # fast method to get the value
#print ('reading pin lopy')
#print (pin_reading)

#class pin.exp_board
#Contains all Pin objects supported by the expansion board. Examples:
#Pin.exp_board.G12
#pin_exp = Pin(Pin.exp_board.G12, mode=Pin.IN)
#Pin.exp_board.G12.id()
#pin_exp_reading = pin_exp()
#print ('reading pin exp board')
#print(pin_exp_reading)

#https://docs.pycom.io/chapter/firmwareapi/pycom/machine/ADC.html
import machine

adc = machine.ADC()             # create an ADC object
apin_current = adc.channel(pin='P17')   # create an analog pin on P17/G31
apin_light = adc.channel(pin='P18')   # create an analog pin on P17/G31

for i in range(0,  10):
    #transformes 'val = apin()' en 'val = apin.value()
    val_current = apin_current.value()                    # read an analog value
    print('getting current  number / value')
    print(i)
    print(val_current)
    val_light = apin_light()                    # read an analog value
    print('getting light  number / value')
    print(i)
    print(val_light)
    time.sleep(5.0)
