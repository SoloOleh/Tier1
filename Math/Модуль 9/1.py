import matplotlib.pyplot as plt
import numpy as np

# Визначення точок для опуклої множини
convex_points = np.array([[1, 1], [2, 4], [5, 5], [7, 5], [8, 2]])

# Визначення точок для не опуклої множини
non_convex_points = np.array([[1, 1], [2, 4], [3, 3], [5, 2], [7, 5], [9, 1]])

# Побудова графіків
plt.figure(figsize=(12, 5))

# Опукла множина
plt.subplot(1, 2, 1)
plt.plot(convex_points[:, 0], convex_points[:, 1], 'bo-', label='Опукла множина')
plt.fill(convex_points[:, 0], convex_points[:, 1], 'b', alpha=0.3)
plt.title('Опукла множина')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

# Не опукла множина
plt.subplot(1, 2, 2)
plt.plot(non_convex_points[:, 0], non_convex_points[:, 1], 'ro-', label='Не опукла множина')
plt.fill(non_convex_points[:, 0], non_convex_points[:, 1], 'r', alpha=0.3)
plt.title('Не опукла множина')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

plt.tight_layout()
plt.show()
