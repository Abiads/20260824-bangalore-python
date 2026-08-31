"""
### Assignment 6: Shipping Cost Decay Optimizer (SciPy Optimization)
#### Scenario
A logistics company analyzes Northwind shipping freight costs. The average freight charge per unit decays exponentially as the total quantity of items ordered in a batch increases. The freight charge is modeled by:
$$\text{freight}(q) = a \cdot e^{-b \cdot q} + 10.0$$
where $q$ is the quantity ordered, $a$ is the maximum shipping surcharge, and $b$ is the cost decay coefficient. You need to write a SciPy optimization script to fit parameters $a$ and $b$ to observed transaction data by minimizing the Sum of Squared Errors (SSE).

#### Problem Description
Write a function `optimize_freight_model(quantity_array, observed_freight_array)`:
1. `quantity_array` is a 1D NumPy array representing quantities $q$.
2. `observed_freight_array` is a 1D NumPy array of the same size representing observed freight costs.
3. **Objective Error Function**: Define a local error function `calculate_sse(params)`:
   - `params` is a list or tuple: `[a, b]`.
   - Calculate the modeled freight for each quantity $q$ in `quantity_array`:
     $$\text{modeled}(q) = a \cdot e^{-b \cdot q} + 10.0$$
   - Compute and return the Sum of Squared Errors (SSE) between the model and observed data:
     $$\text{SSE} = \sum \left( \text{modeled}(q) - \text{observed}(q) \right)^2$$
4. **Optimization**:
   - Use `scipy.optimize.minimize` to find parameters `[a, b]` that minimize `calculate_sse`.
   - Set the initial guess to `[100.0, 0.05]`.
   - Enforce parameter bounds to ensure physical validity: $a \ge 0.0$ and $b \ge 0.001$.
5. **Return**: A dictionary containing:
   `{"a": opt_a, "b": opt_b, "sse": min_sse}`
   where all values are rounded to **4 decimal places**.

#### Example Walkthrough
```python
import numpy as np

# Mock experimental data (quantities and matching observed freights)
q_data = np.array([5, 10, 15, 20, 30, 40, 50])
observed_f = np.array([90.5, 75.2, 60.1, 50.8, 35.4, 25.1, 18.0])

fit_results = optimize_freight_model(q_data, observed_f)
print(fit_results)
# Expected Output format:
# {'a': <value>, 'b': <value>, 'sse': <value>}
```
"""

def solve():
    # TODO: Implement your solution here
    pass

if __name__ == "__main__":
    solve()
