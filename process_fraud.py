import pandas as pd
import joblib
import os
import numpy as np

INPUT_FILE = 'uploads/test_data.csv'
OUTPUT_FILE = 'uploads/final.csv'
MODEL_PATH = r'C:\Users\KIIT\Desktop\uwin_firstSem\Topics in applied AI\random_forest_model.joblib'

rf_model = joblib.load(MODEL_PATH)

def process_file(input_file_path, output_file_path):
    if not os.path.isfile(input_file_path):
        raise FileNotFoundError(f'{input_file_path} file not found')

    df = pd.read_csv(input_file_path)

    required_columns = ['type', 'amount', 'oldbalanceOrg', 'newbalanceOrig', 'type_freq', 'balance_diff']
    if not all(col in df.columns for col in required_columns):
        raise ValueError("CSV does not contain required columns")

    # Extract features for prediction
    features = df[required_columns]

    # Convert features DataFrame to NumPy array
    features_array = features.values

    # Predict fraud cases
    df['isFraud'] = rf_model.predict(features_array)

    fraud_df = df[df['isFraud'] == 1]

    # Save the filtered DataFrame
    fraud_df.to_csv(output_file_path, index=False)
    print(f'Filtered file saved as {output_file_path}')

if __name__ == '__main__':
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    process_file(INPUT_FILE, OUTPUT_FILE)
