from imdb import IMDb

ia = IMDb()   # creates an instance of the IMDb class
movie_name = input("Enter the movie name: ")
movies = ia.search_movie(movie_name)

if movies:
    movie = movies[0]
    ia.update(movie)
    directors = movie.get('directors')
    print(type(directors))
    if directors:
        print("Director(s):")
        for director in directors:
            print(director['name'])
    else:
        print("No director information found.")
else:
    print("Movie not found.")

# Practise this code:

from imdb import IMDb

ia = IMDb()
movie_name = input("Enter the movie name:")
movies = ia.search_movie(movie_name)

if movies:
    movie = movies[0]
    ia.update(movie)
    directors = movie.get('directors')
    if directors:
        print("Director(s):")
        for director in directors:
            print(director['name'])
    else:
        print("No director information found.")
else:
    print("Movie not found")

# redoing the code once more

from imdb import IMDb

ia = IMDb()
movie_name = input("Enter the movie name:")
movies = ia.search_movie(movie_name)

if movies:
    movie = movies[0]
    ia.update(movie)
    directors = movie.get('directors')
    if directors:
        print("Director(s):")
        for director in directors:
            print(director['name'])
        else:
            print("No director information found.")
    else:
        print("Movie not found")

# Redoing the code

from imdb import IMDb

ia = IMDb()
movie_name = input("Enter the name of the movie:")
movies = ia.search_movie(movie_name)

if movies:
    movie = movies[0]
    ia.update(movie)
    directors = movie.get('directors')
    if directors:
        print("Director(s):")
        for director in directors:
            print(director['name'])
        else:
            print("No director information found.")
    else:
        print("Movie not found.")