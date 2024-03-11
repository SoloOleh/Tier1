number_1 = int(input ("Please enter the first number: "))
number_2 = int(input ("Please enter the second number: "))
operator = input ("Please enter the operator: ")
if operator == "+":
    print (f"{number_1}{operator}{number_2} = {number_1 + number_2}")
elif operator == "-":
    print (f"{number_1}{operator}{number_2} = {number_1 - number_2}")
elif operator == "*":
    print (f"{number_1}{operator}{number_2} = {number_1 * number_2}")
elif operator == "/":
    if number_2 != 0:
        print (f"{number_1}{operator}{number_2} = {number_1 / number_2}")
    else:
        print ("You can't divide by zero")
elif operator == "%":
    print (f"{number_1}{operator}{number_2} = {number_1 % number_2}")
else:
    print ("Invalid operator")