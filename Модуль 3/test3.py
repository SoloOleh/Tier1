def convert_camel_to_snake (text):
    j = 0
    res = ""
    for char in text:
        if char.isupper():
            if j == 0:
                res = res + char.lower()
            else:
                res = res + '_' + char.lower()
        else:
            res = res + char
        j = j + 1
    return res

s = "CrazyFrogSounds"

new_title = convert_camel_to_snake (s)
print (new_title)