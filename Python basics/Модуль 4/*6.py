# user_1 = {"name": "Jane", "age": 21}
# user_2 = {"name": "Moris", "age": 23}
# user_3 = {"name": "Steve", "age": 24}

# persons = [user_1, user_2, user_3]

# for user in persons:
#     for field in user:
#         print(user.get(field))

def game(terra, power):
    for sub_list in terra:
        for element in sub_list:
            if element <= power:
                power += element
            else:
                break
    return power