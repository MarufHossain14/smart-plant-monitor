import smbus
import time
import RPi.GPIO as GPIO

# === Setup I2C for ADC (Photodiode and Potentiometer) ===
I2C_ADDRESS = 0x48
PHOTODIODE_CHANNEL = 0x40  # A0 for photodiode
POTENTIOMETER_CHANNEL = 0x43  # A3 for potentiometer

# Initialize I2C bus
bus = smbus.SMBus(1)

# === Setup GPIO for LEDs and Servo ===
LED_PIN = 20
SERVO_PIN = 18
POTENTIOMETER_LED_PIN = 21  # Second LED connected to GPIO 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(SERVO_PIN, GPIO.OUT)
GPIO.setup(POTENTIOMETER_LED_PIN, GPIO.OUT)

# PWM setup for Servo
servo_pwm = GPIO.PWM(SERVO_PIN, 50)  # 50Hz for servo
servo_pwm.start(7)  # Neutral position

# PWM setup for the second LED (controlled by potentiometer)
potentiometer_led_pwm = GPIO.PWM(POTENTIOMETER_LED_PIN, 1000)  # 1kHz PWM for LED brightness control
potentiometer_led_pwm.start(0)  # Start with 0% brightness

# === Function to Read ADC Value ===
def read_adc(channel):
    bus.write_byte(I2C_ADDRESS, channel)
    time.sleep(0.1)  # Allow time for ADC conversion
    return bus.read_byte(I2C_ADDRESS)

# === Function for Servo Full 180 Turn ===
def servo_180_turn():
    # Rotate to 0 degrees
    servo_pwm.ChangeDutyCycle(2.5)
    time.sleep(0.5)
    # Rotate to 180 degrees
    servo_pwm.ChangeDutyCycle(12.5)
    time.sleep(0.5)
    # Return to 0 degrees
    servo_pwm.ChangeDutyCycle(2.5)
    time.sleep(0.5)
    servo_pwm.ChangeDutyCycle(0)  # Stop sending signal to avoid jitter

# === Main Logic ===
try:
    print("Starting photodiode-controlled LED, potentiometer-controlled LED, and servo...")
    while True:
        # Read photodiode value
        photodiode_value = read_adc(PHOTODIODE_CHANNEL)

        # Convert to voltage for photodiode
        photodiode_voltage = photodiode_value * 3.3 / 255
        print(f"Photodiode Voltage: {photodiode_voltage:.3f} V")

        # Read potentiometer value
        potentiometer_value = read_adc(POTENTIOMETER_CHANNEL)

        # Map potentiometer value to PWM duty cycle (0 to 100)
        potentiometer_duty_cycle = potentiometer_value * 100 / 255
        print(f"Potentiometer Value: {potentiometer_value} | Duty Cycle: {potentiometer_duty_cycle:.1f}%")

        # Control brightness of second LED based on potentiometer
        potentiometer_led_pwm.ChangeDutyCycle(potentiometer_duty_cycle)

        # If photodiode voltage < 1V, turn on LED and do a 180° servo turn
        if photodiode_voltage < 1.0:
            GPIO.output(LED_PIN, True)  # Turn on LED
            print("Light detected! LED ON.")
            servo_180_turn()
        else:
            GPIO.output(LED_PIN, False)  # Turn off LED
            print("Low light detected. LED OFF.")

        # Delay before next reading
        time.sleep(0.5)

except KeyboardInterrupt:
    print("Program terminated by user.")

finally:
    # Cleanup GPIO and PWM
    servo_pwm.stop()
    potentiometer_led_pwm.stop()
    GPIO.cleanup()
    print("Cleaned up resources.")
