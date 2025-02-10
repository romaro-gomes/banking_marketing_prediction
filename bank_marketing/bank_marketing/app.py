from fastapi import FastAPI,status,Form
from fastapi.middleware.cors import CORSMiddleware

from .schemas.schemas import FeatureClientSchema,PredictionSchema
import joblib
import pandas as pd

app =FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",  
    "http://127.0.0.1:8000",  
    "http://127.0.0.1:5500",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def openFiles(path):
    file=joblib.load(open(path,'rb'))
    return file

model=openFiles('../artifacts/final_model.joblib')
preprocessor=openFiles('../artifacts/final_preprocessor_features.joblib')




@app.post('/client/', status_code=status.HTTP_201_CREATED, response_model=PredictionSchema)
async def inputClientFeatures(featuresClient: FeatureClientSchema):
    data=pd.DataFrame(featuresClient.__dict__,index=[0])
    processed=preprocessor.transform(data)
    prediction=model.predict(processed)
    response = 'The likelihood of the client adhering to the campaign is low.' if prediction == 0 else 'The likelihood of the client adhering to the campaign is high.'
    return {"prediction": response}

@app.post('/clientForm/', status_code=status.HTTP_201_CREATED, response_model=PredictionSchema)
async def inputClientFeatures( age:int  =Form(...),
    job:str  =Form(...),
    marital:str =Form(...),
    education:str =Form(...),
    default:str =Form(...),
    balance:int =Form(...),
    housing:str =Form(...),
    loan:str =Form(...),
    contact:str =Form(...),
    day:int =Form(...),
    month:str =Form(...),
    duration:int =Form(...),
    campaign:int =Form(...),
    pdays:int =Form(...),
    previous:int =Form(...),
    poutcome:str=Form(...)) :
    featuresClient= FeatureClientSchema(
        age=age,
        job=job,
        marital=marital,
        education=education,
        default=default,
        balance=balance,
        housing=housing,
        loan=loan,
        contact=contact,
        day=day,
        month=month,
        duration=duration,
        campaign=campaign,
        pdays=pdays,
        previous=previous,
        poutcome=poutcome
    )
    data=pd.DataFrame(featuresClient.__dict__,index=[0])
   
    processed=preprocessor.transform(data)
    prediction=model.predict(processed)
    response= 'The possibility of the client adhrence the campaign is low.' if prediction==0 else 'The possibility of the client adhrence the campaign is high.'
    return {"prediction": response}