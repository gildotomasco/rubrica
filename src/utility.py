import re

class _Utility:
    @staticmethod
    def check_email(email):
        """
        Verifies if the provided email address is valid.

        Args:
            email (str): Email address to validate.

        Returns:
            bool: True if the email is valid, False otherwise.
        """
        # Regular expression for email validation
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None

    @staticmethod
    def check_phone_number(phone_number):
        """
        Verifies if the provided phone number is valid.

        Args:
            phone_number (str): Phone number to validate.

        Returns:
            bool: True if the phone number is valid, False otherwise.
        """
        # Remove any non-numeric characters from the phone number
        cleaned_number = re.sub(r'\D', '', phone_number)
    
        # Use a regular expression to check if the cleaned number has at least 8 digits
        pattern = r'^\d{8,}$'
        return re.match(pattern, cleaned_number) is not None
