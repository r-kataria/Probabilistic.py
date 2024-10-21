import probabilistic

def option_a():
    print("Option A executed")
    return "A"

def option_b():
    print("Option B executed")
    return "B"

# Define a mutual function
mutual_func = probabilistic.mutual_function([option_a, option_b], weights=[0.7, 0.3])

# Execute the mutual function multiple times
print("Executing mutual function:")
for i in range(5):
    result = mutual_func()
    print(f"Trial {i + 1}: Result:", result)
