import timeit
import random

def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >= 0 and key < lst[j]:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = key
    return lst

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged, left_index, right_index = [], 0, 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged

def python_timsort(arr):
    return sorted(arr)

test_data_sizes = [100, 1000, 10000]
sort_functions = [insertion_sort, merge_sort, python_timsort]
results = {}

for size in test_data_sizes:
    test_data = [random.randint(1, 1000) for _ in range(size)]
    results[size] = {}
    for sort_function in sort_functions:
        stmt = f"{sort_function.__name__}(test_data.copy())"
        setup = f"from __main__ import test_data, {sort_function.__name__}"
        time_taken = timeit.timeit(stmt, setup=setup, number=1)
        results[size][sort_function.__name__] = time_taken

results

print(results) 

"""
{100: {'insertion_sort': 0.000883166998391971, 'merge_sort': 0.0006915410049259663, 'python_timsort': 3.5792007111012936e-05}, 
1000: {'insertion_sort': 0.11027183299302123, 'merge_sort': 0.009454666986130178, 'python_timsort': 0.0005692089907824993}, 
10000: {'insertion_sort': 12.402782333025243, 'merge_sort': 0.12606800001231022, 'python_timsort': 0.008812084008241072}}
"""

""" Timsort ефективно використовує переваги обох сортувань: вставками на малих сегментах даних та злиттям для більших. 
Це робить його швидким і ефективним навіть на великих масивах. 
Тому більшість людей використовують вбудовані алгоритми сортування в Python, а не пишуть свої. """