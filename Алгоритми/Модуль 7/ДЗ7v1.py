class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def __str__(self, level=0, prefix="Root: "):
        ret = "\\t" * level + prefix + str(self.val) + "\\n"
        if self.left:
            ret += self.left.__str__(level + 1, "L--- ")
        if self.right:
            ret += self.right.__str__(level + 1, "R--- ")
        return ret

# def insert(root, key):
#     if root is None:
#         return Node(key)
#     else:
#         if key < root.val:
#             root.left = insert(root.left, key)
#         else:
#             root.right = insert(root.right, key)
#     return root

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key == root.val:
            return root  # Ігноруємо вставку дубльованого значення
        elif key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def search(root, key):
    if root is None or root.val == key:
        return root
    if key < root.val:
        return search(root.left, key)
    return search(root.right, key)

def min_value_node(node):
    current = node
    while current.left:
        current = current.left
    return current

def delete(root, key):
    if not root:
        return root

    if key < root.val:
        root.left = delete(root.left, key)
    elif key > root.val:
        root.right = delete(root.right, key)
    else:
        if not root.left:
            temp = root.right
            root = None
            return temp
        elif not root.right:
            temp = root.left
            root = None
            return temp
        root.val = min_value_node(root.right).val
        root.right = delete(root.right, root.val)
    return root

# Task_1
def find_max_value(node):
    current = node
    while current.right is not None:
        current = current.right
    return current.val

# Task_2
def find_min_value(node):
    return min_value_node(node).val

# Task_3
def sum_of_values(node):
    if node is None:
        return 0
    return node.val + sum_of_values(node.left) + sum_of_values(node.right)

# Test
root = Node(5)
root = insert(root, 3)
root = insert(root, 2)
root = insert(root, 4)
root = insert(root, 7)
root = insert(root, 6)
root = insert(root, 8)


print(f"Найбільше значення у дереві: {find_max_value(root)}")
print(f"Найменше значення у дереві: {find_min_value(root)}")
print(f"Сума всіх значень у дереві: {sum_of_values(root)}")