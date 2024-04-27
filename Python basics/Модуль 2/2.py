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

#мій варіант
is_active = input("Is the user active? ")
is_admin = input("Is the user administrator? ")
is_permission = input("Does the user have access? ")
is_active = bool(is_active)
is_admin = bool(is_admin)
is_permission = bool(is_permission)
if is_active and is_permission:
    access = True 
    print ('You are user')
elif is_admin = True:
    access = True 
    print ('You are admin')
else:
    access = False 
    print ('Access denied')