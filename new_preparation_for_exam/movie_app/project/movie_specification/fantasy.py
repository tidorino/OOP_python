from project.movie_specification.movie import Movie


class Fantasy(Movie):

    DEFAULT_AGE_RESTRICTION = 6

    def __init__(self, title, year, owner, age_restriction=6):
        super().__init__(title, year, owner, age_restriction)

    @property
    def age_restriction(self):
        return self.__age_restriction

    @age_restriction.setter
    def age_restriction(self, value):
        if value < 6:
            raise ValueError(f'{self.type} movies must be restricted'
                             f' for audience under {self.age_restriction} years!')

        self.__age_restriction = value

    @property
    def type(self):
        return 'Fantasy'

    def details(self):
        return f'{self.type} - ' \
               f'Title:{self.title}, Year:{self.year},' \
               f' Age restriction:{self.age_restriction}, Likes:{self.likes},' \
               f' Owned by:{self.owner.username}'
