def is_valid_password(password):
    if len(password) != 8:
        return False
    is_title = False
    is_lower = False
    is_number = False
    for character in password:
        if character.istitle():
            is_title = True
        if character.islower():
            is_lower = True
        if character.isdigit():
            is_number = True
    return is_title and is_lower and is_number