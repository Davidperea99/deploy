from pydantic import BaseModel

class Diabetesdata(BaseModel):
                N: float
                P: float
                K: float
                Temperature: float
                Humidity: float
                ph: float
                rainfall: float
                label: str

 





   