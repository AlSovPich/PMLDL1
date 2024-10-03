import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib
import os

data_path = '../../data/penguins.csv'
df = pd.read_csv(data_path)

X = df[['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']]
y = df['species']

label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

model = RandomForestClassifier()
model.fit(X, y_encoded)

os.makedirs('../../models', exist_ok=True)
joblib.dump(model, '../../models/penguins_model.pkl')
joblib.dump(label_encoder, '../../models/label_encoder.pkl')
