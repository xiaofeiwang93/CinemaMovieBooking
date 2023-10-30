from typing import List
from Models.Movies.Movie import Movie
from Services.DbService import DbService
from ViewModels.MovieViewModel import MovieViewModel
from ViewModels.ScreeningViewModel import ScreeningViewModel

class MovieService:
    def get_all_movies() -> List[MovieViewModel]:
        """!
        Get a list of all movies.

        :return: List of Movie View Model.
        """
        movie_view_models = []

        movie_list = DbService.read_all_records(DbService.movieDbName)

        for movie_info in movie_list:
            movie_view_model = MovieService.map_movie_view_model(movie_info)

            MovieService.get_movie_media(movie_view_model.id, movie_view_model)
            MovieService.get_movie_screenings(movie_view_model.id, movie_view_model)

            movie_view_models.append(movie_view_model)

        return movie_view_models
    
    def get_movie_media(movie_id: int, movie_view_model: MovieViewModel) -> None:
        """!
        Add media address to MovieViewModel.

        :return: List of Movie View Model.
        """
        movie_media = DbService.search_record_by_id(movie_id, DbService.movieMediaDbName)
        MovieService.map_movie_media_view_model(movie_media, movie_view_model)
    
    def get_movie_screenings(movie_id: int, movie_view_model: MovieViewModel) -> None:
        """!
        Add screenings to MovieViewModel.

        :return: List of Movie View Model.
        """
        movie_screenings = DbService.search_record_by_id(movie_id, DbService.screeningDbName)
        MovieService.map_movie_screening_view_model(movie_screenings, movie_view_model)

    def search_movie_by_id(movie_id: int) -> MovieViewModel:
        """!
        Get a movie by ID.

        :return: Movie View Model.
        """
        movie = DbService.search_record_by_id(movie_id, DbService.movieDbName)

        movie_view_model = MovieService.map_movie_view_model(movie)
        MovieService.get_movie_screenings(movie_view_model.id, movie_view_model)

        MovieService.get_movie_media(movie_id, movie_view_model)

        return movie_view_model

    def search_movies(movie_search: Movie) -> List[MovieViewModel]:
        """!
        Search for movies based on title, language, genre, and release date.

        :param movie_search: The Movie object containing the search criteria.
        :return: List of Movie View Model objects matching the search criteria.
        """
        movie_view_models = []

        movie_list = DbService.search_records_by_multiple_attributes(DbService.movieDbName, movie_search)

        for movie_info in movie_list:
            movie_view_model = MovieService.map_movie_view_model(movie_info)

            MovieService.get_movie_media(movie_view_model.id, movie_view_model)
            MovieService.get_movie_screenings(movie_view_model.id, movie_view_model)

            movie_view_models.append(movie_view_model)

        return movie_view_models

    def search_movies_by_title(title: str) -> List[MovieViewModel]:
        """!
        Search for movies based on title.

        :param title: The title of the movie to search for.
        :return: List of Movie View Model objects matching the search criteria.
        """
        movie_view_models = []

        movie_list = DbService.search_records_by_attribute('title', title, DbService.movieDbName)

        for movie_info in movie_list:
            movie_view_model = MovieService.map_movie_view_model(movie_info)

            MovieService.get_movie_media(movie_view_model.id, movie_view_model)
            MovieService.get_movie_screenings(movie_view_model.id, movie_view_model)

            movie_view_models.append(movie_view_model)

        return movie_view_models

    def search_movie_by_screening_date(date: str, movieid: int) -> List[ScreeningViewModel]:
        """!
        Search for screening based on screening date.

        :param date: The date of the movie to search for.
        :return: List of Movie View Model objects matching the search criteria.
        """
        screening_list = []

        screening_data_list = DbService.search_records_by_attribute('date', date, DbService.screeningDbName)

        for screening_data in screening_data_list:
            if movieid != None and movieid != '':
                if screening_data.get('movieid') == movieid:
                    screening = ScreeningViewModel()
                    screening.id = screening_data.get('id')
                    screening.movieid = screening_data.get('movieid')
                    screening.date = screening_data.get('date')
                    screening.starttime = screening_data.get('starttime')
                    screening.endtime = screening_data.get('endtime')
                    screening.hallid = screening_data.get('hallid')
            
                    screening_list.append(screening)

        return screening_list if bool(screening_list) else []

    def map_movie_view_model(movie_info) -> List[MovieViewModel]:
        """!
        Map the movie_list from dictionary into movie view model.

        :return: List of Movie View Model.
        """

        movie = MovieViewModel()
        movie.id = movie_info.get('id')
        movie.title = movie_info.get('title')
        movie.description = movie_info.get('description')
        movie.duration_mins = movie_info.get('duration_mins')
        movie.language = movie_info.get('language')
        movie.release_date = movie_info.get('release_date')
        movie.country = movie_info.get('country')
        movie.genre = movie_info.get('genre')

        return movie
    
    def map_movie_media_view_model(movie_media, movie_view_model) -> None:
        """!
        Map the movie_media_list from dictionary into movie view model.

        :return: None.
        """
        movie_view_model.cardsrcaddress = movie_media.get('cardsrcaddress')
        movie_view_model.detailbanneraddress = movie_media.get('detailbanneraddress')
    
    def map_movie_screening_view_model(movie_screenings, movie_view_model) -> None:
        """!
        Map the screening_list from dictionary into movie view model.

        :return: None.
        """
        ScreenViewModel = ScreeningViewModel()
        ScreenViewModel.id = movie_screenings.get('id')
        ScreenViewModel.movieid = movie_screenings.get('movieid')
        ScreenViewModel.date = movie_screenings.get('date')
        ScreenViewModel.starttime = movie_screenings.get('starttime')
        ScreenViewModel.endtime = movie_screenings.get('endtime')
        ScreenViewModel.hallid = movie_screenings.get('hallid')

        movie_view_model.screening_list.append(ScreenViewModel)

