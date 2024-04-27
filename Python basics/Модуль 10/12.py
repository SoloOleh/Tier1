class Contacts:
  current_id = 1

  def __init__(self):
    self.contacts = []

  def list_contacts(self):
    return self.contacts

  def add_contacts(self, name, phone, email, favorite):
    new_contact = {
      "id": Contacts.current_id,
      "name": name,
      "phone": phone,
      "email": email,
      "favorite": favorite,
    }
    self.contacts.append(new_contact)
    Contacts.current_id += 1

# Приклад використання
contacts = Contacts()
contacts.add_contacts("Іван Петренко", "+380951234567", "ivan.petrenko@example.com", True)
contacts.add_contacts("Марія Іванова", "+380678901234", "maria.ivanova@example.com", False)

print(contacts.list_contacts())
