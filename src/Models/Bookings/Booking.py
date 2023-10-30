from datetime import date

class Booking:
    def __init__(self, booking_num, customer, number_of_seats, created_on, status, screening_seat_info, screening_detail, seats, order_total):
        self.__booking_num = booking_num
        self.__customer = customer
        self.__number_of_seats = number_of_seats
        self.__created_on = created_on
        self.__status = status
        self.__screening_seat_info = screening_seat_info
        self.__screening_detail = screening_detail
        self.__seats = seats
        self.__order_total = order_total

    # Getter and setter for booking_num
    @property
    def booking_num(self):
        return self.__booking_num

    @booking_num.setter
    def booking_num(self, value):
        self.__booking_num = value

    # Getter and setter for customer
    @property
    def customer(self):
        return self.__customer

    @customer.setter
    def customer(self, value):
        self.__customer = value

    # Getter and setter for number_of_seats
    @property
    def number_of_seats(self):
        return self.__number_of_seats

    @number_of_seats.setter
    def number_of_seats(self, value):
        self.__number_of_seats = value

    # Getter and setter for created_on
    @property
    def created_on(self):
        return self.__created_on

    @created_on.setter
    def created_on(self, value):
        self.__created_on = value

    # Getter and setter for status
    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value

    # Getter and setter for screening_seat_info
    @property
    def screening_seat_info(self):
        return self.__screening_seat_info

    @screening_seat_info.setter
    def screening_seat_info(self, value):
        self.__screening_seat_info = value

    # Getter and setter for screening_detail
    @property
    def screening_detail(self):
        return self.__screening_detail

    @screening_detail.setter
    def screening_detail(self, value):
        self.__screening_detail = value

    # Getter and setter for seats
    @property
    def seats(self):
        return self.__seats

    @seats.setter
    def seats(self, value):
        self.__seats = value

    # Getter and setter for order_total
    @property
    def order_total(self):
        return self.__order_total

    @order_total.setter
    def order_total(self, value):
        self.__order_total = value

    def sendNotification(self):
        # Implement the sendNotification method
        # This method may send a notification to the customer regarding the booking
        # You can customize the notification logic based on your requirements
        pass
