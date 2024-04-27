from collections import UserString


class NumberString(UserString):
    def number_count(self):
        count = 0
        for char in self.data:
            if char.isdigit():
                count += 1
        return count

# Приклад використання:
s = NumberString("Hello 123 World")
print(s.number_count())  # Виведе: 3
