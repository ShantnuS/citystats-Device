import time

def readTemp():
    temp = 0
    #Read temperature here
    return temp

def readLght():
    lght = 0
    #Read light here
    return lght

def readHumi():
    humi = 0
    #Read humidity here
    return humi

def readPrsr():
    prsr = 0
    #Read pressure here
    return prsr

def readAlti():
    alti = 0
    #Read altitude here
    return alti

def readTilt():
    tilt = 0
    #Read tilt here
    return tilt

def percentChange(newValue, oldValue):
    try:
        answer = (abs(newValue - oldValue))/oldValue
        answer *= 100
        return answer
    except ZeroDivisionError:
        if newValue != 0:
            return 100
        else:
            return 0

def isSigDiff(newValue, oldValue):
    percent = percentChange(newValue, oldValue)
    # 10 percent change or greater
    if percent >= 10.0:
        return True
    else:
        return False

#Measure temperature, humidity, light, pressure, altitude and tilt
temp = 0 #Called "t"
humi = 0 #Called "h"
lght = 0 #Called "l"
prsr = 0 #Called "p"
alti = 0 #Called "a"
tilt = 0 #Called "i"

### CITY STATS' COOL LOOP ###
while True:
    output = ""
    time.sleep(0.1) ### SLEEPY TIME ###
    #Temperature
    old = temp
    temp +=1
    if isSigDiff(temp, old):
        output += "t" + str(temp) + ":"
    #Humidity
    old = humi
    humi = 1
    if isSigDiff(humi, old):
        output += "h" + str(humi) + ":"
    #Light
    old = lght
    lght = 1
    if isSigDiff(lght, old):
        output += "l" + str(lght) + ":"
    #Pressure
    old = prsr
    prsr = 1
    if isSigDiff(prsr, old):
        output += "p" + str(prsr) + ":"
    #Altitude
    old = alti
    alti = 1
    if isSigDiff(alti, old):
        output += "a" + str(alti) + ":"
    #Tilt
    old = tilt
    tilt = 1
    if isSigDiff(tilt, old):
        output += "i" + str(tilt) + ":"

    #Send over output if not empty
    if output != "":
        data = output
        print(data)
    else:
        print("No differnce")