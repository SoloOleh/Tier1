import uuid
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from collections import deque

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)

def draw_tree(tree, pos, colors, labels):
    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def bfs_visualization(root):
    if not root:
        return
    queue = deque([root])
    color_scale = mcolors.LinearSegmentedColormap.from_list("", ["darkblue", "lightblue"])
    i = 0
    max_depth = 10  # Adjust this according to your tree size
    while queue:
        current = queue.popleft()
        current.color = color_scale(i / max_depth)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
        tree = nx.DiGraph()
        pos = {root.id: (0, 0)}
        add_edges(tree, root, pos)
        colors = [node[1]['color'] for node in tree.nodes(data=True)]
        labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}
        draw_tree(tree, pos, colors, labels)
        i += 1

def dfs_visualization(root, pos, tree, color_scale, depth=0):
    if not root:
        return
    root.color = color_scale(depth / 10)  # Adjust depth for your tree size
    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}
    draw_tree(tree, pos, colors, labels)
    if root.left:
        dfs_visualization(root.left, pos, tree, color_scale, depth + 1)
    if root.right:
        dfs_visualization(root.right, pos, tree, color_scale, depth + 1)

# Create the tree
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Visualization of tree traversal
tree = nx.DiGraph()
pos = {root.id: (0, 0)}
add_edges(tree, root, pos)
color_scale = mcolors.LinearSegmentedColormap.from_list("", ["darkblue", "lightblue"])

bfs_visualization(root)
dfs_visualization(root, pos, tree, color_scale)

