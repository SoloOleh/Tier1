# def add_ten(a):
#     b = 10
#     return a + b
# print(add_ten(6))  # 16

# a = 5
# b = 0
# def fun():
#     global a
#     a = 10
#     b = 2
# fun()
# print(a)  # 10
# print(b)  # 0

base_rate = 40
price_per_km = 10
total_trip = 0

def calculate_trip_price(distance_km):
   global total_trip
   total_trip += 1 #total_trip = total_trip + 1
   return base_rate + distance_km * price_per_km

distance_km = 15
trip_price = calculate_trip_price(distance_km)

print(f"Вартість поїздки на {distance_km} км складає: {trip_price} грн.")
print(f"Кількість поїздок: {total_trip}")