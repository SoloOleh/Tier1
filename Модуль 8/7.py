from collections import Counter

def get_count_visits_from_ip(ips):
    # Використовуємо Counter для підрахунку кількості входжень кожного IP
    ip_counter = Counter(ips)
    return dict(ip_counter)

def get_frequent_visit_from_ip(ips):
    # Використовуємо Counter для підрахунку кількості входжень кожного IP
    ip_counter = Counter(ips)
    # Знаходимо найбільш часто зустрічаючийся IP та його кількість входжень
    most_common_ip, count = ip_counter.most_common(1)[0]
    return most_common_ip, count

# Приклад використання:
IP = [
    "85.157.172.253",
    "66.50.38.43",
    "66.50.38.43",
    "192.168.1.1",
    "85.157.172.253",
    "66.50.38.43",
    "192.168.1.1",
    "85.157.172.253",
    "66.50.38.43"
]

print("Count visits from IP:")
print(get_count_visits_from_ip(IP))

print("\nFrequent visit from IP:")
print(get_frequent_visit_from_ip(IP))

