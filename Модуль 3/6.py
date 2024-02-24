# def make_article(title, *topics):
#     print(topics)
# make_article("Title", "first", "second", "third")  # ('first', 'second', 'third')

# def make_article(title, **comments):
#     print(comments)
# make_article("Title", comment_one="first", comment_two="second", comment_third="third")
# # {'comment_one': 'first', 'comment_two': 'second', 'comment_third': 'third'}

def first(size, *args):
    return size + len(args)
print(first(5, "first", "second", "third"))
print(first(1, "Alex", "Boris"))
def second(size, **kwargs):
    return size + len(kwargs)
print(second(3, comment_one="first", comment_two="second", comment_third="third"))
print(second(10, comment_one="Alex", comment_two="Boris"))

# мій варіант не канає
# def first(size, *args):
#     print (size, args)
# first(5, "first", "second", "third")
# first(1, "Alex", "Boris")
    
# def second(size, **kwargs):
#     print (size, kwargs)
# second(3, comment_one="first", comment_two="second", comment_third="third")
# second(10, comment_one="Alex", comment_two="Boris")