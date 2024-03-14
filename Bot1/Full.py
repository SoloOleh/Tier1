from datetime import datetime
from collections import UserDict, defaultdict
import re
import pycountry
from pycountry.db import Country
import pickle

def search_country(country):
    """Search counnry by name or ISO code"""
    countries  = pycountry.countries.search_fuzzy(country)
    return  [c for c in countries if isinstance(c, Country)]

def get_country(country,):
    """get counnry by name or ISO code"""
    c = pycountry.countries.get(alpha_2=country)
    return c if c else pycountry.countries.get(name=country)

def get_pattern(name, country_code="UA"):
    """Return patterns by name or country"""
    if name == "POSTAL_CODE":
        if country_code in POSTAL_CODES_BY_COUNTRY:
            return POSTAL_CODES_BY_COUNTRY[country_code]
        return POSTAL_CODES_BY_COUNTRY[country_code]

EMAIL_PATTERN = r"^\S+@\S+\.\S+$"
BULDING_PATTER = r"^\d+(?:[\\/]?\d+[A-Za-z]*)?$"
GB_POSTAL_CODE = r"(GIR[ ]?0AA|((AB|AL|B|BA|BB|BD|BH|BL|BN|BR|BS|BT|CA|CB|CF|CH|CM|CO|CR|CT|CV|"
GB_POSTAL_CODE += r"CW|DA|DD|DE|DG|DH|DL|DN|DT|DY|E|EC|EH|EN|EX|FK|FY|G|GL|GY|GU|HA|HD|HG|HP|HR|"
GB_POSTAL_CODE += r"HS|HU|HX|IG|IM|IP|IV|JE|KA|KT|KW|KY|L|LA|LD|LE|LL|LN|LS|LU|M|ME|MK|ML|N|NE|"
GB_POSTAL_CODE += r"NG|NN|NP|NR|NW|OL|OX|PA|PE|PH|PL|PO|PR|RG|RH|RM|S|SA|SE|SG|SK|SL|SM|SN|SO|"
GB_POSTAL_CODE += r"SP|SR|SS|ST|SW|SY|TA|TD|TF|TN|TQ|TR|TS|TW|UB|W|WA|WC|WD|WF|WN|WR|WS|WV|YO|"
GB_POSTAL_CODE += r"ZE)(\d[\dA-Z]?[ ]?\d[ABD-HJLN-UW-Z]{2}))|BFPO[ ]?\d{1,4})"

