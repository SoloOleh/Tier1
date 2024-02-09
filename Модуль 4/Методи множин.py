numbers = {1, 2, 3}
numbers.add(4)
print(numbers)    # {1, 2, 3, 4}

numbers = {1, 2, 3}
numbers.remove(3)
print(numbers)    # {1, 2}

numbers = {1, 2, 3}
numbers.discard(2) # discard(elem) — видаляє елемент з множини і не викликає виняток, якщо його немає
print(numbers)    # {1, 3}
