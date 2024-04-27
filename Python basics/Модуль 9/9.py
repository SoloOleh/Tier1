def get_favorites(contacts):
    return list(filter(lambda contact: contact['favorite'], contacts))

#або без лямбда

def is_favorite(contact):
    return contact['favorite']
def get_favorites(contacts):
    return list(filter(is_favorite, contacts))
