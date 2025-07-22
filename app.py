import pandas as pd
import numpy as np
import flask
from flask import Flask, render_template, request, jsonify
import pickle

# Creating instance of the class
app = Flask(__name__) # app initialization
loaded_model = pickle.load(open('svm.pkl', 'rb'))

# Telling flask what url should trigger the index function
@app.route('/') 
@app.route('/index')
def index():
    return flask.render_template('index.html')

# Prediction function
def predict(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1,11)
    result = loaded_model.predict(to_predict)
    return result[0]

@app.route('/result', methods = ['POST'])
def result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list=list(to_predict_list.values())
        to_predict_list = list(map(int, to_predict_list))
        result = predict(to_predict_list)
        
        if int(result)==1:
            prediction='Loan is Approved'
        else:
            prediction='Loan is Rejected'
            
        return render_template("result.html",prediction=prediction)

@app.route('/predict_api', methods = ['POST'])
def predict_api(): # For direct API calls through request
    try:
        # Get JSO request data (list of dictionaries)
        data = request.get_json(force=True)
        
        # Convert input dictionary values to numpy array
        input_features = np.array([list(data[0].values())])

        # Get prediction from the model
        prediction = loaded_model.predict(input_features)

        # Convert numeric prediction to a meaningful label
        output = "Loan is Approved" if prediction[0] == 1 else "Loan is Rejected"

        return jsonify({'prediction': output})

    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == "__main__":
    app.run(debug = True)



