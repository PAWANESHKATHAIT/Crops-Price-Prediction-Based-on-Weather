from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load your trained models and scaler
model_min = joblib.load('model_min.pkl')
model_max = joblib.load('model_max.pkl')
scaler = joblib.load('scaler.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get input features
        feature1 = float(request.form['feature1'])  # Adjust according to your input fields
        feature2 = float(request.form['feature2'])  # Adjust according to your input fields
        # Add other features as needed based on your model input

        # Prepare the feature array
        features = np.array([[feature1, feature2]])
        # Scale the input features
        features_scaled = scaler.transform(features)

        # Make predictions using both models
        prediction_min = model_min.predict(features_scaled)
        prediction_max = model_max.predict(features_scaled)

        return render_template('index.html', prediction_min=prediction_min[0], prediction_max=prediction_max[0])

if __name__ == '__main__':
    app.run(debug=True)
