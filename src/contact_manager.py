import json
from contact import Contact
from utility import _Utility


class ContactManager:
    """
    A class that manages contacts and provides various operations.

    Attributes:
        contacts (list): A list of Contact instances representing the contacts.
    """
    def __init__(self):
        """
        Initializes a new instance of the ContactManager class.

        The contacts attribute is initialized as an empty list.
        """
        self.contacts = []

    def add_contact(self, contact):
        """
        Adds a new contact to the list if it does not already exist.

        Args:
            contact (Contact): An instance of Contact to be added.

        Raises:
            ValueError: If the contact already exists.
            ValueError: If the email address is invalid.
            ValueError: If the phone number is invalid.
        """
        if self.find_contact(contact.first_name, contact.last_name):
            raise ValueError("Contact already in address book.")
        if not _Utility.check_phone_number(contact.phone):
            raise ValueError("Invalid phone number.")
        if not _Utility.check_email(contact.email):
            raise ValueError("Invalid email address.")
        
        self.contacts.append(contact)

    def view_contacts(self):
        """
        Displays all contacts in the list.
        """
        self.sort_contacts()
        for contact in self.contacts:
            print(contact)

    def find_contact(self, first_name, last_name):
        """
        Finds a contact by first name and last name.

        Args:
            first_name (str): The first name of the contact to find.
            last_name (str): The last name of the contact to find.

        Returns:
            Contact: An instance of Contact if found, otherwise None.
        """
        for contact in self.contacts:
            if contact.first_name.lower() == first_name.lower() and contact.last_name.lower() == last_name.lower():
                return contact
        return None

    def edit_contact(self, first_name, last_name, new_contact):
        """
        Edits the details of an existing contact.

        Args:
            first_name (str): The first name of the contact to edit.
            last_name (str): The last name of the contact to edit.
            new_contact (Contact): A new Contact instance with updated details.

        Returns:
            bool: True if the contact was successfully edited, otherwise False.
        """
        contact = self.find_contact(first_name, last_name)
        if contact:
            contact.first_name = new_contact.first_name
            contact.last_name = new_contact.last_name
            contact.phone = new_contact.phone
            contact.email = new_contact.email
            return True
        return False

    def delete_contact(self, first_name, last_name):
        """
        Deletes a contact from the list.

        Args:
            first_name (str): The first name of the contact to delete.
            last_name (str): The last name of the contact to delete.

        Returns:
            bool: True if the contact was successfully deleted, otherwise False.
        """
        contact = self.find_contact(first_name, last_name)
        if contact:
            self.contacts.remove(contact)
            return True
        return False

    def save_contacts(self, filename):
        """
        Saves all contacts to a JSON file.

        Args:
            filename (str): The name of the file to save the contacts.
        """
        self.sort_contacts()
        with open(filename, 'w') as file:
            json.dump([contact.__dict__ for contact in self.contacts], file)

    def load_contacts(self, filename):
        """
        Loads contacts from a JSON file.

        Args:
           filename (str): The name of the file from which to load contacts.
        """
        try:
            with open(filename, 'r') as file:
                contacts_data = json.load(file)
                #print (type(contacts_data))
                #print (contacts_data[0]["first_name"])
                
                #self.contacts = [Contact(**data) for data in contacts_data]
                self.contacts = [Contact(data['first_name'], data['last_name'], data['phone'], data['email'] ) for data in contacts_data]                 
                self.sort_contacts()



                '''
                #stampo con enumerate la lista dei contatti
                for i, data in enumerate(contacts_data):
                    print (f"contatto[{i}]:{data}")
                for i, data in enumerate(self.contacts):
                    print (f"contatto[{i}]:{data}")
                '''

        except FileNotFoundError:
            print("File not found. Starting with an empty contact list.")

    def sort_contacts(self):
        """
        Sorts the contacts list by last name and then by first name.
        """
        self.contacts.sort(key=lambda contact: (contact.last_name.lower(), contact.first_name.lower()))

    def __len__(self):
        """
        Returns the number of contacts in the list.

        Returns:
           int: Number of contacts in the list.
        """
        return len(self.contacts)