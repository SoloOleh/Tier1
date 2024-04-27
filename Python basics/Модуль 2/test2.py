# a = "Hello world! What is the weather ?"
# for char in a:
#     print (char)
#     if char.lower() == "i":
#         break
# print ("The end")

a = "iiiHello world! What is the weather ?"
for char in a:
    # print (char)
    if char.lower() == "i":
        continue
    print (char)
  