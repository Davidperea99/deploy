import pickle
from fastapi import  APIRouter
from schemas import schemas
import numpy as np




router = APIRouter()

pkl_filenamec = "RFCultivos.pkl"
with open(pkl_filenamec,'rb') as file:
    model = pickle.load(file)

labels = {"apple","banana","blackgram","chickpea","coconut","coffee","cotton","grapes","jute","kidneybeans","lentil","maize","mango","mothbeans","mungbean","muskmelon","orange","papaya","pigeonpeas","pomegranate","rice","watermelon"}


@router.get("/")    
async def root():
    return {
        "message":"IA service"
    }

@router.post("/predict")
def predict_cultivos(data:schemas.Cultivosdata):
    data = data.model_dump()
    N = data['N']
    P = data['P']
    K = data['K']
    Temperature = data['Temperature']
    Humidity = data['Humidity']
    ph = data['ph']
    rainfall = data['rainfall']
    



    xin = np.array([N,P,K,Temperature,Humidity,ph,rainfall]).reshape(1,7)

    prediction = model.predict(xin)
    

    return {
    'prediction': prediction[0]
    }




