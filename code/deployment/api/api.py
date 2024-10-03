from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import joblib
import os

app = FastAPI()

class PenguinFeatures(BaseModel):
    bill_length_mm: float
    bill_depth_mm: float
    flipper_length_mm: float
    body_mass_g: float

MODEL_PATH = '/models/penguins_model.pkl'
LABEL_ENCODER_PATH = '/models/label_encoder.pkl'

model = joblib.load(MODEL_PATH)
label_encoder = joblib.load(LABEL_ENCODER_PATH)

@app.post("/predict")
def predict_species(features: PenguinFeatures):
    data = np.array([[features.bill_length_mm, features.bill_depth_mm, features.flipper_length_mm, features.body_mass_g]])

    prediction = model.predict(data)
    species = label_encoder.inverse_transform(prediction)[0]
    
    return {"predicted_species": species}