from datetime import date

class Notification:
    def __init__(self, notification_id, created_on, content):
        self.__notification_id = notification_id
        self.__created_on = created_on
        self.__content = content

    # Getter and setter for notification_id
    @property
    def notification_id(self):
        return self.__notification_id

    @notification_id.setter
    def notification_id(self, value):
        self.__notification_id = value

    # Getter and setter for created_on
    @property
    def created_on(self):
        return self.__created_on

    @created_on.setter
    def created_on(self, value):
        self.__created_on = value

    # Getter and setter for content
    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, value):
        self.__content = value
