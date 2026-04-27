import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def run_eda():
    print("Loading cleaned dataset...")
    try:
        df = pd.read_csv('Kaggle_IMDB_Dataset_Cleaned.csv')
    except FileNotFoundError:
        print("Error: Could not find Kaggle_IMDB_Dataset_Cleaned.csv. Run Phase 3 first.")
        return

    # Create an output directory for plots
    os.makedirs("eda_plots", exist_ok=True)
    print("\n--- Phase 4: Exploratory Data Analysis (EDA) ---")

    sns.set_theme(style="whitegrid")

    # 1. Univariate Analysis
    print("Generating Univariate Plots...")
    
    # IMDB_Rating Histogram
    plt.figure(figsize=(10, 6))
    sns.histplot(df['IMDB_Rating'], bins=20, kde=True, color='blue')
    plt.title('Distribution of IMDB Ratings')
    plt.savefig('eda_plots/01_imdb_rating_dist.png')
    plt.close()

    # Released_Year Distribution
    # Note: 'Released_Year' might have errant strings like 'PG' (a known issue in this dataset)
    # so we coerce errors to NaN so we can plot it numerically
    df['Released_Year'] = pd.to_numeric(df['Released_Year'], errors='coerce')
    plt.figure(figsize=(12, 6))
    sns.histplot(df['Released_Year'].dropna(), bins=30, kde=True, color='green')
    plt.title('Distribution of Release Years')
    plt.savefig('eda_plots/02_released_year_dist.png')
    plt.close()

    # Frequency counts of Genres
    # We use the original string column and split it for the plot
    genres_series = df['Genre'].str.split(', ').explode()
    plt.figure(figsize=(12, 8))
    # Note: palette argument without hue is deprecated in future seaborn versions, 
    # but we'll use hue with legend=False to be safe.
    sns.countplot(y=genres_series, order=genres_series.value_counts().index, hue=genres_series, palette="viridis", legend=False)
    plt.title('Frequency Counts of Genres')
    plt.xlabel('Number of Movies')
    plt.ylabel('Genre')
    plt.savefig('eda_plots/03_genre_counts.png')
    plt.close()

    # 2. Bivariate/Multivariate Analysis
    print("Generating Bivariate Plots...")
    
    # Correlation Matrix
    numeric_cols = ['IMDB_Rating', 'Gross', 'Runtime', 'No_of_Votes', 'Meta_score']
    corr = df[numeric_cols].corr()
    plt.figure(figsize=(8, 6))
    sns.heatmap(corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
    plt.title('Correlation Matrix of Numerical Variables')
    plt.savefig('eda_plots/04_correlation_matrix.png')
    plt.close()

    # Scatter plot: IMDB_Rating vs. Gross
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='IMDB_Rating', y='Gross', data=df, alpha=0.6, color='purple')
    plt.title('IMDB Rating vs. Gross Revenue')
    plt.savefig('eda_plots/05_rating_vs_gross.png')
    plt.close()

    # Boxplot: IMDB_Rating across Certificate
    plt.figure(figsize=(12, 6))
    sns.boxplot(x='Certificate', y='IMDB_Rating', data=df, hue='Certificate', palette='Set2', legend=False)
    plt.title('IMDB Rating across Certificates')
    plt.xticks(rotation=45)
    plt.savefig('eda_plots/06_rating_by_certificate.png')
    plt.close()

    print("\nEDA complete! All plots saved to the 'eda_plots' directory.")
    print("\nFindings/Hypotheses to consider based on outputs:")
    print("- Check the correlation matrix to see if Runtime or No_of_Votes strongly correlates with IMDB_Rating.")
    print("- Check the Scatter plot for outliers in Gross revenue.")

if __name__ == "__main__":
    run_eda()
