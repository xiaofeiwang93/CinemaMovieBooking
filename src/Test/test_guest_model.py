import pytest
from Models.Users.Guest import Guest

def test_guest_initialization():
    guest = Guest()
    assert guest.registered is False

def test_register_guest():
    guest = Guest()
    
    # Register the guest
    guest.register()
    
    assert guest.registered is True

def test_set_registered_property():
    guest = Guest()
    
    # Set the 'registered' property directly
    guest.registered = True
    
    assert guest.registered is True

if __name__ == "__main__":
    pytest.main()

