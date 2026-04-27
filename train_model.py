import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
import joblib

# Load data
df = pd.read_csv("data.csv")

encoders = {}

# Encode all columns
for col in df.columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    encoders[col] = le

# Split
X = df.drop("Play", axis=1)
y = df["Play"]

# Train model
model = DecisionTreeClassifier()
model.fit(X, y)

# Save model + encoders
joblib.dump(model, "model.joblib")
joblib.dump(encoders, "encoders.joblib")

print("✅ Model Trained Successfully!")