from abc import ABC, abstractmethod
from Models.Person import Person

class User(Person):
    """!
    @brief Abstract User class derived from Person.

    @param username: The username of the user.
    @param password: The password of the user.
    """
    def __init__(self, username: str, password: str):
        """!
        @brief Constructor for the User class.

        @param username: The username of the user.
        @param password: The password of the user.
        """
        self.username = username
        self.password = password

    @property
    def username(self):
        """!
        @brief Get the username of the user.

        @return: The username of the user.
        """
        return self.__username

    @username.setter
    def username(self, value):
        """!
        @brief Set the username of the user.

        @param value: The new username to set.
        """
        self.__username = value

    @property
    def password(self):
        """!
        @brief Get the password of the user.

        @return: The password of the user.
        """
        return self.__password

    @password.setter
    def password(self, value):
        """!
        @brief Set the password of the user.

        @param value: The new password to set.
        """
        self.__password = value

    @abstractmethod
    def login(self) -> bool:
        """!
        @brief Abstract method to log in the user.

        @return: True if the login is successful, False otherwise.
        """
        pass

    @abstractmethod
    def logout(self) -> bool:
        """!
        @brief Abstract method to log out the user.

        @return: True if the logout is successful, False otherwise.
        """
        pass

    @abstractmethod
    def reset_password(self) -> bool:
        """!
        @brief Abstract method to reset the user's password.

        @return: True if the password reset is successful, False otherwise.
        """
        pass
