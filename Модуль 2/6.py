num = int(input("Enter an integer number: "))

is_even = True if num % 2 == 0 else False
print (is_even)

# мій варіант 
num = int(input("Enter an integer number: "))
if num % 2 == 0:
    is_even = True
elif num % 2 == 1:
    is_even = False