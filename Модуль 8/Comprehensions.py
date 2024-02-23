sq = []
for i in range(1, 5+1):
    sq.append(i**2)
print(sq)   # [1, 4, 9, 16, 25]

numbers = [i for i in range(1, 5+1)]
sq = [i ** 2 for i in range(1, 5+1)]
print(sq)

numbers = [1, 4, 1, 3, 2, 5, 2, 6]
sq = {i ** 2 for i in numbers}
print(sq)   # {1, 4, 36, 9, 16, 25}

numbers = [1, 4, 1, 3, 2, 5, 2, 6]
sq = {i: i ** 2 for i in numbers}
print(sq)   # {1: 1, 4: 16, 3: 9, 2: 4, 5: 25, 6: 36}
