message = "Hello, "

def greet(name):
    print(message, name)

def greet2(name):
    random_variable = 14
    print(locals())
    message = "Good morning"
    print(message, name)

def greet3(name):
    global message
    message = "Good evening"
    print(message, name)


greet3("Jack")
print(globals())