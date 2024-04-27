def make_article(title, *topics):
    print(topics)
make_article("Title", "first", "second", "third")  # ('first', 'second', 'third')

def make_article(title, **comments):
    print(title, comments)
make_article("Title", comment_one="123", comment_two="second", comment_third="third")
# {'comment_one': 'first', 'comment_two': 'second', 'comment_third': 'third'}