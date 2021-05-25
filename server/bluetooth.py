import serial
import time

def getBlueToothValue ():
    print("Start")
    port= "/dev/tty.DSDTECHHC-05-DevB"
    bluetooth= serial.Serial(port, 9600)
    print("Connected")
    data = bluetooth.read_until()
    return data