# num = None

# while num == None: # або num is None:
#     try:
#         num = int(input('please enter number: '))
#         num += 5
#         print (num)
#     except ValueError:
#         print ('you dumbass enter number')

try:
    a = 10
    b = int(input('please enter number: '))
    print (a / b)
# except ValueError:
#      print ('you dumbass enter number')
# except ZeroDivisionError:
#     print ('you dumbass do not divide by 0')
except Exception:
    print ('you dumbass')
else:
    print ('Good dog') 
finally:
    print ('bla') #наприклад зручно закривати файли 