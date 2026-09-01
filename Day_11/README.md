# Day 11: Web Frameworks (Part 2) & Web Scraping

Welcome to Day 11! Today we conclude our Python web technologies and scraping modules. We will cover:
1. **Dynamic Web Applications (Flask + SQLite)**: Designing page templates, processing HTML form submissions, and managing database connections.
2. **Web Scraping Foundations**: Extracting web page HTML using the `requests` library and bypassing basic crawler blocks using custom headers (`User-Agent`).
3. **HTML Parsing with BeautifulSoup**: Navigating the Document Object Model (DOM) and extracting tag attributes and text elements.
4. **Structured Crawling with Scrapy**: Building spiders, setting up pagination followers, and processing items via Database Pipelines.
5. **Wrangling Web Tables**: Utilizing Pandas `pd.read_html()` to parse tables in single function calls.

> [!NOTE]
> **Prerequisites**: It is highly recommended to run the database web application and scraping examples inside an isolated virtual environment.
>
> **Step A: Setup & Activate Virtual Environment**
> * macOS/Linux: `python -m venv .venv && source .venv/bin/activate`
> * Windows (CMD): `python -m venv .venv && .venv\Scripts\activate.bat`
> * Windows (PS): `python -m venv .venv && .venv\Scripts\Activate.ps1`
>
> **Step B: Install Libraries**
> ```bash
> pip install flask requests beautifulsoup4 scrapy lxml html5lib
> ```

---

## Part 1: SQLite-Powered Flask Web Applications

A dynamic web application renders views by pulling data from a database and injecting it into HTML templates. We use Jinja2 syntax in Flask templates to perform loops and conditions.

### 1. Project Directory Structure
For Flask to find templates and static files (like stylesheets), you must organize files into standard subfolders:
```text
my_web_app/
  |- app.py (Main Python application)
  |- templates/
      |- list_books.html (Jinja2 Template file)
  |- static/
      |- style.css (Static stylesheet)
```

### 2. Implementation: Flask App with SQLite
Here is a complete Flask application that queries database items and allows users to append items via HTML form posts.

**Flask backend (`app.py`):**
```python
import sqlite3
from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)
DB_FILE = "library.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT, author TEXT)")
    conn.commit()
    conn.close()

# HTML template with Jinja2 loop syntax
TEMPLATE_HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Library Catalog</title>
</head>
<body>
    <h1>Book Collection</h1>
    <ul>
        {% for book in books %}
            <li><strong>{{ book[1] }}</strong> by {{ book[2] }}</li>
        {% endfor %}
    </ul>

    <hr>
    <h2>Add a New Book</h2>
    <form method="POST" action="/add-book">
        Title: <input type="text" name="title"><br>
        Author: <input type="text" name="author"><br>
        <input type="submit" value="Add Book">
    </form>
</body>
</html>
"""

@app.route("/books")
def list_books():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    conn.close()
    return render_template_string(TEMPLATE_HTML, books=books)

@app.route("/add-book", methods=["POST"])
def add_book():
    title = request.form.get("title")
    author = request.form.get("author")
    
    if title and author:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO books (title, author) VALUES (?, ?)", (title, author))
        conn.commit()
        conn.close()
        
    return redirect(url_for("list_books"))

if __name__ == "__main__":
    init_db()
    # app.run(debug=True)
```

---

## Part 2: Web Scraping with BeautifulSoup

**Web Scraping** is the technique of programmatically downloading web pages and extracting data points from their HTML structure.

### 1. HTTP Requests and Custom Headers
Many websites block default automation tools. To bypass these restrictions, add a **`User-Agent`** string to your HTTP request headers.

```python
import requests

url = "https://quotes.toscrape.com/"
custom_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

response = requests.get(url, headers=custom_headers)
print("HTTP Status Code:", response.status_code) # Output: 200
```

### 2. Navigating the HTML DOM
Use **BeautifulSoup** to parse HTML and search for specific tags using CSS classes, IDs, or element names.

```python
from bs4 import BeautifulSoup

# Initialize BeautifulSoup parser
soup = BeautifulSoup(response.text, "html.parser")

# 1. Locate elements by class name
quote_boxes = soup.find_all("div", class_="quote")

for box in quote_boxes:
    # 2. Extract text contents
    text = box.find("span", class_="text").get_text()
    author = box.find("small", class_="author").get_text()
    print(f"Quote: {text} | Author: {author}")
```

---

## Part 3: Web Crawling with Scrapy

**Scrapy** is a powerful Python framework designed for crawling websites. While BeautifulSoup parses single pages, Scrapy is optimized for traversing pagination links recursively and pipeline operations.

### 1. Basic Spider and Pagination
In Scrapy, you define a `Spider` class containing start URLs and parse callbacks.

```python
import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes_spider"
    start_urls = ['https://quotes.toscrape.com/']

    def parse(self, response):
        # Loop through quote boxes
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
            }

        # Locate next page link and crawl recursively
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            # Yield request to follow link
            yield response.follow(next_page, callback=self.parse)
```

### 2. Item Pipelines
Pipelines process scraped items yielded by the spider (e.g., verifying attributes, deduplicating, or committing directly to a database).

```python
import sqlite3
from scrapy.exceptions import DropItem

class SQLitePipeline:
    def open_spider(self, spider):
        # Open database connection on startup
        self.conn = sqlite3.connect("quotes.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS quotes (text TEXT, author TEXT)")

    def process_item(self, item, spider):
        # Validation checks
        if not item.get("text") or not item.get("author"):
            raise DropItem("Missing text or author.")
            
        # Parameterized insert
        self.cursor.execute("INSERT INTO quotes VALUES (?, ?)", (item["text"], item["author"]))
        self.conn.commit()
        return item

    def close_spider(self, spider):
        # Close connection when crawl completes
        self.conn.close()
```

---

## Part 4: Pandas Web Table Scraper

If you need to extract structured rows and columns from HTML table elements, Pandas offers `pd.read_html()`, which scans the page and returns all found tables as a list of DataFrames.

```python
import pandas as pd

# Target URL containing table elements
url = "https://www.w3schools.com/html/html_tables.asp"

# Parse tables
tables = pd.read_html(url)
print("Total tables found:", len(tables))

# Inspect first table
df = tables[0]
print(df.head(2))
```
