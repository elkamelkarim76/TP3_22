import json
from typing import Optional
import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import create_model

model = joblib.load("models/model.joblib")
FEAT = json.load(open("models/features.json"))

MatchIn = create_model("MatchIn", league=(str, ...),
                       **{f: (Optional[float], None) for f in FEAT["num"]})

app = FastAPI(title="Soccer Result Predictor")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict(match: MatchIn):
    df = pd.DataFrame([match.model_dump()])
    df[FEAT["num"]] = df[FEAT["num"]].astype(float)   # None -> NaN (imputé par le pipeline)
    proba = model.predict_proba(df[FEAT["num"] + FEAT["cat"]])[0]
    return {"prediction": str(model.classes_[proba.argmax()]),
            "probabilities": {str(k): float(v) for k, v in zip(model.classes_, proba.round(4))}}
