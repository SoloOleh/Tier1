# print(0.1 + 0.2 == 0.3)     # False
# print(0.1 + 0.2)            # 0.30000000000000004

# from decimal import Decimal, getcontext
# getcontext().prec = 6
# Decimal(1) / Decimal(7)  # Decimal('0.142857')

# getcontext().prec = 28
# Decimal(1) / Decimal(7) # Decimal('0.1428571428571428571428571429')

from decimal import Decimal, getcontext
getcontext().prec = 6
float(Decimal(0.1) + Decimal(0.2)) == 0.3   # True

Decimal(0.2) + Decimal(0.1) == Decimal(0.3) # False

Decimal(0.2) + Decimal(0.1) == Decimal(0.3)  + Decimal(0.0) # True
