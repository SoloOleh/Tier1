import random
import timeit
from typing import List

# Implementation of insertion sort
def insertion_sort(arr: List[int]) -> List[int]:
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Implementation of merge sort
def merge_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    return merge(left_half, right_half)

def merge(left: List[int], right: List[int]) -> List[int]:
    sorted_list = []
    left_index, right_index = 0, 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            sorted_list.append(left[left_index])
            left_index += 1
        else:
            sorted_list.append(right[right_index])
            right_index += 1
    sorted_list.extend(left[left_index:])
    sorted_list.extend(right[right_index:])
    return sorted_list

# Testing with random data sets of different sizes
sizes = [100, 1000, 10000]
results = []

for size in sizes:
    data = [random.randint(0, 1000) for _ in range(size)]
    t_insertion = timeit.timeit('insertion_sort(data.copy())', globals=globals(), number=1)
    t_merge = timeit.timeit('merge_sort(data.copy())', globals=globals(), number=1)
    t_tim = timeit.timeit('sorted(data.copy())', globals=globals(), number=1)
    results.append(f'test data size: {size}, insertion {t_insertion}, merge {t_merge}, phyton {t_tim}')

results

print(results)  
