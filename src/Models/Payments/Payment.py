from datetime import datetime
from abc import ABC, abstractmethod

class Payment(ABC):
    def __init__(self, amount, created_on, payment_id):
        self.__amount = amount
        self.__created_on = created_on
        self.__payment_id = payment_id

    # Getter and setter for amount
    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, value):
        self.__amount = value

    # Getter and setter for created_on
    @property
    def created_on(self):
        return self.__created_on

    @created_on.setter
    def created_on(self, value):
        self.__created_on = value

    # Getter and setter for payment_id
    @property
    def payment_id(self):
        return self.__payment_id

    @payment_id.setter
    def payment_id(self, value):
        self.__payment_id = value

    @abstractmethod
    def calc_discount(self):
        pass

    @abstractmethod
    def calc_final_payment(self):
        pass
