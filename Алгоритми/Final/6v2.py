def greedy_algorithm(items, budget):
    # Сортування елементів за співвідношенням калорій до вартості
    sorted_items = sorted(items.items(), key=lambda item: item[1]["calories"] / item[1]["cost"], reverse=True)
    total_cost = 0
    chosen_items = []
    
    for item, data in sorted_items:
        if total_cost + data["cost"] <= budget:
            chosen_items.append(item)
            total_cost += data["cost"]
    
    return chosen_items

def dynamic_programming(items, budget):
    # Ініціалізація таблиці з максимальними калоріями, які можна отримати для кожного рівня бюджету
    dp = [0] * (budget + 1)
    
    for cost in range(budget + 1):
        for item, data in items.items():
            if cost >= data["cost"]:
                dp[cost] = max(dp[cost], dp[cost - data["cost"]] + data["calories"])
    
    # Знаходження комбінації страв, що дає максимальну калорійність
    result = []
    current_budget = budget
    while current_budget > 0:
        for item, data in items.items():
            if current_budget >= data["cost"] and dp[current_budget] == dp[current_budget - data["cost"]] + data["calories"]:
                result.append(item)
                current_budget -= data["cost"]
                break
    
    return result

# Приклад використання:
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 90
print("Greedy approach:", greedy_algorithm(items, budget))
print("Dynamic programming approach:", dynamic_programming(items, budget))
