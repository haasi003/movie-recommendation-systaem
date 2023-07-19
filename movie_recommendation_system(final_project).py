# -*- coding: utf-8 -*-
"""Movie Recommendation System(final project)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YauoGrghhMHdQUITcGsZAahIHW-MB43l

### **Title of Project**
Movie Recommendation System using Content-Based Filtering

### **Objective**

The objective of the project is to develop a content-based movie recommendation system that suggests movies to users based on their preferences and the similarity between the movies. The system uses natural language processing (NLP) techniques to extract features from movie data, and then applies machine learning algorithms to build a recommendation model. The model recommends movies that are similar to the user's favorite movie, based on features such as genres, keywords, taglines, cast, and director.

### **Data Source**

The data used in the project is the MovieLens dataset, which can be obtained from the official website: https://grouplens.org/datasets/movielens/latest/. Specifically, we used the small version of the dataset, which contains 100,000 ratings and 3,600 tag applications applied to 9,000 movies by 600 users.

The dataset that I used can be found at https://raw.githubusercontent.com/akhilpinikeshi/Movie-Recommendation-System-using-Content-Based-Filtering/main/movies.csv.

### **Import Library**
"""

import numpy as np
import pandas as pd
import difflib  # It provides classes and functions for comparing sequences(i.e. movies that are similar in terms of their titles).
from sklearn.feature_extraction.text import TfidfVectorizer # It is used to evaluate how relevant a word is to a document(i.e. importance of certain words or features (such as genre, actors, and director) in a movie's description, and compare it to the importance of those same features in other movies).
from sklearn.metrics.pairwise import cosine_similarity # It is used to compute the similarity between movies based on their feature vectors.It ranks the movies in terms of similarity, with the most similar movies appearing at the top of the list

"""### **Import Data**"""

# loading the data from the csv file to a pandas dataframe(movies_data)
movies_data = pd.read_csv('https://raw.githubusercontent.com/akhilpinikeshi/finalproject-YBI/main/movies.csv')

"""### **Describe Data**"""

# printing the first 5 rows of the dataframe
movies_data.head()

# printing names of columns in dataset
movies_data.columns

# printing the concise summary of dataset
movies_data.info()

# printig summary of the statistical properties of the numerical columns in the dataset,
movies_data.describe()

#printing the dimensions (number of rows and columns) of the dataset.
movies_data.shape

"""### **Data Visualization**"""

#  histogram of the movie popularity to see how they are distributed.
import matplotlib.pyplot as plt

plt.hist(movies_data['popularity'], bins=10)
plt.xlabel('Popularity')
plt.ylabel('Frequency')
plt.title('Distribution of Movie Popularity')
plt.show()

# scatter plot to see if there is any correlation between the budget and revenue of movies.
import seaborn as sns

sns.scatterplot(data=movies_data, x='budget', y='revenue')
plt.xlabel('Budget')
plt.ylabel('Revenue')
plt.title('Scatterplot of Movie Budget vs Revenue')
plt.show()

"""### **Data Preprocessing**"""

# selecting the relevant features for recommendation

selected_features = ['genres','keywords','tagline','cast','director']
print(selected_features)

# replacing the null valuess with null string

for feature in selected_features:
  movies_data[feature] = movies_data[feature].fillna('')

# combining all the 5 selected features

combined_features = movies_data['genres']+' '+movies_data['keywords']+' '+movies_data['tagline']+' '+movies_data['cast']+' '+movies_data['director']

print(combined_features)

"""### vectorization of features

TfidfVectorizer will create a matrix where each row represents a movie and each column represents a feature (i.e., a keyword). The value in each cell of the matrix will be the weight of the corresponding feature in the corresponding movie.

"""

# converting the text data to feature vectors

vectorizer = TfidfVectorizer()

feature_vectors = vectorizer.fit_transform(combined_features)

print(feature_vectors)

"""### **Cosine Similarity**
The cosine similarity metric is used to compute the similarity between each pair of movies.

The result will be a similarity matrix where each row and column represents a movie, and each cell represents the similarity score between the corresponding pair of movies.
"""

# getting the similarity scores using cosine similarity

similarity = cosine_similarity(feature_vectors)

print(similarity)

print(similarity.shape)

