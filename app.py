from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load the trained machine learning model
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get the form data
        journey_date = request.form['journeyDate']
        departure_time = request.form['departureTime']
        departure_place = request.form['departurePlace']
        duration = request.form['expectedDuration']
        destination = request.form['destination']
        stops = request.form['stops']
        airline_preference = request.form['airlinePreference']
        airline_code = request.form['airlineCode']
        airline_class = request.form['airlineClass']

        # Preprocess the data and make predictions
        data = [journey_date, departure_time, departure_place, destination, stops, airline_preference, airline_code, airline_class]
        prediction = model.predict(data)

        # Render the prediction on the webpage
        return render_template('index.html', prediction=prediction)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)