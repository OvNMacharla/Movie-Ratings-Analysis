# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Load CSV data
movies = pd.read_csv("data/movies_data.csv")
print("Data Loaded Successfully")
print(movies.head())  # First 5 rows

# Step 2: Top-rated movies
top_movies = movies.sort_values(by='Rating', ascending=False).head(5)
print("\nTop 5 Rated Movies:\n", top_movies[['Title', 'Rating']])

# Step 3: Average rating per genre
genre_rating = movies.groupby('Genre')['Rating'].mean().sort_values(ascending=False)
print("\nAverage Rating per Genre:\n", genre_rating)

# Step 4: Count of movies per genre
genre_count = movies['Genre'].value_counts()
print("\nNumber of Movies per Genre:\n", genre_count)

# Step 5: Visualization

# Bar Plot - Top Rated Movies
plt.figure(figsize=(8,5))
plt.bar(top_movies['Title'], top_movies['Rating'], color='purple')
plt.title("Top 5 Rated Movies")
plt.xlabel("Movie Title")
plt.ylabel("Rating")
plt.xticks(rotation=45)
plt.show()

# Bar Plot - Average Rating per Genre
plt.figure(figsize=(8,5))
plt.bar(genre_rating.index, genre_rating.values, color='green')
plt.title("Average Rating per Genre")
plt.xlabel("Genre")
plt.ylabel("Average Rating")
plt.show()

# Pie Chart - Number of Movies per Genre
plt.figure(figsize=(6,6))
plt.pie(genre_count.values, labels=genre_count.index, autopct='%1.1f%%', startangle=140)
plt.title("Movies Distribution by Genre")
plt.show()
