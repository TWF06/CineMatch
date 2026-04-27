import pandas as pd
import numpy as np

def load_and_prepare():
    """Load the cleaned dataset and calculate Weighted Ratings."""
    print("Loading cleaned dataset...")
    try:
        df = pd.read_csv('Kaggle_IMDB_Dataset_Cleaned.csv')
    except FileNotFoundError:
        print("Error: Could not find Kaggle_IMDB_Dataset_Cleaned.csv. Run 02_data_cleaning.py first.")
        return None, []

    # --- Calculate Weighted Rating (IMDB Formula) ---
    # C = mean rating across all movies
    C = df['IMDB_Rating'].mean()
    # m = minimum votes required (75th percentile)
    m = df['No_of_Votes'].quantile(0.75)

    def weighted_rating(row):
        v = row['No_of_Votes']
        R = row['IMDB_Rating']
        return (v / (v + m)) * R + (m / (v + m)) * C

    df['Weighted_Rating'] = df.apply(weighted_rating, axis=1)

    # Identify the available genre columns (one-hot encoded columns from Phase 3)
    # These are columns that only contain 0s and 1s and are not our known numeric columns
    known_cols = [
        'Poster_Link', 'Series_Title', 'Released_Year', 'Certificate',
        'Runtime', 'Genre', 'IMDB_Rating', 'Overview', 'Meta_score',
        'Director', 'Star1', 'Star2', 'Star3', 'Star4',
        'No_of_Votes', 'Gross', 'Weighted_Rating'
    ]
    genre_columns = [col for col in df.columns if col not in known_cols]

    print(f"Weighted Ratings calculated. (C={C:.2f}, m={m:.0f})")
    print(f"Available genres: {', '.join(sorted(genre_columns))}\n")

    return df, sorted(genre_columns)


def recommend_movies(df, genre, genre_columns, top_n=10):
    """Filter by genre and return top N movies by Weighted Rating."""
    # Case-insensitive match
    matched = [g for g in genre_columns if g.lower() == genre.lower()]

    if not matched:
        print(f"  Genre '{genre}' not found.")
        print(f"  Available genres: {', '.join(genre_columns)}")
        return None

    genre_col = matched[0]
    filtered = df[df[genre_col] == 1].copy()

    if filtered.empty:
        print(f"  No movies found for genre '{genre_col}'.")
        return None

    filtered = filtered.sort_values('Weighted_Rating', ascending=False).head(top_n)

    # Display columns
    display_cols = ['Series_Title', 'Released_Year', 'Genre', 'IMDB_Rating', 'Weighted_Rating', 'Director', 'Runtime']
    result = filtered[display_cols].reset_index(drop=True)
    result.index = result.index + 1  # Start ranking from 1
    return result


def main():
    df, genre_columns = load_and_prepare()
    if df is None:
        return

    print("=" * 60)
    print("  ***  MOVIE GENRE RECOMMENDATION ENGINE  ***")
    print("=" * 60)
    print("Type a genre to get top movie recommendations.")
    print("Type 'genres' to see all available genres.")
    print("Type 'quit' to exit.\n")

    while True:
        user_input = input("Enter a genre: ").strip()

        if not user_input:
            continue

        if user_input.lower() == 'quit':
            print("Goodbye!")
            break

        if user_input.lower() == 'genres':
            print(f"\n  Available genres: {', '.join(genre_columns)}\n")
            continue

        print(f"\n  Top recommendations for '{user_input}':\n")
        result = recommend_movies(df, user_input, genre_columns)
        if result is not None:
            print(result.to_string())
        print()


if __name__ == "__main__":
    main()
