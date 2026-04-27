import pandas as pd
import numpy as np

def main():
    # 1. Load Data
    print("1.Loading dataset...")
    # The zip contains the csv, but it's already extracted in the directory as Kaggle_IMDB_Dataset.csv
    try:
        df = pd.read_csv('Kaggle_IMDB_Dataset.csv')
    except FileNotFoundError:
        print("Error: Could not find Kaggle_IMDB_Dataset.csv. Please ensure it's unzipped and in the same directory.")
        return
    
    print("\n--- Initial Inspection ---")
    
    # 2. View first few rows and last few rows
    print("\n2. First 5 rows:")
    print(df.head())
    print("\n3. Last 5 rows:")
    print(df.tail())
    
    # 4. Check dataset dimensions
    print(f"\n4. Dataset dimensions: {df.shape[0]} rows, {df.shape[1]} columns")
    
    # 4. Review column names and data types
    print("\n4. Data Types and Non-Null Counts:")
    df.info()
    
    # 5. Summary statistics
    print("\n5. Summary Statistics (Numerical):")
    print(df.describe())
    
    print("\n6. Summary Statistics (Categorical):")
    print(df.describe(include=['object']))

if __name__ == "__main__":
    main()
