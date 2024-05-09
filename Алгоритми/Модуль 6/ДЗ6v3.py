import networkx as nx
import matplotlib.pyplot as plt

# Створення графа
G = nx.Graph()

# Додавання вершин (районів міста)
G.add_nodes_from(['Центр', 'Сихів', 'Личаків', 'Франківський', 'Шевченківський', 
                  'Залізничний', 'Левандівка', 'Рясне', 'Збоїща', 'Козельники', 
                  'Білогорща', 'Майорівка', 'Зубра', 'Кульпарків', 'Богданівка'])

# Додавання ребер (маршрутів транспорту)
G.add_edges_from([('Центр', 'Сихів'), ('Центр', 'Личаків'), ('Центр', 'Франківський'),
                  ('Сихів', 'Личаків'), ('Сихів', 'Шевченківський'), ('Сихів', 'Зубра'), 
                  ('Личаків', 'Франківський'), ('Личаків', 'Левандівка'), ('Личаків', 'Рясне'),
                  ('Франківський', 'Шевченківський'), ('Франківський', 'Залізничний'), 
                  ('Шевченківський', 'Залізничний'), ('Шевченківський', 'Рясне'), ('Шевченківський', 'Збоїща'),
                  ('Залізничний', 'Левандівка'), ('Левандівка', 'Рясне'), ('Левандівка', 'Козельники'),
                  ('Рясне', 'Збоїща'), ('Збоїща', 'Козельники'), ('Козельники', 'Білогорща'),
                  ('Білогорща', 'Майорівка'), ('Майорівка', 'Кульпарків'), ('Кульпарків', 'Богданівка')])

# Візуалізація графа
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, font_weight='bold')
plt.show()

# Аналіз характеристик графа
print(f"Кількість вершин: {G.number_of_nodes()}")
print(f"Кількість ребер: {G.number_of_edges()}")
print("Ступені вершин:")
for node, degree in G.degree():
    print(f"{node}: {degree}")
    
# Реалізація DFS
def dfs(graph, start):
    visited = set()
    stack = [start]
    path = []
    
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            path.append(vertex)
            stack.extend(graph[vertex] - visited)
            
    return path

# Реалізація BFS 
def bfs(graph, start):
    visited = set()
    queue = [start]
    path = []
    
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            path.append(vertex)
            queue.extend(graph[vertex] - visited)
            
    return path

# Приклад використання DFS та BFS
start_node = 'Центр'
dfs_path = dfs(G, start_node)
bfs_path = bfs(G, start_node)

print(f"\nШлях DFS від вершини '{start_node}': {' -> '.join(dfs_path)}")
print(f"Шлях BFS від вершини '{start_node}': {' -> '.join(bfs_path)}")

# Реалізація алгоритму Дейкстри
def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    unvisited = list(graph.keys())
    
    while unvisited:
        current = min(unvisited, key=lambda x: distances[x])
        unvisited.remove(current)
        
        for neighbor, weight in graph[current].items():
            new_distance = distances[current] + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                
    return distances

# Додавання ваг до ребер графа
weights = {
    ('Центр', 'Сихів'): 4, ('Центр', 'Личаків'): 2, ('Центр', 'Франківський'): 3,
    ('Сихів', 'Личаків'): 5, ('Сихів', 'Шевченківський'): 3, ('Сихів', 'Зубра'): 6,
    ('Личаків', 'Франківський'): 4, ('Личаків', 'Левандівка'): 2, ('Личаків', 'Рясне'): 6,
    ('Франківський', 'Шевченківський'): 2, ('Франківський', 'Залізничний'): 4,
    ('Шевченківський', 'Залізничний'): 3, ('Шевченківський', 'Рясне'): 5, ('Шевченківський', 'Збоїща'): 4,
    ('Залізничний', 'Левандівка'): 3, ('Левандівка', 'Рясне'): 2, ('Левандівка', 'Козельники'): 4,
    ('Рясне', 'Збоїща'): 3, ('Збоїща', 'Козельники'): 5, ('Козельники', 'Білогорща'): 2,
    ('Білогорща', 'Майорівка'): 4, ('Майорівка', 'Кульпарків'): 3, ('Кульпарків', 'Богданівка'): 2
}

G = nx.Graph()
for edge, weight in weights.items():
    G.add_edge(*edge, weight=weight)
    
start_node = 'Центр'
shortest_paths = dijkstra(G, start_node)

print(f"\nНайкоротші шляхи від вершини '{start_node}':")
for node, distance in shortest_paths.items():
    print(f"{start_node} -> {node}: {distance}")