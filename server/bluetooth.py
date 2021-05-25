import serial
import time

print("Start")
port= "/dev/tty.DSDTECHHC-05-DevB"
bluetooth= serial.Serial(port, 9600)
print("connected")
while(True):
    data = bluetooth.read(5)
    print(data)