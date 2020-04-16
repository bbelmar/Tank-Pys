import time
from mpu9250_jmdev.registers import *
from mpu9250_jmdev.mpu_9250 import MPU9250

mpu = MPU9250(
    address_ak=AK8963_ADDRESS, 
    address_mpu_master=MPU9050_ADDRESS_68, # In 0x68 Address
    address_mpu_slave=None, 
    bus=1, 
    gfs=GFS_1000, 
    afs=AFS_8G, 
    mfs=AK8963_BIT_16, 
    mode=AK8963_MODE_C100HZ)

# mpu.calibrate()
#mpu.reset()
mpu.calibrate()

mpu.configure() # Apply the settings to the registers.



while True:
    
    acceleration = mpu.readAccelerometerMaster()
    accelerationX = acceleration[0]
    accelerationY = acceleration[1]
    accelerationZ = acceleration[2]
    
    rotation = mpu.readGyroscopeMaster()
    rotationX = rotation[0]
    rotationY = rotation[1]
    rotationZ = rotation[2]
    
    magnetic = mpu.readMagnetometerMaster()
    magneticX = magnetic[0]
    magneticY = magnetic[1]
    magneticZ = magnetic[2]
    
    
    print("Acceleration: ", "\n", "Accel in X ", acceleration[0],"\n", "Accel in Y ", acceleration[1], "\n", "Accel in Z ", acceleration[2])
    print("Rotation: ", "\n", "Rotation in X ", rotation[0],"\n", "Rotation in Y ", rotation[1], "\n", "Rotation in Z ", rotation[2])
    print("Magnetometer: ", "\n", "Magnetometer in X ", magnetic[0],"\n", "Magnetometer in Y ", magnetic[1], "\n", "Magnetometer in Z ", magnetic[2])




#     print("|.....MPU9250 in 0x68 Address.....|")
#     print("Accelerometer", mpu.readAccelerometerMaster())
#     print("Gyroscope", mpu.readGyroscopeMaster())
#     print("Magnetometer", mpu.readMagnetometerMaster())
#     print("Temperature", mpu.readTemperatureMaster())
#     print("\n")

    time.sleep(2)