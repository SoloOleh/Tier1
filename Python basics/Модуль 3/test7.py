# def invite_to_event(username):
#     text = (f"Dear {username}, we have the honour to invite you to our event")
#     return text

# print (invite_to_event("John"))


# base_rate = 40
# price_per_km = 10
# total_trip = 0


# def calculate_trip_price(distance_km):
#     global total_trip
#     total_trip += 1
#     total_cost = base_rate + price_per_km*distance_km
#     return total_cost

# print(calculate_trip_price(20))
# print(calculate_trip_price(30))
# print(total_trip)


def get_fullname (first_name, last_name, middle_name=None):
    if middle_name is None:
        return f"{first_name} {last_name}"
    else:
        return f"{first_name} {middle_name} {last_name}"
print(get_fullname("John", "Doe"))