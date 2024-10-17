from flask import Flask, render_template
import csv

app = Flask(__name__)

# Route to display data on the web interface
@app.route('/')
def index():
    """
    Reads the most recent sensor data from the CSV file and sends it to the web interface.
    Returns:
        Rendered HTML page with sensor data.
    """
    with open('sensor_data.csv', 'r') as file:
        reader = csv.reader(file)
        data = list(reader)[-1]  # Get the last row (latest data)
    return render_template('index.html', data=data)

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
