from flask import Flask,render_template,request
import pandas as pd
import numpy as np
import pickle


model=pickle.load(open("Linear regression model.pk1",'rb'))
app=Flask(__name__)

car=pd.read_csv('Cleaned Car.csv')


@app.route('/')

def index():
    companies=sorted(car['company'].unique())
    car_models=sorted(car['name'].unique())
    years=sorted(car['year'].unique(),reverse=True)
    fuel_type=sorted(car['fuel_type'].unique())
    companies.insert(0,'Select Company')
    return render_template('index.html',companies=companies,car_models=car_models,years=years,fuel_types=fuel_type)

@app.route('/predict',methods=['POST'])
def predict():
    company=request.form.get('company')
    car_model=request.form.get('model')
    years=int(request.form.get('year'))
    fuel_type=request.form.get('fuel_type')
    kms_driven=int(request.form.get('kilo_driven'))

    print(company,car_model,years,fuel_type,kms_driven)

    prediction=model.predict(pd.DataFrame([[company,car_model,years,fuel_type,kms_driven]],columns=['company','name','year','fuel_type','kms_driven']))
    print(np.round(prediction[0],2))
    return str(np.round(prediction[0],2))




if ( __name__=='__main__'):
    app.run(debug=True)

    