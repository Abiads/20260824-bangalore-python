"""
### Assignment 2: Vehicle Fleet Management
#### Scenario
A delivery company manages different vehicle classes. They want to calculate travel range based on fuel capacity, and adjust range for trucks depending on cargo load.

#### Problem Description
1. Create a base class named `Vehicle` with:
   - **Constructor (`__init__`)**: Accepts `make` (string), `model` (string), and `fuel_capacity` (float, in liters).
   - **Method `calculate_range(fuel_efficiency)`**: Calculates and returns the vehicle's range (in kilometers) by multiplying the `fuel_capacity` by the `fuel_efficiency` (km per liter).
   - **Method `get_description()`**: Returns a formatted string: `"Vehicle: <make> <model>"`.
2. Create a subclass named `DeliveryTruck` that inherits from `Vehicle`:
   - **Constructor (`__init__`)**: Accepts `make` (string), `model` (string), `fuel_capacity` (float), and `cargo_load` (float, in metric tons). Uses `super().__init__()` to initialize base vehicle parameters.
   - **Method `calculate_range(fuel_efficiency)`**: Overrides the base method. Heavy loads reduce efficiency. Reduce the range calculation by **10% for every metric ton** of `cargo_load` currently carried.
     $$\text{Adjusted Range} = \text{Base Range} \times (1.0 - 0.1 \times \text{cargo\_load})$$
   - **Method `get_description()`**: Overrides the base method. Returns a formatted string: `"Truck: <make> <model> carrying <cargo_load> tons"`.

#### Example Walkthrough
```python
truck = DeliveryTruck("Volvo", "FH16", 300.0, cargo_load=2.0)

# Base range calculations without load adjustment would be 300 * 5 = 1500 km.
# 2.0 tons load reduces range by 20% (10% * 2) -> 1500 * 0.8 = 1200 km.
print(truck.calculate_range(5.0)) # Output: 1200.0
print(truck.get_description())    # Output: Truck: Volvo FH16 carrying 2.0 tons
```
"""

def solve():
    # TODO: Implement your solution here
    pass

if __name__ == "__main__":
    solve()
