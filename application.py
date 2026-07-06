import pickle
from flask import Flask, request, jsonify, render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

application = Flask(__name__)
app = application

## Import ridge regressor and standard scaler pickle
ridge_model = pickle.load(open('models/ridge.pkl', 'rb'))
standard_scaler = pickle.load(open('models/scaler.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html') # Or rendering your index.html

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == "POST":
        temp = float(request.form.get('Temperature'))
        rh = float(request.form.get('RH'))
        ws = float(request.form.get('Ws'))
        rain = float(request.form.get('Rain'))
        ffmc = float(request.form.get('FFMC'))
        dmc = float(request.form.get('DMC'))
        isi = float(request.form.get('ISI'))
        classes = float(request.form.get('Classes'))
        region = float(request.form.get('Region'))

        new_data_scaled = standard_scaler.transform([[temp, rh, ws, rain, ffmc, dmc, isi, classes, region]])
        result = ridge_model.predict(new_data_scaled)
        prediction = float(result[0])
        percentage = prediction * 100 if 0 <= prediction <= 1 else prediction
        formatted_result = f"{percentage:.2f}%"

        return render_template('home.html', results=formatted_result)

    else:
        return render_template('home.html')

if __name__ == "__main__":
    import os

    # Render dynamically assigns a port via environment variables
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
