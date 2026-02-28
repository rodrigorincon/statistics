import random
import matplotlib.pyplot as plt

print("----------------- formula to calculate the Probability")
num_people = 23

prob = (1.0/365)**num_people # below part of the combinatory function
for i in range( (366-num_people), 366): # 365, 364, 363... 365-num_people+1
    prob *= i # above parte of the combinatory function. Factorial of 365, already removed the (365-n)!
prob = 1 - prob
print("Probability of ", num_people, ":", round(prob*100, 2))

print("----------------- calculating the Probability for each number")

def has_duplicate_birthday(num_people):
    birthdays = [random.randint(1, 365) for _ in range(num_people)]
    return len(birthdays) != len(set(birthdays)) # Returns True if a match exists

list_percents = []
# Run for many size of groups see the probability for each size
for num_people in range(1, 100):
	simulations = 100_000
	matches = sum(has_duplicate_birthday(num_people) for _ in range(simulations)) # Run simulation
	percent = round(matches/simulations * 100, 2)
	list_percents.append(percent)
	print(f"Probability with {num_people} people: {percent}%")
	if percent == 100: break
	# 23 people = 50%
	# 50 people = 97%
	# 70 people = 99,9%

print("----------------- plot the probabilities")

plt.plot(range(1,len(list_percents)+1), list_percents)
plt.title('Birthday Paradox')
plt.xlabel('Num People')
plt.ylabel('Probability of pairing')
plt.legend()
plt.grid(True)
plt.show()