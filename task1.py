import pandas as pd

df = pd.read_csv("netflix_titles.csv")

print("Original shape:", df.shape)
print("\nMissing values:\n", df.isnull().sum())


duplicates = df.duplicated().sum()
print(f"\nDuplicate rows: {duplicates}")
df = df.drop_duplicates()


df = df.dropna(subset=['title'])

df['director'] = df['director'].fillna('Unknown')


df['cast'] = df['cast'].fillna('Not Available')


df['country'] = df['country'].fillna(df['country'].mode()[0])


df['date_added'] = df['date_added'].fillna('01-Jan-2000')


df['rating'] = df['rating'].fillna('Not Rated')
df['duration'] = df['duration'].fillna('Not Available')
df['listed_in'] = df['listed_in'].fillna('Not Specified')


df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].str.strip()



df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

df['year_added'] = df['date_added'].dt.year
df['month_added'] = df['date_added'].dt.month

df['release_year'] = df['release_year'].astype(int)


df.to_csv("netflix_titles_cleaned.csv", index=False)
print("\n✅ Data cleaning complete. Cleaned file saved as 'netflix_titles_cleaned.csv'")
