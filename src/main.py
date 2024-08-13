import os
import json

from contact import Contact
from contact_manager import ContactManager
from translation_manager import _TranslationManager
from utility import _Utility

def main():
    """
    Main function that manages the Address Book user interface.
    """
    language = input("Choose the language (en/it/fr): ")
    while language not in ["en", "it", "fr"]:
        language = input("Invalid language. Choose the language (en/it/fr): ")


    filename = os.path.join(os.path.dirname(__file__), '../data/contacts.json')
    cm = ContactManager()
    cm.load_contacts(filename)
    tm = _TranslationManager()

    while True:
        print("\nContactEase Solutions Menu")
        tm._print("1. Add Contact",language)
        tm._print("2. View Contacts",language)
        tm._print("3. Edit Contact",language)
        tm._print("4. Delete Contact",language)
        tm._print("5. Search Contact",language)
        tm._print("6. Save and Exit",language)
        choice = tm._input("Choose an option: ", language)

        print ("\n")

        if choice == '1':
            last_name = tm._input("Last Name: ", language)
            first_name = tm._input("First Name: ", language)
            phone = tm._input("Phone: ", language)
            email = tm._input("Email: ", language)
            try:
                cm.add_contact(Contact(first_name, last_name, phone, email))
                tm._print("Contact added successfully.", language)
            except ValueError as e:
                tm._print(str(e), language)
                tm._print("Please try again.", language)
        elif choice == '2':
            cm.view_contacts()            
        elif choice == '3':
            last_name = tm._input("Last Name of the contact to edit: ", language)
            first_name = tm._input("First Name of the contact to edit: ", language)
            if not cm.find_contact(first_name, last_name):
                tm._print("Contact not found.", language)
                continue;
            print ("\n")
            new_last_name = tm._input("Last Name: ", language)
            new_first_name = tm._input("First Name: ", language)
            new_phone = tm._input("Phone: ", language)
            new_email = tm._input("Email: ", language)
            if cm.edit_contact(first_name, last_name, Contact(new_first_name, new_last_name, new_phone, new_email)):
                tm._print("Contact updated successfully.", language)
            else:
                tm._print("Contact not found.", language)
        elif choice == '4':
            last_name = tm._input("Last Name of the contact to delete: ", language)
            first_name = tm._input("First Name of the contact to delete: ", language)
            if cm.delete_contact(first_name, last_name):
                tm._print("Contact deleted successfully.", language)
            else:
                tm._print("Contact not found.")
        elif choice == '5':
            last_name = tm._input("Last Name: ", language)
            first_name = tm._input("First Name: ", language)
            contact = cm.find_contact(first_name, last_name)
            if contact:
                print(contact)
            else:
                tm._print("Contact not found.", language)
        elif choice == '6':
            cm.save_contacts(filename)
            tm._print("Contacts saved. Exiting...", language)
            break
        else:
            tm._print("Invalid choice. Please try again.", language)

if __name__ == "__main__":
    main()