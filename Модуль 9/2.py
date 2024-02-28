DEFAULT_DISCOUNT = 0.05

def get_discount_price_customer(price, customer):
    # Визначаємо розмір знижки
    discount = customer.get("discount", DEFAULT_DISCOUNT)
    
    # Розраховуємо ціну з урахуванням знижки
    discounted_price = price * (1 - discount)
    
    return discounted_price
