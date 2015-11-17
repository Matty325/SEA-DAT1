'''
Pandas Homework with IMDb data
'''

'''
BASIC LEVEL
'''

import pandas as pd
import matplotlib.pyplot as plt

# read in 'imdb_1000.csv' and store it in a DataFrame named movies
file_path = 'C:\Users\Matt\githubclones\GA-SEA-DAT1\data\\'
movies_url = file_path + 'imdb_1000.csv'
movies = pd.read_table(movies_url, sep=',', header=0)
movies.head()



# check the number of rows and columns
movies.shape

# check the data type of each column
movies.dtypes

# calculate the average movie duration
movies.duration.mean()

# sort the DataFrame by duration to find the shortest and longest movies
movies.sort('duration')
''' The shortest movie is Freaks, at 64 mins.  The longest is Hamlet, at 242 mins'''


# create a histogram of duration, choosing an "appropriate" number of bins
movies.duration.plot(kind = 'hist', bins=20, title = 'Histgram of Movie Duration')
plt.xlabel('Duration (minutes)')
plt.ylabel('Count of Movies by Duration Bucket')


# use a box plot to display that same data
movies.duration.plot(kind='box')

'''
INTERMEDIATE LEVEL
'''

# count how many movies have each of the content ratings
movies.groupby('content_rating').content_rating.describe()


# use a visualization to display that same data, including a title and x and y labels
movies.content_rating.value_counts().plot(kind='bar')
plt.xlabel('Rating')
plt.ylabel('Count by Rating')


# convert the following content ratings to "UNRATED": NOT RATED, APPROVED, PASSED, GP
# replace all instances of a value in a column (must match entire value)
movies.content_rating.replace(('NOT RATED', 'APPROVED', 'PASSED', 'GP'), "UNRATED", inplace=True)
movies.groupby('content_rating').content_rating.describe()



# convert the following content ratings to "NC-17": X, TV-MA
movies.content_rating.replace(('X', 'TV-MA'), "NC-17", inplace=True)
movies.groupby('content_rating').content_rating.describe()


# count the number of missing values in each column
movies.isnull().sum() 


# if there are missing values: examine them, then fill them in with "reasonable" values
import numpy as np

movies[movies['content_rating'].isnull()]
movies.content_rating.fillna(value='UNRATED', inplace=True) 
movies.isnull().sum() 

# calculate the average star rating for movies 2 hours or longer,
movies[movies.duration > 120].star_rating.mean()
movies.duration.describe()
movies.star_rating.describe()

# and compare that with the average star rating for movies shorter than 2 hours
movies[movies.duration < 120].star_rating.mean()



# use a visualization to detect whether there is a relationship between duration and star rating
plt.rcParams['figure.figsize'] = (8, 6)
plt.rcParams['font.size'] = 14
movies.plot(kind='scatter', x='duration', y='star_rating')

# calculate the average duration for each genre
movies.groupby('genre').mean()

'''
ADVANCED LEVEL
'''

# visualize the relationship between content rating and duration
movies.boxplot(column='duration', by='content_rating')


# determine the top rated movie (by star rating) for each genre
movies.sort(['genre', 'star_rating']).groupby('genre').head(1)

# check if there are multiple movies with the same title, and if so, determine if they are actually duplicates
movies.sort('title').title.duplicated()
movies.duplicated(['title']).sum()
movie_dupes = movies[movies.duplicated('title')].title

# calculate the average star rating for each genre, but only include genres with at least 10 movies
'''
I can't get this approach to work.  I think it should be somethign like 1) find the genre's with >= 10 movies (done), 
2) create a boolean mask that picks out records in those genres; 3) for that subset, group by genre and take the mean.
'''
movies.genre.value_counts()
movies[movie_subset >= 10].star_rating.mean()
movies[movies['genre'].value_counts() >= 10].groupby('genre').star_rating.mean()



'''
BONUS
'''

# Figure out something "interesting" using the actors data!
