import smbus
import time
import RPi.GPIO as GPIO

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.OUT)  # Red LED on GPIO 20
GPIO.setup(21, GPIO.OUT)  # Blue LED on GPIO 21

address = 0x48
A2 = 0x42  # external

outvalue = 0
cmd = 0x40

bus = smbus.SMBus(1)

try:
    while True:
        bus.write_byte_data(address, cmd, outvalue)
        outvalue += 1
        if outvalue == 256:
            outvalue = 0
        print("COUNT:%3d" % outvalue)

        bus.write_byte(address, A2)
        value = bus.read_byte(address)
        
        # Calculate moisture level
        level = value * 3.3 / 255
        print(f"MOISTURE LEVEL: {level:1.3f}")
        
        # If moisture level is above 2, turn on red LED (indicating high moisture)
        if level > 2.45:
            GPIO.output(20, GPIO.HIGH)  # Turn on red LED
            GPIO.output(21, GPIO.LOW)   # Turn off blue LED
            print("Moisture level is low. Please add water to the plant.\n")

            
        # If moisture level is below 1, turn on blue LED (indicating low moisture)
        elif level < 1:
            GPIO.output(20, GPIO.LOW)   # Turn off red LED
            GPIO.output(21, GPIO.HIGH)  # Turn on blue LED
            print("Moisture level is high. No need to water the plant.\n")
            
        # If moisture level is in the middle range, turn off both LEDs
        else:
            GPIO.output(20, GPIO.LOW)   # Turn off red LED
            GPIO.output(21, GPIO.LOW)   # Turn off blue LED
            print("Moisture level is adequate. Keep monitoring.\n")
            
        time.sleep(1)

except KeyboardInterrupt:
    print("Program interrupted. Shutting down.")

finally:
    # Clean up the GPIO settings and turn off both LEDs
    GPIO.output(20, GPIO.LOW)   # Turn off red LED
    GPIO.output(21, GPIO.LOW)   # Turn off blue LED
    GPIO.cleanup()               # Reset all GPIO settings
    print("GPIO cleaned up. LEDs turned off.")
