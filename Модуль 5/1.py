# string = "Привіт, світ!"
# length = len(string)
# print(length)

# import re

# string = "Привіт,\nсвіт!"
# pattern = r'[\n\f\r\t\v]'
# stripped_string = re.sub(pattern, '', string)
# length = len(stripped_string)
# print(length)


# def real_len(text):
#     control_characters = '\n\f\r\t\v'
#     length = 0
#     for char in text:
#         if char not in control_characters:
#             length += 1
#     return length

# text = "Alex\nKdfe23\t\f\v.\r"
# text = 'Al\nKdfe23\t\v.\r'

# print(f"Довжина рядка без керівних символів: {real_len(text)}")

def real_len(text):
    control_characters = '\n\f\r\t\v'
    length = 0
    for char in text:
        if char not in control_characters:
            length += 1
    return length

text1 = "Alex\nKdfe23\t\f\v.\r"
text2 = 'Al\nKdfe23\t\v.\r'

length1 = real_len(text1)
length2 = real_len(text2)

print(f"Довжина рядка text1 без керівних символів: {length1}")
print(f"Довжина рядка text2 без керівних символів: {length2}")