from datetime import datetime
from typing import List

from flask import jsonify, redirect, render_template, request, url_for
from Models.Bookings.Booking import Booking
from Models.Movies.Movie import Movie
from Models.Movies.Screening import Screening
from ViewModels.BookingViewModel import BookingViewModel

class MovieTicketController:
    def __init__(self, db_service, login_service, common_service, movie_service, booking_service, admin_service) -> None:
        """!
        Constructor for the MovieTicketController class. Implement the Inversion of Control (IoC) principle here via Dependency Injection - constructor injection.

        @param ticket_system: An instance of the MovieTicketSystem.
        """
        self.db_service = db_service
        self.login_service = login_service
        self.common_service = common_service
        self.movie_service = movie_service
        self.booking_service = booking_service
        self.admin_service = admin_service

    def login(self):
        self.login_service.login()
        return render_template('Common/login_view.html')
    
    def home(self):
        """!
        home page

        @param ticket_system: None.
        """
        movie_list = self.movie_service.get_all_movies()
        print(movie_list)
        return render_template('home.html', movie_list=movie_list)

    def view_movie_list(self):
        movie_list = self.movie_service.get_all_movies()
        booking_dates = self.common_service.generate_booking_dates()

        return render_template('./Movies/movie_list.html', movie_list=movie_list, booking_dates=booking_dates, current_date=booking_dates["Today"])
    
    def view_movie_detail(self, movie_id: int):
        """!
        Search for movies based on id.

        @param id: The id of the movie.
        @return: A Movie objects matching the id.

        """
        movie = self.movie_service.search_movie_by_id(movie_id)
        booking_dates = self.common_service.generate_booking_dates()

        return render_template('./Movies/movie_detail.html', movie=movie, booking_dates=booking_dates, current_date=booking_dates["Today"])

    def search_movie_by_screening_date(self):
        """!
        Search for screening based on screening date.

        @param date: The date of the movie to search for.
        @return: List of Movie objects matching the search criteria.
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

        @param date: The date of the movie to search for.
        @return: List of Movie objects matching the search criteria -- only return the movies that have screening for the selected date.
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

        @param title: The title of the movie to search for.
        @param language: The language of the movie.
        @param genre: The genre of the movie.
        @param release_date: The release date of the movie.
        @return: List of Movie objects matching the search criteria.
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

        @param title: The title of the movie to search for.
        @return: List of Movie objects matching the search criteria.
        """

        title = request.form.get('search')

        movie_list = self.movie_service.search_movies_by_title(title)
        booking_dates = self.common_service.generate_booking_dates()
        
        return render_template('./Movies/movie_list.html', movie_list=movie_list, booking_dates=booking_dates)

    def select_seats(self):
        """!
        Book tickets for a movie on behalf of a customer.

        @param movie_title: The title of the movie to book.
        @param customer_name: The name of the customer making the booking.
        @param seats: List of seat numbers to book.
        @return: A Booking object representing the booking.
        """

        booking_view_model = BookingViewModel()
        movie_id = request.args.get('movieid')
        screening_id = request.args.get('screeningid')

        movie = self.movie_service.search_movie_by_id(movie_id)
        screening = self.movie_service.search_screening_by_id(screening_id)
        
        booking_view_model.movie = movie
        booking_view_model.screening = screening
        
        seats = self.common_service.generate_seats()
        print(seats)

        return render_template('./Booking/select_seats.html', booking=booking_view_model, seats = seats)
        
    def checkout(self):
        """!
        Checkout as a customer

        @param movie_title: The title of the movie to book.
        @param customer_name: The name of the customer making the booking.
        @param seats: List of seat numbers to book.
        @return: A Booking object representing the booking.
        """
        
        selected_seats = []
        for key, value in request.form.items():
            selected_seats.append(key)

        booking_view_model = BookingViewModel()

        movie_id = request.args.get('movieid')
        screening_id = request.args.get('screeningid')

        movie = self.movie_service.search_movie_by_id(movie_id)
        screening = self.movie_service.search_screening_by_id(screening_id)

        booking_view_model.movie = movie
        booking_view_model.screening = screening
        booking_view_model.seats = selected_seats
        booking_view_model.seat_count = len(selected_seats)
        booking_view_model.total_price = len(selected_seats) * 10

        # convert from view model to model for db operation
        booking_model = Booking()
        booking_model.movieid = booking_view_model.movie.id
        booking_model.screeningid = booking_view_model.screening.id
        booking_model.hallid = booking_view_model.screening.hallid
        booking_model.customerid = 1
        self.booking_service.save_booking(booking_model)
        
        return render_template('./Booking/checkout.html', booking=booking_view_model)
    
    def make_payment(self):
        """!
        Make payment for the booking.

        @param booking: The booking to be paid for.
        @return: A Booking object representing the booking.
        """

        payment_method = request.form.get('payment_method')
        coupon_id = request.form.get('couponid')
        
        if coupon_id:
            check_coupon = self.booking_service.check_coupon(coupon_id)
        else:
            check_coupon = "Empty"
        
        print(check_coupon)
        
        if payment_method == 'credit_card':
            # Process credit card payment
            return render_template('./Payment/creditcard.html', check_coupon=check_coupon)
        elif payment_method == 'debit_card':
            # Process debit card payment
            return render_template('./Payment/debitcard.html', check_coupon=check_coupon)
        else:
            return render_template('./Booking/mybookings.html', payment_method='cash')
    
    def process_payment(self):
        """!
        Process payment for the booking.

        @param booking: The booking to be paid for.
        @return: A Booking object representing the booking.
        """
        payment_method = request.args.get('payment')
        is_payment_made = self.booking_service.process_payment()

        if is_payment_made:
            return render_template('./Booking/mybookings.html', payment_method=payment_method)

        else:
            return render_template('./Booking/mybookings.html', payment_method=payment_method)

    def my_bookings(self):
        """!
        View a list of bookings made by a customer.

        @param customer_name: The name of the customer for whom to retrieve bookings.
        @return: List of Booking objects made by the customer.
        """
        #booking_list = self.booking_service.get_customer_bookings("test")

        booking_list = self.booking_service.view_booking_list()
        print(booking_list)

        payment_method = request.args.get('payment')
        return render_template('./Booking/mybookings.html', payment_method=payment_method)

    def get_customer_bookings(self, customer_name: str) -> List[Booking]:
        """!
        Get a list of bookings made by a specific customer.

        @param customer_name: The name of the customer for whom to retrieve bookings.
        @return: List of Booking objects made by the customer.
        """
        pass

    def cancel_booking(self, booking: Booking) -> None:
        
        """!
        Cancel a booking and provide a refund to the customer.

        @param booking: The booking to be canceled.
        """
        pass

    def add_movie(self):
        """!
        Add a movie to the database.

        @param movie: The movie to be added.
        """
        #self.admin_service.add_movie(movie)

        movie = Movie()
        is_movie_added = False

        print(request.method)
        print("add movie")

        if request.method == 'POST':
            movie.title = request.form.get('title')
            movie.description = request.form.get('description')
            movie.duration = request.form.get('duration')
            movie.language = request.form.get('language')
            movie.release_date = request.form.get('releaseDate')
            movie.country = request.form.get('country')
            movie.genre = request.form.get('genre')

            print(movie)

            is_movie_added = self.admin_service.add_movie(movie)

        return render_template('./Admin/add_movie.html', is_movie_added=is_movie_added)