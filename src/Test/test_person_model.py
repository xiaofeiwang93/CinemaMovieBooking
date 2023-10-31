import pytest
from Models.Users.Person import Person

class TestPerson:
    def test_person_initialization(self):
        # Create a concrete Person instance
        person = ConcretePerson(name="John Doe", address="123 Main St", email="john@example.com", phone="123-456-7890")

        # Test that the attributes are correctly set
        assert person.name == "John Doe"
        assert person.address == "123 Main St"
        assert person.email == "john@example.com"
        assert person.phone == "123-456-7890"

class ConcretePerson(Person):
    pass  # Create a concrete subclass of Person

if __name__ == "__main__":
    pytest.main()
