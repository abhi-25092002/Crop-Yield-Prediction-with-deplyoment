import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

application  = Flask(__name__) # Initialize the flask App
model = pickle.load(open('xg.pkl', 'rb'))



@application.route('/')
def home():
    return render_template('index1.html')


@application.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    
    
    output = round(prediction[0],4)
    
    return render_template('index1.html',prediction_text='Yield predicton {}'.format(output))

if __name__=="__main__":
   application.run(debug=True)