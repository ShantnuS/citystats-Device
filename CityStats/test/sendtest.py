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

def sendData(data):
    s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
    s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)
    s.setblocking(False)
    #s.send(bytearray(data))
    #s.send(data)
    s.send(data.encode('utf-8'))


app_eui = binascii.unhexlify('70B3D57ED0008813')
app_key = binascii.unhexlify('FDFDA4AB9CB96B494BEDC19591B6746F')


data = "t31.58:h34.97:l516:p1012.39:i-9.25:v4.73"
connectOTAA(app_eui, app_key)
sendData(data)
