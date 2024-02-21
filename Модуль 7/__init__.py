# import utility
# utility.useful.functions.nice_function 
# utility.dummy.functions.not_bad()

# або 
# from utility.useful.functions import nice_function
# from utility.dummy.functions import not_bad
# nice_function()
# not_bad()

# Якщо ж розробник подумав про користувача і __init__.py виглядає ось так:
from utility.useful.functions import nice_function
from utility.dummy.functions import not_bad
__all__ = ['nice_function', 'not_bad']

# Тоді можна скористатися таким імпортом:
# from utility import nice_function, not_bad
# nice_function()
# not_bad()

# або:
# from utility import *
# nice_function()
# not_bad()


