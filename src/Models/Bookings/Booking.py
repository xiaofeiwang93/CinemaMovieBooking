from datetime import date

class Booking:
    def __init__(self):
        self.__movieid = None
        self.__screeningid = None
        self.__hallid = None
        self.__customerid = None
    
    @property
    def movieid(self):
        """!
        @brief Getter for the booking's movie ID property.

        @return The movie ID of the booking.
        """
        return self.__movieid
    
    @movieid.setter
    def movieid(self, value):
        """!
        @brief Setter for the booking's movie ID property.

        @param value: The movie ID of the booking.
        """
        self.__movieid = value

    @property
    def screeningid(self):
        """!
        @brief Getter for the booking's screening ID property.

        @return The screening ID of the booking.
        """
        return self.__screeningid
    
    @screeningid.setter
    def screeningid(self, value):
        """!
        @brief Setter for the booking's screening ID property.

        @param value: The screening ID of the booking.
        """
        self.__screeningid = value


    @property
    def hallid(self):
        """!
        @brief Getter for the booking's hall ID property.

        @return The hall ID of the booking.
        """
        return self.__hallid
    
    @hallid.setter
    def hallid(self, value):
        """!
        @brief Setter for the booking's hall ID property.

        @param value: The hall ID of the booking.
        """
        self.__hallid = value

    @property
    def customerid(self):
        """!
        @brief Getter for the booking's customer ID property.

        @return The customer ID of the booking.
        """
        return self.__customerid
    
    @customerid.setter
    def customerid(self, value):
        """!
        @brief Setter for the booking's customer ID property.

        @param value: The customer ID of the booking.
        """
        self.__customerid = value

    def to_dict(self):
                """!
                @brief Convert the booking object to a dictionary.

                @return A dictionary containing the booking's details.
                """
                return {
                    "movieid": self.movieid,
                    "screeningid": self.screeningid,
                    "hallid": self.hallid,
                    "customerid": self.customerid
                }

    def __str__(self):
        """!
        @brief String representation of the booking.

        @return A string containing the booking's details.
        """
        return f"Movie: {self.movieid}\nScreening: {self.screeningid}\nHall: {self.hallid}\nCustomer: {self.customerid}"
    
