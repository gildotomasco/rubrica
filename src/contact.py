class Contact:
    def __init__(self, first_name, last_name, phone, email):
        """
        Initializes a new contact.

        :param first_name: First name of the contact
        :param last_name: Last name of the contact
        :param phone: Phone number of the contact
        :param email: Email address of the contact
        """
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email

    def __str__(self):
        """
        Returns a string representation of the contact.

        :return: String representation of the contact
        """
        return f"{self.last_name.capitalize()} {self.first_name.capitalize()}, Phone: {self.phone}, Email: {self.email}"