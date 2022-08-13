from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def register_user(self, username, age):
        if self.users_collection:
            for user in self.users_collection:
                if user.username == username:
                    raise Exception('User already exists!')
                # new_user = User(username, age)
                # self.users_collection.append(new_user)
                # return f'{username} registered successfully.'
        new_user = User(username, age)
        self.users_collection.append(new_user)
        return f'{username} registered successfully.'

    def upload_movie(self, username, movie: Movie):
        if movie in self.movies_collection:
            raise Exception('Movie already added to the collection!')
        for user in self.users_collection:
            if user.username == username:
                if user.username != movie.owner.username:
                    raise Exception(f'{username} is not the owner of the movie {movie.title}!')
                self.movies_collection.append(movie)
                user.movies_owned.append(movie)
                return f'{username} successfully added {movie.title} movie.'

        raise Exception('This user does not exist!')

    def edit_movie(self, username, movie, **kwargs):
        if movie not in self.movies_collection:
            raise Exception(f'The movie {movie.title} is not uploaded!')
        for user in self.users_collection:
            if user.username == username:
                if user.username != movie.owner.username:
                    raise Exception(f'{username} is not the owner of the movie {movie.title}!')
        for key, value in kwargs.items():
            if key == 'title':
                movie.title = value
            elif key == 'year':
                movie.year = value
            elif key == 'age_restriction':
                movie.age_restriction = value
        return f'{username} successfully edited {movie.title} movie.'

    def delete_movie(self, username, movie: Movie):
        if movie not in self.movies_collection:
            raise Exception(f'The movie {movie.title} is not uploaded!')
        for user in self.users_collection:
            if user.username == username:
                if user.username != movie.owner.username:
                    raise Exception(f'{username} is not the owner of the movie {movie.title}!')
                user.movies_owned.remove(movie)
        self.movies_collection.remove(movie)
        return f'{username} successfully deleted {movie.title} movie.'

    def like_movie(self, username, movie: Movie):

        for user in self.users_collection:
            if user.username == username:
                if user.username == movie.owner.username:
                    raise Exception(f'{username} is the owner of the movie {movie.title}!')
                if movie.title in user.movies_liked:
                    raise Exception(f'{username} already liked the movie {movie.title}!')
                movie.likes += 1
                user.movies_liked.append(movie)
                return f'{username} liked {movie.title} movie.'

    def dislike_movie(self, username, movie: Movie):
        for user in self.users_collection:
            if user.username == username:
                if movie.title in user.movies_liked:
                    raise Exception(f'{username} has not liked the movie {movie.title}!')
                movie.likes -= 1
                user.movies_liked.remove(movie)
                return f'{username} disliked {movie.title} movie.'

    def display_movies(self):
        if len(self.movies_collection) == 0:
            return 'No movies found.'
        else:
            result_str = []
            for movie in sorted(self.movies_collection, key=lambda x: (-x.year, x.title)):
                result_str.append(movie.details())
            return '\n'.join(result_str)
        # if not self.movies_collection:
        #     return 'No movies found'
        #
        # sorted_movies = sorted(self.movies_collection, key=lambda x: (-x.year, x.title))
        # return '\n'.join(m.details() for m in sorted_movies)

    def __str__(self):
        users = ''
        movies = ''
        if len(self.users_collection) == 0:
            users = 'No users.'
        else:
            users = ', '.join([user.username for user in self.users_collection])
        if len(self.movies_collection) == 0:
            movies = 'No movies.'
        else:
            movies = ', '.join([movie.title for movie in self.movies_collection])

        return f'All users: {users}\nAll movies: {movies}'
        # result = ''
        # if self.users_collection:
        #     result += f'All users: {", ".join([x.username for x in self.users_collection])}\n'
        # else:
        #     result += 'All users: No users.'
        #
        # if self.movies_collection:
        #     result += f'All movies: {", ".join([x.title for x in self.movies_collection])}\n'
        # else:
        #     result += 'All movies: No movies.'
        #
        # return result.strip()

