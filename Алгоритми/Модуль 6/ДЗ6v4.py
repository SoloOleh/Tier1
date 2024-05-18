import networkx as nx
import matplotlib.pyplot as plt

# Створити граф
G = nx.Graph()

# Додати вершини та ребра
stops = ["Площа Ринок", "Проспект Свободи", "Вулиця Личаківська", 
         "Площа Соборна", "Вулиця Шевченка", "Вулиця Замарстинівська"]
routes = [
    ("Площа Ринок", "Проспект Свободи"),
    ("Проспект Свободи", "Вулиця Личаківська"),
    ("Вулиця Личаківська", "Площа Соборна"),
    ("Площа Соборна", "Вулиця Шевченка"),
    ("Вулиця Шевченка", "Вулиця Замарстинівська"),
    ("Площа Ринок", "Вулиця Замарстинівська"),
    ("Проспект Свободи", "Площа Соборна"),
    ("Вулиця Личаківська", "Вулиця Шевченка"),
]
G.add_nodes_from(stops)
G.add_edges_from(routes)

# Візуалізувати граф
nx.draw(G, node_size=400, node_color='skyblue', edge_color='gray', with_labels=True)  # Use with_labels instead of node_labels
plt.show()

print(f"Кількість вершин: {nx.number_of_nodes(G)}")
print(f"Кількість ребер: {nx.number_of_edges(G)}")
print(f"Ступені вершин: {nx.degree(G)}")

def dfs(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node in visited:
            continue

        visited.add(node)
        print(node)

        for neighbor in graph.neighbors(node):
            stack.append(neighbor)


def bfs(graph, start):
    visited = set()
    queue = [start]

    while queue:
        node = queue.pop(0)
        if node in visited:
            continue

        visited.add(node)
        print(node)

        for neighbor in graph.neighbors(node):
            queue.append(neighbor)

dfs(G, "Площа Ринок")
bfs(G, "Площа Ринок")

# Додати ваги до ребер
edge_weights = {
    ("Площа Ринок", "Проспект Свободи"): 2,
    ("Проспект Свободи", "Вулиця Личаківська"): 4,
    ("Вулиця Личаківська", "Площа Соборна"): 3,
    ("Площа Соборна", "Вулиця Шевченка"): 5,
    ("Вулиця Шевченка", "Вулиця Замарстинівська"): 10,
    ("Площа Ринок", "Вулиця Замарстинівська"): 6,
    ("Проспект Свободи", "Площа Соборна"): 2,
    ("Вулиця Личаківська", "Вулиця Шевченка"): 8,
}

nx.add_edge_weights(G, edge_weights)


def dijkstra(graph, start):
    shortest_paths = {node: float('inf') for node in graph.nodes()}
    shortest_paths[start] = 0

    processed = set()
    while processed != graph.nodes():
        current_node = min((node, shortest_paths[node]) for node in graph.nodes() if node not in processed)
        processed.add(current_node)

        for neighbor in graph.neighbors(current_node):
            weight = graph.edges[current_node, neighbor]['weight']
            new_path = shortest_paths[current_node] + weight
            if new_path < shortest_paths[neighbor]:
                shortest_paths[neighbor] = new_path

    return shortest_paths

# Знайти найкоротші шляхи від початкової вершини до всіх інших
shortest_paths = dijkstra(G, "Площа Ринок")

# Вивести найкоротші шляхи до деяких вершин
for node, distance in shortest_paths.items():
    if distance != float('inf'):
        print(f"Найкоротший шлях до {node}: {distance}")

