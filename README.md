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

### Installation Instructions

#### **1. On Windows (for development and testing):**

If you're developing or testing the project on a Windows machine, some libraries specific to Raspberry Pi's hardware (like `Adafruit_DHT` and `RPi.GPIO`) should not be installed. Instead, you can mock the sensor data for testing purposes.

1. **Install Flask and other required libraries:**
   These libraries are platform-independent and can be installed using the following command:
   ```bash
   pip install Flask luma.oled
   ```

2. **Skip the Raspberry Pi-specific libraries:**
   - Do not install `Adafruit_DHT` or `RPi.GPIO` on Windows, as these libraries are specific to Raspberry Pi's hardware.
   - In your development code, make sure to mock sensor data as needed.

#### **2. On Raspberry Pi (for deployment and real sensor testing):**

When you’re running the project on a Raspberry Pi, you need to install the libraries that interact with the actual hardware.

1. **Update your package list and install dependencies:**
   ```bash
   sudo apt-get update
   sudo apt-get install python3-dev python3-pip
   ```

2. **Install the required Python libraries:**
   Run the following commands to install all necessary libraries, including the ones for Raspberry Pi sensors:
   ```bash
   pip install Flask luma.oled
   sudo pip3 install Adafruit_DHT RPi.GPIO
   ```

3. **Run the project with real sensors:**
   Once installed, you can connect your sensors to the Raspberry Pi and run the project with actual sensor data.

### Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/smart-plant-monitor.git
   cd smart-plant-monitor
   ```

2. **Connect the sensors** to the appropriate GPIO pins on the Raspberry Pi as described in the file `monitor.py`.

3. **Run the Monitoring Script**:
   Start collecting data and displaying it on the OLED:
   ```bash
   python3 monitor.py
   ```

4. **Run the Flask Web App**:
   To display the data on a web interface, run:
   ```bash
   python3 app.py
   ```
   Navigate to `http://<your-raspberry-pi-ip>:5000` in your web browser to view the data.

## Project Structure

```
smart-plant-monitor/
│
├── monitor.py               # Main Python script for sensor data collection and display
├── app.py                   # Flask web server for displaying data on a web interface
├── sensor_data.csv           # Auto-generated CSV file for logging sensor data
├── templates/
│   └── index.html           # HTML template for Flask to display data on the web
├── README.md                # Detailed description and setup instructions
└── requirements.txt         # List of required Python libraries
```

## Future Improvements
- **Automated Watering**: Integrate a water pump to water the plants based on moisture readings.
- **Camera Monitoring**: Add a camera module for visual plant monitoring.
- **Machine Learning**: Analyze long-term plant health data and provide customized care suggestions.

## License
This project is licensed under the MIT License. See `LICENSE` for more information.

---