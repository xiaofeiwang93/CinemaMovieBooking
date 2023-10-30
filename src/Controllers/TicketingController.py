from datetime import datetime
from typing import List

from flask import jsonify, render_template, request
from Models.Bookings.Booking import Booking
from Models.Movies.Movie import Movie
from Models.Movies.Screening import Screening

class MovieTicketController:
    def __init__(self, db_service, login_service, common_service, movie_service) -> None:
        """!
        Constructor for the MovieTicketController class. Implement the Inversion of Control (IoC) principle here via Dependency Injection - constructor injection.

        :param ticket_system: An instance of the MovieTicketSystem.
        """
        self.db_service = db_service
        self.login_service = login_service
        self.common_service = common_service
        self.movie_service = movie_service

    def login(self):
        self.login_service.login()
        return render_template('Common/login_view.html')
    
    def home(self):
        """!
        home page

        :param ticket_system: None.
        """
        movie_list = self.movie_service.get_all_movies()
        return render_template('home.html', movie_list=movie_list)

    def view_movie_list(self):
        movie_list = self.movie_service.get_all_movies()
        booking_dates = self.common_service.generate_booking_dates()

        return render_template('./Movies/movie_list.html', movie_list=movie_list, booking_dates=booking_dates, current_date=booking_dates["Today"])
    
    def view_movie_detail(self, movie_id: int):
        """!
        Search for movies based on id.

        :param id: The id of the movie.
        :return: A Movie objects matching the id.

        """
        movie = self.movie_service.search_movie_by_id(movie_id)
        booking_dates = self.common_service.generate_booking_dates()

        return render_template('./Movies/movie_detail.html', movie=movie, booking_dates=booking_dates, current_date=booking_dates["Today"])

    def search_movie_by_screening_date(self):
        """!
        Search for screening based on screening date.

        :param date: The date of the movie to search for.
        :return: List of Movie objects matching the search criteria.
        """

        movieid = request.args.get('movieid')
        date = request.args.get('date')

        movie = self.movie_service.search_movie_by_id(movieid)
        booking_dates = self.common_service.generate_booking_dates()
        current_date = booking_dates["Today"]
        screening_list = self.movie_service.search_movie_by_screening_date(booking_dates[date], movieid)
        movie.screening_list = screening_list

        if movieid and date:
            current_date = booking_dates[date]
        
        return render_template('./Movies/movie_detail.html', movie=movie, screening_list=screening_list, booking_dates=booking_dates, current_date=current_date)
        
    def search_movie_list_by_screening_date(self):
        """!
        Search for list of screening based on screening date.

        :param date: The date of the movie to search for.
        :return: List of Movie objects matching the search criteria -- only return the movies that have screening for the selected date.
        """

        date = request.args.get('date')

        movie_list = self.movie_service.get_all_movies()
        booking_dates = self.common_service.generate_booking_dates()

        for movie in movie_list:
            screening_list = self.movie_service.search_movie_by_screening_date(booking_dates[date], movie.id)
            movie.screening_list = screening_list

        # remove movie with no screening
        movie_list = [movie for movie in movie_list if movie.screening_list != []]
        
        if date:
            current_date = booking_dates[date]
        
        return render_template('./Movies/movie_list.html', movie_list=movie_list, screening_list=screening_list, booking_dates=booking_dates, current_date=current_date)
        
    def search_movies(self):
        """!
        Search for movies based on title, language, genre, and release date.

        :param title: The title of the movie to search for.
        :param language: The language of the movie.
        :param genre: The genre of the movie.
        :param release_date: The release date of the movie.
        :return: List of Movie objects matching the search criteria.
        """

        movie = Movie()
        movie.title = request.form.get('titleSearch')
        movie.language = request.form.get('languageSearch')
        movie.genre = request.form.get('genreSearch')
        movie.release_date = request.form.get('releasedateSearch')

        movie_list = self.movie_service.search_movies(movie)
        booking_dates = self.common_service.generate_booking_dates()
        
        return render_template('./Movies/movie_list.html', movie_list=movie_list, booking_dates=booking_dates)
    
    def search_movies_by_title(self):
        """!
        Search for movies based on title.

        :param title: The title of the movie to search for.
        :return: List of Movie objects matching the search criteria.
        """

        title = request.form.get('search')

        movie_list = self.movie_service.search_movies_by_title(title)
        booking_dates = self.common_service.generate_booking_dates()
        
        return render_template('./Movies/movie_list.html', movie_list=movie_list, booking_dates=booking_dates)

    def book_tickets(self):
        """!
        Book tickets for a movie on behalf of a customer.

        :param movie_title: The title of the movie to book.
        :param customer_name: The name of the customer making the booking.
        :param seats: List of seat numbers to book.
        :return: A Booking object representing the booking.
        """
        movie_id = request.args.get('movieid')
        date = request.args.get('date')
        start_time = request.args.get('starttime')

        print(movie_id)
        print(date)
        print(start_time)
        #booking = self.movie_service.book_tickets(movie_id, customer_name, seats, screening_id)

        if request.method=="POST":
            print("Back here")
            selected_seats = request.get_json()
            print(selected_seats)

        return render_template('./Booking/booking.html')

    def get_available_seats(self, movie_title: str) -> List[int]:
        """!
        Get a list of available seats for a specific movie.

        :param movie_title: The title of the movie for which to retrieve available seats.
        :return: List of available seat numbers.
        """
        pass

    def get_customer_bookings(self, customer_name: str) -> List[Booking]:
        """!
        Get a list of bookings made by a specific customer.

        :param customer_name: The name of the customer for whom to retrieve bookings.
        :return: List of Booking objects made by the customer.
        """
        pass

    def cancel_booking(self, booking: Booking) -> None:
        
        """!
        Cancel a booking and provide a refund to the customer.

        :param booking: The booking to be canceled.
        """
        pass