import probabilistic
import random

def greet():
    print("Hello!")
    return "Greeted"

# Create a probabilistic function
prob_greet = probabilistic.function(greet, p=0.5)

# Execute the probabilistic function multiple times
print("Executing probabilistic greet function:")
for i in range(5):
    result = prob_greet()
    print(f"Trial {i + 1}: Result:", result)
