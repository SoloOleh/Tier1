class A:
    x = 'I am A class'


class B:
    x = 'I am B class'
    y = 'I exist only in B'


class C(A, B):
    z = "This exists only in C"


c = C()
print(c.z)  # This exists only in C
print(c.y)  # I exist only in B
print(c.x)  # I am A class




class A:
    x = 'I am A class'


class B:
    x = 'I am B class'
    y = 'I exist only in B'


class C(B, A):
    z = "This exists only in C"


c = C()
print(c.z)  # This exists only in C
print(c.y)  # I exist only in B
print(c.x)  # I am B class
