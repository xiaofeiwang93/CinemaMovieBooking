from datetime import datetime
import pytest

from Models.Payments.Coupon import Coupon


def test_coupon_properties_and_methods():
    # Create a Coupon instance with valid arguments
    coupon = Coupon(coupon_id=1, expiry_date=datetime(2023, 12, 31), discount=0.1)
    
    # Test getters
    assert coupon.coupon_id == 1
    assert coupon.expiry_date == datetime(2023, 12, 31)
    assert coupon.discount == 0.1

    # Test string representation
    expected_string = "Coupon ID: 1\nExpiry Date: 2023-12-31 00:00:00\nDiscount: 0.1"
    assert str(coupon) == expected_string