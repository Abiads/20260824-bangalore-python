"""
Assignment 6: Server Log Analyzer & Traffic Classifier (Advanced RegEx)

Scenario:
Parse web server logs using named capture groups and filter out local IP addresses.

Problem Description:
Write `analyze_server_logs(logs_text)`:
- Log line format: `"<IP> - - [<timestamp>] \"<HTTP_METHOD> <URL> <HTTP_VERSION>\" <STATUS_CODE> <BYTES>"`
- Named capture groups: `ip`, `time`, `method`, `resource`, `status`, `bytes`.
- Filters out local IPs starting with "192.168." or "10.".
- Returns list of dicts: `[{"ip": ..., "time": ..., "method": ..., "resource": ..., "status": int, "bytes": int}, ...]`
"""

import re

def analyze_server_logs(logs_text: str) -> list[dict]:
    # TODO: Implement your solution here
    pass

if __name__ == "__main__":
    log_data = """192.168.1.5 - - [28/Aug/2026:10:00:00] "GET /index.html HTTP/1.1" 200 1024
8.8.8.8 - - [28/Aug/2026:10:10:00] "GET /api/v1/users HTTP/1.1" 200 4096
Corrupted log entry here
10.0.0.12 - - [28/Aug/2026:10:15:00] "POST /submit_data HTTP/1.1" 403 512
172.16.0.4 - - [28/Aug/2026:10:20:00] "POST /login HTTP/1.1" 401 256"""
    parsed = analyze_server_logs(log_data)
    print("Parsed External Logs:", parsed)

