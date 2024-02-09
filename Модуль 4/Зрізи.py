some_str = "This is awesome string"
first_five = some_str[0:5]
print (first_five)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = numbers[0:9:2] #0 це номер 1; 9 - це номер 10, але його не враховує, тобто від 1 до 10 не включно; 2 це крок 2.
even_numbers = numbers[1:9:2]
three_numbers = numbers[2:9:3]
print (odd_numbers)
print (even_numbers)
print (three_numbers)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = numbers[::2]
even_numbers = numbers[1::2]
three_numbers = numbers[2:9:3]
numbers_copy = numbers[:]
print (odd_numbers)
print (even_numbers)
print (three_numbers)
print (numbers_copy)

numbers = [0, 1, 2, 3]
first_three = numbers[0:3]  # [0, 1, 2]