"""### **Define Target Variable (y) and Feature Variables (X)**
In this project, we do not have a target variable since we are not predicting any outcome. Instead, we are trying to recommend similar movies based on a user's input. Therefore, we only have feature variables (X), which are the movie attributes such as genre, cast, and director.

### **Train Test Split**
In a movie recommendation system, the goal is to build a model that can predict which movies a user will enjoy based on their past viewing history or other relevant features. To build and evaluate such a model, it is common to use a train-test split, where the data is split into two sets, a training set and a testing set. However, in some cases, it may be difficult to use train-test split if the features are not well-defined or understood.

For example, if we don't have proper features to use as input to our model, it may be challenging to split the data into a training set and a testing set.

### **Modeling**
Modelling in a movie recommendation system involves the process of training a machine learning model to predict which movies a user will enjoy based on their past viewing history or other relevant features. There are several popular approaches to building such models.

**Content-based filtering**: This approach builds a model based on the characteristics of the movies themselves. It finds similarities between movies based on their genre, cast, plot, and other features and recommends movies that are similar to movies the user has already enjoyed.
"""

# getting the movie name from the user

movie_name = input(' Enter your favourite movie name : ')

# creating a list with all the movie names given in the dataset

list_of_all_titles = movies_data['title'].tolist()
print(list_of_all_titles)

# finding the close match for the movie name given by the user

find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)
print(find_close_match)

close_match = find_close_match[0]
print(close_match)

# finding the index of the movie with title

index_of_the_movie = movies_data[movies_data.title == close_match]['index'].values[0]
print(index_of_the_movie)

# getting a list of similar movies

similarity_score = list(enumerate(similarity[index_of_the_movie]))
print(similarity_score)

len(similarity_score)

# sorting the movies based on their similarity score

sorted_similar_movies = sorted(similarity_score, key = lambda xyz:xyz[1], reverse = True)
print(sorted_similar_movies)

# print the name of similar movies based on the index

print('Movies suggested for you : \n')

i = 1

for movie in sorted_similar_movies:
  index = movie[0]
  title_from_index = movies_data[movies_data.index==index]['title'].values[0]
  if (i<30):
    print(i, '.',title_from_index)
    i+=1

"""### **Model Evaluation**

we cannot perform model evaluation for a content-based movie recommendation system as it does not use any explicit ratings or feedback data. In a content-based approach, the recommendations are based on the similarity between the features of movies. Therefore, the evaluation of such a system usually involves a qualitative analysis by assessing the relevance of the recommended movies based on the user's preferences or subjective criteria.

### **Prediction**

we cannot make predictions for a content-based movie recommendation system as it does not involve predicting ratings or preferences for a user. Instead, it suggests movies that are similar to the ones a user has liked in the past based on the content of the movies. Therefore, it only recommends movies based on similarity, not on explicit ratings or preferences.

### **Explaination**

This code implements a content-based movie recommendation system using cosine similarity.

First, the code reads movie data from a CSV file and selects relevant features for recommendation, which include genres, keywords, tagline, cast, and director. The null values in these features are replaced with null strings, and all five features are combined into a single string called combined_features.

The code then uses TfidfVectorizer to convert the text data in combined_features into feature vectors. These feature vectors are then used to calculate the similarity scores between all pairs of movies using cosine similarity.

When the user inputs their favorite movie name, the code finds the closest match to the input name using difflib. The index of the matched movie is then used to retrieve the similarity scores between that movie and all other movies. The movies are then sorted in descending order of similarity score and the top 30 movies are recommended to the user.

Overall, the code works by calculating similarity between movies based on their features, and recommending movies that are most similar to the user's input movie.

### Movie Recommendation Sytem
"""

movie_name = input(' Enter your favourite movie name : ')

list_of_all_titles = movies_data['title'].tolist()

find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)

close_match = find_close_match[0]

index_of_the_movie = movies_data[movies_data.title == close_match]['index'].values[0]

similarity_score = list(enumerate(similarity[index_of_the_movie]))

sorted_similar_movies = sorted(similarity_score, key = lambda x:x[1], reverse = True)

print('Movies suggested for you : \n')

i = 1

for movie in sorted_similar_movies:
  index = movie[0]
  title_from_index = movies_data[movies_data.index==index]['title'].values[0]
  if (i<30):
    print(i, '.',title_from_index)
    i+=1