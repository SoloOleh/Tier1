"""" Спочатку я закодив так проте завжди любий текст виходив True
is_active = bool(input("Is the user active? "))
is_admin = bool(input("Is the user administrator? "))
is_permission = bool(input("Does the user have access? "))

access = is_admin or (is_permission and is_active)
if access:
    print("Користувач має доступ!")
else:
    print("Користувач не має доступу")
"""

is_active = input("Is the user active? ") == "1"
is_admin = input("Is the user administrator? ") == "1"
is_permission = input("Does the user have access? ") == "1"
access = is_admin or (is_permission and is_active)
print (access)