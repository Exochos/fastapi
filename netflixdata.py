# You are a Data Analyst at a media consulting firm. Netflix, a major client, is interested in comprehensive insights about their catalog of shows and movies.
import pandas as pd

# Load the data
file_path = 'netflix_data.csv'

# Read the dataset into a pandas DataFrame named netflix_titles.
netflix_titles = pd.read_csv(file_path)

# Display the first 5 rows of the DataFrame
print(netflix_titles.head())

# Show basic information about the dataset
print(netflix_titles.info())
print(netflix_titles.describe())


# Count the number of titles per country.
# Find the top 5 countries in terms of the number of titles.
# Identify the year with the highest number of releases.
titles_per_country = netflix_titles['country'].value_counts()
top_countries = titles_per_country.head(5)
year_with_most_releases = netflix_titles['release_year'].value_counts().idxmax()

# Show the results
print(titles_per_country)
print(top_countries)
print(year_with_most_releases)

# Create a new DataFrame named movies that contains only the entries where the type is 'Movie', including all relevant columns from the original dataset.
movies = netflix_titles[netflix_titles['type'] == 'Movie']

print(movies.head())

# List unique directors present in the dataset.
unique_directors = netflix_titles['director'].unique()

print(unique_directors)

# Replace missing director values with "unknown".
netflix_titles['director'] = netflix_titles['director'].fillna('unknown')

