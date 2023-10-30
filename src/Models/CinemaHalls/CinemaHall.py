class CinemaHall:
    def __init__(self, name, total_seats, list_of_seats):
        self.__name = name
        self.__total_seats = total_seats
        self.__list_of_seats = list_of_seats

    # Getter and setter for name
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    # Getter and setter for total_seats
    @property
    def total_seats(self):
        return self.__total_seats

    @total_seats.setter
    def total_seats(self, value):
        self.__total_seats = value

    # Getter and setter for list_of_seats
    @property
    def list_of_seats(self):
        return self.__list_of_seats

    @list_of_seats.setter
    def list_of_seats(self, value):
        self.__list_of_seats = value
