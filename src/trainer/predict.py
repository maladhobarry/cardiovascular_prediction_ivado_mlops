import pandas as pd
import joblib

def predict(model_path, data_path):
    # Load data
    data = pd.read_csv(data_path)
    data = data.drop(['cardio', 'id'], axis=1)

    # Load model
    model = joblib.load(model_path)

    # Predict
    predictions = model.predict(data)
    print(predictions)

if __name__ == '__main__':
    predict('../models/random_forest.pkl', '../../data/processed/prediction_data.csv')
    predict('../models/svm.pkl', '../../data/processed/prediction_data.csv')
