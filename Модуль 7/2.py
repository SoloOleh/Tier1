from setuptools import setup


def do_setup(args_dict, requires):
    setup(name=args_dict['name'],
          version=args_dict['version'],
          description=args_dict['description'],
          url=args_dict['url'],
          author=args_dict['author'],
          author_email=args_dict['author_email'],
          license=args_dict['license'],
          packages=args_dict['packages'],
          install_requires=requires)

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

# Приклад залежностей
requires = ['numpy', 'pandas']

# Виклик функції з заданими параметрами
do_setup(args_dict, requires)

# do_setup(args_dict, requires=args_dict['requires'])