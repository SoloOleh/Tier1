game_string = 'My "Game"'

s = "Hello world!"
print(s[0])   # H
print(s[-1])  # !

# s[0] = "Q" # Тут буде викликано виняток (помилка) TypeError

s = "Hello"
s.upper()  #усі літери рядка перевести у верхній регістр
print(s)    # Виведе 'HELLO'

s = "Some Text"
print(s.lower())    # переведення в нижній регістр # Виведе 'some text'

s = "Bill Jons"
print(s.startswith("Bi"))   # перевірити, що рядок починається з підрядка # Виведе True

s = "hello.jpg"
print(s.endswith("jpg"))    # перевірити, що рядок закінчується підрядком # Виведе True




