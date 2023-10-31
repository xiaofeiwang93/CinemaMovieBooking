import pytest
from datetime import date
from Models.Bookings.Notification import Notification

# Test the getters and setters of the Notification class
def test_notification_getters_and_setters():
    # Create a Notification instance
    notification = Notification(1, date(2023, 10, 31), "Test notification content")

    # Test notification_id getter and setter
    assert notification.notification_id == 1
    notification.notification_id = 2
    assert notification.notification_id == 2

    # Test created_on getter and setter
    assert notification.created_on == date(2023, 10, 31)
    notification.created_on = date(2023, 11, 1)
    assert notification.created_on == date(2023, 11, 1)

    # Test content getter and setter
    assert notification.content == "Test notification content"
    notification.content = "Updated notification content"
    assert notification.content == "Updated notification content"

if __name__ == "__main__":
    pytest.main([__file__])
