class Guest:
    def __init__(self):
        self.__registered = False

    def register(self):
        # Implement the registration logic here
        # You can set the 'registered' attribute to True upon registration
        self.__registered = True

    # Getter for 'registered'
    @property
    def registered(self):
        return self.__registered

    # Setter for 'registered'
    @registered.setter
    def registered(self, value):
        self.__registered = value