# num = [1, 3.1415, 41, 3]
# num.append(30)
# print(num)  # [1, 3.1415, 41, 3, 30]

# num = [1, 3.1415, 41, 3]
# num.insert(2, 30)
# print(num)  # [1, 3.1415, 30, 41, 3]

# num = [1, 3.1415, 41, 3]
# second = num.pop(1)
# print(second)  # 3.1415
# print(num)  # [1, 41, 3]

# num = [1, 3.1415, 41, 3]
# num.remove(3.1415)
# print(num)  # [1, 41, 3]

# num = [1, 3.1415, 41, 3]
# new_num = sorted(num)
# print(new_num)  # [1, 3, 3.1415, 41]
# print(num)  # [1, 3.1415, 41, 3]

# num = [1, 3.1415, 41, 3]
# num.sort() 
# print(num) 



# def prepare_data():
#     sorted_data = sorted(data)
#     return sorted_data
#     poped_data = sorted_data.pop(0, -1)
#     return 
# data = [1, 3.1415, 30, 41, 3]
# print(prepare_data())


def prepare_data(): #мій варіант не працює в автоперевірці
    data.sort()
    data.pop(0)
    data.pop(-1)
    return  
data = [10, 5, 8, 3, 12, 2]
prepare_data()
print (data)

def prepare_data(data): #мій працює в автоперевірці
    data.sort()
    data.pop(0)
    data.pop(-1)
    return data
data = [10, 5, 8, 3, 12, 2]
prepare_data(data)
print (data)

def prepare_data(data):
    data.remove(max(data))
    data.remove(min(data))
    data.sort()
    return data
data = [10, 5, 8, 3, 12, 2]
prepared_data = prepare_data(data)
print(f"Дані після обробки: {prepared_data}")
