import numpy as np
import matplotlib.pyplot as plt

# Parameters
num_rolls = 1000000
dice_sides = 6

# Simulation
results = np.random.randint(1, dice_sides+1, (num_rolls, 2))
sums = np.sum(results, axis=1)

# Counting sums
sum_counts = {sum_value: np.count_nonzero(sums == sum_value) for sum_value in range(2, 13)}

# Probability calculation
sum_probabilities = {sum_value: count / num_rolls * 100 for sum_value, count in sum_counts.items()}

# Theoretical probabilities
theoretical_probabilities = {
    2: 2.78, 3: 5.56, 4: 8.33, 5: 11.11, 6: 13.89,
    7: 16.67, 8: 13.89, 9: 11.11, 10: 8.33, 11: 5.56, 12: 2.78
}

# Plotting
plt.figure(figsize=(10, 5))
keys = list(sum_probabilities.keys())
values = list(sum_probabilities.values())
theo_values = [theoretical_probabilities[k] for k in keys]

plt.bar(keys, values, color='b', width=0.4, label='Monte Carlo Simulation')
plt.bar([k + 0.4 for k in keys], theo_values, color='r', width=0.4, label='Theoretical Probabilities')
plt.xlabel('Sum of two dice')
plt.ylabel('Probability (%)')
plt.title('Probability Distribution of Dice Rolls')
plt.xticks([k + 0.2 for k in keys], keys)
plt.legend()
plt.show()

sum_probabilities, theoretical_probabilities
