password = "qwerty123"
if "qwerty" in password or "123" in password:
    print("This password is too weak!")

prime_numbers = {2, 3, 5, 7, 11, 13, 17, 19, 23}
is_prime = 3 in prime_numbers
print (is_prime)

user = {
    "name": "Bill",
    "surname": "Bosh",
    "age": 22
}

if "age" in user:
    print(f"User is {user['age']} years old.")
