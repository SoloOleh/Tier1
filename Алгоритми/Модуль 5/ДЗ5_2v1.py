# def binary_search(arr, target):
#     low = 0
#     high = len(arr) - 1
#     iterations = 0
#     upper_bound = None

#     while low <= high:
#         iterations += 1
#         mid = (low + high) // 2
#         if arr[mid] < target:
#             low = mid + 1
#         elif arr[mid] > target:
#             high = mid - 1
#             upper_bound = arr[mid]  # Update upper_bound when we move left
#         else:
#             # When target is exactly found
#             upper_bound = arr[mid]
#             break

#     if upper_bound is None and low < len(arr):
#         upper_bound = arr[low]  # If target is greater than all elements

#     return (iterations, upper_bound)

# # Example usage
# arr = [0.5, 1.2, 3.3, 4.4, 5.6, 6.7, 7.8]
# target = 4.5
# print(binary_search(arr, target))

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    iterations = 0
    upper_bound = None

    while low <= high:
        iterations += 1
        mid = (low + high) // 2
        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
            upper_bound = arr[mid]  # Update upper_bound when we move left
        else:
            # When target is exactly found
            upper_bound = arr[mid]
            break

    # Ensure upper_bound is correct
    if upper_bound is None or upper_bound < target:
        if low < len(arr):
            upper_bound = arr[low]

    return (iterations, upper_bound)
