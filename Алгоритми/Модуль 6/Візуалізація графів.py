import networkx as nx
import matplotlib.pyplot as plt

G = nx.complete_graph(4)
options = {
    "node_color": "yellow",
    "edge_color": "lightblue",
    "node_size": 500,
    "width": 3,
    "with_labels": True
}
nx.draw(G, **options)
plt.show()


G = nx.complete_graph(4)
options = {
    "node_color": "yellow",
    "edge_color": "lightblue",
    "node_size": 500,
    "width": 3,
    "with_labels": True
}
nx.draw(G, **options)
plt.show()


G = nx.complete_graph(8)
pos = nx.circular_layout(G)
nx.draw(G, pos, with_labels=True)
plt.title("Circular Layout")
plt.show()


G = nx.complete_graph(8)
pos = nx.random_layout(G)
nx.draw(G, pos, with_labels=True)
plt.title("Random Layout")
plt.show()

G = nx.complete_graph(8)
pos = [[0, 1, 2], [3, 4], [5, 6, 7]]  # Вказує камери для розташування вершин
pos = nx.shell_layout(G, pos)
nx.draw(G, pos, with_labels=True)
plt.title("Shell Layout")
plt.show()




# Створення орієнтованого графа
G = nx.DiGraph()
# Додавання ребер
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 3), (4, 1)])
# Малювання графа
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, arrows=True)
plt.show()


# Створення графа
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

G = nx.Graph(graph)

# DFS
dfs_tree = nx.dfs_tree(G, source='A')
print(list(dfs_tree.edges()))  # виведе ребра DFS-дерева з коренем у вузлі A

# BFS
bfs_tree = nx.bfs_tree(G, source='A')
print(list(bfs_tree.edges()))  # виведе ребра BFS-дерева з коренем у вузлі A
