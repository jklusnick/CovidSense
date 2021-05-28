import serial
import time

def getBlueToothValue ():
    print("Start")
    port= "/dev/tty.DSDTECHHC-05-DevB"
    try:
        bluetooth= serial.Serial(port, 9600)
        print("Connected")
        data = bluetooth.read_until()
        return data
    except:
        # return bytes("No bluetooth module detected", 'utf-8')
        return "No bluetooth module detected"