POSTAL_CODES_BY_COUNTRY = {
    "GB": GB_POSTAL_CODE,
    "JE": r"JE\d[\dA-Z]?[ ]?\d[ABD-HJLN-UW-Z]{2}",
    "GG": r"GY\d[\dA-Z]?[ ]?\d[ABD-HJLN-UW-Z]{2}",
    "IM": r"IM\d[\dA-Z]?[ ]?\d[ABD-HJLN-UW-Z]{2}",
    "US": r"\d{5}([ \-]\d{4})?",
    "CA": r"[ABCEGHJKLMNPRSTVXY]\d[ABCEGHJ-NPRSTV-Z][ ]?\d[ABCEGHJ-NPRSTV-Z]\d",
    "DE": r"\d{5}",
    "JP": r"\d{3}-\d{4}",
    "FR": r"\d{2}[ ]?\d{3}",
    "AU": r"\d{4}",
    "IT": r"\d{5}",
    "CH": r"\d{4}",
    "AT": r"\d{4}",
    "ES": r"\d{5}",
    "NL": r"\d{4}[ ]?[A-Z]{2}",
    "BE": r"\d{4}",
    "DK": r"\d{4}",
    "SE": r"\d{3}[ ]?\d{2}",
    "NO": r"\d{4}",
    "BR": r"\d{5}[\-]?\d{3}",
    "PT": r"\d{4}([\-]\d{3})?",
    "FI": r"\d{5}",
    "AX": r"22\d{3}",
    "KR": r"\d{3}[\-]\d{3}",
    "CN": r"\d{6}",
    "TW": r"\d{3}(\d{2})?",
    "SG": r"\d{6}",
    "DZ": r"\d{5}",
    "AD": r"AD\d{3}",
    "AR": r"([A-HJ-NP-Z])?\d{4}([A-Z]{3})?",
    "AM": r"(37)?\d{4}",
    "AZ": r"\d{4}",
    "BH": r"((1[0-2]|[2-9])\d{2})?",
    "BD": r"\d{4}",
    "BB": r"(BB\d{5})?",
    "BY": r"\d{6}",
    "BM": r"[A-Z]{2}[ ]?[A-Z0-9]{2}",
    "BA": r"\d{5}",
    "IO": r"BBND 1ZZ",
    "BN": r"[A-Z]{2}[ ]?\d{4}",
    "BG": r"\d{4}",
    "KH": r"\d{5}",
    "CV": r"\d{4}",
    "CL": r"\d{7}",
    "CR": r"\d{4,5}|\d{3}-\d{4}",
    "HR": r"\d{5}",
    "CY": r"\d{4}",
    "CZ": r"\d{3}[ ]?\d{2}",
    "DO": r"\d{5}",
    "EC": r"([A-Z]\d{4}[A-Z]|(?:[A-Z]{2})?\d{6})?",
    "EG": r"\d{5}",
    "EE": r"\d{5}",
    "FO": r"\d{3}",
    "GE": r"\d{4}",
    "GR": r"\d{3}[ ]?\d{2}",
    "GL": r"39\d{2}",
    "GT": r"\d{5}",
    "HT": r"\d{4}",
    "HN": r"(?:\d{5})?",
    "HU": r"\d{4}",
    "IS": r"\d{3}",
    "IN": r"\d{6}",
    "ID": r"\d{5}",
    "IL": r"\d{5}",
    "JO": r"\d{5}",
    "KZ": r"\d{6}",
    "KE": r"\d{5}",
    "KW": r"\d{5}",
    "LA": r"\d{5}",
    "LV": r"\d{4}",
    "LB": r"(\d{4}([ ]?\d{4})?)?",
    "LI": r"(948[5-9])|(949[0-7])",
    "LT": r"\d{5}",
    "LU": r"\d{4}",
    "MK": r"\d{4}",
    "MY": r"\d{5}",
    "MV": r"\d{5}",
    "MT": r"[A-Z]{3}[ ]?\d{2,4}",
    "MU": r"(\d{3}[A-Z]{2}\d{3})?",
    "MX": r"\d{5}",
    "MD": r"\d{4}",
    "MC": r"980\d{2}",
    "MA": r"\d{5}",
    "NP": r"\d{5}",
    "NZ": r"\d{4}",
    "NI": r"((\d{4}-)?\d{3}-\d{3}(-\d{1})?)?",
    "NG": r"(\d{6})?",
    "OM": r"(PC )?\d{3}",
    "PK": r"\d{5}",
    "PY": r"\d{4}",
    "PH": r"\d{4}",
    "PL": r"\d{2}-\d{3}",
    "PR": r"00[679]\d{2}([ \-]\d{4})?",
    "RO": r"\d{6}",
    "SM": r"4789\d",
    "SA": r"\d{5}",
    "SN": r"\d{5}",
    "SK": r"\d{3}[ ]?\d{2}",
    "SI": r"\d{4}",
    "ZA": r"\d{4}",
    "LK": r"\d{5}",
    "TJ": r"\d{6}",
    "TH": r"\d{5}",
    "TN": r"\d{4}",
    "TR": r"\d{5}",
    "TM": r"\d{6}",
    "UA": r"\d{5}",
    "UY": r"\d{5}",
    "UZ": r"\d{6}",
    "VA": r"00120",
    "VE": r"\d{4}",
    "ZM": r"\d{5}",
    "AS": r"96799",
    "CC": r"6799",
    "CK": r"\d{4}",
    "RS": r"\d{6}",
    "ME": r"8\d{4}",
    "CS": r"\d{5}",
    "YU": r"\d{5}",
    "CX": r"6798",
    "ET": r"\d{4}",
    "FK": r"FIQQ 1ZZ",
    "NF": r"2899",
    "FM": r"(9694[1-4])([ \-]\d{4})?",
    "GF": r"9[78]3\d{2}",
    "GN": r"\d{3}",
    "GP": r"9[78][01]\d{2}",
    "GS": r"SIQQ 1ZZ",
    "GU": r"969[123]\d([ \-]\d{4})?",
    "GW": r"\d{4}",
    "HM": r"\d{4}",
    "IQ": r"\d{5}",
    "KG": r"\d{6}",
    "LR": r"\d{4}",
    "LS": r"\d{3}",
    "MG": r"\d{3}",
    "MH": r"969[67]\d([ \-]\d{4})?",
    "MN": r"\d{6}",
    "MP": r"9695[012]([ \-]\d{4})?",
    "MQ": r"9[78]2\d{2}",
    "NC": r"988\d{2}",
    "NE": r"\d{4}",
    "VI": r"008(([0-4]\d)|(5[01]))([ \-]\d{4})?",
    "PF": r"987\d{2}",
    "PG": r"\d{3}",
    "PM": r"9[78]5\d{2}",
    "PN": r"PCRN 1ZZ",
    "PW": r"96940",
    "RE": r"9[78]4\d{2}",
    "SH": r"(ASCN|STHL) 1ZZ",
    "SJ": r"\d{4}",
    "SO": r"\d{5}",
    "SZ": r"[HLMS]\d{3}",
    "TC": r"TKCA 1ZZ",
    "WF": r"986\d{2}",
    "XK": r"\d{5}",
    "YT": r"976\d{2}",
}


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        self.value = value

