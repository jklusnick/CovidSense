import serial
import time

def getBlueToothValue ():
    print("Start")
    port= "/dev/tty.DSDTECHHC-05-DevB"
#    try:
#        bluetooth= serial.Serial(port, 9600)
#        print("Connected")
#        data = bluetooth.read_until()
    data = 98.1,102.4
    return data
#    except:
    return "No bluetooth module detected"