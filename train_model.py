import os
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


DATA_PATH = "data/student_data.csv"
MODEL_DIR = "model"

features = [
    "attendance",
    "study_hours",
    "internal_marks",
    "assignment_score",
    "previous_score"
]


df = pd.read_csv(DATA_PATH)

X = df[features]
y = df["performance"]

encoder = LabelEncoder()
y = encoder.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

model = RandomForestClassifier(
    n_estimators=200,
    max_depth=8,
    random_state=42
)

print("🤖 Training model...")
model.fit(X_train, y_train)

accuracy = accuracy_score(y_test, model.predict(X_test))

os.makedirs(MODEL_DIR, exist_ok=True)

joblib.dump(model, f"{MODEL_DIR}/student_model.pkl")
joblib.dump(encoder, f"{MODEL_DIR}/label_encoder.pkl")

print("\n🎉 Model training completed!")
print(f"📊 Accuracy: {accuracy * 100:.2f}%")
print(f"📁 Model saved: {MODEL_DIR}/student_model.pkl")
print(f"📁 Encoder saved: {MODEL_DIR}/label_encoder.pkl")