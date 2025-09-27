import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Group A (Old version) - mean = 50 transactions/day, std dev = 10
group_a = np.random.normal(loc=50, scale=10, size=500)

# Group B (New version) - mean = 55 transactions/day, std dev = 12
group_b = np.random.normal(loc=55, scale=12, size=500)

plt.figure(figsize=(10,6))

sns.kdeplot(group_a, fill=True, label="Group A (Old App)")
sns.kdeplot(group_b, fill=True, label="Group B (New App)")

plt.title("A/B Testing Simulation - Transactions per Day")
plt.xlabel("Transactions")
plt.ylabel("Density")
plt.legend()
plt.show()

print("Group A Average:", np.mean(group_a))
print("Group B Average:", np.mean(group_b))
