"""
### Assignment 1: Smart Home Appliance Control
#### Scenario
You are designing a control model for a smart home thermostat. The target temperature must be guarded against invalid bounds (e.g., set too high or too low, causing damage or excessive energy usage).

#### Problem Description
Create a class named `SmartThermostat` that implements the following specifications:
1. **Class-level Constant Variables**:
   - `MIN_TEMP = 10.0` (float)
   - `MAX_TEMP = 35.0` (float)
2. **Constructor (`__init__`)**:
   - Accepts parameters: `appliance_name` (string) and `initial_temp` (float).
   - Sets a private attribute `__appliance_name` (assigned from `appliance_name`).
   - Sets a private attribute `__target_temp` (float). Call the setter property inside the constructor or perform checks to ensure that if the `initial_temp` is out of the `[MIN_TEMP, MAX_TEMP]` bounds, it defaults to `22.0`.
3. **Properties**:
   - **`target_temp`** (read-write property):
     - **Getter**: Returns the value of `__target_temp`.
     - **Setter**: Checks if the new temperature is within the range `[MIN_TEMP, MAX_TEMP]` inclusive. If valid, updates `__target_temp`. If invalid, raises a `ValueError` with message: `"Temperature must be between 10.0 and 35.0 degrees."`
   - **`appliance_name`** (read-only property):
     - **Getter**: Returns `__appliance_name`.
     - (No setter defined, making it read-only after creation).

#### Example Walkthrough
```python
thermostat = SmartThermostat("Living Room AC", 24.0)
print(thermostat.appliance_name)  # Output: Living Room AC
print(thermostat.target_temp)     # Output: 24.0

thermostat.target_temp = 28.0     # Updates successfully
print(thermostat.target_temp)     # Output: 28.0

try:
    thermostat.target_temp = 5.0  # Out of range!
except ValueError as e:
    print(e)  # Output: Temperature must be between 10.0 and 35.0 degrees.
```

---
"""

def solve():
    # TODO: Implement your solution here
    pass

if __name__ == "__main__":
    solve()
