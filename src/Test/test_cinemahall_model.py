from Models.CinemaHalls.CinemaHall import CinemaHall


def test_cinema_hall_properties():
    # Create an instance of the CinemaHall class
    cinema_hall = CinemaHall(name="Hall A", total_seats=100, list_of_seats=[1, 2, 3])

    # Test the name property
    assert cinema_hall.name == "Hall A"
    cinema_hall.name = "Hall B"
    assert cinema_hall.name == "Hall B"

    # Test the total_seats property
    assert cinema_hall.total_seats == 100
    cinema_hall.total_seats = 150
    assert cinema_hall.total_seats == 150

    # Test the list_of_seats property
    assert cinema_hall.list_of_seats == [1, 2, 3]
    cinema_hall.list_of_seats = [4, 5, 6]
    assert cinema_hall.list_of_seats == [4, 5, 6]

# Run the test if this script is executed
if __name__ == "__main__":
    test_cinema_hall_properties()
