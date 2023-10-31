from datetime import datetime

class Coupon:
    def __init__(self, coupon_id, expiry_date, discount):
        self.__coupon_id = coupon_id
        self.__expiry_date = expiry_date
        self.__discount = discount

    # Getter and setter for coupon_id
    @property
    def coupon_id(self):
        return self.__coupon_id

    @coupon_id.setter
    def coupon_id(self, value):
        self.__coupon_id = value

    # Getter and setter for expiry_date
    @property
    def expiry_date(self):
        return self.__expiry_date

    @expiry_date.setter
    def expiry_date(self, value):
        self.__expiry_date = value

    # Getter and setter for discount
    @property
    def discount(self):
        return self.__discount

    @discount.setter
    def discount(self, value):
        self.__discount = value
    
    def __str__(self):
        return f"Coupon ID: {self.__coupon_id}\nExpiry Date: {self.__expiry_date}\nDiscount: {self.__discount}"

