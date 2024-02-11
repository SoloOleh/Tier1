# # empty = set()
# # print(empty)  # set()

# # string_set = set("My set")
# # print(string_set)  # {'s', ' ', 'y', 'M', 't', 'e'}
# # list_set = set(["My", "set"])  # {'My', 'set'}
# # print(list_set)

# # new_set = {1, 2, 3, "My", "set", "H", "i"}
# # print(new_set)  # {1, 2, 3, 'My', 'i', 'set', 'H'}
# # add(elem) - додає елемент у множину
# # remove(elem) — видаляє елемент із множини, викликає виключення, якщо такого елемента не існує
# # discard(elem) - видаляє елемент з множини, але не викликає виключення, якщо його не існує

# first = {1, 2, 3}
# second = {3, 4, 5}
# print(first & second)  # {3} спільні елементи двох множин

# first = {1, 2, 3}
# second = {3, 4, 5}
# print(first ^ second)  # {1, 2, 4, 5} всі елементи з двох множин, крім спільних,

# first = {1, 2, 3}
# second = {3, 4, 5}
# print(first | second)  # {1, 2, 3, 4, 5} Об'єднання двох множин

# first = {1, 2, 3}
# second = {3, 4, 5}
# print(first - second)  # {1, 2} Віднімання двох множин

# first = set([1, 2, 3, 4])
# second = set([2, 3])
# print(list(first - second))  # [1, 4] ивести всі елементи першого списку, яких немає у другому


def is_valid_pin_codes(pin_codes):
    if len(pin_codes) == 0:
        return False
    for pin_code in pin_codes:
        if len(pin_code) != 4:
            return False
        if not (isinstance(pin_code, str)):
            return False
        if not pin_code.isdigit():
            return False
    return len(set(pin_codes)) == len(pin_codes)