class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise NotValidPhoneNumber
        self.value = value

class Birthday(Field):
    def __init__(self, value):
        try:
            day, month, year = map(int, value.split('.'))
            self.value = datetime(year, month, day)
        except:
            raise NotValidDate

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record
    
    def find(self, name):
        contact = self.data.get(name)
        if not contact:
            raise KeyError
        return contact

    def delete(self, name):
        contact = self.data.pop(name, None)
        if not contact:
            raise KeyError
    
    def get_birthdays_per_week(self):
        today = datetime.now().date()
        birthdays = defaultdict(list)
        users = [{"name": user.name.value, "birthday": user.birthday.value} for user in self.data.values() if hasattr(user, 'birthday')]
        def sort_by_date(user):
            return user['birthday'].date()
        users.sort(key=sort_by_date)
        
        for user in users:
            name = user['name']
            birthday = user['birthday'].date()
            birthday_this_year = birthday.replace(year=today.year)

            if birthday_this_year < today:
                birthday_this_year = birthday_this_year.replace(year=today.year + 1)
            
            delta_days = (birthday_this_year - today).days

            if delta_days < 7:
                if birthday_this_year.weekday() > 4: 
                    if today.weekday() != 0 and today.weekday() < 5:
                        birthdays['Monday'].append(name)
                else:
                    birthdays[birthday_this_year.strftime('%A')].append(name)
        return birthdays

class Street(Field):
    """Street class"""
    def __init__(self, name):
        if not isinstance(name, str):
            raise  StreetNotString
        super().__init__(name)

class BuldingNumber(Field):
    """Building number"""
    def __init__(self, build_number):
        build_number = str(build_number)
        if not re.match(BULDING_PATTER, build_number):
            raise BuildingNumberNotCorrect
        super().__init__(build_number)

class City(Field):
    """City"""
    def __init__(self, name):
        if not isinstance(name, str):
            raise  CityNotString
        super().__init__(name)

class CountryInfo(Field):
    """Country class"""
    def __init__(self, country):
        self.__country = country
        self.country = country
        super().__init__(country)

    @property
    def country(self):
        """Return country ISO code"""
        return self.__country.alpha_2

    @country.setter
    def country(self, country):
        """Setter for country"""
        found_country = get_country(country)
        if not found_country :
            raise CountryCodeNotCorrect
        self.__country = found_country

    @property
    def name(self):
        """Return country ISO name"""
        return self.__country.name


class PostalCode:
    """Postal code"""
    def __init__(self, code, country="UA") -> None:
        self.__code = None
        self.country = CountryInfo(country)
        self.code = code

    @property
    def code(self):
        """Return postal code"""
        return self.__code

    @code.setter
    def code(self, code):
        """Setter for postal code"""
        country_code = self.country.country
        postal_code_pattern = get_pattern("POSTAL_CODE", country_code)
        if not re.match(postal_code_pattern, str(code)):
            raise PostalCodeNotCorrect
        self.__code = str(code)


class Address:
    """Address for contact record"""
    def __init__(self, street, building_number,
                 city=None, postal_code=None, country="UA"):
        self.street = Street(street)
        self.building_number = BuldingNumber(building_number)
        self.city = City(city) if city else None
        self.postal_code = PostalCode(postal_code, country) if postal_code else None
        self.country = CountryInfo(country)

    def __str__(self):
        return f"{self.street}, {self.building_number}, {self.city}"

class Email(Field):
    """Email field for contact"""
    def __init__(self, email):
        self.__email = None
        self.email = email
        super().__init__(email)

    @property
    def email(self):
        """Return email"""
        return self.__email

    @email.setter
    def email(self, email):
        """Setter for email"""
        if not re.match(EMAIL_PATTERN, email):
            raise EmailNotCorrect
        self.__email = email



class Note:

    def __init__(self, title, description, date=None, note_id=None, tag=None):
        self.title = title
        self.description = description
        self.date = datetime.datetime.now()
        self.note_id = self.generate_id()
        self.tag = tag

    id_counter = 1

    @classmethod
    def generate_id(cls):
        note_id = cls.id_counter
        cls.id_counter += 1
        return note_id

