def info(word):
    print (word, end = '')
    print ('!')

# test_func('hello')
# words = 'home'
# test_func(words)
# test_func ('Hi')

# def summa(a, b):
#     res = a + b
#     info(res)
#     return res

# res1 = summa(5, 6)
# res2 = summa ('Hi', ' world')

nums1 = [5,3,7,3, -5, 0]
min_num = nums1[0]
for i in nums1:
    if i < min_num:
        min_num = i
print (min_num)

def minimal(l):
    min_num = l[0]
    for i in l:
        if i < min_num:
            min_num = i
    return min_num

res1 = minimal(nums1)

print (res1)


func = lambda x, y: x * y
print (func (5, 6))