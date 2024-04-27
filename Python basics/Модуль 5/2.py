# name = "Avril Lavigne        "
# a = name.rstrip()
# print(a)  # Avril Lavigne

# name = "         Avril Lavigne"
# print(name.lstrip())  # Avril Lavigne

# name = "         Avril Lavigne          "
# print(name.strip())  # Avril Lavigne


def sanitize_phone_number(phone):
    sanitized = phone.replace("(", "").replace(")", "").replace("-", "").replace(" ", "").replace("+", "").rstrip().lstrip().strip()
    return sanitized
phone_numbers = [
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   "]
# normalized_numbers = [sanitize_phone_number(phone) for phone in phone_numbers]
# print (normalized_numbers)

# або 
for phone in phone_numbers:
    normalized_numbers = sanitize_phone_number(phone)
    print (normalized_numbers)




