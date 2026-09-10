"""
### Assignment 6: Server Log Analyzer & Traffic Classifier (Advanced RegEx)
"""

import re

LOG_PATTERN = re.compile(
    r'^(?P<ip>\S+) - - \[(?P<time>[^\]]+)\] "(?P<method>[A-Z]+) (?P<resource>\S+) [^"]+" (?P<status>\d+) (?P<bytes>\d+)$'
)


def analyze_server_logs(logs_text: str) -> list[dict]:
    results = []
    for line in logs_text.strip().splitlines():
        line_clean = line.strip()
        if not line_clean:
            continue
        match = LOG_PATTERN.match(line_clean)
        if not match:
            print(f"Warning: Could not parse line: '{line_clean}'. Skipping.")
            continue

        ip = match.group("ip")
        if ip.startswith("192.168.") or ip.startswith("10."):
            continue

        results.append({
            "ip": ip,
            "time": match.group("time"),
            "method": match.group("method"),
            "resource": match.group("resource"),
            "status": int(match.group("status")),
            "bytes": int(match.group("bytes")),
        })
    return results


if __name__ == "__main__":
    log_data = (
        '192.168.1.5 - - [28/Aug/2026:10:00:00] "GET /index.html HTTP/1.1" 200 1024\n'
        '8.8.8.8 - - [28/Aug/2026:10:10:00] "GET /api/v1/users HTTP/1.1" 200 4096\n'
        'Corrupted log entry here\n'
        '10.0.0.12 - - [28/Aug/2026:10:15:00] "POST /submit_data HTTP/1.1" 403 512\n'
        '172.16.0.4 - - [28/Aug/2026:10:20:00] "POST /login HTTP/1.1" 401 256'
    )
    parsed = analyze_server_logs(log_data)
    print("Parsed External Logs:", parsed)
