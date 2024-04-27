money = 0
if money:
    print(f"You have {money} on your bank account")
else:
    print("You have no money and no debts")

result = None #але канає 0 та 1
if result:
    print(result)
else:
    print("Result is None, do something")

user_name = input("Enter your name: ")
if user_name:
    print(f"Hello {user_name}")
else:
    print("Hi Anonym!")

a = True and False # False
print (a)

a = True or False  # True
print (a)

a = 2 < 0  # False
print (a)

a = not 2 < 0  # True
print (a)