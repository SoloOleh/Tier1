def total(a=5, *numbers, **phone_book): #numbers — це кортеж, а phone_book — словник.
    print('a', a)
    # прохід по всіх елементах кортежу
    for single_item in numbers:
        print('single_item', single_item)

    #прохід по всіх елементах словника
    for first_part, second_part in phone_book.items():
        print(first_part,second_part)

print(total(10, 1, 2, 3, Jack=1123, John=2231, Inge=1560))

# a 10
# single_item 1
# single_item 2
# single_item 3
# Jack 1123
# John 2231
# Inge 1560
# None

