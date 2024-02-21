chars = ['a', 'b']
chars.append('c')
print(chars)  # ['a', 'b', 'c']

chars = ['a', 'b']
chars.remove('b')
print(chars)  # ['a']

chars = ['a', 'b', 'c']
last = chars.pop(2) #Повернути i-ий елемент та видалити його зі списку i_element = my_list.pop(i). За замовчуванням i = -1
print(chars)  # ['a', 'b']
print(last)  # 'c'

chars = ['a', 'b']
numbers = [1, 2]
chars.extend(numbers)
print(chars)  # ['a', 'b', 1, 2]

chars = ["a", "b"]
chars.insert(1, "c")
print(chars)  # ['a', 'c', 'b']

chars = ['a', 'b']
last =  chars.clear() 
print(chars) # []

chars = ['a', 'b', 'c', 'd']
c_ind = chars.index('c') # Знайти індекс першого елемента у списку, що дорівнює x: index = my_list.index(x)
print(c_ind) #2

chars = ['a', 'b', 'c', 'a']
a_count = chars.count('a') # Повернути кількість елементів у списку, що дорівнюють x: x_number = my_list.count(x)
print(a_count) # 2

chars = ['z', 'a', 'b']
chars.sort() # Відсортувати список за зростанням: my_list.sort(key=None, reverse=False)
print(chars) # ['a', 'b', 'z']

chars = ['a', 'b']
chars.reverse() #Змінити порядок елементів у списку на зворотний: my_list.reverse()
print(chars) # ['b', 'a']

chars =  ['a', 'b']
chars_copy = chars.copy() #Повернути копію списку: copy_of_my_list = my_list.copy()
chars == chars_copy # True
