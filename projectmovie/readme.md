pip install IMDbPY
This will install the IMDbPY package
pip list to check the package

IMDb class is imported from the IMDbPY package which will provide access to IMDB data. IMDbPY is a Python library for accessing IMDb's movie database.
ia is the instance of the IMDb class. It will be used to interact with IMDb database, such as searching for movies, retrieving their details, and updating movie information. The user is prompted to input the name of the movie which is stored in a variable (movie_name). The search_movie method from the IMDb class searches for movies that match the user's input(movie_name). A list of movie objects are returned which is assigned to a variable(movies).
if movies: will check if the movies list is empty or not. If it is empty, else statement is executed.
movies[0] selects the first movie from the list movies assigns it to a variable(movie)
update() method will add details to the movie object such as the director, cast, plot, and more.
The get() method will access the 'director' key in the movie object. If no such key is found, None is returned.
if directors: will check if the directors list is not empty. If directors are found, it will print the names, otherwise else block will be executed.
the loop after that will iterate through each director in the directors list and prints their name. Each value from directors i.e. director is a dictionary and 'name' is the key.
else: part will be executed if no director is found.


