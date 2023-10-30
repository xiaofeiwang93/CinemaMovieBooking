from Models.Payments.Payment import Payment


class CreditCard(Payment):
    def __init__(self, amount, created_on, payment_id, credit_card_number, card_type, expiry_date, name_on_card):
        super().__init__(amount, created_on, payment_id)
        self.__credit_card_number = credit_card_number
        self.__card_type = card_type
        self.__expiry_date = expiry_date
        self.__name_on_card = name_on_card

    # Getter and setter for credit_card_number
    @property
    def credit_card_number(self):
        return self.__credit_card_number

    @credit_card_number.setter
    def credit_card_number(self, value):
        self.__credit_card_number = value

    # Getter and setter for card_type
    @property
    def card_type(self):
        return self.__card_type

    @card_type.setter
    def card_type(self, value):
        self.__card_type = value

    # Getter and setter for expiry_date
    @property
    def expiry_date(self):
        return self.__expiry_date

    @expiry_date.setter
    def expiry_date(self, value):
        self.__expiry_date = value

    # Getter and setter for name_on_card
    @property
    def name_on_card(self):
        return self.__name_on_card

    @name_on_card.setter
    def name_on_card(self, value):
        self.__name_on_card = value

    def calc_discount(self):
        # Implement discount calculation logic for credit card payments
        return 0.05 * self.amount

    def calc_final_payment(self):
        # Implement final payment calculation logic for credit card payments
        return self.amount - self.calc_discount()