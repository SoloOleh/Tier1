import numpy as np
from numpy import linalg as LA
a = np.array([1, 3])
b = np.array([2, 0])
print(LA.norm(a - b, ord=2))
