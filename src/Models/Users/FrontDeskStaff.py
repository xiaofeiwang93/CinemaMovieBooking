from Models.User import User


class FrontDeskStaff(User):
    def __init__(self, username, email):
        super().__init__(username, email)

    def login(self):
        # Implement login logic for front desk staff
        pass

    def logout(self):
        # Implement logout logic for front desk staff
        pass

    def makeBooking(self):
        # Implement the makeBooking method for front desk staff
        # This method may require additional parameters to specify the booking details
        # Perform the booking logic and return True if successful, else return False
        pass

    def cancelBooking(self):
        # Implement the cancelBooking method for front desk staff
        # This method may require a booking ID or other details to cancel a booking
        # Perform the cancellation logic and return True if successful, else return False
        pass