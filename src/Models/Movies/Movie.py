from datetime import datetime
from typing import List

class Movie:
    def __init__(self):
        """!
        @brief Constructor for the MovieModel class.
        Initializes all properties to None.
        """
        self._id = None
        self.__title = None
        self.__description = None
        self.__duration_mins = None
        self.__language = None
        self.__release_date = None
        self.__country = None
        self.__genre = None
        self.__screening_list = []

    # Getter and setter for title
    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        self.__title = value

    # Getter and setter for description
    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value

    # Getter and setter for duration_mins
    @property
    def duration_mins(self):
        return self.__duration_mins

    @duration_mins.setter
    def duration_mins(self, value):
        self.__duration_mins = value

    # Getter and setter for language
    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, value):
        self.__language = value

    # Getter and setter for release_date
    @property
    def release_date(self):
        return self.__release_date

    @release_date.setter
    def release_date(self, value):
        self.__release_date = value

    # Getter and setter for country
    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, value):
        self.__country = value

    # Getter and setter for genre
    @property
    def genre(self):
        return self.__genre

    @genre.setter
    def genre(self, value):
        self.__genre = value

    # Getter for screening_list
    @property
    def screening_list(self):
        return self.__screening_list

    def getSscreenings(self):
        return self.__screening_list
    
    def to_dict(self):
        """!
        @brief Converts the MovieModel object to a dictionary.

        @return A dictionary representing the MovieModel object.
        """
        return {
            "title": self.__title,
            "description": self.__description,
            "duration_mins": self.__duration_mins,
            "language": self.__language,
            "release_date": self.__release_date,
            "country": self.__country,
            "genre": self.__genre
        }

    def __str__(self):
        return f"Movie: title={self.__title}, description={self.__description}, duration_mins={self.__duration_mins}, language={self.__language}, release_date={self.__release_date}, country={self.__country}, genre={self.__genre}, screening_list={self.__screening_list}"
