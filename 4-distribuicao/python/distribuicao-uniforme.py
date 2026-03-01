import random
import matplotlib.pyplot as plt

dice_results = [ random.randint(1, 6) for x in range(100_000)]

plt.hist(dice_results, rwidth=0.9, bins=6, color='skyblue', edgecolor='black')
plt.xlabel("Dice values")
plt.ylabel("Frequency")
plt.title("Uniform Distribution")
plt.show()