"""
### Assignment 3: Corporate Event Logger
#### Scenario
You are developing a secure authentication firewall. The login gateway must log authorization attempts. File logs must track serious threats with detailed timestamps, while console channels show warnings in real time.

#### Problem Description
1. Write a function `configure_system_logger(log_file_path)`:
   - Configure a logger named `"CDAC_Security"` and set its baseline capture level to `logging.DEBUG`.
   - Clear any existing handlers on the logger to prevent duplicate outputs.
   - Create two log destination handlers:
     - **File Handler (`logging.FileHandler`)**: Writes logs to `log_file_path`. Set its logging threshold level to `logging.WARNING`.
     - **Console Handler (`logging.StreamHandler`)**: Outputs logs to standard console. Set its logging threshold level to `logging.INFO`.
   - Create and link formatters for both handlers:
     - The File Handler log format must be: `"[%(asctime)s] [%(levelname)s] - %(message)s"`
     - The Console Handler log format must be: `"[CONSOLE] %(levelname)s: %(message)s"`
   - Add both handlers to the `"CDAC_Security"` logger and return it.
2. Write a function `process_login_attempt(logger, username, is_success, ip_address)`:
   - If `is_success` is `True`, write an `INFO` message: `"User '<username>' successfully logged in from IP <ip_address>."`
   - If `is_success` is `False`:
     - If the username is `"admin"`, this indicates a critical threat. Write an `ERROR` message: `"CRITICAL: Unauthorized admin access attempt from IP <ip_address>!"`
     - For any other username, write a `WARNING` message: `"Failed login attempt for user '<username>' from IP <ip_address>."`

#### Expected Output
* Calling `process_login_attempt(logger, "arham", True, "192.168.1.100")` prints to console:
  `[CONSOLE] INFO: User 'arham' successfully logged in from IP 192.168.1.100.` (Not written to file).
* Calling `process_login_attempt(logger, "lisa", False, "10.0.0.5")` prints to console:
  `[CONSOLE] WARNING: Failed login attempt for user 'lisa' from IP 10.0.0.5.`
  And writes to log file: `[<timestamp>] [WARNING] - Failed login attempt for user 'lisa' from IP 10.0.0.5.`
* Calling `process_login_attempt(logger, "admin", False, "8.8.8.8")` prints to console:
  `[CONSOLE] ERROR: CRITICAL: Unauthorized admin access attempt from IP 8.8.8.8!`
  And writes to log file: `[<timestamp>] [ERROR] - CRITICAL: Unauthorized admin access attempt from IP 8.8.8.8!`
"""

def solve():
    # TODO: Implement your solution here
    pass

if __name__ == "__main__":
    solve()
