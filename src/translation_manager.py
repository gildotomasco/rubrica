class _TranslationManager:
    """
    A class that manages translations for a multilingual application.

    Attributes:
        _translation_dict (dict): A dictionary containing translation mappings.
    """

    def __init__(self):
        """
        Initializes a new instance of the _TranslationManager class.

        The _translation_dict attribute is populated with translation mappings.
        """
        self._translation_dict = {
            "1. Add Contact": {
                "it": "1. Aggiungi Contatto",
                "fr": "1. Ajouter un contact"
            },
            "2. View Contacts": {
                "it": "2. Visualizza Contatti",
                "fr": "2. Voir les contacts"
            },
            "3. Edit Contact": {
                "it": "3. Modifica Contatto",
                "fr": "3. Modifier le contact"
            },
            "4. Delete Contact": {
                "it": "4. Elimina Contatto",
                "fr": "4. Supprimer le contact"
            },
            "5. Search Contact": {
                "it": "5. Cerca Contatto",
                "fr": "5. Rechercher un contact"
            },
            "6. Save and Exit": {
                "it": "6. Salva ed Esci",
                "fr": "6. Enregistrer et quitter"
            },
            "Choose an option: ": {
                "it": "Scegli un'opzione: ",
                "fr": "Choisissez une option : "
            },
            "First Name: ": {
                "it": "Nome: ",
                "fr": "Prénom : "
            },
            "Last Name: ": {
                "it": "Cognome: ",
                "fr": "Nom de famille : "
            },
            "Phone: ": {
                "it": "Telefono: ",
                "fr": "Téléphone : "
            },
            "Email: ": {
                "it": "Email: ",
                "fr": "E-mail : "
            },
            "First Name of the contact to edit: ": {
                "it": "Nome del contatto da modificare: ",
                "fr": "Prénom du contact à modifier "
            },
            "First Name of the contact to delete: ": {
                "it": "Nome del contatto da cancellare: ",
                "fr": "Prénom du contact à supprimer: "
            },
            "Last Name of the contact to edit: ": {
                "it": "Cognome del contatto da modificare: ",
                "fr": "Nom de famille du contact à modifier: "
            },
            "Last Name of the contact to delete: ": {
                "it": "Cognome del contatto da cancellare: ",
                "fr": "Nom de famille du contact à supprimer: "
            },
            "Contact added successfully.": {
                "it": "Contatto aggiunto con successo.",
                "fr": "Contact ajouté avec succès."
            },
            "Please try again.": {
                "it": "Si prega di riprovare.",
                "fr": "Veuillez réessayer."
            },
            "Contact updated successfully.": {
                "it": "Contatto aggiornato con successo.",
                "fr": "Contact mis à jour avec succès."
            },
            "Contact not found.": {
                "it": "Contatto non trovato.",
                "fr": "Contact introuvable."
            },
            "Contact deleted successfully.": {
                "it": "Contatto eliminato con successo.",
                "fr": "Contact supprimé avec succès."
            },
            "Contacts saved. Exiting...": {
                "it": "Contatti salvati. Uscita...",
                "fr": "Contacts enregistrés. Fermeture..."
            },
            "Invalid choice. Please try again.": {
                "it": "Scelta non valida. Si prega di riprovare.",
                "fr": "Choix invalide. Veuillez réessayer."
            },
            "Contact already in address book.": {
                "it": "Contatto già presente.",
                "fr": "Contact déjà dans le répertoire."
            },
            "Invalid email address.": {
                "it": "indirizzo email non valido.",
                "fr": "Adresse e-mail non valide."
            },
            "Invalid phone number.":{
                "it": "numero di telefono non valido.",
                "fr": "Numéro de téléphone non valide."
            },
            "File not found. Starting with an empty contact list.":{
                "it": "File non trovato. Iniziamo con una rubrica vuota.",
                "fr": "Fichier introuvable. Commencer avec une liste de contacts vide."
            }
        }

    def _translate_message(self, message, language="en"):
        """
        Translates a given message to the specified language.

        Args:
            message (str): The message to be translated.
            language (str, optional): The target language (default is "en").

        Returns:
            str: The translated message.
        """
        #print (message)
        #message="Invalid email address."
        if message in self._translation_dict:
            return self._translation_dict[message][language]#.get(message, {}).get(language, message)
        else:
            return message
        #return self._translation_dict.get(message, {}).get(language, message)

    def _print(self, message, language="en"):
        """
        Prints a translated message to the console.

        Args:
            message (str): The message to be printed.
            language (str, optional): The target language (default is "en").
        """
        print(self._translate_message(message, language))

    def _input(self, message, language="en"):
        """
        Prompts the user for input and returns the translated input.

        Args:
            message (str): The input prompt message.
            language (str, optional): The target language (default is "en").

        Returns:
            str: The translated user input.
        """
        return input(self._translate_message(message, language))
