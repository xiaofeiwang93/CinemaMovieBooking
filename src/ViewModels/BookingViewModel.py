class BookingViewModel:
    def __init__(self):
        self._id = None
        self._movie = None
        self._customer = None
        self._hall = None
        self._screening = None
        self._seat_list = None
        self._seat_count = None
        self._total_price = None
    
    @property
    def id(self):
        """!
        @brief Getter for the booking's ID property.

        @return The ID of the booking.
        """
        return self._id
    
    @id.setter
    def id(self, value):
        """!
        @brief Setter for the booking's ID property.

        @param value: The ID of the booking.
        """
        self._id = value

    @property
    def movie(self):
        """!
        @brief Getter for the booking's movie property.

        @return The movie of the booking.
        """
        return self._movie
    
    @movie.setter
    def movie(self, value):
        """!
        @brief Setter for the booking's movie property.

        @param value: The movie of the booking.
        """
        self._movie = value

    @property
    def customer(self):
        """!
        @brief Getter for the booking's customer property.

        @return The customer of the booking.
        """
        return self._customer
    
    @customer.setter
    def customer(self, value):
        """!
        @brief Setter for the booking's customer property.

        @param value: The customer of the booking.
        """
        self._customer = value

    @property
    def hall(self):
        """!
        @brief Getter for the booking's hall property.

        @return The hall of the booking.
        """
        return self._hall
    
    @hall.setter
    def hall(self, value):
        """!
        @brief Setter for the booking's hall property.

        @param value: The hall of the booking.
        """
        self._hall = value

    @property
    def screening(self):
        """!
        @brief Getter for the booking's screening property.

        @return The screening of the booking.
        """
        return self._screening
    
    @screening.setter
    def screening(self, value):
        """!
        @brief Setter for the booking's screening property.

        @param value: The screening of the booking.
        """
        self._screening = value

    @property
    def seat_list(self):
        """!
        @brief Getter for the booking's seat_list property.

        @return The seat_list of the booking.
        """
        return self._seat_list
    
    @seat_list.setter
    def seat_list(self, value):
        """!
        @brief Setter for the booking's seat_list property.

        @param value: The seat_list of the booking.
        """
        self._seat_list = value
    
    @property
    def seat_count(self):
        """!
        @brief Getter for the booking's seat_count property.

        @return The seat_count of the booking.
        """
        return self._seat_count
    
    @seat_count.setter
    def seat_count(self, value):
        """!
        @brief Setter for the booking's seat_count property.

        @param value: The seat_count of the booking.
        """
        self._seat_count = value

    @property
    def total_price(self):
        """!
        @brief Getter for the booking's total_price property.

        @return The total_price of the booking.
        """
        return self._total_price
    
    @total_price.setter
    def total_price(self, value):
        """!
        @brief Setter for the booking's total_price property.

        @param value: The total_price of the booking.
        """
        self._total_price = value
    
    def __str__(self):
        """!
        @brief String representation of the BookingViewModel object.

        @return String representation of the BookingViewModel object.
        """
        return f"BookingViewModel: [id: {self._id}, movie: {self._movie}, customer: {self._customer}, hall: {self._hall}, screening: {self._screening}, seat_list: {self._seat_list}]"