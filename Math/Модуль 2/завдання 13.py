import numpy as np
a = np.array(
    [[3, 0, 0],
     [2, 1, 0],
     [1, 1, 1]]
    )
b = np.array([60, 50, 90])

print(f"A = {a}")
print(b)
print(np.linalg.solve(a, b))