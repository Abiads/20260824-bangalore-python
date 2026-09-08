"""
### Assignment 2: Multi-Format Log Converter (Text to CSV & JSON)
#### Scenario
A server records raw access events as unformatted plain-text log lines. You need to parse the log lines into structured records and export them to both CSV and JSON formats.

#### Problem Description
Create a function `convert_log_file(input_log_path, output_csv_path, output_json_path)`:
1. Each line in `input_log_path` follows the format:
   `"<TIMESTAMP> | <USER_ID> | <ENDPOINT> | <STATUS_CODE>"`
   (e.g., `"2026-09-01 10:15:30 | USR102 | /api/v1/predict | 200"`).
2. Parses each line into a dictionary containing keys: `timestamp`, `user_id`, `endpoint`, `status_code` (as integer).
3. Writes all parsed records to `output_csv_path` with a header row using `csv.DictWriter`.
4. Writes the list of records to `output_json_path` with an indentation of 2 spaces using `json.dump()`.

#### Example Walkthrough
```python
convert_log_file("server_access.log", "access_records.csv", "access_records.json")
```
"""
import csv
import json


def convert_log_file(input_log_path, output_csv_path, output_json_path):
    records = []
    with open(input_log_path, mode="r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = [part.strip() for part in line.split("|")]
            if len(parts) == 4:
                records.append({
                    "timestamp": parts[0],
                    "user_id": parts[1],
                    "endpoint": parts[2],
                    "status_code": int(parts[3]),
                })

    # Write CSV
    fieldnames = ["timestamp", "user_id", "endpoint", "status_code"]
    with open(output_csv_path, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)

    # Write JSON
    with open(output_json_path, mode="w", encoding="utf-8") as f:
        json.dump(records, f, indent=2)

    return records


if __name__ == "__main__":
    pass
