import copy
import pickle

class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite

    def __copy__(self):
        # Create a new instance of the Person class with the same attribute values
        return Person(self.name, self.email, self.phone, self.favorite)

class Contacts:
    def __init__(self, filename: str, contacts: list[Person] = None):
        if contacts is None:
            contacts = []
        self.filename = filename
        self.contacts = contacts
        self.is_unpacking = False
        self.count_save = 0

    def save_to_file(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self, file)

    def read_from_file(self):
        with open(self.filename, "rb") as file:
            content = pickle.load(file)
        return content

    def __getstate__(self):
        attributes = self.__dict__.copy()
        attributes["count_save"] = attributes["count_save"] + 1
        return attributes

    def __setstate__(self, value):
        self.__dict__ = value
        self.is_unpacking = True

    def __copy__(self):
        # Create a new instance of the Contacts class
        new_contacts = Contacts(self.filename)
        # Copy the list of contacts using shallow copy
        new_contacts.contacts = copy.copy(self.contacts)
        # Copy other attributes
        new_contacts.is_unpacking = self.is_unpacking
        new_contacts.count_save = self.count_save
        return new_contacts

    def __deepcopy__(self, memo):
        # Create a new instance of the Contacts class
        new_contacts = Contacts(self.filename)
        # Copy the list of contacts using deep copy
        new_contacts.contacts = copy.deepcopy(self.contacts, memo)
        # Copy other attributes
        new_contacts.is_unpacking = self.is_unpacking
        new_contacts.count_save = self.count_save
        return new_contacts
