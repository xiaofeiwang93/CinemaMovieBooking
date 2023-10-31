from Services.DbService import DbService


class BookingService:
    def save_booking(self, booking):
        """!
        Save a booking to the database.

        :param booking: The booking to be saved.
        """
        DbService.add_record(DbService.bookingDbName, booking, DbService.bookingDbNameColumns)

    def make_payment():
        """!
        Make payment for the booking.

        :param booking: The booking to be paid for.
        :return: A Booking object representing the booking.
        """

        print("Payment made")
        return None