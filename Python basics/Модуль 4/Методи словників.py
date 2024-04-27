chars = {'a': 1, 'b': 2}
b_num = chars.pop('b') #pop(key) — повертає значення елементу і видаляє пару ключ-значення зі словника
print(chars)  # {'a': 1}
print(b_num)  # 2

chars = {'a': 1, 'b': 2}
chars.update({'b': 4, "c": 3})
print(chars)  # {'a': 1, 'b': 4, 'c': 3}

chars = {'a': 1, 'b': 2}
chars.clear()
print(chars)  # {}

chars = {'a': 1, 'b': 2}
chars_copy = chars.copy()
chars_copy == chars  # True
print(chars_copy) 

chars = {'a': 1, 'b': 2}
c_idx = chars.get('c', -1) #get(key[, default]) — не викликає виключення, якщо ключа немає в словнику, повертає default, за замовчуванням default=None.
print(c_idx)  # -1