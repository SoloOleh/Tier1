def say_hello(name):
    print(f'Hello {name}')
if __name__ == '__main__':
    print("You imported hello.py")
    say_hello('user')


def say_hello(name):
    print(f'Hello {name}')

def main():
    print("You imported hello.py")
    say_hello('user')

for arg in sys.argv: # не працює
    print(arg)
if __name__ == '__main__':
    main()