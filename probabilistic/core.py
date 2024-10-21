from typing import Callable, List, Any, Dict, Optional
import random

# Define a type for the random engine
RandomEngine = Callable[[], float]

def function(
    func: Callable,
    random_engine: RandomEngine = random.random,
    p: float = 1.0
) -> Callable:
    """
    Returns a function that, when called, executes the given function based on the specified probability.

    :param func: The function to execute.
    :param random_engine: A callable that returns a float between 0 and 1.
    :param p: Probability of executing the function. Defaults to 1.0 (always execute).
    :return: Callable function that executes the given function based on probability.
    """
    if not (0 <= p <= 1):
        raise ValueError("Probability p must be between 0 and 1.")

    def wrapper(*args, **kwargs):
        rand_val = random_engine()
        if rand_val <= p:
            return func(*args, **kwargs)
        else:
            return None

    return wrapper


def mutual_function(
    funcs: List[Callable],
    weights: List[float],
    random_engine: RandomEngine = random.random
) -> Callable:
    """
    Returns a function that, when called, executes one function from the list based on the given weights.

    :param funcs: List of functions to choose from.
    :param weights: List of weights corresponding to each function.
    :param random_engine: A callable that returns a float between 0 and 1.
    :return: Callable function that executes one of the provided functions based on weights.
    """
    if len(funcs) != len(weights):
        raise ValueError("The length of funcs and weights must be the same.")
    if sum(weights) == 0:
        raise ValueError("Sum of weights must be greater than 0.")

    cumulative_weights = []
    total = sum(weights)
    cumsum = 0
    for w in weights:
        cumsum += w
        cumulative_weights.append(cumsum / total)

    def wrapper(*args, **kwargs):
        rand_val = random_engine()
        for func, cum_weight in zip(funcs, cumulative_weights):
            if rand_val <= cum_weight:
                return func(*args, **kwargs)
        return None  # Should not reach here if weights are valid

    return wrapper

def distribution_function(
    func: Callable,
    n: int = 1000
) -> Callable:
    """
    Returns a function that, when called, computes the distribution of outcomes over `n` trials.

    :param func: The function to execute.
    :param n: Number of trials.
    :return: Callable function that computes the distribution of outcomes.
    """

    def wrapper(*args, **kwargs):
        results_count = {}
        for _ in range(n):
            result = func(*args, **kwargs)
            # Ensure the result is hashable
            if not isinstance(result, (str, int, float, tuple, frozenset, bool, type(None))):
                raise TypeError(f"Unhashable type returned: {type(result)}")
            results_count[result] = results_count.get(result, 0) + 1
        # Normalize the counts to probabilities
        total_counts = sum(results_count.values())
        distribution = {k: v / total_counts for k, v in results_count.items()}
        return distribution

    return wrapper