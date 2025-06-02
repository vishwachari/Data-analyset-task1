# Data-analyset-task1
# 🎬 Netflix Movies and TV Shows Dataset Cleaning

## 📌 Task Overview

This project is part of a **Data Analyst Internship** Task 1 focused on **Data Cleaning and Preprocessing** using Python and Pandas.

The raw dataset contains information about movies and TV shows on Netflix, including fields like title, director, cast, country, date added, release year, rating, and more.

---

## 📂 Dataset Source

- Dataset: `netflix_titles.csv`
- Source: [Kaggle - Netflix Movies and TV Shows](https://www.kaggle.com/datasets/shivamb/netflix-shows)

---

## ✅ Cleaning Steps Performed

1. **Removed Duplicate Records**
   - Used `.drop_duplicates()` to remove exact duplicate rows.

2. **Handled Missing Values**
   - Dropped rows where `title` was missing.
   - Filled `director` with `'Unknown'`.
   - Filled `cast` with `'Not Available'`.
   - Filled `country` with the most frequent country.
   - Filled missing `date_added`, `rating`, `duration`, and `listed_in` with default placeholders.

3. **Standardized Text Values**
   - Stripped extra whitespace from text columns.
   - Lowercased and cleaned column headers using underscores.

4. **Date Formatting**
   - Converted `date_added` to datetime format.
   - Extracted `year_added` and `month_added` from `date_added`.

5. **Ensured Proper Data Types**
   - Converted `release_year` to integer.

---

## 💾 Output

- Cleaned file: `netflix_titles_cleaned.csv`
- Python script: `netflix_cleaning.py`

---

## 📘 Tools Used

- Python 3
- Pandas
