# Importing required modules
from flask import Flask,render_template,request
import numpy as np
import pickle

''' Loading our saved model '''
model = pickle.load(open('model.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def index():
    ''' Function which returns the homepage html '''
    return render_template("home.html")

@app.route('/predict',methods=['POST'])
def home():
    ''' Function for getting input values from user and 
        using those values to get prediction from our model '''
    data = [int(x) for x in request.form.values()]
    arr = [np.array(data)]
    prediction = model.predict(arr)
    return render_template('after.html',data= prediction)


if __name__ == "__main__":
    app.run(debug=True)