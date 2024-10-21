# API Reference

### `function`

**Description**:  
Returns a callable that, when invoked, executes the specified function based on the given probability.

**Parameters**:
- `func` (`Callable`):  
  The function to execute.
- `random_engine` (`RandomEngine`, optional):  
  A callable that returns a float between 0 and 1. Defaults to `random.random` if not provided.
- `p` (`float`):  
  Probability of executing the function. Must be between 0 and 1. Defaults to `1.0` (always execute).

**Returns**:
- `Callable`:  
  A function that executes `func` with probability `p`. Returns the result of `func` if executed, otherwise `None`.

**Raises**:
- `ValueError`:  
  If `p` is not within the range [0, 1].

**Usage**:

```python
import probabilistic

def greet():
    print("Hello!")
    return "Greeted"

# Create a probabilistic function with 50% execution probability
prob_greet = probabilistic.function(func=greet, p=0.5)

# Execute the probabilistic function multiple times
print("Executing probabilistic greet function:")
for i in range(5):
    result = prob_greet()
    print(f"Trial {i + 1}: Result:", result)
```

**Example Output**:
```
Executing probabilistic greet function:
Hello!
Trial 1: Result: Greeted
Trial 2: Result: None
Hello!
Trial 3: Result: Greeted
Trial 4: Result: None
Hello!
Trial 5: Result: Greeted
```

---
  
### `mutual_function`

**Description**:  
Returns a callable that, when invoked, selects and executes one function from the provided list based on the specified weights.

**Parameters**:
- `funcs` (`List[Callable]`):  
  List of functions to choose from.
- `weights` (`List[float]`):  
  List of weights corresponding to each function in `funcs`. Determines the probability of each function being selected.
- `random_engine` (`RandomEngine`, optional):  
  A callable that returns a float between 0 and 1. Defaults to `random.random` if not provided.

**Returns**:
- `Callable`:  
  A function that selects one of the provided `funcs` based on `weights` and executes it. Returns the result of the selected function.

**Raises**:
- `ValueError`:  
  - If the lengths of `funcs` and `weights` do not match.
  - If the sum of `weights` is not greater than 0.

**Usage**:

```python
import probabilistic

def option_a():
    print("Option A executed")
    return "A"

def option_b():
    print("Option B executed")
    return "B"

# Define a mutual function with weights 0.7 and 0.3
mutual_func = probabilistic.mutual_function(
    funcs=[option_a, option_b],
    weights=[0.7, 0.3]
)

# Execute the mutual function multiple times
print("Executing mutual function:")
for i in range(5):
    result = mutual_func()
    print(f"Trial {i + 1}: Result:", result)
```

**Example Output**:
```
Executing mutual function:
Option A executed
Trial 1: Result: A
Option B executed
Trial 2: Result: B
Option A executed
Trial 3: Result: A
Option A executed
Trial 4: Result: A
Option B executed
Trial 5: Result: B
```

---

### `distribution_function`

**Description**:  
Returns a callable that, when invoked, computes the distribution of outcomes by executing the specified function over `n` trials.

**Parameters**:
- `func` (`Callable`):  
  The function to execute repeatedly.
- `n` (`int`):  
  Number of trials to perform for the distribution assessment. Defaults to `1000`.

**Returns**:
- `Callable`:  
  A function that runs `func` `n` times and returns a dictionary representing the distribution of results, where keys are the unique outcomes and values are their normalized probabilities.

**Raises**:
- `TypeError`:  
  If `func` returns an unhashable type during any of the trials.
- `ValueError`:  
  If `n` is not a positive integer.

**Usage**:

```python
import probabilistic
import random

def roll_die():
    return random.randint(1, 6)

# Create a distribution function for rolling a die 10,000 times
roll_die_distribution = probabilistic.distribution_function(func=roll_die, n=10000)

# Compute and print the distribution
print("Die roll distribution over 10,000 trials:")
distribution = roll_die_distribution()
print(distribution)  # Example Output: {1: 0.167, 2: 0.166, ...}
```

**Example Output**:
```
Die roll distribution over 10,000 trials:
{1: 0.168, 2: 0.165, 3: 0.167, 4: 0.166, 5: 0.168, 6: 0.166}
```
