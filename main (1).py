#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# main.py
"""
Main script to run the Online Fraud Detection project.
This script loads data, preprocesses it, trains the model, and evaluates it.
"""

import pandas as pd
from src.preprocessing import preprocess_data
from src.models import train_model, evaluate_model

def main():
    # 1. Load dataset
    data_path = 'data/raw/transactions.csv'  # <-- Replace with your dataset path
    data = pd.read_csv(data_path)
    print("Data loaded successfully!")

    # 2. Preprocess data
    X_train, X_test, y_train, y_test = preprocess_data(data)
    print("Data preprocessing done!")

    # 3. Train model
    model = train_model(X_train, y_train)
    print("Model training completed!")

    # 4. Evaluate model
    evaluate_model(model, X_test, y_test)
    print("Model evaluation completed!")

if __name__ == "__main__":
    main()

