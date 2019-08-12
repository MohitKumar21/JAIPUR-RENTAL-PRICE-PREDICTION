# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 19:05:31 2019

@author: Suman
"""

import untitled1
import pickle

from flask import Flask,render_template,request,jsonify

with open('model.pkl','rb') as f1:
    model = pickle.load(f1)
    
with open('PropertyType_encoder.pkl','rb') as f1:
    pe = pickle.load(f1)
    
with open('location_encoder.pkl','rb') as f1:
    le = pickle.load(f1)

app = Flask(__name__)

@app.route('/')
def home():
    areas = untitled1.a
    hunt = untitled1.hunt
    location = untitled1.location
    property_type = untitled1.property_type
    
    return render_template('index.html',property_type=property_type,location=location,areas=areas,tables=[hunt.to_html(classes='data',index=False,justify='center')])


@app.route('/process', methods=['POST'])
def process():

    location = request.form['locn']
    property_type = request.form['pt']
    bhk = request.form['bk']
    property_type = pe.transform([property_type])
    location = le.transform([location])
    price = int(model.predict([[location[0], property_type[0], bhk]]))
    return jsonify(msg=str(price))

if __name__ == '__main__':
	app.run(debug=True,use_reloader=False)
    