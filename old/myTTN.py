
from network import LoRa
import time
import binascii

#Get EUI of the device
def getDeviceEUI():
    lora = LoRa(mode=LoRa.LORAWAN)
    result = binascii.hexlify(lora.mac()).upper().decode('utf-8')
    print(result)
    return result

def connect(myEUI,myKey):
    lora = LoRa(mode=LoRa.LORAWAN)

    #app_eui = binascii.unhexlify('70B3D57ED0008034')
    #app_key = binascii.unhexlify('47FA75005398C64CFAE2387C7A94E5E3')

    lora.join(activation=LoRa.OTAA, auth=(myEUI, myKey), timeout=0)

    # wait until the module has joined the network
    while not lora.has_joined():
        time.sleep(2.5)
        print('Connection: retrying...')

    print('Connection: connected!')


def sendData():
    import socket
    s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
    s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)
    s.setblocking(False)
    s.send(bytes([1,2,3,4,5,6,7,8,9,10]))
