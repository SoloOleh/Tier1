# replace_dict = {117: "o"}
# txt = "sun"
# print(txt.translate(replace_dict))  # son

# replace_dict = {ord("u"): "o"}
# txt = "sun"
# # print(txt.translate(replace_dict))  # son
# # або
# translation = txt.translate(replace_dict)
# print (translation)


# replace_dict = txt.maketrans("u", "o")
# txt = "sun"
# print(txt.translate(replace_dict))  # son

# txt = "sun"
# replace_dict = txt.maketrans("nus", "mot")
# print(txt.translate(replace_dict))  # tom

# txt = "the sun"
# replace_dict = txt.maketrans("nus", "nos", "he t")
# print(txt.translate(replace_dict))  # son

# CYRILLIC = ("а", "ч", "ш")
# LATIN = ("a", "ch", "sh")
# TRANSLIT_DICT = {}
# for c, l in zip(CYRILLIC, LATIN):
#     TRANSLIT_DICT[ord(c)] = l
#     TRANSLIT_DICT[ord(c.upper())] = l.upper()

# print("чаша".translate(TRANSLIT_DICT))  # chasha
# print("ЧАША".translate(TRANSLIT_DICT))  # CHASHA

CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

# Adjusting the TRANS dictionary to accommodate for the requirement to output names with appropriate capitalization
TRANS = {}
for c, l in zip(CYRILLIC_SYMBOLS + CYRILLIC_SYMBOLS.upper(), TRANSLATION + tuple(l.upper() for l in TRANSLATION)):
    # For uppercase Cyrillic characters, map to uppercase Latin characters
    if c.isupper():
        TRANS[ord(c)] = l.upper()
    else:
        # For lowercase Cyrillic characters, map to lowercase Latin characters
        TRANS[ord(c)] = l

# Adjusting the translate function to maintain the original case of the input
def translate(name):
    return ''.join(TRANS.get(ord(c), c) for c in name)

# Example usage with adjusted output
print(translate("Дмитро Короб"))  # Dmitro Korob
print(translate("Олекса Івасюк"))  # Oleksa Ivasyuk


