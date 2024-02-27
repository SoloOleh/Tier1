# import time 
import datetime as d
import sys
import os
# print (sys.path)
# print (os.name)
# print (platform.system())



# from math import sqrt as s, ceil
# print (ceil(s(25)))

# time.sleep(2)
# print (d.datetime.now().time())

# import mymodule as my
from mymodule import add_3_numbers as add

# my.hi()
# print (my.name)
# res = my.add_3_numbers(3,5,7)
res = add(3, 5, 7)
print(res)

import cowsay

cowsay.cow ("Hello")