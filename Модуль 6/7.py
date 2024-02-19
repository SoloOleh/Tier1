#  s = b'Hello!'
#   print(s[1])  # b'e'

# byte_string = b'Hello world!'

# byte_str = 'some text'.encode()

# numbers = [0, 128, 255]
# byte_numbers = bytes(numbers)

# ord('a')  # 97
# chr(128)  # 'd'

# s = "Привіт!"

# utf8 = s.encode()
# print(utf8)  # b'\xd0\x9f\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82!'

# utf16 = s.encode('utf-16')
# print(utf16)  # b'\xff\xfe\x1f\x04@\x048\x042\x045\x04B\x04!\x00'

# s_from_utf16 = utf16.decode('utf-16')
# print(s_from_utf16 == s)  # True

# print(b'Hello world!'.decode('utf-16'))  # 效汬潷汲Ⅴ



def is_equal_string(utf8_string, utf16_string):
    # Декодування UTF-8 та UTF-16 рядків до Unicode
    unicode_from_utf8 = utf8_string.decode('utf-8')
    unicode_from_utf16 = utf16_string.decode('utf-16')

    # Порівняння Unicode рядків
    return unicode_from_utf8 == unicode_from_utf16
