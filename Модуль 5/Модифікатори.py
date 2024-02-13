s = "{name} {last_name}".format(last_name="Dilan", name="Bob")
print(s)   # Bob Dilan

s =  "{name!r} {last_name!s}".format(last_name="Dilan", name="Bob")
print(s)  # 'Bob' Dilan

