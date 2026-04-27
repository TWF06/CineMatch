# Data Science Project Plan: Movie Genre DSP

This document outlines the standard phases of a Data Science project, tailored for the IMDb Top 1000 Movies Dataset. The end goal is to build a movie recommendation system based on user-selected genres.

---

## Phase 1: Problem Definition & Goals ✅
**Status:** Complete  
**Objective:** Define what we want to achieve with this dataset.
*   **Define the Target:** We will create a recommendation system that suggests movies when a user enters a genre they like.
*   **Identify Key Metrics:** For recommendations without user history, success means surfacing highly rated, relevant movies. We will prioritize high `IMDB_Rating` and `No_of_Votes` to ensure quality and popularity within the selected genre.
*   **Determine Scope:** Primary features: `Genre` and `IMDB_Rating`. Supporting features: `Overview`, `Certificate`, `Runtime`, `Director`, and the `Star` columns.

---

## Phase 2: Data Acquisition & Initial Understanding ✅
**Status:** Complete — `01_data_understanding.py`  
**Objective:** Load the data and get a high-level overview of its structure.
*   **Load Data:** Read the `Kaggle_IMDB_Dataset.csv` into a Pandas DataFrame.
*   **Initial Inspection:** 
    *   View the first and last few rows (`df.head()`, `df.tail()`).
    *   Check dataset dimensions (`df.shape`) → **1000 rows, 16 columns**.
    *   Review column names and data types (`df.info()`).
    *   Generate summary statistics for numerical and categorical columns (`df.describe()`).

**Key Findings:**
| Column | Missing Values | Notes |
|---|---|---|
| Certificate | 101 | Filled with 'Unrated' in Phase 3 |
| Meta_score | 157 | Filled with median in Phase 3 |
| Gross | 169 | Filled with median in Phase 3 |

---

## Phase 3: Data Cleaning & Preprocessing ✅
**Status:** Complete — `02_data_cleaning.py`  
**Output:** `Kaggle_IMDB_Dataset_Cleaned.csv`  
**Objective:** Prepare the raw data for analysis by handling errors, missing values, and formatting issues.
*   **Handle Missing Values (NaN):** 
    *   `Certificate` → filled with `'Unrated'`.
    *   `Meta_score` → filled with median value.
    *   `Gross` → filled with median value.
*   **Data Type Conversion:**
    *   `Gross`: Removed commas, converted string → float.
    *   `Runtime`: Removed `" min"` suffix, converted string → int.
*   **Handle Duplicates:** 0 duplicates found.
*   **String Formatting:** Stripped whitespace from `Series_Title` and `Director`.
*   **Feature Engineering (Initial):**
    *   Split the `Genre` column into **21 one-hot encoded boolean columns** (e.g., `Action`, `Drama`, `Sci-Fi`).

---

## Phase 4: Exploratory Data Analysis (EDA) ✅
**Status:** Complete — `03_eda.py`  
**Output:** `eda_plots/` directory (6 plot images)  
**Objective:** Discover patterns, spot anomalies, test hypotheses, and check assumptions.
*   **Univariate Analysis:**
    *   Distribution of `IMDB_Rating` (Histogram) → `eda_plots/01_imdb_rating_dist.png`
    *   Distribution of `Released_Year` → `eda_plots/02_released_year_dist.png`
    *   Frequency counts of `Genre` (Bar chart) → `eda_plots/03_genre_counts.png`
*   **Bivariate/Multivariate Analysis:**
    *   Correlation matrix (`IMDB_Rating`, `Gross`, `Runtime`, `No_of_Votes`, `Meta_score`) → `eda_plots/04_correlation_matrix.png`
    *   Scatter plot: `IMDB_Rating` vs. `Gross` → `eda_plots/05_rating_vs_gross.png`
    *   Boxplot: `IMDB_Rating` across `Certificate` types → `eda_plots/06_rating_by_certificate.png`

---

## Phase 5: Recommendation Engine ✅
**Status:** Complete — `04_recommendation_engine.py`  
**Script:** `04_recommendation_engine.py`  
**Objective:** Build the core recommendation system that suggests top movies based on a user's preferred genre.

*   **Weighted Rating Formula (IMDB WR):**
    *   `WR = (v / (v+m)) * R + (m / (v+m)) * C`
    *   `v` = number of votes for the movie (`No_of_Votes`)
    *   `m` = minimum votes required (75th percentile threshold)
    *   `R` = average rating of the movie (`IMDB_Rating`)
    *   `C` = mean rating across all movies
*   **Genre Filtering:** Use the one-hot encoded genre columns to filter movies matching the user's selected genre.
*   **Ranking:** Sort filtered results by Weighted Rating (descending) and return top N recommendations.
*   **Interactive CLI:** Provide a terminal-based loop where users can type a genre and receive recommendations.

---

## Phase 6: Flask Web UI (CineMatch) ✅
**Status:** Complete — `app.py`  
**URL:** `http://127.0.0.1:5000`  
**Objective:** Provide a visual, browser-based interface for the recommendation engine.

*   **Tech Stack:** Flask (backend), Vanilla HTML/CSS/JS (frontend).
*   **Backend (`app.py`):**
    *   Loads cleaned data and calculates Weighted Ratings at startup.
    *   Serves the main page at `/`.
    *   Exposes a `/recommend` POST endpoint returning JSON results.
*   **Frontend (`templates/index.html` + `static/style.css`):**
    *   Dark-mode premium design with animated background particles.
    *   Interactive genre chip selector with icons (21 genres).
    *   AJAX-powered movie cards with staggered entrance animations.
    *   Each card displays: poster, title, year, IMDB rating (gold/silver/bronze badge), weighted rating, genre tags, overview, director, stars, and vote count.
    *   Responsive layout for mobile and desktop.
*   **How to Run:**
    ```
    venv\Scripts\python.exe app.py
    ```
    Then open `http://127.0.0.1:5000` in a browser.

---

## Project File Structure

```
Movie Genre DSP/
├── app.py                          # Phase 6: Flask web server (CineMatch)
├── 01_data_understanding.py        # Phase 2: Load & inspect raw data
├── 02_data_cleaning.py             # Phase 3: Clean, convert, and engineer features
├── 03_eda.py                       # Phase 4: Generate visual analysis plots
├── 04_recommendation_engine.py     # Phase 5: CLI recommendation system
├── Kaggle_IMDB_Dataset.csv         # Raw dataset (1000 movies, 16 columns)
├── Kaggle_IMDB_Dataset.zip         # Original zipped dataset
├── Kaggle_IMDB_Dataset_Cleaned.csv # Cleaned dataset (output of Phase 3)
├── Kaggle_IMDB_Metadata.json       # MLCommons Croissant metadata
├── Planning.md                     # This file
├── requirements.txt                # Python dependencies
├── templates/
│   └── index.html                  # Phase 6: Main web page template
├── static/
│   └── style.css                   # Phase 6: CSS styling (dark theme)
├── eda_plots/                      # EDA output images
│   ├── 01_imdb_rating_dist.png
│   ├── 02_released_year_dist.png
│   ├── 03_genre_counts.png
│   ├── 04_correlation_matrix.png
│   ├── 05_rating_vs_gross.png
│   └── 06_rating_by_certificate.png
└── venv/                           # Python virtual environment
```
