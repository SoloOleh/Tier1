def get_item_by_index(items, index):
    return items[index]

def reverse_list(items):
    return items[::-1]

def generate_pairs(items):
  return [(items[i], items[j]) for i in range(len(items)) for j in range(i+1, len(items))]

items = [1, 2, 3, 4]
print(generate_pairs(items))