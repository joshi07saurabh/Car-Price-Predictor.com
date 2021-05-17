from flask import Flask, render_template, request,url_for
import requests
import pickle
import numpy as np
import pandas as pd
import sklearn
import joblib
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
model = model=joblib.load("carPricePredictor.pkl")
@app.route('/',methods=['GET'])
def Home():
    return render_template('home.html')



#standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    
    
    
    if request.method == 'POST':
        Kms_Driven=int(request.form['Kms_Driven'])
        Fuel_Type=request.form['Fuel_Type']
        Year = int(request.form['Year'])
        Make=request.form['Make']
        
      
        prediction=model.predict(pd.DataFrame([[Kms_Driven,Fuel_Type,Year ,Make]],columns=['Distance(km)','Fuel Type','Manufacturing Year','Make']))
        output=round(prediction[0],2)
        if output<0:
            return render_template('home.html',prediction_texts="Sorry you cannot sell this car")
        else:
            return render_template('home.html',prediction_text="You can sell the Car at {} lakhs".format(output))
    else:
        return render_template('home.html')

if __name__=="__main__":
    app.run(debug=True)