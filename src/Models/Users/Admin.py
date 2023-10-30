from Models.User import User


class Admin(User):
    def __init__(self, username, email):
        super().__init__(username, email)

    def login(self):
        # Implement login logic for admin
        pass

    def logout(self):
        # Implement logout logic for admin
        pass

    def addMovie(self):
        # Implement the addMovie method
        # This method may require additional parameters to specify movie details
        # Perform the movie addition logic and return True if successful, else return False
        pass

    def makeBooking(self):
        # Implement the makeBooking method for admin
        # This method may require additional parameters to specify booking details
        # Perform the booking logic and return True if successful, else return False
        pass

    def addScreening(self):
        # Implement the addScreening method for admin
        # This method may require additional parameters to specify screening details
        # Perform the screening addition logic and return True if successful, else return False
        pass

    def cancelBooking(self):
        # Implement the cancelBooking method for admin
        # This method may require a booking ID or other details to cancel a booking
        # Perform the cancellation logic and return True if successful, else return False
        pass

    def cancelMovie(self):
        # Implement the cancelMovie method for admin
        # This method may require a movie ID or other details to cancel a movie
        # Perform the movie cancellation logic and return True if successful, else return False
        pass

    def cancelScreening(self):
        # Implement the cancelScreening method for admin
        # This method may require a screening ID or other details to cancel a screening
        # Perform the screening cancellation logic and return True if successful, else return False
        pass