from flask import Flask, request, render_template
import joblib
import pandas as pd
import gzip
import joblib
import pickle
import os
import flasgger
from flasgger import Swagger
import gzip

PEOPLE_FOLDER = os.path.join('static', 'image')

app = Flask(__name__, template_folder='templates')
Swagger(app)

app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER

with open('Price_Regression.pkl', 'rb') as f:
    regressor = joblib.load(f)

@app.route('/')
def home():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'flight-1.jpg')
    return render_template('home.html', user_image=full_filename)

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':

        # Date_of_Journey
        departure_date = request.form["Dep_Time"]

        Journey_Day = int(pd.to_datetime(departure_date, format="%Y-%m-%dT%H:%M").day)
        Journey_Month = int(pd.to_datetime(departure_date, format="%Y-%m-%dT%H:%M").month)

        # Departure_Time
        Departure_Hour = int(pd.to_datetime(departure_date, format="%Y-%m-%dT%H:%M").hour)
        Departure_Minute = int(pd.to_datetime(departure_date, format="%Y-%m-%dT%H:%M").minute)

        # Arrival_Time
        arrival_date = request.form["Arrival_Time"]

        Arrival_Hour = int(pd.to_datetime(arrival_date, format="%Y-%m-%dT%H:%M").hour)
        Arrival_Minute = int(pd.to_datetime(arrival_date, format="%Y-%m-%dT%H:%M").minute)

        # Duration_Time
        dur_hour = abs(Arrival_Hour - Departure_Hour)
        dur_minute = abs(Arrival_Minute - Departure_Minute)

        # Total_Stops
        total_stops= int(request.form['stops'])

        # Airline
        airline = request.form['airline']
            #Jet Airways   
            # IndiGo                               
            # Air India                            
            # Multiple carriers                    
            # SpiceJet                             
            # Vistara                              
            # Air Asia == 0                             
            # GoAir                                 
            # Multiple carriers Premium economy      
            # Vistara Premium economy                
            # Jet Airways Business               
            # Trujet
        if airline == 'Jet Airways':
            Jet_Airways = 1 
            IndiGo = 0                                                       
            Multiple_carriers =0                  
            SpiceJet =0                            
            Vistara =0                             
            Air_India =0                             
            GoAir =0                                
            Multiple_carriers_Premium_economy =0     
            Vistara_Premium_economy =0               
            Jet_Airways_Business =0              
            Trujet =0

        elif airline == 'Indigo':
            Jet_Airways = 0 
            IndiGo = 1                                                       
            Multiple_carriers =0                  
            SpiceJet =0                            
            Vistara =0                             
            Air_India =0                             
            GoAir =0                                
            Multiple_carriers_Premium_economy =0     
            Vistara_Premium_economy =0               
            Jet_Airways_Business =0              
            Trujet =0
        
        elif airline == 'Multiple carriers':
            Jet_Airways = 0 
            IndiGo = 0                                                       
            Multiple_carriers =1                  
            SpiceJet =0                            
            Vistara =0                             
            Air_India =0                             
            GoAir =0                                
            Multiple_carriers_Premium_economy =0     
            Vistara_Premium_economy =0               
            Jet_Airways_Business =0              
            Trujet =0
        
        elif airline == 'SpiceJet':
            Jet_Airways = 0 
            IndiGo = 0                                                       
            Multiple_carriers =0                 
            SpiceJet =1                            
            Vistara =0                             
            Air_India =0                             
            GoAir =0                                
            Multiple_carriers_Premium_economy =0     
            Vistara_Premium_economy =0               
            Jet_Airways_Business =0              
            Trujet =0
        
        elif airline == 'Vistara':
            Jet_Airways = 0 
            IndiGo = 0                                                       
            Multiple_carriers =0                 
            SpiceJet =0                            
            Vistara =1                             
            Air_India =0                             
            GoAir =0                                
            Multiple_carriers_Premium_economy =0     
            Vistara_Premium_economy =0               
            Jet_Airways_Business =0              
            Trujet =0
        
        elif airline == 'Air India':
            Jet_Airways = 0 
            IndiGo = 0                                                       
            Multiple_carriers =0                 
            SpiceJet =0                            
            Vistara =0                             
            Air_India =1                             
            GoAir =0                                
            Multiple_carriers_Premium_economy =0     
            Vistara_Premium_economy =0               
            Jet_Airways_Business =0              
            Trujet =0
        
        elif airline == 'GoAir':
            Jet_Airways = 0 
            IndiGo = 0                                                       
            Multiple_carriers =0                 
            SpiceJet =0                            
            Vistara =0                             
            Air_India =0                             
            GoAir =1                                
            Multiple_carriers_Premium_economy =0     
            Vistara_Premium_economy =0               
            Jet_Airways_Business =0              
            Trujet =0
        
        elif airline == 'Multiple carriers Premium economy':
            Jet_Airways = 0 
            IndiGo = 0                                                       
            Multiple_carriers =0                 
            SpiceJet =0                            
            Vistara =0                             
            Air_India =0                             
            GoAir =0                                
            Multiple_carriers_Premium_economy =1     
            Vistara_Premium_economy =0               
            Jet_Airways_Business =0              
            Trujet =0
        
        elif airline == 'Vistara Premium economy':
            Jet_Airways = 0 
            IndiGo = 0                                                       
            Multiple_carriers =0                 
            SpiceJet =0                            
            Vistara =0                             
            Air_India =0                             
            GoAir =0                                
            Multiple_carriers_Premium_economy =0     
            Vistara_Premium_economy =1               
            Jet_Airways_Business =0              
            Trujet =0
        
        elif airline == 'Jet Airways Business':
            Jet_Airways = 0 
            IndiGo = 0                                                       
            Multiple_carriers =0                 
            SpiceJet =0                            
            Vistara =0                             
            Air_India =0                             
            GoAir =0                                
            Multiple_carriers_Premium_economy =0     
            Vistara_Premium_economy =0               
            Jet_Airways_Business =1              
            Trujet =0
        
        # elif airline == 'Trujet':
        #     Jet_Airways = 0 
        #     IndiGo = 0                                                       
        #     Multiple_carriers =0                 
        #     SpiceJet =0                            
        #     Vistara =0                             
        #     Air_India =0                             
        #     GoAir =0                                
        #     Multiple_carriers_Premium_economy =0     
        #     Vistara_Premium_economy =0               
        #     Jet_Airways_Business =0              
        #     Trujet =1
        
        else:
            Jet_Airways = 0 
            IndiGo = 0                                                       
            Multiple_carriers =0                 
            SpiceJet =0                            
            Vistara =0                             
            Air_India =0                             
            GoAir =0                                
            Multiple_carriers_Premium_economy =0     
            Vistara_Premium_economy =0               
            Jet_Airways_Business =0              
            Trujet =0

        # Source
        # Banglore = 0
        Source = request.form["Source"]
        if (Source == 'Delhi'):
            s_Delhi = 1
            s_Kolkata = 0
            s_Mumbai = 0
            s_Chennai = 0

        elif (Source == 'Kolkata'):
            s_Delhi = 0
            s_Kolkata = 1
            s_Mumbai = 0
            s_Chennai = 0

        elif (Source == 'Mumbai'):
            s_Delhi = 0
            s_Kolkata = 0
            s_Mumbai = 1
            s_Chennai = 0

        elif (Source == 'Chennai'):
            s_Delhi = 0
            s_Kolkata = 0
            s_Mumbai = 0
            s_Chennai = 1

        else:
            s_Delhi = 0
            s_Kolkata = 0
            s_Mumbai = 0
            s_Chennai = 0

        # print(s_Delhi,
        #     s_Kolkata,
        #     s_Mumbai,
        #     s_Chennai)

        # Destination
        # Banglore = 0 (not in column)
        Source = request.form["Destination"]
        if (Source == 'Cochin'):
            d_Cochin = 1
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 0
        
        elif (Source == 'Delhi'):
            d_Cochin = 0
            d_Delhi = 1
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 0

        elif (Source == 'New_Delhi'):
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 1
            d_Hyderabad = 0
            d_Kolkata = 0

        elif (Source == 'Hyderabad'):
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 1
            d_Kolkata = 0

        elif (Source == 'Kolkata'):
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 1

        else:
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 0
        
        prediction=regressor.predict([[
            total_stops,
            Journey_Day,
            Journey_Month,
            Departure_Hour,
            Departure_Minute,
            Arrival_Hour,
            Arrival_Minute,
            dur_hour,
            dur_minute,
            Air_India,
            GoAir,
            IndiGo,
            Jet_Airways,
            Jet_Airways_Business,
            Multiple_carriers,
            Multiple_carriers_Premium_economy,
            SpiceJet,
            Vistara,
            Vistara_Premium_economy,
            s_Chennai,
            s_Delhi,
            s_Kolkata,
            s_Mumbai,
            d_Cochin,
            d_Delhi,
            d_Hyderabad,
            d_Kolkata,
            d_New_Delhi
        ]])

        output=round(prediction[0],2)

        return render_template('predict.html', prediction_text="Your Flight Fare Price is Rs. {}".format(output))


    return render_template('predict.html')

@app.route('/predictfile', methods=['POST'])
def predict_file():
    
    """Let's Aunthenticate the Flight Prices
    This is using docstring for specifications.
    ---
    parameters:
      - name: file
        in: formData
        type: file
        required: true
    responses:
      200:
        description: A list of Price prediction
    """
    data_test = pd.read_csv(request.files.get('file'))
    predict_the_file = regressor.predict(data_test)
    return 'The test data prediction'+str(list(predict_the_file))



if __name__ == '__main__':
    app.run(debug=True)
