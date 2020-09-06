from domainmodel.genre import Genre
from domainmodel.actor import Actor
from domainmodel.director import Director


class Movie:

    def __init__(self, title: str, release_year: int):
        self.__genres = list()
        self.__actors = list()
        self.__release_year = None
        self.__title = None
        self.__description = None
        self.__runtime_minutes = 0
        self.__favourite = False

        if title != "" and type(title) is str:
            self.__title = title.strip()

        if release_year >= 1900 or type(release_year) is int:
            self.__release_year = release_year

    @property
    def title(self) -> str:
        return self.__title

    @property
    def release_year(self) -> int:
        return self.__release_year

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description):
        if type(description) is str:
            self.__description = description.strip()

    @property
    def actors(self) -> list:
        return self.__actors

    @actors.setter
    def actors(self, actors):
        if type(actors) is list:
            self.__actors = actors

    @property
    def genres(self) -> list:
        return self.__genres

    @genres.setter
    def genres(self, genres):
        if type(genres) is list:
            self.__genres = genres

    @property
    def runtime_minutes(self) -> int:
        return self.__runtime_minutes

    @runtime_minutes.setter
    def runtime_minutes(self, runtime_minutes):
        if type(runtime_minutes) is int:
            if runtime_minutes <= 0:
                raise ValueError

            self.__runtime_minutes = runtime_minutes

    @property
    def favourite(self) -> bool:
        return self.__favourite

    def __repr__(self):
        return f"<Movie {self.__title}, {self.__release_year}>"

    def __eq__(self, other):
        return (self.__title, self.__release_year) == (other.__title, other.__release_year)

    def __hash__(self):
        return hash((self.__title, self.__release_year))

    def __lt__(self, other):
        return (self.__title, self.__release_year) < (other.__title, other.__release_year)

    def add_actor(self, actor):
        if type(actor) is Actor:
            self.__actors.append(actor)

    def remove_actor(self, actor):
        if type(actor) is Actor:
            if actor in self.__actors:
                self.__actors.remove(actor)

    def add_genre(self, genre):
        if type(genre) is Genre:
            self.__genres.append(genre)

    def remove_genre(self, genre):
        if type(genre) is Genre:
            if genre in self.__genres:
                self.__genres.remove(genre)

    def add_favourite(self):
        self.__favourite = True

    def remove_favourite(self):
        self.__favourite = False
