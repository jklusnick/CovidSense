import serial
import time

def getBlueToothValue ():
    print("Start")
    port= "/dev/tty.DSDTECHHC-05-DevB"
    try:
        bluetooth= serial.Serial(port, 9600)
        print("Connected")
        data = bluetooth.read_until()
        bluetooth.close()
        return data
    except:
        print("Error")
        return "No bluetooth module detected"