"""
Assignment 5: Deep JSON/Configuration Key Traverser

Scenario:
Traverse nested dictionary configuration tree using dot notation path string (e.g. "server.database.port").

Problem Description:
Write `traverse_nested_config(config_dict, path_str, default=None)`:
- Split `path_str` on `.` and navigate down `config_dict`.
- Constraint: Use try...except block catching `KeyError`, `TypeError`, and `AttributeError` instead of if-in checks.
- If path is empty, invalid, or traversal fails, return `default`.
"""

def traverse_nested_config(config_dict: dict, path_str: str, default=None):
    if not path_str or not isinstance(config_dict, dict):
        return default
        
    keys = path_str.split(".")
    curr = config_dict
    
    try:
        for k in keys:
            curr = curr[k]
        return curr
    except (KeyError, TypeError, AttributeError):
        return default

if __name__ == "__main__":
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
    print("Valid path:", traverse_nested_config(config, "server.ssl.cert_path"))
    print("Missing key (default):", traverse_nested_config(config, "server.database.username", "guest"))
    print("TypeError on string indexing (default):", traverse_nested_config(config, "database.host", "localhost"))

