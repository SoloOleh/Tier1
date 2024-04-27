# def modeling(factor, *numbers, correction):
#     result = 0
#     for number in numbers:
#         result += number * factor
#     result = result - correction
#     return result


# print(modeling(10, 1, 2, 3, correction=2))  # 58
def cost_delivery(quantity, *args, discount = 0):
    if quantity >= 1:
        delivery_cost = (quantity - 1) * 2 + 5
    else:
        delivery_cost = 0
    return delivery_cost - delivery_cost * discount
print(cost_delivery(2, 1, 2, 3)) 
print(cost_delivery(3, 3)) 
print(cost_delivery(1)) 
print(cost_delivery(2, 1, 2, 3, discount=0.5)) 