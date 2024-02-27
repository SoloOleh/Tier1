# work = True
# while work:
#     user_input = input("please enter stop ")
#     if user_input == "stop":
#             work = False

# for i in range(1,11):
#     if i % 2 == 0:
#         continue
#     if i == 7:
#         break
#     print ("El:", i)

# for i in "Hello World!":
#     if i == 'v':
#         print ('found v')
#         break
#     else:
#         print ('not found')
#         break

# # abo

# for i in "Hello World!":
#     if i == 'v':
#         print ('found v')
#         break
# else:
#     print ('not found')


# nums = [1, 2, 5, 10.5, 45]
# for el in nums:
#     res = el **2
#     print(res)

user_count_hobby = input ("Enter hobby number: ") #можна до int
i = 0
hobby = []
while i < int(user_count_hobby):
    text = "Enter hooby: " + str(i + 1) + ": "
    hobby.append(input (text))
    i = i + 1

print (hobby)