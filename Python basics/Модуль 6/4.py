# fh = open('text.txt')
# try:
#     some_useful_function(fh)
# except:
#     print('An error has occurred!')
# finally:
#     fh.close()

# #скорочено
# with open('text.txt', 'w+') as fh:
#     some_useful_function(fh)

def get_cats_info(path):
    result_list = []
    with open(path, 'r') as file:
        for line in file:
            id, name, age = line.strip().split(',')
            cat_dict = {
                'id': id,
                'name': name,
                'age': age
            }
            result_list.append(cat_dict)
    return result_list
# path = "/Users/solo/Desktop/IT/Repository/Tier1/Модуль 6/test.txt"
# print(get_cats_info(path))
# new_path = "/Users/solo/Desktop/IT/Repository/Tier1/Модуль 6/test2.txt"
# fh = open(new_path, "w")
# fh.write(f'{get_cats_info(path)}\n')  
# fh.close()
