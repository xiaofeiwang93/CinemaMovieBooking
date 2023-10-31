from Models.Movies.Movie import Movie
from Services.DbService import DbService


class AdminServce:
    def add_movie(movie: Movie):
        """!
        Add a movie to the database.

        :param movie: The movie to be added.
        """

        is_movie_added = DbService.add_record(DbService.movieDbName, movie.to_dict(), DbService.movieDbColumns)
        is_movie_media_added = DbService.add_record(DbService.movieMediaDbName, movie.to_dict(), DbService.movieMediaDbColumns)

        return 