import joblib
import pandas as pd

model = joblib.load("model.joblib")
encoders = joblib.load("encoders.joblib")

def predict_match(data_dict):
    df = pd.DataFrame([data_dict])

    # Encode input
    for col in df.columns:
        le = encoders[col]
        df[col] = le.transform(df[col])

    prediction = model.predict(df)[0]

    result = encoders["Play"].inverse_transform([prediction])[0]
    return result