class CinemaHallSeat:
    def __init__(self, seat_number, seat_column, seat_type, is_reserved, seat_price):
        self.__seat_number = seat_number
        self.__seat_column = seat_column
        self.__seat_type = seat_type
        self.__is_reserved = is_reserved
        self.__seat_price = seat_price

    # Getter and setter for seat_number
    @property
    def seat_number(self):
        return self.__seat_number

    @seat_number.setter
    def seat_number(self, value):
        self.__seat_number = value

    # Getter and setter for seat_column
    @property
    def seat_column(self):
        return self.__seat_column

    @seat_column.setter
    def seat_column(self, value):
        self.__seat_column = value

    # Getter and setter for seat_type
    @property
    def seat_type(self):
        return self.__seat_type

    @seat_type.setter
    def seat_type(self, value):
        self.__seat_type = value

    # Getter and setter for is_reserved
    @property
    def is_reserved(self):
        return self.__is_reserved

    @is_reserved.setter
    def is_reserved(self, value):
        self.__is_reserved = value

    # Getter and setter for seat_price
    @property
    def seat_price(self):
        return self.__seat_price

    @seat_price.setter
    def seat_price(self, value):
        self.__seat_price = value

