from flask import Flask, render_template, request
import pandas as pd
import joblib  # To load the saved model

# Load the trained model
model = joblib.load('average_price_model.pkl')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Getting user input from the form
    state = request.form['State']
    district = request.form['District']
    market = request.form['Market']
    commodity = request.form['Commodity']
    grade = request.form['Grade']
    temperature = int(request.form['Temperature'])
    weather = request.form['Weather']
    weather_condition = request.form['Weather_Condition']
    
    # Create a DataFrame for the input
    input_data = {
        'State': [state],
        'District': [district],
        'Market': [market],
        'Commodity': [commodity],
        'Grade': [grade],
        'temperature': [temperature],
        'weather': [weather],
        'Weather_Condition': [weather_condition]
    }
    
    input_df = pd.DataFrame(input_data)
    
    # Predict the average price
    predicted_price = model.predict(input_df)
    
    return render_template('index.html', predicted_price=predicted_price[0])

if __name__ == '__main__':
    app.run(debug=True)
