from pydantic import BaseModel


class FeatureClientSchema(BaseModel):
    age:int
    job:str
    marital:str
    education:str
    default:str
    balance:int
    housing:str
    loan:str
    contact:str
    day:int
    month:str
    duration:int
    campaign:int
    pdays:int
    previous:int
    poutcome:str

class PredictionSchema(BaseModel):
    prediction: str
    