from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)
conn = sqlite3.connect('data.db')
cursor = conn.cursor()
cursor.execute('SELECT * FROM cars')
data = cursor.fetchall()
conn.close()

@app.route('/')
def home():
    return render_template('hello.html')

@app.route('/list')
def dogs():
    return render_template('list.html', data = data)

@app.route('/details')
def details():
    # Get car_id from query string
    car_id = request.args.get('id', type=int)

    # Find the car by car_id in the data list
    car = next((item for item in data if item[0] == car_id), None)

    # If no car is found, return a 404 error
    if car is None:
        return "Car not found", 404

    # Render the car details page
    return render_template('details.html', car=car)

if __name__ == '__main__':
    app.run(debug=True)
