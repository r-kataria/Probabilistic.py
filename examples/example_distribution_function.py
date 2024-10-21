import probabilistic
import random

def roll_die():
    return random.randint(1, 6)

# Create a distribution function
roll_die_distribution = probabilistic.distribution_function(roll_die, n=10000)

# Compute and print the distribution
print("Die roll distribution over 10,000 trials:")
distribution = roll_die_distribution()
print(distribution)  # Example Output: {1: 0.167, 2: 0.166, ...}
