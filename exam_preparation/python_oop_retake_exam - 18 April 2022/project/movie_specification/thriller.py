from project.movie_specification.movie import Movie


class Thriller(Movie):

    def __init__(self, title: str, year: int, owner: object, age_restriction: int = 16):
        super().__init__(title, year, owner, age_restriction)

    def details(self):
        return f"Thriller - Title:{self.title}, Year:{self.year}," \
               f" Age restriction:{self.age_restriction}, Likes:{self.likes}, Owned by:{self.owner.username}"
