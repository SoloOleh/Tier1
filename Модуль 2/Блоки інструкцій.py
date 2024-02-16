# x = int(input("X: "))
# y = int(input("Y: "))

# if x == 0:
#     print("X can`t be equal to zero")
#     x = int(input("X: "))
# result = y / x
# print (result)

# x = int(input("X: "))
# y = int(input("Y: "))

# if x == 0:
#     print("X can`t be equal to zero")
#     x = int(input("X: "))

#     if x == 0:
#         print("X can`t be equal to zero")
#         x = int(input("X: "))

#         if x == 0:
#             print("X can`t be equal to zero")
#             x = int(input("X: "))

# result = y / x
# x = int(input("X: "))
# y = int(input("Y: "))
if x >= 0:
    if y >= 0:               # x > 0, y > 0
        print("Перша чверть")
    else:                    # x > 0, y < 0
        print("Четверта чверть")
else:
    if y >= 0:               # x < 0, y > 0
        print("Друга чверть")
    else:                    # x < 0, y < 0
        print("Третя чверть")
