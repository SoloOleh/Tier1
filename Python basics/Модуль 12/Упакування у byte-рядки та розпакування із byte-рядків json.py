import json


some_data = {'key': 'value', 2: [1, 2, 3], 'tuple': (5, 6), 'a': {'key': 'value'}}

byte_string = json.dumps(some_data)
unpacked = json.loads(byte_string)

unpacked is some_data    # False
unpacked == some_data    # False

unpacked['key'] == some_data['key']     # True
unpacked['a'] == some_data['a']         # True
unpacked['2'] == some_data[2]           # True
unpacked['tuple'] == [5, 6]             # True
