

def show_even_numbers (start, end = 10, step = 1):
    for i in range (start, end + 1, step):
        if i % 2 == 0:
            print (f'{i} : {i**2}')

show_even_numbers (0, 20)


