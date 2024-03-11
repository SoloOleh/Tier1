sentences = ["I am learning strings in Python", "Some new methods got now."]
text = ". ".join(sentences)
print(text) # I am learning strings in Python. Some new methods got now.

clean = '   spacious   '.strip() # видалити зайві пробіли на початку і в кінці рядка\
# "лівий", lstrip, видаляє тільки пробіли на початку рядка;
# та "правий", rstrip, видаляє тільки пробіли в кінці рядка.
print(clean)  # spacious

dogs_text = "All dogs bark like dogs."
cats_text = dogs_text.replace("dogs", "cats")
print(cats_text) # All cats bark like cats.

print('TestHook'.removeprefix('Test'))   # Hook
print('TestHook'.removeprefix('Hook'))   # TestHook

print('TestHook'.removesuffix('Hook'))   # Test
print('TestHook'.removesuffix('Test'))   # TestHook

text_2 = 'TestHook'
text_3 = text_2.removeprefix('Test')
print(text_3)   # Hook
