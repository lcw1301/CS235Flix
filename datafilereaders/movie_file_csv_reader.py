import csv

from domainmodel.movie import Movie
from domainmodel.actor import Actor
from domainmodel.genre import Genre
from domainmodel.director import Director


class MovieFileCSVReader:

    def __init__(self, file_name: str):
        self.__file_name = file_name
        self.dataset_of_movies = list()
        self.dataset_of_actors = set()
        self.dataset_of_directors = set()
        self.dataset_of_genres = set()

    def read_csv_file(self):
        with open(self.__file_name, mode='r', encoding='utf-8-sig') as csvfile:
            movie_file_reader = csv.DictReader(csvfile)

            for row in movie_file_reader:
                title = row['Title']
                release_year = int(row['Year'])
                actors = row['Actors']
                genres = row['Genre']
                director = row['Director']
                runtime_minutes = row['Runtime (Minutes)']
                rating = row['Rating']
                votes = row['Votes']
                revenue = row['Revenue (Millions)']
                metascore = row['Metascore']

                for actor in actors.split(','):
                    self.dataset_of_actors.add(Actor(actor.strip()))

                for genre in genres.split(','):
                    self.dataset_of_genres.add(Genre(genre.strip()))

                self.dataset_of_movies.append(Movie(title.strip(), release_year))
                self.dataset_of_directors.add(Director(director.strip()))
