import numpy as np
from numpy import linalg as LA
a = np.array([1, 3])
b = np.array([2, 0])
cos_angle = np.dot(a, b) / LA.norm(a) / LA.norm(b)
print(f"Косинус кута:{cos_angle}")
print(f"Значення кута (радіани) {np.arccos(cos_angle)}")