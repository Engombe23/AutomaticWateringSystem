from pyfirmata import Arduino
import time

board = Arduino('com6')

print(board.get_firmata_version())

#Ultrasonic Sensor - Measures distance from water to the sensor
duration = 0
distanceFromWater = 0

#Timer
counter = 0

#LED
led = 7

#Relay Module
relay = 13

#Moisture sensor
waterCount = 0

def checkWaterLevel():
    # Add code to set the "digitalWrite (OUTPUT) to either low or high"

    if duration > 0:
        distanceFromWater = duration / 2
        distanceFromWater = distanceFromWater * 340 * 100 / 1000000
        print(str(distanceFromWater) + " cm")
        

def checkMoistureLevel():
    moisture = 0 # moisture for now = 0
    print("Moisture Sensor Value:")
    print(moisture)

    if moisture <= 300:
        waterCount += 1
        if waterCount == 5:
            waterCount == 0


while True:
    if counter == 1:
        checkWaterLevel()
        checkMoistureLevel()
    
    else:
        time.sleep(10)
        counter += 1

    if counter >= 6:
        counter = 0
    
    checkWaterLevel()



