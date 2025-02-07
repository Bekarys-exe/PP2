# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

#1
def is_high_rated(movie):
    return movie['imdb'] > 5.5

print(is_high_rated(movies[0]))

#2
def filter_high_rated_movies(movies):
    return list(filter(lambda movie: movie['imdb'] > 5.5, movies))

high_rated_movies = filter_high_rated_movies(movies)
print(high_rated_movies)

3#
def filter_movies_by_category(movies, category):
    return list(filter(lambda movie: movie['category'] == category, movies))

romance_movies = filter_movies_by_category(movies, "Romance")
print(romance_movies)

4#
def average_imdb_score(movies):
    if not movies:
        return 0
    total_score = sum(movie['imdb'] for movie in movies)
    return total_score / len(movies)

average_score = average_imdb_score(movies)
print(average_score)

5#
def average_imdb_score_by_category(movies, category):
    category_movies = filter_movies_by_category(movies, category)
    return average_imdb_score(category_movies)

average_romance_score = average_imdb_score_by_category(movies, "Romance")
print(average_romance_score)