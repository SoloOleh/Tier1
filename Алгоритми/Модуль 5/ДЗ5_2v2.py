# def binary_search(arr, target):
#     low = 0
#     high = len(arr) - 1
#     iterations = 0
#     best_index = None

#     while low <= high:
#         iterations += 1
#         mid = (low + high) // 2
#         if arr[mid] < target:
#             low = mid + 1
#         elif arr[mid] > target:
#             high = mid - 1
#             best_index = mid  # Зберігаємо потенційну верхню межу
#         else:
#             # Якщо знайдено точне значення, вертаємо його
#             return (iterations, arr[mid])

#     # Якщо точного значення не знайдено, то best_index має вказувати на найближчий більший елемент
#     if best_index is not None:
#         return (iterations, arr[best_index])
#     elif low < len(arr):
#         # Якщо всі елементи були менші за target
#         return (iterations, arr[low])
#     else:
#         # Якщо target більше за всі елементи у масиві
#         return (iterations, None)  # Верхньої межі немає

# # Приклад використання
# arr = [1.5, 2.3, 3.4, 4.7, 5.6, 6.8, 8.9]
# target = 4.5
# print(binary_search(arr, target))  # Виведе кількість ітерацій і верхню межу


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    iterations = 0
    best_index = None

    while low <= high:
        iterations += 1
        mid = (low + high) // 2
        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
            best_index = mid  # Зберігаємо потенційну верхню межу
        else:
            return (iterations, arr[mid])

    if best_index is not None and arr[best_index] >= target:
        return (iterations, arr[best_index])
    if low < len(arr) and arr[low] >= target:
        return (iterations, arr[low])
    return (iterations, None)  # Якщо верхньої межі немає

# Приклад використання
arr = [1.5, 2.3, 3.4, 4.7, 5.6, 6.8, 8.9]
target = 4.5
print(binary_search(arr, target))  # Виведе кількість ітерацій і верхню межу

