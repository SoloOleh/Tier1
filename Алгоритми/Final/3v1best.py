import heapq

def dijkstra(graph, start):
    # Ініціалізація відстаней і черги
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    visited = set()
    
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        # Якщо вершина вже відвідана, продовжуємо
        if current_vertex in visited:
            continue

        visited.add(current_vertex)
        
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Якщо нова відстань коротша, оновлюємо її
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

# Приклад графа у вигляді словника
graph = {
    'A': {'B': 5, 'C': 10},
    'B': {'A': 5, 'D': 3},
    'C': {'A': 10, 'D': 2},
    'D': {'B': 3, 'C': 2, 'E': 4},
    'E': {'D': 4}
}

# Виклик функції для вершини A
distances = dijkstra(graph, 'A')
print("Найкоротші відстані від вершини A:", distances)

# # Функція для виведення таблиці з відстанями та статусом перевірки
# def print_table(distances, visited):
#     print("{:<10} {:<10} {:<10}".format("Вершина", "Відстань", "Перевірено"))
#     print("-" * 30)
    
#     for vertex in distances:
#         distance = distances[vertex]
#         if distance == float('infinity'):
#             distance = "∞"
#         else:
#             distance = str(distance)
        
#         status = "Так" if vertex in visited else "Ні"
#         print("{:<10} {:<10} {:<10}".format(vertex, distance, status))
#     print("\n")

# # Виклик функції для виведення таблиці
# print_table(distances, {'A', 'B', 'C', 'D', 'E'})


# import networkx as nx
# import matplotlib.pyplot as plt

# # Створення графа
# G = nx.Graph()

# # Додавання міст і доріг
# G.add_edge('A', 'B', weight=5)
# G.add_edge('A', 'C', weight=10)
# G.add_edge('B', 'D', weight=3)
# G.add_edge('C', 'D', weight=2)
# G.add_edge('D', 'E', weight=4)

# # Візуалізація графа
# pos = nx.spring_layout(G, seed=42)
# nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=15, width=2)
# labels = nx.get_edge_attributes(G, 'weight')
# nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

# plt.show()
