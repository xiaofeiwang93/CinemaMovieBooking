from datetime import datetime
from Models.Payments.CreditCard import CreditCard
import pytest
from Models.Payments.Payment import Payment

def test_payment_abstract_class():
    # Attempting to create an instance of the abstract class should raise a TypeError
    with pytest.raises(TypeError):
        payment = Payment(amount=100, created_on=datetime(2023, 1, 15), payment_id=1)

def test_credit_card_concrete_class():
    # Create a CreditCard instance with valid arguments
    credit_card = CreditCard(
        amount=100.0,
        created_on=datetime(2023, 1, 15),
        payment_id=1,
        credit_card_number="1234-5678-1234-5678",
        card_type="Visa",
        expiry_date="12/25",
        name_on_card="John Doe"
    )
    
    # Test inherited properties from Payment class
    assert credit_card.amount == 100.0
    assert credit_card.created_on == datetime(2023, 1, 15)
    assert credit_card.payment_id == 1

    # Test CreditCard-specific properties
    assert credit_card.credit_card_number == "1234-5678-1234-5678"
    assert credit_card.card_type == "Visa"
    assert credit_card.expiry_date == "12/25"
    assert credit_card.name_on_card == "John Doe"

    # Test calc_discount method
    assert credit_card.calc_discount() == 0.05 * 100.0

    # Test calc_final_payment method
    assert credit_card.calc_final_payment() == 100.0 - credit_card.calc_discount()

if __name__ == "__main__":
    pytest.main()
