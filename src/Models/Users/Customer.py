from Models.User import User


class Customer(User):
    def __init__(self, username, email):
        super().__init__(username, email)
        self.__bookingList = []
        self.__notificationList = []

    @property
    def bookingList(self):
        return self.__bookingList

    @property
    def notificationList(self):
        return self.__notificationList

    def makeBooking(self):
        # Implement the makeBooking method
        booking = Booking()  # Create a Booking object (you should define the Booking class)
        self.__bookingList.append(booking)
        return True  # Return True if booking is successful

    def cancelBooking(self):
        # Implement the cancelBooking method
        # You should define the Booking class and its attributes for proper cancellation
        if len(self.__bookingList) > 0:
            canceled_booking = self.__bookingList.pop()
            return True  # Return True if booking is canceled
        return False  # Return False if booking not found

    def getBookingList(self):
        # Implement the getBookingList method
        return self.__bookingList
