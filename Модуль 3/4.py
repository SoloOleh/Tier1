# def func_outer():
#     x = 2

#     def func_inner():
#         nonlocal x
#         x = 5

#     func_inner()
#     return x


# result = func_outer()  # 5
# print (result)

def discount_price(price, discount):
    def apply_discount():
      nonlocal price
      price *= (1 - discount)   #price = price * (1 - discount)
    apply_discount()
    return price
price = 100
discount = 0.2
discounted_price = discount_price(price, discount)
print(f"Ціна без знижки: {price}")
print(f"Знижка: {discount}")
print(f"Ціна зі знижкою: {discounted_price}")