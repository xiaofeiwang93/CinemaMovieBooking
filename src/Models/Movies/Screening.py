from datetime import datetime

class Screening:
    def __init__(self, screening_date, start_time, end_time, hall):
        self.__screening_date = screening_date
        self.__start_time = start_time
        self.__end_time = end_time
        self.__hall = hall

    # Getter and setter for screening_date
    @property
    def screening_date(self):
        return self.__screening_date

    @screening_date.setter
    def screening_date(self, value):
        self.__screening_date = value

    # Getter and setter for start_time
    @property
    def start_time(self):
        return self.__start_time

    @start_time.setter
    def start_time(self, value):
        self.__start_time = value

    # Getter and setter for end_time
    @property
    def end_time(self):
        return self.__end_time

    @end_time.setter
    def end_time(self, value):
        self.__end_time = value

    # Getter and setter for hall
    @property
    def hall(self):
        return self.__hall

    @hall.setter
    def hall(self, value):
        self.__hall = value

