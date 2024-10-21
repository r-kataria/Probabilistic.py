# Probabilistic.py

Probabilistic is a Python library designed to facilitate the probabilistic execution of functions and the analysis of their outcome distributions. Whether you're simulating uncertain events, performing randomized experiments, or adding an element of chance to your applications, Probabilistic provides a straightforward and flexible toolkit to meet your needs.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Documentation](#documentation)
- [Support This Project](#support-this-project)


## Features
- [x] Probabilistic Function Function
- [x] Mutual Exclusivity Function
- [x] Distribution Analysis Function
- [x] Customizable Random Engines

- [ ] Conditional Probability-Based Function
- [ ] Probability Chains
- [ ] Asynchronous Execution Support
- [ ] Integration with Popular Libraries like NumPy and Pandas for enhanced data handling and analysis.

## Installation

You can install the **Probabilistic** library using `pip`. Ensure that you have Python 3.6 or higher installed on your system.

```bash
pip install probabilistic.py
```

## Quick Start

Here's a quick example to get you started with Probabilistic.

```python
import probabilistic

def hello():
    print("Hello!")

# Create a probabilistic function with a 50% execution probability
maybe_hello = probabilistic.function(func=hello, p=0.5)

# Execute the probabilistic function
maybe_hello()
```

## Documentation
For documentation, please see the [API Reference](docs/API_Reference.md) and [Examples](docs/Examples.md).


## Support This Project
If you find this project helpful, please consider giving it a star on GitHub! 🌟

If you'd like to improve this project, feel free to submit a pull request or open an issue. Let's build something great together! 🚀

*Happy Probabilistic Coding!*