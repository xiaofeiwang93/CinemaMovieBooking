import pytest
from datetime import datetime, timedelta

from Services.CommonService import CommonService

def test_generate_seats():
    # Call the function to generate seats
    seating_arrangement = CommonService.generate_seats()

    # Check if the seating arrangement contains the expected seats
    assert 1 in seating_arrangement
    assert seating_arrangement[1] == {"row": 1, "seat": 1}

    assert 20 in seating_arrangement
    assert seating_arrangement[20] == {"row": 2, "seat": 10}

    assert len(seating_arrangement) == 20

if __name__ == "__main__":
    pytest.main([__file__])
