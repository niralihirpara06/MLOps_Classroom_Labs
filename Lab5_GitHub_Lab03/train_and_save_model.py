import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from google.cloud import storage
import joblib
from datetime import datetime

# Download Breast Cancer dataset
def download_data():
  from sklearn.datasets import load_breast_cancer
  data = load_breast_cancer()
  features = pd.DataFrame(data.data, columns=data.feature_names)
  target = pd.Series(data.target)
  return features, target

# Preprocess: split into train and test sets
def preprocess_data(X, y):
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
  return X_train, X_test, y_train, y_test

# Train Logistic Regression model
def train_model(X_train, y_train):
  model = LogisticRegression(max_iter=10000, random_state=42)
  model.fit(X_train, y_train)
  return model

# Save model to GCS
def save_model_to_gcs(model, bucket_name, blob_name):
  joblib.dump(model, "model.joblib")
  
  storage_client = storage.Client()
  bucket = storage_client.bucket(bucket_name)
  blob = bucket.blob(blob_name)
  blob.upload_from_filename('model.joblib')

# Main function
def main():
  # Download data
  X, y = download_data()
  X_train, X_test, y_train, y_test = preprocess_data(X, y)
  
  # Train model
  model = train_model(X_train, y_train)
  
  # Evaluate model with multiple metrics
  y_pred = model.predict(X_test)
  accuracy = accuracy_score(y_test, y_pred)
  precision = precision_score(y_test, y_pred)
  recall = recall_score(y_test, y_pred)
  f1 = f1_score(y_test, y_pred)
  
  print(f'Model Accuracy: {accuracy:.4f}')
  print(f'Model Precision: {precision:.4f}')
  print(f'Model Recall: {recall:.4f}')
  print(f'Model F1-Score: {f1:.4f}')
  
  # Save the model to GCS
  bucket_name = "mlops-lab03-github-actions"
  timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
  blob_name = f"trained_models/logistic_model_{timestamp}.joblib"
  save_model_to_gcs(model, bucket_name, blob_name)
  print(f"Model saved to gs://{bucket_name}/{blob_name}")
  
if __name__ == "__main__":
  main()