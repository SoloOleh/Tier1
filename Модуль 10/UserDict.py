from collections import UserDict


class ValueSearchableDict(UserDict):
    def has_in_values(self, value):
        return value in self.data.values()


as_dict = ValueSearchableDict()
as_dict['a'] = 1
as_dict.has_in_values(1)    # True
as_dict.has_in_values(2)    # False
