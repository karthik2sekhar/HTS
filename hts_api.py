from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
import pandas as pd
from pycaret.classification import load_model, predict_model

app = FastAPI()
model = load_model('models/hts_special_rate_model')

API_KEY = "htfb-lijm-sdfer-aov"


class InputData(BaseModel):
    Indent: int
    Description: str
    Unit_of_Quantity: str
    Chapter: str
    Country_of_Origin: str
    heading_code: str
    subheading_code: str
    hts_length: int


@app.post("/predict/")
def predict(data: InputData, x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    df = pd.DataFrame([data.dict()])
    df = df.rename(columns={
        "Unit_of_Quantity": "Unit of Quantity",
        "Country_of_Origin": "Country of Origin"
    })
    prediction = predict_model(model, data=df)
    return {"prediction": int(prediction['prediction_label'][0])}