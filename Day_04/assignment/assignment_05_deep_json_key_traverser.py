"""
### Assignment 5: Deep JSON/Configuration Key Traverser
#### Scenario
Configuration files loaded from JSON databases consist of nested dictionary hierarchies. Checking key existence at every level using nested conditions (`if key in dictionary`) leads to complex and verbose code. You need to write a clean traverser utility that navigates nested dictionaries using exceptions.

#### Problem Description
Write a function `traverse_nested_config(config_dict, path_str, default=None)`:
- `config_dict` is a nested dictionary configuration tree.
- `path_str` is a string specifying the configuration path using dot notation (e.g., `"server.database.port"`).
- The function should split the `path_str` on `.` characters and traverse down `config_dict`.
- **Implementation Constraint**: You **must** attempt to traverse keys directly. Do not use key-existence checks (like `if key in dict`) or class-checks (like `if isinstance(sub_dict, dict)`). Instead, handle the lookup path directly inside a `try` block and catch the following exceptions to return the `default` value:
  - Catch `KeyError` if any key in the path does not exist.
  - Catch `TypeError` or `AttributeError` if you try to index a primitive, non-dictionary value (e.g., trying to access a key like `"port"` on a configuration value that resolved to a string or number).
- If `path_str` is empty or `config_dict` is not a valid dictionary, return the `default` value.

#### Test Data & Test Cases
```python
config = {
    "server": {
        "host": "127.0.0.1",
        "port": 8080,
        "ssl": {
            "enabled": True,
            "cert_path": "/etc/ssl/certs"
        }
    },
    "database": "postgresql://localhost:5432"
}

# Test Case 1: Valid Path
print(traverse_nested_config(config, "server.ssl.cert_path"))
# Output: /etc/ssl/certs

# Test Case 2: Missing Key (Triggers KeyError)
print(traverse_nested_config(config, "server.database.username", "guest"))
# Output: guest

# Test Case 3: Indexing Non-Dictionary value (Triggers TypeError)
# Here config["database"] is a string, which cannot be indexed with "host"
print(traverse_nested_config(config, "database.host", "localhost"))
# Output: localhost
```
"""

def traverse_nested_config(config_dict: dict, path_str: str, default=None):
    if not path_str or not isinstance(config_dict, dict):
        return default
        
    keys = path_str.split(".")
    current = config_dict
    
    try:
        for key in keys:
            current = current[key]
        return current
    except (KeyError, TypeError, AttributeError):
        return default


if __name__ == "__main__":
    app_config = {
        "server": {
            "host": "127.0.0.1",
            "port": 8080,
            "ssl": {
                "enabled": True,
                "cert_path": "/etc/ssl/certs"
            }
        },
        "database": "postgresql://localhost:5432"
    }
    
    # Test valid path
    cert = traverse_nested_config(app_config, "server.ssl.cert_path")
    print("Found SSL Cert Path:", cert)
    
    # Test non-existent key with default fallback
    user = traverse_nested_config(app_config, "server.database.username", "guest")
    print("Fallback User:", user)
    
    # Test type error path (indexing into string) with default fallback
    db_host = traverse_nested_config(app_config, "database.host", "localhost")
    print("Fallback DB Host:", db_host)
