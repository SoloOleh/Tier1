import networkx as nx
import matplotlib.pyplot as plt

# Створення графа
G = nx.Graph()

# Додавання нових вершин (зупинок громадського транспорту)
central_and_district_stops = ["Площа Ринок", "Вокзал", "Сихів", "Підзамче", "Франківський район"]

# Додавання нових ребер (маршрутів між зупинками)
new_routes = [("Площа Ринок", "Вокзал"), ("Площа Ринок", "Сихів"), ("Площа Ринок", "Підзамче"), ("Площа Ринок", "Франківський район")]

G.add_nodes_from(central_and_district_stops)
G.add_edges_from(new_routes)

# Візуалізація оновленого графу
plt.figure(figsize=(10, 8))
nx.draw(G, with_labels=True, node_color='lightgreen', node_size=2000, font_size=15, font_weight='bold', edge_color='gray')
plt.title("Транспортна мережа з'єднань між центром і районами Львова")
plt.show()

# Вивід основних характеристик оновленого графу
updated_num_nodes = G.number_of_nodes()
updated_num_edges = G.number_of_edges()
updated_degree_of_nodes = dict(G.degree())

updated_num_nodes, updated_num_edges, updated_degree_of_nodes


from collections import deque

# Граф, представлений як словник суміжності
graph_lviv = {
    'Площа Ринок': ['Вокзал', 'Сихів', 'Підзамче', 'Франківський район'],
    'Вокзал': ['Площа Ринок'],
    'Сихів': ['Площа Ринок'],
    'Підзамче': ['Площа Ринок'],
    'Франківський район': ['Площа Ринок']
}

def dfs_iterative(graph, start_vertex):
    visited = set()
    stack = [start_vertex]
    result = []
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            result.append(vertex)
            visited.add(vertex)
            # Додаємо сусідні вершини до стеку
            stack.extend(reversed(graph[vertex]))
    return result

def bfs_iterative(graph, start):
    visited = set()
    queue = deque([start])
    result = []
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            result.append(vertex)
            visited.add(vertex)
            # Додаємо сусідні вершини, які ще не були відвідані
            queue.extend(set(graph[vertex]) - visited)
    return result

# Запуск DFS і BFS
dfs_path = dfs_iterative(graph_lviv, 'Площа Ринок')
bfs_path = bfs_iterative(graph_lviv, 'Площа Ринок')

dfs_path, bfs_path


# Повторна реалізація DFS і BFS на прикладі графу транспортної мережі Львова

def dfs_iterative(graph, start_vertex):
    visited = set()
    stack = [start_vertex]
    result = []
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            result.append(vertex)
            visited.add(vertex)
            stack.extend(reversed(graph[vertex]))  # Додаємо сусідні вершини до стеку в зворотному порядку
    return result

def bfs_iterative(graph, start):
    visited = set()
    queue = deque([start])
    result = []
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            result.append(vertex)
            visited.add(vertex)
            queue.extend(set(graph[vertex]) - visited)  # Додаємо сусідні вершини, які ще не були відвідані
    return result

# Виконання DFS і BFS
dfs_result = dfs_iterative(graph_lviv, 'Площа Ринок')
bfs_result = bfs_iterative(graph_lviv, 'Площа Ринок')

dfs_result, bfs_result


import heapq

# Оновлений граф із вагами
graph_weighted = {
    'Площа Ринок': {'Вокзал': 10, 'Сихів': 15, 'Підзамче': 7, 'Франківський район': 20},
    'Вокзал': {'Площа Ринок': 10},
    'Сихів': {'Площа Ринок': 15},
    'Підзамче': {'Площа Ринок': 7},
    'Франківський район': {'Площа Ринок': 20}
}

def dijkstra(graph, start):
    # Відстані: від start до кожної вершини ініціалізуються як нескінченність, окрім стартової вершини (0)
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    # Черга з пріоритетами для відстеження мінімальної відстані
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Вузли можуть бути додані в чергу кілька разів. Потрібно перевірити, чи є шлях ще актуальним
        if current_distance > distances[current_vertex]:
            continue

        # Перегляд сусідів поточної вершини
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Тільки якщо знайдено коротший шлях до сусіда, то оновлюємо його відстань і ре-додаємо в чергу
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Запуск алгоритму Дейкстри від 'Площа Ринок'
shortest_paths = dijkstra(graph_weighted, 'Площа Ринок')
shortest_paths
