from Models.CinemaHalls.CinemaHallSeat import CinemaHallSeat


def test_cinema_hall_seat_properties():
    # Create an instance of the CinemaHallSeat class
    cinema_hall_seat = CinemaHallSeat(
        seat_number=1, seat_column="A", seat_type="Standard", is_reserved=False, seat_price=10.0
    )

    # Test the seat_number property
    assert cinema_hall_seat.seat_number == 1
    cinema_hall_seat.seat_number = 2
    assert cinema_hall_seat.seat_number == 2

    # Test the seat_column property
    assert cinema_hall_seat.seat_column == "A"
    cinema_hall_seat.seat_column = "B"
    assert cinema_hall_seat.seat_column == "B"

    # Test the seat_type property
    assert cinema_hall_seat.seat_type == "Standard"
    cinema_hall_seat.seat_type = "VIP"
    assert cinema_hall_seat.seat_type == "VIP"

    # Test the is_reserved property
    assert not cinema_hall_seat.is_reserved
    cinema_hall_seat.is_reserved = True
    assert cinema_hall_seat.is_reserved

    # Test the seat_price property
    assert cinema_hall_seat.seat_price == 10.0
    cinema_hall_seat.seat_price = 12.5
    assert cinema_hall_seat.seat_price == 12.5

# Run the test if this script is executed
if __name__ == "__main__":
    test_cinema_hall_seat_properties()
