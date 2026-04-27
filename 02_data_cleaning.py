import pandas as pd
import numpy as np

def clean_data():
    print("Loading data for cleaning...")
    try:
        df = pd.read_csv('Kaggle_IMDB_Dataset.csv')
    except FileNotFoundError:
        print("Error: Could not find Kaggle_IMDB_Dataset.csv.")
        return

    print("\n--- Phase 3: Data Cleaning ---")
    
    # 1. Handle Missing Values
    print("1. Handling missing values...")
    # Fill missing certificates with 'Unrated'
    df['Certificate'] = df['Certificate'].fillna('Unrated')
    
    # 2. Data Type Conversion
    print("2. Converting data types...")
    # Convert 'Gross' from string (e.g., '28,341,469') to numeric float
    if df['Gross'].dtype == 'object' or df['Gross'].dtype.name == 'str':
        df['Gross'] = df['Gross'].str.replace(',', '', regex=False).astype(float)
    
    # Fill Gross NaNs with the median value
    df['Gross'] = df['Gross'].fillna(df['Gross'].median())
    
    # Fill Meta_score NaNs with the median value
    df['Meta_score'] = df['Meta_score'].fillna(df['Meta_score'].median())

    # Clean 'Runtime' (e.g., '142 min' -> 142)
    if df['Runtime'].dtype == 'object' or df['Runtime'].dtype.name == 'str':
        df['Runtime'] = df['Runtime'].str.replace(' min', '', regex=False).astype(int)

    # 3. Handle Duplicates
    print("3. Checking for duplicates...")
    duplicates = df.duplicated().sum()
    print(f"   Found {duplicates} duplicate rows. Dropping if any...")
    df = df.drop_duplicates()

    # 4. String Formatting
    print("4. Formatting strings...")
    # Strip whitespace from typical string columns
    df['Series_Title'] = df['Series_Title'].str.strip()
    df['Director'] = df['Director'].str.strip()
    
    # 5. Feature Engineering (Initial): Split Genre
    print("5. Engineering 'Genre' features...")
    # Genres are usually formatted like "Action, Adventure, Sci-Fi"
    # We create one-hot encoded genre columns for modeling
    genres_dummies = df['Genre'].str.get_dummies(sep=', ')
    # Append the new one-hot encoded genre columns to our dataframe
    df = pd.concat([df, genres_dummies], axis=1)

    print("\nCleaning complete! Data preview (selected columns):")
    print(df[['Series_Title', 'Runtime', 'Gross']].head())
    print(f"Total genres one-hot encoded columns added: {genres_dummies.shape[1]}")
    
    # Save the cleaned dataset for the next phase
    output_file = 'Kaggle_IMDB_Dataset_Cleaned.csv'
    df.to_csv(output_file, index=False)
    print(f"\nCleaned dataset saved to {output_file}")

if __name__ == "__main__":
    clean_data()
