class MovieViewModel:
    """!
    @brief View model for representing movie data.

    @param id: The ID of the movie.
    @param title: The title of the movie.
    @param description: A brief description of the movie.
    @param duration_mins: The duration of the movie in minutes.
    @param language: The language of the movie.
    @param release_date: The release date of the movie.
    @param country: The country of origin for the movie.
    @param genre: The genre of the movie.
    @param cardsrcaddress: The source address for the movie's card image.
    @param detailbanneraddress: The source address for the movie's detail banner image.
    """

    def __init__(self):
        """!
        @brief Constructor for the MovieViewModel class.
        Initializes all properties to None.
        """
        self._id = None
        self._title = None
        self._description = None
        self._duration_mins = None
        self._language = None
        self._release_date = None
        self._country = None
        self._genre = None
        self._cardsrcaddress = None
        self._detailbanneraddress = None
        self._screening_list = []

    def __str__(self):
        return f"Movie ID: {self.id}\nTitle: {self.title}\nDescription: {self.description}\n" \
            f"Duration (mins): {self.duration_mins}\nLanguage: {self.language}\n" \
            f"Release Date: {self.release_date}\nCountry: {self.country}\n" \
            f"Genre: {self.genre}\nCard Source Address: {self.cardsrcaddress}\n" \
            f"Detail Banner Address: {self.detailbanneraddress}\n" \
            f"Screening List: {self.screening_list}" 

    @property
    def id(self):
        """!
        @brief Getter for the movie's ID property.

        @return The ID of the movie.
        """
        return self._id

    @id.setter
    def id(self, value):
        """!
        @brief Setter for the movie's ID property.

        @param value: The ID of the movie.
        """
        self._id = value

    @property
    def title(self):
        """!
        @brief Getter for the movie's title property.

        @return The title of the movie.
        """
        return self._title

    @title.setter
    def title(self, value):
        """!
        @brief Setter for the movie's title property.

        @param value: The title of the movie.
        """
        self._title = value

    @property
    def description(self):
        """!
        @brief Getter for the movie's description property.

        @return A brief description of the movie.
        """
        return self._description

    @description.setter
    def description(self, value):
        """!
        @brief Setter for the movie's description property.

        @param value: A brief description of the movie.
        """
        self._description = value

    @property
    def duration_mins(self):
        """!
        @brief Getter for the movie's duration property.

        @return The duration of the movie in minutes.
        """
        return self._duration_mins

    @duration_mins.setter
    def duration_mins(self, value):
        """!
        @brief Setter for the movie's duration property.

        @param value: The duration of the movie in minutes.
        """
        self._duration_mins = value

    @property
    def language(self):
        """!
        @brief Getter for the movie's language property.

        @return The language of the movie.
        """
        return self._language

    @language.setter
    def language(self, value):
        """!
        @brief Setter for the movie's language property.

        @param value: The language of the movie.
        """
        self._language = value

    @property
    def release_date(self):
        """!
        @brief Getter for the movie's release date property.

        @return The release date of the movie.
        """
        return self._release_date

    @release_date.setter
    def release_date(self, value):
        """!
        @brief Setter for the movie's release date property.

        @param value: The release date of the movie.
        """
        self._release_date = value

    @property
    def country(self):
        """!
        @brief Getter for the movie's country property.

        @return The country of origin for the movie.
        """
        return self._country

    @country.setter
    def country(self, value):
        """!
        @brief Setter for the movie's country property.

        @param value: The country of origin for the movie.
        """
        self._country = value

    @property
    def genre(self):
        """!
        @brief Getter for the movie's genre property.

        @return The genre of the movie.
        """
        return self._genre

    @genre.setter
    def genre(self, value):
        """!
        @brief Setter for the movie's genre property.

        @param value: The genre of the movie.
        """
        self._genre = value

    @property
    def cardsrcaddress(self):
        """!
        @brief Getter for the movie's card source address property.

        @return The source address for the movie's card image.
        """
        return self._cardsrcaddress

    @cardsrcaddress.setter
    def cardsrcaddress(self, value):
        """!
        @brief Setter for the movie's card source address property.

        @param value: The source address for the movie's card image.
        """
        self._cardsrcaddress = value

    @property
    def detailbanneraddress(self):
        """!
        @brief Getter for the movie's detail banner source address property.

        @return The source address for the movie's detail banner image.
        """
        return self._detailbanneraddress

    @detailbanneraddress.setter
    def detailbanneraddress(self, value):
        """!
        @brief Setter for the movie's detail banner source address property.

        @param value: The source address for the movie's detail banner image.
        """
        self._detailbanneraddress = value

    @property
    def screening_list(self):
        """!
        @brief Getter for the movie's screening list property.

        @return The cinema screening list of the movie.
        """
        return self._screening_list
    
    @screening_list.setter
    def screening_list(self, value):
        """!
        @brief Setter for the movie's cinema screening list property.

        @param value: The cinema screening list of the movie.
        """
        self._screening_list = value
