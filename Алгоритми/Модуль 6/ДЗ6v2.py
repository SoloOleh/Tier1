import networkx as nx
import matplotlib.pyplot as plt

# Створення графа
G = nx.Graph()

# Додавання вершин (районів)
nodes = ["Центр", "Сихів", "Личаківський район", "Франківський район", "Залізничний район", "Винники"]
G.add_nodes_from(nodes)

# Додавання ребер (маршрутів)
edges = [
    ("Центр", "Сихів", {"weight": 7}),
    ("Центр", "Франківський район", {"weight": 3}),
    ("Личаківський район", "Франківський район", {"weight": 5}),
    ("Залізничний район", "Сихів", {"weight": 6}),
    ("Винники", "Центр", {"weight": 8})
]
G.add_edges_from(edges)

# Візуалізація графа
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G)  # Розміщення вершин за допомогою алгоритму
nx.draw_networkx_nodes(G, pos, node_size=7000, node_color='lightblue')
nx.draw_networkx_edges(G, pos, width=2, alpha=0.6, edge_color='gray')
nx.draw_networkx_labels(G, pos, font_size=12, font_family="sans-serif")
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): d['weight'] for u, v, d in G.edges(data=True)}, font_color='red')
plt.title("Граф транспортної мережі м. Львова")
plt.axis('off')  # Вимкнення осей для кращого візуального представлення
plt.show()

# Основні характеристики графа
number_of_nodes = G.number_of_nodes()
number_of_edges = G.number_of_edges()
degrees = G.degree()

number_of_nodes, number_of_edges, dict(degrees)



def dfs_iterative(graph, start_vertex):
    visited = set()
    stack = [start_vertex]
    dfs_order = []

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            dfs_order.append(vertex)
            visited.add(vertex)
            stack.extend(reversed([v for v in graph[vertex] if v not in visited]))

    return dfs_order

def bfs_iterative(graph, start):
    visited = set()
    queue = [start]
    bfs_order = []

    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            bfs_order.append(vertex)
            visited.add(vertex)
            queue.extend([v for v in graph[vertex] if v not in visited])

    return bfs_order

# Виконання DFS і BFS
start_vertex = "Центр"
dfs_result = dfs_iterative(G, start_vertex)
bfs_result = bfs_iterative(G, start_vertex)

dfs_result, bfs_result



import heapq

def dijkstra(graph, start_vertex):
    # Ініціалізація відстаней: відстань до стартової вершини 0, для всіх інших нескінченність
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start_vertex] = 0
    # Приорітетна черга для тримання вершин з найменшими відстанями
    priority_queue = [(0, start_vertex)]
    
    while priority_queue:
        # Вилучаємо вершину з найменшою відстанню
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        # Ітерація по сусідніх вершинах і оновлення відстаней
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight['weight']
            
            # Якщо знайдена менша відстань, оновлюємо і додаємо в чергу
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

# Виконання алгоритму Дейкстри з початкової вершини "Центр"
dijkstra_result = dijkstra(G, "Центр")
dijkstra_result
