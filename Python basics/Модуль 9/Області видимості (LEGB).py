# SOME_VAR = 3

# def func(x):
#     SOME_VAR = x
#     print(SOME_VAR)


# def procedure():
#     print(SOME_VAR)


# procedure()     # 3
# func(5)         # 5
# print(SOME_VAR) # 3

GLOBAL_SCOPE_VAR = 1

def func():
    enclosed_scope_var = 2
    def inner():
        inner_var = 3
