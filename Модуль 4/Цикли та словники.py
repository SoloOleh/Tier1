numbers = {
    1: "one",
    2: "two",
    3: "three"
}
for key in numbers:
    print(key)
for key in numbers.keys(): # це то саме що for key in numbers:
    print(key)
for val in numbers.values():
    print(val)
for key, value in numbers.items():
    print(key, value)
