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


def get_phone_numbers_for_countries(list_phones):
    countries = {
        "JP": [],
        "SG": [],
        "TW": [],
        "UA": []
    }

    for phone in list_phones:
        sanitized_phone = sanitize_phone_number(phone)
        if sanitized_phone.startswith("81"):
            countries["JP"].append(sanitized_phone)
        elif sanitized_phone.startswith("65"):
            countries["SG"].append(sanitized_phone)
        elif sanitized_phone.startswith("886"):
            countries["TW"].append(sanitized_phone)
        else:
            countries["UA"].append(sanitized_phone)

    return countries


# Test the function
test_phones = ['380998759405', '818765347', '8867658976', '657658976']
print(get_phone_numbers_for_countries(test_phones))
