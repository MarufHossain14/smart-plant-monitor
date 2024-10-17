# Smart Plant Monitoring System

## Description
This project is a **Raspberry Pi-based Smart Plant Monitoring System** designed to help users monitor their plants in real-time. It tracks and logs soil moisture, temperature, humidity, and light levels. The data is displayed on an OLED screen and through a web interface that you can access remotely. Additionally, the system can send alerts when specific thresholds are met to ensure your plants are well cared for.

## Features
- **Soil Moisture Sensor**: Monitors the moisture level in the soil.
- **Temperature & Humidity Sensor (DHT11)**: Tracks environmental conditions.
- **Light Sensor**: Detects the light intensity around the plant.
- **OLED Display**: Displays real-time data directly on the device.
- **Web Dashboard**: View data in real time via a Flask-powered web interface.
- **Data Logging**: Logs all sensor data into a CSV file for analysis.
- **Alerts**: Sends notifications when conditions fall below set thresholds (optional).

## Components Used
- Raspberry Pi
- Soil Moisture Sensor
- DHT11 Sensor (Temperature & Humidity)
- Light Sensor (Photoresistor)
- OLED Display (I2C)
- Optional: Wi-Fi module for Raspberry Pi (if not built-in)

## Getting Started

### Prerequisites
Make sure your Raspberry Pi is set up and connected to the internet. You'll need to install the following Python libraries:
- RPi.GPIO
- Adafruit_DHT
- luma.oled
- Flask

Install them with pip:
```bash
sudo pip3 install RPi.GPIO Adafruit_DHT luma.oled Flask
