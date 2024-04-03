import numpy as np

A = np.array([
    [-1, 1, 2],
    [0, -1, 3],
    [4, -3, 2]
])
B = np.array([1, -4, 7])

print(f"A = {A}")
print(B)
print(np.linalg.solve(A, B))

def solve_inv_matrix(a, b, verbose=False):
  if np.linalg.det(a) == 0:
    return "Матриця невирішувальна (визначник дорівнює 0)"
  a_inv = np.linalg.inv(a)
  x = np.dot(a_inv, b)
  return x
print(f"Вектор рішення: \r\n {solve_inv_matrix(A, B)}")

def solve_cramer(a, b, verbose=False):
    if np.linalg.det(a) == 0:
        return "Матриця невирішувальна (визначник дорівнює 0)"
    n = len(b)
    det_A = np.linalg.det(a)
    x = np.zeros(n)
    for i in range(n):
        a_copy = a.copy()
        a_copy[:, i] = b
        x[i] = np.linalg.det(a_copy) / det_A
    return x

print(f"Вектор рішення: \r\n {solve_cramer(A, B)}")