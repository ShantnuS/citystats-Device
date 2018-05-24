#This used to be the m
print("Hello!")
'''
from machine import Pin
from machine import UART
from machine import ADC

from machine import enable_irq, disable_irq
import time

#adc = ADC(0)
adc = ADC()
light = adc.channel(pin='P16')
temp = adc.channel(pin='P13')

#thing = adc.channel(pin='P9')
#thing = apin()
#pin = Pin('P1', mode=Pin.IN)

while (1):
    lightout = light()
    tempout = temp()
    print(lightout, tempout)
    time.sleep(1)
'''
'''
def getval(pin) :
    ms = [1]*300
    pin(0)
    time.sleep_us(20000)
    pin(1)
    irqf = disable_irq()
    for i in range(len(ms)):
        ms[i] = pin()      ## sample input and store value
    enable_irq(irqf)
    return ms

def decode(inp):
    res= [0]*5
    bits=[]
    ix = 0
    try:
        if inp[0] == 1 : ix = inp.index(0, ix) ## skip to first 0
        ix = inp.index(1,ix) ## skip first 0's to next 1
        ix = inp.index(0,ix) ## skip first 1's to next 0
        while len(bits) < len(res)*8 : ##need 5 * 8 bits :
            ix = inp.index(1,ix) ## index of next 1
            ie = inp.index(0,ix) ## nr of 1's = ie-ix
            bits.append(ie-ix)
            ix = ie
    except:
        return([0xff,0xff,0xff,0xff])

    for i in range(len(res)):
        for v in bits[i*8:(i+1)*8]:   #process next 8 bit
            res[i] = res[i]<<1  ##shift byte one place to left
            if v > 2:
                res[i] = res[i]+1  ##and add 1 if lsb is 1

    if (res[0]+res[1]+res[2]+res[3])&0xff != res[4] :   ##parity error!
        print("Checksum Error")
        res= [0xff,0xff,0xff,0xff]

    return(res[0:4])

def DHT11(pin):
    res = decode(getval(pin))
    temp = 10*res[0] + res[1]
    hum = 10 * res[2] + res[3]
    return temp, hum

def go_DHT():
    dht_pin=Pin('P9', Pin.OPEN_DRAIN)	# connect DHT22 sensor data line to pin P9/G16 on the expansion board
    dht_pin(1)							# drive pin high to initiate data conversion on DHT sensor

    while (True):
        temp, hum = DHT11(dht_pin)
        # temp = temp * 9 // 5 + 320   # uncomment for Fahrenheit
        temp_str = '{}.{}'.format(temp//10,temp%10)
        hum_str = '{}.{}'.format(hum//10,hum%10)
        # Print or upload it
        print('temp = {}C; hum = {}%'.format(temp_str, hum_str))
        #if hum!=0xffff:
            #sendtoLoRa(dev_ID,  temp,  hum)
        time.sleep(0.2)

go_DHT()
'''
'''
dht_pin=Pin('G4', Pin.OPEN_DRAIN)

temp, hum = DHT11(dht_pin)

temp_str = '{}.{}'.format(temp//10,temp%10)
hum_str = '{}.{}'.format(hum//10,hum%10)

print(temp_str, hum_str)
'''
'''
pin = Pin('P5', mode=Pin.IN)

while (1):
    output = pin.value()
    print(output)
    time.sleep(1)
    '''

from network import LoRa
import binascii
lora = LoRa(mode=LoRa.LORAWAN)
print(binascii.hexlify(lora.mac()).upper().decode('utf-8'))


from network import LoRa
import time
import binascii
import pycom
pycom.heartbeat(False)
pycom.rgbled(0x7f0000) # red
time.sleep(1)

lora = LoRa(mode=LoRa.LORAWAN)

app_eui = binascii.unhexlify('70B3D57ED0008813')
app_key = binascii.unhexlify('FDFDA4AB9CB96B494BEDC19591B6746F')

lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0)

# wait until the module has joined the network
while not lora.has_joined():
    pycom.rgbled(0x7f7f00) # yellow
    time.sleep(1)
    pycom.heartbeat(False)
    time.sleep(1)
    print('Not joined yet...')

print('Network joined!')

import socket
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)
s.setblocking(False)
s.send(bytes([1,2,3,4,5,6,7,8,9,10]))
pycom.rgbled(0x007f00) # green
time.sleep(2)
pycom.heartbeat(False)
