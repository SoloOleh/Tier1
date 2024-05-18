import heapq

def min_cost_to_connect_cables(cables):
    heapq.heapify(cables)
    total_cost = 0
    while len(cables) > 1:
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        combined = first + second
        total_cost += combined
        heapq.heappush(cables, combined)
    
    return total_cost

cables_lengths = [8, 4, 6, 12, 2]
print(f"Мінімальні витрати на з'єднання кабелів: {min_cost_to_connect_cables(cables_lengths)}")
