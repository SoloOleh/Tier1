def format_phone_number(func):
    def inner(phone):
        sanitized = func(phone)
        # Якщо довжина номера після нормалізації становить 10 символів, додати префікс +38
        if len(sanitized) == 10:
            return '+38' + sanitized
        # Якщо довжина номера після нормалізації становить 12 символів, додати лише знак +
        elif len(sanitized) == 12:
            return '+' + sanitized
        # Якщо номер не відповідає жодному з цих умов, просто повернути нормалізований номер
        else:
            return sanitized
    return inner

@format_phone_number
def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
            .removeprefix("+")
            .replace("(", "")
            .replace(")", "")
            .replace("-", "")
            .replace(" ", "")
    )
    return new_phone
