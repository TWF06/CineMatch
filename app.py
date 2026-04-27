from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np

app = Flask(__name__)

# --- Load and prepare data once at startup ---
def load_and_prepare():
    df = pd.read_csv('Kaggle_IMDB_Dataset_Cleaned.csv')

    C = df['IMDB_Rating'].mean()
    m = df['No_of_Votes'].quantile(0.75)

    def weighted_rating(row):
        v = row['No_of_Votes']
        R = row['IMDB_Rating']
        return (v / (v + m)) * R + (m / (v + m)) * C

    df['Weighted_Rating'] = df.apply(weighted_rating, axis=1)

    known_cols = [
        'Poster_Link', 'Series_Title', 'Released_Year', 'Certificate',
        'Runtime', 'Genre', 'IMDB_Rating', 'Overview', 'Meta_score',
        'Director', 'Star1', 'Star2', 'Star3', 'Star4',
        'No_of_Votes', 'Gross', 'Weighted_Rating'
    ]
    genre_columns = sorted([col for col in df.columns if col not in known_cols])

    return df, genre_columns

DF, GENRES = load_and_prepare()


def recommend_movies(genre, top_n=10):
    matched = [g for g in GENRES if g.lower() == genre.lower()]
    if not matched:
        return None

    genre_col = matched[0]
    filtered = DF[DF[genre_col] == 1].copy()

    if filtered.empty:
        return None

    filtered = filtered.sort_values('Weighted_Rating', ascending=False).head(top_n)
    results = []
    for _, row in filtered.iterrows():
        results.append({
            'title': row['Series_Title'],
            'year': row['Released_Year'],
            'genre': row['Genre'],
            'rating': round(row['IMDB_Rating'], 1),
            'weighted_rating': round(row['Weighted_Rating'], 2),
            'director': row['Director'],
            'runtime': int(row['Runtime']),
            'overview': row['Overview'],
            'poster': row['Poster_Link'],
            'votes': f"{int(row['No_of_Votes']):,}",
            'stars': ', '.join(filter(None, [
                str(row.get('Star1', '')),
                str(row.get('Star2', '')),
            ])),
        })
    return results


@app.route('/')
def index():
    return render_template('index.html', genres=GENRES)


@app.route('/recommend', methods=['POST'])
def recommend():
    genre = request.form.get('genre', '').strip()
    if not genre:
        return jsonify({'error': 'No genre provided'}), 400

    results = recommend_movies(genre)
    if results is None:
        return jsonify({'error': f'Genre "{genre}" not found'}), 404

    return jsonify({'movies': results, 'genre': genre})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
