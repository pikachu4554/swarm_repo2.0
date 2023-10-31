import os
print("1")
import sys
print("2")
import time
print("3")
import smbus
print("4")
from imusensor.MPU9250 import MPU9250
print("5")
import imu1function as imus
import servo_function as sf
address=0x68
print("6")
bus=smbus.SMBus(1)
print("7")
imu=MPU9250.MPU9250(bus,address)
print("8")
imu.begin()
print("9")
print(imus.imu_read())
rotate=input("Enter the amount to rotate")
sf.run_servo(rotate)
