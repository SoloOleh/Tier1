# File = None
# try:
#     file = open('/Users/solo/Desktop/IT/Repository/Tier1/Школа/myfile.txt', 'r')
#     print (file.read())
#     file.close()
# except FileNotFoundError:
#     print('File Not Found')
# finally:
#     file.close()

# замість того всього вище

try:
    with open('Школа/myfile.txt', 'r', encoding = 'utf-8') as file: #with as автоматично зачиняє 
        print (file.read())
except FileNotFoundError:
    print('File Not Found')