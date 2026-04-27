# 🎬 CineMatch — Movie Genre Recommendation System

A data-driven movie recommendation engine built on the **IMDb Top 1000** dataset. CineMatch uses a **weighted rating algorithm** to surface the best movies by genre, presented through a premium interactive web interface.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.x-000000?logo=flask&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

---

## ✨ Features

- **Genre-Based Recommendations** — Select a genre and instantly get the top-rated movies, ranked by a weighted rating formula
- **Weighted Rating Algorithm** — Balances IMDb rating with vote count to avoid bias toward low-vote outliers
- **Interactive Web UI** — Clean, responsive Flask frontend with poster images, ratings, and movie details
- **Full Data Pipeline** — From raw data ingestion → cleaning → EDA → recommendation engine → deployment

---

## 📊 How It Works

CineMatch uses a **Bayesian weighted rating** inspired by IMDb's own formula:

```
Weighted Rating = (v / (v + m)) × R + (m / (v + m)) × C
```

| Symbol | Meaning |
|--------|---------|
| `v` | Number of votes for the movie |
| `m` | Minimum votes required (75th percentile) |
| `R` | Average rating of the movie |
| `C` | Mean rating across all movies |

This ensures movies with fewer votes are pulled toward the global average, giving a fairer ranking.

---

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/TWF06/CineMatch.git
cd CineMatch

# Create virtual environment
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

Open your browser at **http://localhost:5000** 🎉

---

## 📁 Project Structure

```
CineMatch/
├── app.py                          # Flask web server
├── templates/
│   └── index.html                  # Frontend UI
├── static/
│   └── style.css                   # Styling
├── 01_data_understanding.py        # Step 1: Data exploration
├── 02_data_cleaning.py             # Step 2: Data cleaning & preprocessing
├── 03_eda.py                       # Step 3: Exploratory Data Analysis
├── 04_recommendation_engine.py     # Step 4: Weighted rating algorithm
├── generate_report.py              # Auto-generate project report
├── Kaggle_IMDB_Dataset_Cleaned.csv # Cleaned dataset
├── Kaggle_IMDB_Metadata.json       # Dataset metadata (Croissant format)
├── Planning.md                     # Project planning document
├── Procfile                        # Deployment config (Render/Railway)
├── requirements.txt                # Python dependencies
└── README.md                       # You are here
```

---

## 🔬 Data Science Pipeline

| Phase | Script | Description |
|-------|--------|-------------|
| **1. Understanding** | `01_data_understanding.py` | Initial data inspection, schema analysis |
| **2. Cleaning** | `02_data_cleaning.py` | Handle missing values, type conversion, genre encoding |
| **3. EDA** | `03_eda.py` | Visualizations — rating distributions, genre trends, correlations |
| **4. Modeling** | `04_recommendation_engine.py` | Weighted rating computation and recommendation logic |
| **5. Deployment** | `app.py` | Flask web app serving recommendations |

---

## 🌐 Deployment

The app is deployment-ready for platforms like **Render**, **Railway**, or **PythonAnywhere**.

```bash
# Production server (used by Procfile)
gunicorn app:app
```

---

## 📦 Tech Stack

| Layer | Technology |
|-------|-----------|
| **Backend** | Flask, Python |
| **Data Processing** | Pandas, NumPy |
| **Visualization** | Matplotlib, Seaborn |
| **ML Utilities** | Scikit-learn |
| **Production Server** | Gunicorn |

---

## 📄 Dataset

- **Source:** [IMDb Top 1000 Movies — Kaggle](https://www.kaggle.com/datasets/harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows)
- **Records:** 1,000 movies
- **Features:** Title, genre, rating, votes, director, stars, runtime, gross revenue, and more

---

## 📝 License

This project is for educational purposes. Dataset sourced from Kaggle under its terms of use.

---

<p align="center">
  Built with ❤️ by <a href="https://github.com/TWF06">TWF06</a>
</p>
