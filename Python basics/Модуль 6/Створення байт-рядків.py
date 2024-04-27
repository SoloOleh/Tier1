s = b'Hello!'
print(s[1]) # b'e'

byte_string = b'Hello world!'
print(byte_string[1])

byte_str = 'some text'.encode()

numbers = [127, 255, 156]
byte_numbers = bytes(numbers)
print (byte_numbers) # b'\x7f\xff\x9c

some_numbers = bytes([127, 255, 156])
print(some_numbers) # b'\x7f\xff\x9c'

for numbers in [127, 255, 156]:
  print(hex(numbers))





