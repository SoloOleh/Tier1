from collections import UserList


class AmountPaymentList(UserList):
    
    def amount_payment(self):
        sum = 0
        for value in payment:
            if value > 0:
                sum = sum + value
        return sum
        
payment = [1, -3, 4]   