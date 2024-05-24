# import uuid
# import networkx as nx
# import matplotlib.pyplot as plt
# from matplotlib.colors import to_hex
# import colorsys

# class Node:
#     def __init__(self, key, color="skyblue"):
#         self.left = None
#         self.right = None
#         self.val = key
#         self.color = color
#         self.id = str(uuid.uuid4())

# def add_edges(graph, node, pos, x=0, y=0, layer=1):
#     if node is not None:
#         graph.add_node(node.id, color=node.color, label=node.val)
#         if node.left:
#             graph.add_edge(node.id, node.left.id)
#             l = x - 1 / 2 ** layer
#             pos[node.left.id] = (l, y - 1)
#             add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
#         if node.right:
#             graph.add_edge(node.id, node.right.id)
#             r = x + 1 / 2 ** layer
#             pos[node.right.id] = (r, y - 1)
#             add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)

# def draw_tree(tree_root, highlight_nodes=[]):
#     tree = nx.DiGraph()
#     pos = {tree_root.id: (0, 0)}
#     add_edges(tree, tree_root, pos)
    
#     colors = [node[1]['color'] for node in tree.nodes(data=True)]
#     labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

#     plt.figure(figsize=(8, 5))
#     nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    
#     if highlight_nodes:
#         highlight_ids = [node.id for node in highlight_nodes]
#         highlight_colors = [node.color for node in highlight_nodes]
#         highlight_labels = {node.id: node.val for node in highlight_nodes}
#         nx.draw(tree, pos=pos, labels=highlight_labels, nodelist=highlight_ids, node_size=2500, node_color=highlight_colors, edge_color='r', width=2)
    
#     plt.show()

# def generate_colors(n):
#     colors = []
#     for i in range(n):
#         hue = i / n
#         lightness = (1 + i / n) / 2
#         rgb = colorsys.hls_to_rgb(hue, lightness, 1)
#         colors.append(to_hex(rgb))
#     return colors

# def dfs(node, visit_order, visited=None):
#     if visited is None:
#         visited = set()
#     if node and node.id not in visited:
#         visit_order.append(node)
#         visited.add(node.id)
#         dfs(node.left, visit_order, visited)
#         dfs(node.right, visit_order, visited)

# def bfs(node, visit_order):
#     queue = [node]
#     visited = set()
#     while queue:
#         current = queue.pop(0)
#         if current.id not in visited:
#             visit_order.append(current)
#             visited.add(current.id)
#             if current.left:
#                 queue.append(current.left)
#             if current.right:
#                 queue.append(current.right)

# def visualize_traversal(tree_root, traversal_func):
#     visit_order = []
#     traversal_func(tree_root, visit_order)
#     colors = generate_colors(len(visit_order))
#     for node, color in zip(visit_order, colors):
#         node.color = color
#     draw_tree(tree_root, highlight_nodes=visit_order)

# # Створення дерева
# root = Node(0)
# root.left = Node(4)
# root.left.left = Node(5)
# root.left.right = Node(10)
# root.right = Node(1)
# root.right.left = Node(3)

# # Відображення обходу в глибину
# print("Обхід в глибину (DFS):")
# visualize_traversal(root, dfs)

# # Відображення обходу в ширину
# print("Обхід в ширину (BFS):")
# visualize_traversal(root, bfs)


import uuid
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.colors import to_hex
import matplotlib.cm as cm

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

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

def draw_tree(tree_root, node_colors=None):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    if node_colors is None:
        colors = [node[1]['color'] for node in tree.nodes(data=True)]
    else:
        colors = [node_colors[node[0]] for node in tree.nodes(data=True)]
    
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def generate_colors(n):
    cmap = cm.get_cmap('viridis', n)
    colors = [to_hex(cmap(i)) for i in range(n)]
    return colors

def dfs(node, visit_order, colors, depth=0):
    if node:
        visit_order.append(node)
        node.color = colors[len(visit_order) - 1]
        if node.left:
            dfs(node.left, visit_order, colors, depth + 1)
        if node.right:
            dfs(node.right, visit_order, colors, depth + 1)

def bfs(root, visit_order, colors):
    queue = [root]
    while queue:
        node = queue.pop(0)
        visit_order.append(node)
        node.color = colors[len(visit_order) - 1]
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

# Функція для побудови дерева з масиву
def build_heap_tree(arr):
    nodes = [Node(key) for key in arr]
    for i in range(len(nodes)):
        left_index = 2 * i + 1
        right_index = 2 * i + 2
        if left_index < len(nodes):
            nodes[i].left = nodes[left_index]
        if right_index < len(nodes):
            nodes[i].right = nodes[right_index]
    return nodes[0] if nodes else None

# Елементи для бінарної купи
elements = [10, 20, 15, 30, 40, 50, 60]

# Побудова дерева
tree_root = build_heap_tree(elements)

# Генерація кольорів для вузлів
colors = generate_colors(len(elements))

# Обхід в глибину (DFS)
visit_order_dfs = []
dfs(tree_root, visit_order_dfs, colors)
draw_tree(tree_root)

# Перебудова дерева для обходу в ширину (BFS)
tree_root = build_heap_tree(elements)

# Обхід в ширину (BFS)
visit_order_bfs = []
bfs(tree_root, visit_order_bfs, colors)
draw_tree(tree_root)


