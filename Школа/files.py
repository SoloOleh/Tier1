# data = input('Hobby: ')

# file = open('/Users/solo/Desktop/IT/Repository/Tier1/Школа/myfile.txt', 'a')
# file.write(data + '\n')

# file.close()


file = open('/Users/solo/Desktop/IT/Repository/Tier1/Школа/myfile.txt', 'r')
# print (file.read(10))
for line in file:
    print (line, end = '')

file.close()