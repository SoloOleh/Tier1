# my_tuple = tuple()
# another_tuple = ()

# not_empty = (1, 2, 3)
# other_tuple = 4, 5

# not_empty = (1, 2, 3)
# not_empty[0]  # 1
# not_empty[1]  # 2
# not_empty[2]  # 3
# print (not_empty[0])

# single_tuple = (7,)

# x, y = 1, 2  # x = 1, y = 2
# x, y = y, x  # обмін значеннями між змінними x = 2, y = 1

def split_list(grade):
    if len(grade) == 0:
        return [], []
    less_then_average, greater_than_average = [], []
    average = sum(grade) / len(grade)

    for student_grade in grade:
        if student_grade <= average:
            less_then_average.append(student_grade)
        else:
            greater_than_average.append(student_grade)
    return less_then_average, greater_than_average