class ScreeningViewModel:
    """!
    @brief View model for representing cinema hall data.

    @param id: The ID of the movie.
    @param movieid: The id of the movie.
    @param date: The date of the screening.
    @param starttime: The start time of the screening.
    @param endtime: The end time of the screening.
    @param hallid: The id halls.
    """

    def __init__(self):
        """!
        @brief Constructor for the ScreeningViewModel class.
        Initializes all properties to None.
        """
        self._id = None
        self._movieid = None
        self._date = None
        self._starttime = None
        self._endtime = None
        self._hallid = None
    
    def __str__(self):
        return f"Screening ID: {self.id}\nMovie ID: {self.movieid}\nDate: {self.date}\n" \
            f"Start Time: {self.starttime}\nEnd Time: {self.endtime}\nHall ID: {self.hallid}"
    
    @property
    def id(self):
        """!
        @brief Getter for the Screening's ID property.

        @return The ID of the Screening.
        """
        return self._id
    
    @id.setter
    def id(self, value):
        """!
        @brief Setter for the Screening's ID property.

        @param value: The ID of the Screening.
        """
        self._id = value

    @property
    def movieid(self):
        """!
        @brief Getter for the Screening's movie ID property.

        @return The movie ID of the Screening.
        """
        return self._movieid
    
    @movieid.setter
    def movieid(self, value):
        """!
        @brief Setter for the Screening's movie ID property.

        @param value: The movie ID of the Screening.
        """
        self._movieid = value

    @property
    def date(self):
        """!
        @brief Getter for the Screening's date property.

        @return The date of the Screening.
        """
        return self._date

    @date.setter
    def date(self, value):
        """!
        @brief Setter for the Screening's date property.

        @param value: The date of the Screening.
        """
        self._date = value

    @property
    def starttime(self):
        """!
        @brief Getter for the Screening's start time property.

        @return The start time of the Screening.
        """
        return self._starttime
    
    @starttime.setter
    def starttime(self, value):
        """!
        @brief Setter for the Screening's start time property.

        @param value: The start time of the Screening.
        """
        self._starttime = value
    
    @property
    def endtime(self):
        """!
        @brief Getter for the Screening's end time property.

        @return The end time of the Screening.
        """
        return self._endtime
    
    @endtime.setter
    def endtime(self, value):
        """!
        @brief Setter for the Screening's end time property.

        @param value: The end time of the Screening.
        """
        self._endtime = value

    @property
    def hallid(self):
        """!
        @brief Getter for the Screening's hall ID property.

        @return The hall ID of the Screening.
        """
        return self._hallid
    
    @hallid.setter
    def hallid(self, value):
        """!
        @brief Setter for the Screening's hall ID property.

        @param value: The hall ID of the Screening.
        """
        self._hallid = value
