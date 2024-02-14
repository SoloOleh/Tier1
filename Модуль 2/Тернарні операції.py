is_nice = True
state = "nice" if is_nice else "not nice"
print (state)

is_nice = True
if is_nice:
    state = "nice"
else:
    state = "not nice"
print(state)


some_data = None #0 також як none
msg = some_data or "Не було повернено даних"
print (msg)
