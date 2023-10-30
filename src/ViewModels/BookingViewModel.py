class BookingViewModel:
    def __init__(self):
        self._id = None
        self._movie = None
        self._customer = None
        self._hall = None
        self._screening = None
        self._seat_list = None
    
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
    
    def __str__(self):
        """!
        @brief String representation of the BookingViewModel object.

        @return String representation of the BookingViewModel object.
        """
        return f"BookingViewModel: [id: {self._id}, movie: {self._movie}, customer: {self._customer}, hall: {self._hall}, screening: {self._screening}, seat_list: {self._seat_list}]"