from flask import Flask,render_template,request,redirect
from flask_cors import CORS,cross_origin
import pickle
import pandas as pd
import numpy as np

app=Flask(__name__)
model=pickle.load(open('LinearRegressionModel.pkl','rb'))
data=pd.read_csv('Cleaned_Potato_data.csv')

@app.route('/')
def index():
    state_name = sorted(data['state_name'].unique())
    district_name = sorted(data['district_name'].unique())
    market_center_name = sorted(data['market_center_name'].unique())
    Variety = sorted(data['Variety'].unique())
    group_name = sorted(data['group_name'].unique())
    month_name = (data['month_name'].unique())

    return  render_template('index.html',state_name=state_name, district_name=district_name, market_center_name=market_center_name,Variety=Variety,group_name=group_name,month_name=month_name)

@app.route('/predict',methods=['POST'])
@cross_origin()
def predict():

    state_name=request.form.get('state_name')
    district_name=request.form.get('district_name')
    market_center_name=request.form.get('market_center_name')
    Variety=request.form.get('Variety')
    group_name=request.form.get('group_name')
    Arrival = request.form.get('Arrival')
    MIN = request.form.get('MIN')
    MAX = request.form.get('MAX')
    month_name = request.form.get('month_name')

    print("->",state_name," ",district_name,market_center_name,Variety,group_name,Arrival,MIN,MAX,month_name)
    prediction = model.predict(pd.DataFrame(columns=['state_name', 'district_name', 'market_center_name', 'Variety', 'group_name', 'Arrival', 'MIN', 'MAX','month_name'],data=np.array([state_name,district_name,market_center_name,Variety,group_name,Arrival,MIN,MAX,month_name]).reshape(1, 9)))
    print(prediction)

    return str(np.round(prediction[0], 2))

# app=Flask(__name__)
# cors=CORS(app)
# model=pickle.load(open('LinearRegressionModel.pkl','rb'))
#car=pd.read_csv('Cleaned_Potato_data.csv')
#
# @app.route('/',methods=['GET','POST'])
# def index():
#     state_name=sorted(data['state_name'].unique())
#     district_name = sorted(data['district_name'].unique())
#     market_center_name = sorted(data['market_center_name'].unique())
#     Variety = sorted(data['Variety'].unique())
#     group_name = sorted(data['group_name'].unique())
#     month_name = sorted(data['month_name'].unique())
#
#
#     # car_models=sorted(car['name'].unique())
#     # year=sorted(car['year'].unique(),reverse=True)
#     # fuel_type=car['fuel_type'].unique()
#
#     state_name.insert(0,'Select state')
#     return render_template('index.html',state_name=state_name, district_name=district_name, market_center_name=market_center_name,Variety=Variety,group_name=group_name,month_name=month_name)
#
#
# @app.route('/predict',methods=['POST'])
# @cross_origin()
# def predict():
#
#     company=request.form.get('company')
#     district_name = request.form.get('district_name')
#     market_center_name = request.form.get('market_center_name')
#     Variety = request.form.get('Variety')
#     group_name = request.form.get('group_name')
#     month_name = request.form.get('month_name')
#     Arrival  = request.form.get('Arrival')
#     MIN = request.form.get('MIN')
#     MAX = request.form.get('MAX')
#
#     # car_model=request.form.get('car_models')
#     # year=request.form.get('year')
#     # fuel_type=request.form.get('fuel_type')
#     #
#     # driven=request.form.get('kilo_driven')
#
#     prediction=model.predict(pd.DataFrame(columns=['state_name','district_name','market_center_name','Variety','group_name','Arrival','MIN','MAX','month_name'],
#                               data=np.array([state_name,district_name,market_center_name,Variety,group_name,Arrival,MIN,MAX,month_name]).reshape(1, 9)))
#     print(prediction)
#
#     return str(np.round(prediction[0],2))



if __name__=='__main__':
    app.run()