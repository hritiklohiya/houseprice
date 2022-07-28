import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle


app = Flask(__name__)
model = pickle.load(open('houseprice.pkl','rb')) 

@app.route('/')
def home():
  
    return render_template("index.html")
  
@app.route('/predict',methods=['GET'])
def predict():
    
    
    '''
    For rendering results on HTML GUI
    '''
    SqFt = float(request.args.get('SqFt'))
    
    prediction = model.predict([[SqFt]])
    
        
    return render_template('index.html', prediction_text='Regression Model  has predicted price for given SqFt area is : {}'.format(prediction))

if __name__ == "__main__":
    app.run(debug = True)
