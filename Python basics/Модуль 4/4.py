# lang = {"Python": 1991, "Java": 1995, "JS": 1995}
# for l in lang:
#     print(l)

# lang = {"Python": 1991, "Java": 1995, "JS": 1995}
# for l in lang.keys():
#     print(l)

# lang = {"Python": 1991, "Java": 1995, "JS": 1995}
# for value in lang.values():
#     print(value)

# lang = {"Python": 1991, "Java": 1995, "JS": 1995}
# for l, value in lang.items():
#     print(f"Programming language {l} - released {value}")

def lookup_key(data, value):
    result_keys = []
    for key, dict_value in data.items():
        if dict_value == value:
            result_keys.append(key)
    return result_keys

def lookup_key(data, value):
    result_keys = []
    for key in data.keys():
        if data[key] == value:
            result_keys.append(key)
    return result_keys