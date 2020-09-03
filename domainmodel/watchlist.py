from domainmodel.movie import Movie


class WatchList:

    def __init__(self):
        self.__watchlist = list()

    def __repr__(self):
        return str(self.__watchlist)

    def __getitem__(self, index):
        return self.__watchlist[index]

    def __iter__(self):
        self.__index = 0
        return iter(self.__watchlist)

    def __next__(self):
        if self.__index < len(self.__watchlist):
            return self.__watchlist[self.__index]

        self.__index += 1
        raise StopIteration

    @property
    def watchlist(self) -> list:
        return self.__watchlist

    @watchlist.setter
    def watchlist(self, watchlist: list):
        if type(watchlist) is list:
            self.__watchlist = watchlist

    def add_movie(self, movie: Movie):
        if type(movie) is Movie:
            if movie not in self.__watchlist:
                self.__watchlist.append(movie)

    def remove_movie(self, movie: Movie):
        if type(movie) is Movie:
            if movie in self.watchlist:
                self.__watchlist.remove(movie)

    def select(self, index: int):
        if type(index) is int and 0 <= index < len(self.__watchlist):
            return self.__watchlist[index]

    def size(self):
        return len(self.__watchlist)

    def first(self):
        if len(self.__watchlist) != 0:
            return self.__watchlist[0]