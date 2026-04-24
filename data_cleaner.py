import pandas as pd
import numpy as np

def clean_dataset(file_path):
    # 1. Load the data
    df = pd.read_csv(file_path)
    print(f"Original Shape: {df.shape}")

    # 2. The 'Janitor' Work: Remove duplicates and empty rows
    df.drop_duplicates(inplace=True)
    df.dropna(how='all', inplace=True)

    # 3. Standardize Date Formats (Crucial for QA)
    # Assuming there's a column named 'date'
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'], errors='coerce')

    # 4. Handle Outliers/Missing Values
    # Fill numeric gaps with the mean for basic statistical consistency
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

    print(f"Cleaned Shape: {df.shape}")
    return df

if __name__ == "__main__":
    # Example usage for uTest Data Quality project
    print("Initializing Data Wrangling Script...")
