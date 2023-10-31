from datetime import datetime
import pytest
from Models.Payments.CreditCard import CreditCard

def test_credit_card_properties_and_methods():
    # Create a CreditCard instance with valid arguments
    credit_card = CreditCard(
        amount=100.0,
        created_on=datetime(2023, 1, 15),
        payment_id=1,
        credit_card_number="1234-5678-9012-3456",
        card_type="Visa",
        expiry_date=datetime(2025, 12, 31),
        name_on_card="John Doe"
    )
    
    # Test inherited properties from Payment class
    assert credit_card.amount == 100.0
    assert credit_card.created_on == datetime(2023, 1, 15)
    assert credit_card.payment_id == 1

    # Test CreditCard-specific properties
    assert credit_card.credit_card_number == "1234-5678-9012-3456"
    assert credit_card.card_type == "Visa"
    assert credit_card.expiry_date == datetime(2025, 12, 31)
    assert credit_card.name_on_card == "John Doe"

    # Test calc_discount method
    assert credit_card.calc_discount() == 0.05 * 100.0

    # Test calc_final_payment method
    assert credit_card.calc_final_payment() == 100.0 - credit_card.calc_discount()

if __name__ == "__main__":
    pytest.main()
