from setuptools import setup

def do_setup(args_dict):
    setup(**args_dict)

# Приклад використання функції
args_dict = {
    "name": "useful",
    "version": "1",
    "description": "Very useful code",
    "url": "http://github.com/dummy_user/useful",
    "author": "Flying Circus",
    "author_email": "flyingcircus@example.com",
    "license": "MIT",
    "packages": ["useful"],
}
do_setup(args_dict)
