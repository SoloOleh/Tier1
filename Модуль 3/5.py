# def fun(a, b=2, c=3):
#     return a + b * c
# a = int(input("enter a "))
# test = fun(a, b=2, c=3)
# print (test)

def get_fullname(first_name, last_name, middle_name=None):
  if middle_name:
    return f"{first_name} {middle_name} {last_name}"
  else:
    return f"{first_name} {last_name}"
 
full_name = get_fullname("Oleh", "Solomko")
print(full_name)  
full_name = get_fullname("Oleh", "Solomko", "Bohdanovych")
print(full_name)  
