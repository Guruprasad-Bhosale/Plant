from flask import Flask, render_template, request, redirect, url_for
import os
from werkzeug.utils import secure_filename
import pandas as pd
from ml_model import predict_plant  # Replace with actual ML module

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'plantdata/uploads/'

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Load plant data
plant_df = pd.read_csv('plantdata/plants_data.csv')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/scan')
def scan():
    return render_template('scan.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'plantImage' not in request.files:
        return redirect(request.url)
    file = request.files['plantImage']
    if file.filename == '':
        return redirect(request.url)
    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Predict plant
        plant_name = predict_plant(filepath)  # Implement this function
        
        # Retrieve plant info
        plant_info = plant_df[plant_df['Name'].str.lower() == plant_name.lower()].to_dict(orient='records')
        if plant_info:
            plant_info = plant_info[0]
        else:
            plant_info = {'Name': 'Unknown', 'Info': 'No data available.', 'Medicinal Use': 'N/A', 'Dishes': 'N/A'}
        
        return render_template('C:/Users/shivani/Desktop/PlantPedia/templates/result.html', user_image=filename, plant_info=plant_info)

if __name__ == '__main__':
    app.run(debug=True)
