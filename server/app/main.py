# API
# Backend -> Request
# Post (Create / Insert / Send)
# Get (Read)
# Put (Update)
# Delete (Delete)


from fastapi import FastAPI
from app.schema import CardioSchema
from app.l_model import load_logistic_model
from app.svm_models import load_svm_model
import pandas as pd

app = FastAPI()

logistic_model, logistic_scaler = load_logistic_model()
svm_model, svm_scaler = load_svm_model()

@app.get('/')
def home():
    return 'Welcome to cardiovascular disease prediction api.'

@app.post('/request-logistic-cardio')
def predictCardio(data: CardioSchema):
    input_data = pd.DataFrame([data.model_dump()])

    input_scaler = logistic_scaler.transform(input_data)
    prediction = logistic_model.predict(input_scaler)[0]

    return{
        'Prediction Stats' : int(prediction),
        'Status' : 'Likely to be Healthy' if prediction == 0 else 'Likely to have cardiovascular Disease'
    }

@app.post('/request-svm-cardio')
def predict_svm_cardio(data: CardioSchema):
    input_data = pd.DataFrame([data.model_dump()])

    input_scaler = svm_scaler.transform(input_data)
    prediction = svm_model.predict(input_scaler)[0]

    return{
        'Prediction Stats' : int(prediction),
        'Status' : 'Likely to be Healthy' if prediction == 0 else 'Likely to have cardiovascular Disease'
    }

    #run -> python -m uvicorn app.main:app --reload