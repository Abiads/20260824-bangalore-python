"""
### Assignment 2: JSON Configuration Validator
#### Scenario
An AI web engine boots configurations from a JSON file. If the file is missing, empty, or contains corrupt syntax, the system crashes. You need to write a safe configuration loading module that provides default values in case of errors.

#### Problem Description
Write a function `load_config_safely(file_path_str)`:
1. Convert `file_path_str` to a path using `pathlib.Path`.
2. **Check Existence**: Check if the file exists and is indeed a file. If the file is missing, print: `"Error: Config file not found."` and return the default fallback configuration:
   `{"status": "default", "port": 8080}`.
3. **Check Size**: Check if the file size is 0 bytes (empty). If empty, print: `"Error: Config file is empty."` and return the default fallback dictionary.
4. **JSON Parsing**: Read the file contents. Attempt to deserialize the contents as JSON using `json.loads()` or `json.load()`.
   - If the file contains invalid JSON structures (throws `json.JSONDecodeError`), catch the exception, print: `"Error: Invalid JSON syntax."`, and return the default fallback dictionary.
5. If the file parses successfully, return the loaded configuration dictionary.

#### Example Walkthrough
```python
from pathlib import Path

# Setup files for testing
Path("corrupt.json").write_text("invalid data string")
Path("empty.json").write_text("")

# Test Cases
print(load_config_safely("missing.json"))
# Output: Error: Config file not found.
# Returns: {"status": "default", "port": 8080}

print(load_config_safely("empty.json"))
# Output: Error: Config file is empty.
# Returns: {"status": "default", "port": 8080}

print(load_config_safely("corrupt.json"))
# Output: Error: Invalid JSON syntax.
# Returns: {"status": "default", "port": 8080}
```
"""

def solve():
    # TODO: Implement your solution here
    pass

if __name__ == "__main__":
    solve()
