def discount_price(discount):
    # Ця внутрішня функція буде використовувати зовнішню змінну 'discount'
    def apply_discount(price):
        return price * (1 - discount)

    return apply_discount

# Тестування функції
cost_15 = discount_price(0.15)
cost_10 = discount_price(0.10)
cost_05 = discount_price(0.05)

price = 100
print(cost_15(price))  # 85.0
print(cost_10(price))  # 90.0
print(cost_05(price))  # 95.0
