import uuid
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def insert(root, key):
    new_node = Node(key)
    queue = [root]
    while queue:
        current = queue.pop(0)
        if not current.left:
            current.left = new_node
            heapify_up(current.left)
            return root
        elif not current.right:
            current.right = new_node
            heapify_up(current.right)
            return root
        queue.append(current.left)
        queue.append(current.right)

def heapify_up(node):
    while node != root:
        parent = find_parent(root, node)
        if parent and parent.val > node.val:
            parent.val, node.val = node.val, parent.val
        node = parent

def find_parent(root, child):
    queue = [root]
    while queue:
        current = queue.pop(0)
        if current.left == child or current.right == child:
            return current
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return None

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

# Створення та візуалізація бінарної купи
root = Node(0)
insert(root, 4)
insert(root, 5)
insert(root, 10)
insert(root, 1)
insert(root, 3)

draw_tree(root)
