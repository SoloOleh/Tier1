my_list = [1, 2, 3]
copy_list = my_list
copy_list.append(4)
print(my_list)  # [1, 2, 3, 4]


my_list = [1, 2, 3]
copy_list = my_list[:]
copy_list.append(4)
print(my_list)  # [1, 2, 3]
print (copy_list) # [1, 2, 3, 4]

d = {1: 'a'}
d_copy = {**d}
d_copy[2] = 'b'
print(d)        # {1: 'a'}
print(d_copy)   # {1: 'a', 2: 'b'}
