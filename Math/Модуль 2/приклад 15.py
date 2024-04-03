import numpy as np
a = np.array(
    [[2, 3, 4],
     [1, 2, 0],
     [3, 0, 1]]
)
b = np.array([150, 70, 90])


print(f"A = {a}")
print(b)
print(np.linalg.solve(a, b))


