import Adafruit_DHT
import RPi.GPIO as GPIO
import time
import csv
from luma.core.interface.serial import i2c
from luma.oled.device import ssd1306
from luma.core.render import canvas
from PIL import ImageFont

# GPIO pin assignments
DHT_PIN = 17               # Pin for the DHT11 sensor
SOIL_PIN = 18              # Pin for the soil moisture sensor
LIGHT_PIN = 27             # Pin for the light sensor

# Sensor setup
DHT_SENSOR = Adafruit_DHT.DHT11  # DHT11 sensor type

# OLED display setup
serial = i2c(port=1, address=0x3C)
device = ssd1306(serial)

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(SOIL_PIN, GPIO.IN)
GPIO.setup(LIGHT_PIN, GPIO.IN)

# Initialize CSV file with headers
with open('sensor_data.csv', mode='w') as file:
    writer = csv.writer(file)
    writer.writerow(["Timestamp", "Humidity", "Temperature", "Soil Moisture", "Light"])

# Function to read sensor data
def read_sensors():
    """
    Reads data from the DHT11, Soil Moisture, and Light sensors.
    Returns:
        humidity (float): The humidity percentage from DHT11.
        temperature (float): The temperature in Celsius from DHT11.
        soil_moisture (int): The state of the soil moisture sensor (1=Wet, 0=Dry).
        light (int): The state of the light sensor (1=Bright, 0=Dim).
    """
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    soil_moisture = GPIO.input(SOIL_PIN)
    light = GPIO.input(LIGHT_PIN)
    return humidity, temperature, soil_moisture, light

# Function to log data to CSV file
def log_data(humidity, temperature, soil_moisture, light):
    """
    Logs sensor data into the CSV file.
    """
    with open('sensor_data.csv', mode='a') as file:
        writer = csv.writer(file)
        writer.writerow([time.time(), humidity, temperature, soil_moisture, light])

# Function to display sensor data on OLED screen
def display_data(humidity, temperature, soil_moisture, light):
    """
    Displays sensor data on the OLED display.
    """
    with canvas(device) as draw:
        draw.text((0, 0), f"Temp: {temperature}C", fill="white")
        draw.text((0, 15), f"Humidity: {humidity}%", fill="white")
        draw.text((0, 30), f"Soil: {'Wet' if soil_moisture else 'Dry'}", fill="white")
        draw.text((0, 45), f"Light: {'Bright' if light else 'Dim'}", fill="white")

# Main loop to read, log, and display data
while True:
    humidity, temperature, soil_moisture, light = read_sensors()
    print(f"Humidity: {humidity}% Temp: {temperature}°C")
    print(f"Soil Moisture: {'Wet' if soil_moisture else 'Dry'}")
    print(f"Light Level: {'Bright' if light else 'Dim'}")
    
    log_data(humidity, temperature, soil_moisture, light)
    display_data(humidity, temperature, soil_moisture, light)
    
    time.sleep(2)
