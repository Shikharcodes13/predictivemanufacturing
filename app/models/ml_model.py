import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score
import joblib
import os

# File paths
DATA_PATH = "app/data/uploaded_data.csv"
MODEL_PATH = "app/models/trained_model.joblib"

def save_model(model, model_path):
    """Save the trained model using joblib."""
    try:
        joblib.dump(model, model_path)
        print(f"Model saved successfully to {model_path}")
    except Exception as e:
        print(f"Error saving model: {e}")

def load_model(model_path):
    """Load the trained model using joblib."""
    try:
        model = joblib.load(model_path)
        print(f"Model loaded successfully from {model_path}")
        return model
    except Exception as e:
        print(f"Error loading model: {e}")
        return None

def train_model():
    """Train the machine learning model and save it."""
    # Load the data
    data = pd.read_csv(DATA_PATH)
    
    # Prepare the features and target variable
    X = data[["Temperature", "Run_Time"]]
    y = data["Downtime_Flag"]
    
    # Split data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train the logistic regression model
    model = LogisticRegression()
    model.fit(X_train, y_train)
    
    # Make predictions and evaluate the model
    y_pred = model.predict(X_test)
    metrics = {
        "accuracy": accuracy_score(y_test, y_pred),
        "f1_score": f1_score(y_test, y_pred)
    }
    
    # Save the trained model
    save_model(model, MODEL_PATH)
    
    return metrics

def predict(input_data):
    """Make predictions using the trained model."""
    model = load_model(MODEL_PATH)
    if model is None:
        return {"error": "Model not found or failed to load"}
    
    # Prepare the input data for prediction
    X = pd.DataFrame([input_data])
    
    # Make prediction
    prediction = model.predict(X)[0]
    confidence = max(model.predict_proba(X)[0])
    
    return {"Downtime": "Yes" if prediction == 1 else "No", "Confidence": round(confidence, 2)}
