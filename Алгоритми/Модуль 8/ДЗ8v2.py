import heapq

def min_cost_to_combine_cables(lengths):
    # Створення мінімальної купи зі списку довжин кабелів
    heapq.heapify(lengths)
    
    total_cost = 0

    # Об'єднуємо кабелі доти, доки в купі не залишиться менше двох кабелів
    while len(lengths) > 1:
        # Виймаємо два найменші кабелі
        first = heapq.heappop(lengths)
        second = heapq.heappop(lengths)

        # Обчислюємо вартість їх об'єднання
        cost = first + second
        total_cost += cost

        # Додаємо об'єднаний кабель назад до купи
        heapq.heappush(lengths, cost)

    return total_cost

# Приклад використання
cable_lengths = [4, 3, 2, 6]
print("Мінімальні загальні витрати:", min_cost_to_combine_cables(cable_lengths))
