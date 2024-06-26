import random

class UniversalHash:
    def __init__(self, m, max_key):
        self.m = m
        self.p = self._next_prime(max_key)
        self.a = random.randint(1, self.p - 1)
        self.b = random.randint(0, self.p - 1)

    def _next_prime(self, n):
        while True:
            n += 1
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    break
            else:
                return n

    def hash(self, key):
        return ((self.a * key + self.b) % self.p) % self.m

# Приклад використання:
hasher = UniversalHash(100, 1000)
print(hasher.hash(123))
print(hasher.hash(456))