class NotesManager:
    def __init__(self):
        self.notes = []

    def add_note(self, note):
        self.notes.append(note)

    def display_notes(self):
        for note in self.notes:
            print("ID:", note.note_id)
            print("Title:", note.title)
            print("Description:", note.description)
            print("Date:", note.date.strftime("%d.%m.%Y"))
            print("Tag:", note.tag)
            print()


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        
        except NotValidPhoneNumber:
            return "Phone number should contain only 10 digits."
        except NotValidDate:
            return "Date should be in format DD.MM.YYYY."
        except NameIsString:
            return "Name should contain only letters."
        except ValueError:
            return "Give me name and phone please."
        except NoBirthday:
            return "No birthday for this contact."
        except IndexError:
            return "Phone not found."
        except KeyError:
            return "Contact not found."
        except NoContacts: 
            return "No contacts in phonebook."
        except NoBirthdays:
            return "No birthdays in the next 7 days."
        except EmailNotCorrect:
            return "Email not correct."
        except:
            return "Something went wrong."
    return inner

@input_error
def add_birthday(args, contacts):
    name, birthday = args
    if not name.isalpha():
        raise NameIsString

    record = contacts.find(name)
    if birthday.count('.') != 2 or len(birthday) != 10 or not birthday.replace('.', '').isdigit():
        raise NotValidDate

    record.add_birthday(birthday)
    return f"{name}'s birthday added."

@input_error
def add_contact(args, contacts):
    name, phone = args
    if not phone.isdigit() or len(phone) != 10:
        raise NotValidPhoneNumber
    if not name.isalpha():
        raise NameIsString
    record = Record(name)
    record.add_phone(phone)
    contacts.add_record(record)
    return f"{name} with phone {phone} added."

@input_error
def add_note(notes_manager):
    title = input("Enter the title of the note: ")
    description = input("Enter the description of the note: ")
    tag = input("Enter the tag for the note: ")
    note = Note(title, description, tag=tag)
    notes_manager.add_note(note)
    return "Note added successfully!"

@input_error
def all_contacts(contacts):
    if not contacts:
        raise NoContacts
    all_contacts_list = []
    for i in contacts.data.values():
        all_contacts_list.append(str(i))

    return '\n'.join(all_contacts_list)

class NotValidPhoneNumber(ValueError):
    pass

class NotValidDate(ValueError):
    pass

class NameIsString(ValueError):
    pass

class NoContacts(Exception):
    pass

class NoBirthdays(Exception):
    pass

class NoBirthday(KeyError):
    pass

class EmailNotCorrect(Exception):
    """Email not passed reqular expression"""

class BuildingNumberNotCorrect(Exception):
    """Email not passed reqular expression"""

class StreetNotString(Exception):
    """Email not passed reqular expression"""

class CityNotString(Exception):
    """Email not passed reqular expression"""

class PostalCodeNotCorrect(Exception):
    """Email not passed reqular expression"""

class CountryCodeNotCorrect(Exception):
    """Given country code not correct"""

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def main():
    contacts = AddressBook()
    notes_manager = NotesManager()
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit", "bye", "quit"]:
            print("Good bye!")
            save_data(contacts)
            break
        elif command in ["hello", "hi", "hey", "yo", "sup"]:
            print("How can I help you?")
        elif command in ["add", "create", "new"]:
            print(add_contact(args, contacts))
        elif command in ["change", "edit", "update"]:
            print(change_contact(args, contacts))
        elif command in ["delete", "remove", "drop"]:
            print(remove_contact(args, contacts))
        elif command == "phone":
            print(show_contact(args, contacts))
        elif command == "all":
            print(all_contacts(contacts))
        elif command == "birthdays":
            print(birthdays(contacts))
        elif command == "add-birthday":
            print(add_birthday(args, contacts))
        elif command == "show-birthday":
            print(show_birthday(args, contacts))
        elif command == "add-email":
            print(add_email(args, contacts))
        elif command == "add-address":
            print(add_address(args, contacts))
        elif command == "show-address":
            print(show_address(args, contacts))
        elif command == "add-note":
            print(add_note(notes_manager))
        elif command == "edit-note":
            edit_note(args, notes_manager)
        elif command == "delete-note":
            print(delete_note(args, notes_manager))
        elif command == "show-note":
            print(show_note(args, notes_manager))
        elif command == "show-all-notes":
            notes_manager.display_notes()
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
