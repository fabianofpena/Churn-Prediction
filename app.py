from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
from sklearn.preprocessing import StandardScaler
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open("churn.pkl", "rb"))



@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")


@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":


        # Tenure
        tenure = int(request.form["tenure"])
        # print(Total_stops)

        # Monthly Charges
        monthly_charges = float(request.form["monthly"])
        
        # Tenure
        total_charges = float(request.form["total"])
        


        # Contract
        # contract-month-to-month = 0 (not in column)
        contract = request.form['contract']
        if(contract == 'One Year'):
            contract_one_year = 1
            contract_two_year = 0
        elif (contract == 'Two Years'):
            contract_one_year = 0
            contract_two_year = 1
        else:
            contract_one_year = 0
            contract_two_year = 0

        # print(One_Year, Two_Years)

        # Dependents
        # dependents_no = 0 (not in column)
        dependents = request.form["dependents"]
        if (dependents == 'Yes'):
            dependents_yes = 1

        else:
            dependents_yes = 0

        # print(dependents_yes)

        # DeviceProtection
        # DeviceProtection_No = 0 (not in column)
        protection = request.form["protection"]
        if (protection == 'Yes'):
            device_protection_yes = 1
        else:
            device_protection_yes = 0

        # print(DeviceProtection_Yes)
        
        # Gender
        # gender_Female = 0 (not in column)
        gender = request.form["gender"]
        if (gender == 'Male'):
            gender_male = 1
        else:
            gender_male = 0

        # print(gender_Male)
        
        # Internet Service
        # InternetService_DSL = 0 (not in column)
        services = request.form["services"]
        if (services == 'Fiber Optic'):
            internet_service_fiber_optic = 1
            internet_service_no = 0
        elif (services == 'None'):
            internet_service_fiber_optic = 0
            internet_service_no = 1
        else:
            internet_service_fiber_optic = 0
            internet_service_no = 0
        # print(internet_service_fiber_optic,
        #       InternetService_No)

        # Multiple Lines
        # MultipleLines_No = 0 (not in column)
        multiplelines = request.form["multiplelines"]
        if (multiplelines == 'No Phone Service'):
            multiplelines_no_phone_service = 1
            multiplelines_yes = 0
        elif (multiplelines == 'Yes'):
            multiplelines_no_phone_service = 0
            multiplelines_yes = 1
        else:
            multiplelines_no_phone_service = 0
            multiplelines_yes = 0
        # print(multipleLines_no_phone_service,
        #       MultipleLines_Yes)
        
        
        # Backup
        # OnlineBackup_No = 0 (not in column)
        backup = request.form["backup"]
        if (backup == 'Yes'):
            online_backup_yes = 1
        else:
            online_backup_yes = 0

        # print(online_backup_yes)

        
        # Security
        # OnlineSecurity_No = 0 (not in column)
        security = request.form["security"]
        if (security == 'Yes'):
            online_security_yes = 1
        else:
            online_security_yes = 0
        # print(online_security_yes)
        
        # Paperless Billing
        # PaperlessBilling_No = 0 (not in column)
        paperless = request.form["paperless"]
        if (paperless == 'Yes'):
            paperless_billing_yes = 1
        else:
            paperless_billing_yes = 0
        # print(paperless_billing_yes)
        
        
        # Partner
        # Partner_No = 0 (not in column)
        partner = request.form["partner"]
        if (partner == 'Yes'):
            partner_yes = 1
        else:
            partner_yes = 0
        # print(partner_yes)
        
        
        # Payment Method
        # PaymentMethod_Bank_Transfer = 0 (not in column)
        payment = request.form["payment"]
        if (payment == 'Credit Card'):
            payment_method_credit_card = 1
            payment_method_electronic_check = 0
            payment_method_mailed_check = 0
        elif (payment == 'Eletronic Check'):
            payment_method_credit_card = 0
            payment_method_electronic_check = 1
            payment_method_mailed_check = 0
        elif (payment == 'Mailed Check'):
            payment_method_credit_card = 0
            payment_method_electronic_check = 0
            payment_method_mailed_check = 1

        else:
            payment_method_credit_card = 0
            payment_method_electronic_check = 0
            payment_method_mailed_check = 0
            
        # print(payment_method_credit_card,
        #       payment_method_electronic_check,
        #       payment_method_mailed_check)
        
        
        # Phone Service
        # PhoneService_No = 0 (not in column)
        phone = request.form["phone"]
        if (phone == 'Yes'):
            phone_service_yes = 1
        else:
            phone_service_yes = 0
            
        # print(phone_service_yes)


        # Senior Citizen
        # SeniorCitizen_0 = 0 (not in column)
        senior = request.form["senior"]
        if (senior == 'Yes'):
            senior_citizen_1 = 1
        else:
            senior_citizen_1 = 0

        # print(senior_citizen_1)

        # Streaming Movies
        # StreamingMovies_No = 0 (not in column)
        movies = request.form["movies"]
        if (movies == 'Yes'):
            streaming_movies_yes = 1
        else:
            streaming_movies_yes = 0

        # print(streaming_movies_yes)

        # Streaming TV
        # StreamingTV_No = 0 (not in column)
        tv = request.form["tv"]
        if (tv == 'Yes'):
            streaming_tv_yes = 1
        else:
            streaming_tv_yes = 0

        # print(streaming_tv_yes)
        
        # Technical Support
        support = request.form["support"]
        if (support == 'Yes'):
            tech_support_yes = 1
        else:
            tech_support_yes = 0

        # print(tech_support_yes)


        
    #     ['Total_Stops', 'Journey_day', 'Journey_month', 'Dep_hour',
    #    'Dep_min', 'Arrival_hour', 'Arrival_min', 'Duration_hours',
    #    'Duration_mins', 'Airline_Air India', 'Airline_GoAir', 'Airline_IndiGo',
    #    'Airline_Jet Airways', 'Airline_Jet Airways Business',
    #    'Airline_Multiple carriers',
    #    'Airline_Multiple carriers Premium economy', 'Airline_SpiceJet',
    #    'Airline_Trujet', 'Airline_Vistara', 'Airline_Vistara Premium economy',
    #    'Source_Chennai', 'Source_Delhi', 'Source_Kolkata', 'Source_Mumbai',
    #    'Destination_Cochin', 'Destination_Delhi', 'Destination_Hyderabad',
    #    'Destination_Kolkata', 'Destination_New Delhi']
        
    
        data = [[
            tenure,
            monthly_charges,
            total_charges,
            contract_one_year,
            contract_two_year,
            dependents_yes,
            device_protection_yes,
            gender_male,
            internet_service_fiber_optic,
            internet_service_no,
            multiplelines_no_phone_service,
            multiplelines_yes,
            online_backup_yes,
            online_security_yes,
            paperless_billing_yes,
            partner_yes,
            payment_method_credit_card,
            payment_method_electronic_check,
            payment_method_mailed_check,
            phone_service_yes,
            senior_citizen_1,
            streaming_movies_yes,
            streaming_tv_yes,
            tech_support_yes
        ]]
        
        # define a Standard scaler
        scaler = StandardScaler()
        
        # transform data
        scaled = scaler.fit_transform(data)

        
        prediction=model.predict(scaled)

        proba=model.predict_proba(scaled)
       
        def result(threshold):
            if (threshold == 1):
                return "This customer will churn"
            else:
                return "This customer will not churn"
        


        return render_template('home.html',prediction_text = result(prediction))


    return render_template("home.html")




if __name__ == "__main__":
    app.run(debug=True)
