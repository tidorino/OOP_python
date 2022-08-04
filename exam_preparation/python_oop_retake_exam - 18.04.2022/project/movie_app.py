from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def register_user(self, username, age):
        for user in self.users_collection:
            if user.username == username:
                raise Exception('User already exists!')
        new_user = User(username, age)
        self.users_collection.append(new_user)

        return f'{username} registered successfully.'

    def upload_movie(self, username, movie: Movie):

        if User.username not in self.users_collection:
            raise Exception('This user does not exist!')
        for movie in self.movies_collection:
            if movie.owner != username:
                raise Exception(f'{username} is not the owner of the movie {movie.title}!')

        # if movie.owner != user.username:
        #     raise Exception(f'{username} is not the owner of the movie {movie.title}!')
        for movie_title in self.movies_collection:
            if movie_title == movie.title:
                raise Exception('Movie already added to the collection!')

        for user in self.users_collection:
            if user.username == username:
                user.movies_owned.append(movie)
        self.movies_collection.append(movie)
        return f'{username} successfully added {movie.title} movie.'


    def edit_movie(self, username, movie: Movie, **kwargs):
        pass

    def delete_movie(self, username, movie: Movie):
        pass

    def like_movie(self, username, movie: Movie):
        pass

    def dislike_movie(self, username, movie: Movie):
        pass

    def display_movies(self):
        pass

    def __str__(self):
        pass

