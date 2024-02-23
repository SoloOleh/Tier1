def all_sub_lists(lst):
    sub_lists = [[]]
    # Спочатку додаємо одноелементні підсписки
    for i in range(len(lst)):
        sub_lists.append([lst[i]])
    # Потім додаємо підсписки довші за один елемент
    for length in range(2, len(lst) + 1):
        for start in range(len(lst) - length + 1):
            sub_lists.append(lst[start:start + length])
    return sub_lists

# Перевірка з оновленою логікою
all_sub_lists(example_list)


