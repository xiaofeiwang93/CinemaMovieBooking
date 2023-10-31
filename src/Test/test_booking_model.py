from datetime import date
import pytest
from Models.Bookings.Booking import Booking

def test_booking_properties():
    # Create a Booking instance
    booking = Booking()

    # Set values for the properties
    booking.movieid = 1
    booking.screeningid = 2
    booking.hallid = 3
    booking.customerid = 4

    # Check if the properties return the correct values
    assert booking.movieid == 1
    assert booking.screeningid == 2
    assert booking.hallid == 3
    assert booking.customerid == 4

def test_booking_to_dict():
    # Create a Booking instance
    booking = Booking()
    booking.movieid = 1
    booking.screeningid = 2
    booking.hallid = 3
    booking.customerid = 4

    # Convert the booking to a dictionary
    booking_dict = booking.to_dict()

    # Check if the dictionary contains the correct values
    assert booking_dict == {
        "movieid": 1,
        "screeningid": 2,
        "hallid": 3,
        "customerid": 4
    }

def test_booking_string_representation():
    # Create a Booking instance
    booking = Booking()
    booking.movieid = 1
    booking.screeningid = 2
    booking.hallid = 3
    booking.customerid = 4

    # Get the string representation of the booking
    booking_str = str(booking)

    # Check if the string representation is in the expected format
    assert booking_str == "Movie: 1\nScreening: 2\nHall: 3\nCustomer: 4"

if __name__ == "__main__":
    pytest.main()
