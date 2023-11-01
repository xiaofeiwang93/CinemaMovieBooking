from datetime import datetime
from Models.Bookings.Booking import Booking
from Models.Payments.Coupon import Coupon
from Services.DbService import DbService
from ViewModels.BookingViewModel import BookingViewModel


class BookingService:
    def save_booking(booking: Booking):
        """!
        Save a booking to the database.

        @param booking: The booking to be saved.
        """
        DbService.add_record(DbService.bookingDbName, booking.to_dict(), DbService.bookingDbNameColumns)

    def view_booking_list():
        """!
        View bookings from the database.

        @param 
        @return: A List of Booking model object representing the booking.
        """
        booking = DbService.read_all_records(DbService.bookingDbName)

        print(f"booking: {booking}")
        return booking

    def process_payment():
        """!
        Make payment for the booking. In this case, we just print a message and return True. In a real application, we would use a payment gateway to process the payment.

        @param booking: The booking to be paid for.
        @return: A Booking object representing the booking.
        """

        print("Payment made")
        return True
    
    def check_coupon(couponid):
        """!
        Check if the coupon is valid.

        @param coupon: The coupon to be checked.
        @return: Coupon model object if the coupon is valid, None otherwise.
        """

        return DbService.validate_coupon(couponid)