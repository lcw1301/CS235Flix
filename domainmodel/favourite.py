from domainmodel.movie import Movie


class Favourite:

    def __init__(self):
        self.__favourite_movies = list()

    def __repr__(self):
        return str(self.__favourite_movies)

    def __getitem__(self, index):
        return self.__favourite_movies[index]

    def __iter__(self):
        self.__index = 0
        return iter(self.__favourite_movies)

    def __next__(self):
        if self.__index < len(self.__favourite_movies):
            return self.__favourite_movies[self.__index]

        self.__index += 1
        raise StopIteration

    @property
    def favourite_movies(self) -> list:
        return self.__favourite_movies

    def size(self):
        return len(self.__favourite_movies)

    def add_favourite(self, movie: Movie):
        if type(movie) is Movie:
            if movie not in self.__favourite_movies:
                movie.add_favourite()
                self.__favourite_movies.append(movie)

    def remove_favourite(self, movie: Movie):
        if type(movie) is Movie:
            if movie in self.__favourite_movies:
                movie.remove_favourite()
                self.__favourite_movies.remove(movie)
