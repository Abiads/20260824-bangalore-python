"""
### Assignment 3: Academic Tables Extractor (Pandas & BeautifulSoup)
#### Scenario
A research department analyzes national demographics tables. You need to write a utility that parses HTML tables from a target webpage and saves them to a CSV spreadsheet.

#### Problem Description
Write a function `extract_html_table_to_csv(url, table_id, output_csv_path)`:
1. **Fetch & Locate**:
   - Fetch the raw HTML from `url` using `requests` with a custom `User-Agent` header.
   - Use BeautifulSoup to locate the specific `table` element in the parsed DOM matching the given ID attribute (`id=table_id`).
   - If no table matches the ID, raise a `ValueError` with the message: `"Table with id '<table_id>' not found."`
2. **Pandas Parsing**:
   - Convert the BeautifulSoup table tag element to a string, and pass it to Pandas: `pd.read_html(str(table_element))`.
   - Extract the first DataFrame from the parsed list of tables.
3. **Clean & Save**:
   - Clean the DataFrame: Drop any columns that are entirely null/empty (`NaN`) using `.dropna(how='all', axis=1)`.
   - Save the cleaned DataFrame to `output_csv_path` as a CSV file (set `index=False` to ignore row indexes).
4. **Return**: The total number of rows written to the CSV file (integer).

#### Example Walkthrough
```python
# Extract and save population details from Wikipedia sandbox
url = "https://en.wikipedia.org/wiki/List_of_countries_by_population_(United_Nations)"
try:
    row_count = extract_html_table_to_csv(url, "wikitable", "wiki_population.csv")
    print(f"Extracted {row_count} rows.")
except ValueError as e:
    print(e)
```
"""

def solve():
    # TODO: Implement your solution here
    pass

if __name__ == "__main__":
    solve()
