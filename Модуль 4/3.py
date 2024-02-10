# lang = {"Python": 1991, "Java": 1995}
# lang["Java"] = 1991
# lang["JS"] = 1995
# print(lang)  # {"Python": 1991, "Java": 1991, "JS": 1995}

# lang = {"Python": 1991, "Java": 1995}
# lang["Java"] = 1991
# lang["JS"] = 1995
# print(lang)  # {"Python": 1991, "Java": 1991, "JS": 1995}

# lang = {"Python": 1991, "Java": 1995}
# result = lang.pop("Python")
# print(result)  # 1991
# print(lang)  # {"Java": 1995}

# lang = {"Python": 1991, "Java": 1995}
# lang.update({"JS": 1995})
# print(lang)  # {"Python": 1991, "Java": 1995, "JS": 1995}

# lang = {"Python": 1991, "Java": 1995}
# lang.clear()
# print(lang)  # {}

# lang = {"Python": 1991, "Java": 1995}
# new_lang = lang.copy()
# print(new_lang)  # {"Python": 1991, "Java": 1995}
# print(lang)  # {"Python": 1991, "Java": 1995}

# lang = {"Python": 1991, "Java": 1995}
# java = lang.get("Java", 1991)  # 1995
# js = lang.get("JS", 1995)  # 1995
# pascal = lang.get("Pascal")  # None
# print(lang)