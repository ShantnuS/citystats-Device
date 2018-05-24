from network import LoRa
import time
import binascii
import pycom
import struct
import socket

def connectOTAA(myEUI,myKey):
    lora = LoRa(mode=LoRa.LORAWAN)

    lora.join(activation=LoRa.OTAA, auth=(myEUI, myKey), timeout=0)

    # wait until the module has joined the network
    while not lora.has_joined():
        '''
        pycom.rgbled(0x7f7f00) # yellow
        time.sleep(1)
        pycom.heartbeat(False)
        '''
        time.sleep(1)
        print('Connection: retrying...')

    print('Connection: connected!')

def connectABP(devAddress,netSessKey,appSessKey):
    lora = LoRa(mode=LoRa.LORAWAN)

    dev_addr = struct.unpack(">l", devAddress)[0]

    lora.join(activation=LoRa.ABP, auth=(dev_addr, netSessKey, appSessKey))
    # The loop below is not even needed as connection is instant
    # However since it has no impact I have left it.
    while not lora.has_joined():
        time.sleep(2)
        print('Not joined yet...')
    print('Connection: connected!')

def sendData(data):
    s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
    s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)
    s.setblocking(False)
    #s.send(bytearray(data))
    #s.send(data)
    s.send(data.encode('utf-8'))
    #Set LED to green at the end

app_eui = binascii.unhexlify('70B3D57ED0008813')
app_key = binascii.unhexlify('FDFDA4AB9CB96B494BEDC19591B6746F')

#This is needed for ABP (but is prone to changing)
dAdd = binascii.unhexlify('2601223B')
netSKey = binascii.unhexlify('167FC4ABA47B91E6A837765E884320FF')
appSKey = binascii.unhexlify('1A17A04EAEF92C0A3D149FB000300302')

data="test"
start = (time.time())
connectOTAA(app_eui, app_key)
#connectABP(dAdd,netSKey,appSKey)
sendData(data)
end = (time.time())
result = end - start
print(result)
