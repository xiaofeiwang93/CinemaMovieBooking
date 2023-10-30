class DebitCard(Payment):
    def __init__(self, amount, created_on, payment_id, card_number, bank_name, name_on_card):
        super().__init__(amount, created_on, payment_id)
        self.__card_number = card_number
        self.__bank_name = bank_name
        self.__name_on_card = name_on_card

    # Getter and setter for card_number
    @property
    def card_number(self):
        return self.__card_number

    @card_number.setter
    def card_number(self, value):
        self.__card_number = value

    # Getter and setter for bank_name
    @property
    def bank_name(self):
        return self.__bank_name

    @bank_name.setter
    def bank_name(self, value):
        self.__bank_name = value

    # Getter and setter for name_on_card
    @property
    def name_on_card(self):
        return self.__name_on_card

    @name_on_card.setter
    def name_on_card(self, value):
        self.__name_on_card = value

    def calc_discount(self):
        # Implement discount calculation logic for debit card payments
        return 0.03 * self.amount

    def calc_final_payment(self):
        # Implement final payment calculation logic for debit card payments
        return self.amount - self.calc_discount()