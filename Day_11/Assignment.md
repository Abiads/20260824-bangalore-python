# Day 11 Practice Assignments: Web Scraping & Database Integration

## Objective
Combine web framework layouts with local databases, implement web scrapers using BeautifulSoup and custom request headers, write recursive crawlers, and simulate Scrapy Spider classes and pipeline components.

---

## Easy Assignments

### Assignment 1: Academic Quotes Collector (BeautifulSoup Scraper)
#### Scenario
You are building an educational dashboard. You need to write a scraper that extracts quotes and authors from the sandbox quotes website and saves the formatted results to a local text file.

#### Problem Description
Write a function `scrape_academic_quotes(url, output_file_path)`:
1. **HTTP Request**:
   - Use the `requests` library to fetch the HTML content of the target quotes website `url` (e.g. `https://quotes.toscrape.com/`).
   - Define a custom request headers dictionary containing a browser identity:
     `{"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}`.
     Pass this headers dictionary in your `requests.get()` call.
2. **Parsing**:
   - Parse the page content using BeautifulSoup (`html.parser`).
   - Locate all quote container blocks (represented by `div` tags with class `"quote"`).
   - From each block, extract:
     - The quote text (inside a `span` tag with class `"text"`).
     - The author name (inside a `small` tag with class `"author"`).
3. **Save**:
   - Write the parsed quotes and authors to a local text file at `output_file_path` in the exact format:
     `"Quote: <quote_text> | Author: <author_name>\n"`.
4. **Return**: The total count of quotes parsed and written (integer).

#### Example Walkthrough
```python
total_quotes = scrape_academic_quotes("https://quotes.toscrape.com/", "scraped_quotes.txt")
print(f"Scraped {total_quotes} quotes.")
# Check your local folder for a file named "scraped_quotes.txt" containing 10 lines.
```

---

### Assignment 2: SQLite-Powered Library Directory (Flask Web App)
#### Scenario
You are developing a library registry database portal. The backend needs to query book registers from an SQLite database and display them on a web page, and allow users to append new book titles using an HTML form.

#### Problem Description
Implement a complete Flask web application connected to a local SQLite database named `library.db`:
1. **Database Setup**:
   - In your initialization code, check if the table `books` exists. If not, create it:
     `id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, author TEXT`.
2. **Flask Routes**:
   - **`GET /books`**:
     - Establishes an SQLite database connection and queries all records from the `books` table.
     - Formats and returns an HTML list string containing the book records. Each book must be rendered inside a list element:
       `<li><strong><title></strong> by <author></li>`.
     - Include a simple HTML form pointing to `POST /add-book` at the bottom of the page:
       ```html
       <form method="POST" action="/add-book">
           Title: <input type="text" name="title"><br>
           Author: <input type="text" name="author"><br>
           <input type="submit" value="Add Book">
       </form>
       ```
   - **`POST /add-book`**:
     - Extracts the form fields `"title"` and `"author"` from the request (`request.form.get()`).
     - **Validation**: If either parameter is missing or empty, return a plain text error message `"Error: Title and Author are required!"` with an HTTP status code of `400`.
     - If both are valid, execute a parameterized SQL INSERT query to append the book record to `library.db`, commit the changes, and redirect the client to `/books` (using `redirect(url_for('list_books'))` or direct path).
3. Ensure cursors and database connections are closed cleanly inside each route handler.

*Note: Define the Flask app instance variable as `app`.*

---

## Medium Assignments

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

---

### Assignment 4: Dynamic News Portal with Auto-Updater
#### Scenario
You are developing a news aggregation page. The web server needs a route `/refresh-news` that scrapes article headlines and links from a news portal, inserts them into an SQLite database, and displays them on a styled homepage.

#### Problem Description
Implement a Flask application connected to a local SQLite database named `news.db`:
1. **Database Setup**:
   - Create a table named `articles` if it does not exist:
     `id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT UNIQUE, url TEXT`.
2. **Flask Routes**:
   - **`GET /`**:
     - Queries all records from the `articles` table in `news.db`.
     - Returns an HTML string rendering each article headline as a clickable link:
       `[CONSOLE] <a href="<url>"><title></a><br>`.
   - **`GET /refresh-news`**:
     - Fetches raw HTML from Hacker News (`https://news.ycombinator.com/`) using `requests` and a custom `User-Agent` header.
     - Parse the HTML with BeautifulSoup to locate the top 10 article title lines. (In Hacker News, these are represented by `span` elements with class `"titleline"`, containing a nested `a` tag).
     - Extract the text of the link (the title) and the link destination (`href`).
     - Loop through the top 10 articles and execute a parameterized SQLite query to insert them into `news.db`.
       - **Constraint**: Use `INSERT OR IGNORE` to prevent database crashes when trying to insert duplicate titles.
     - Commit the transaction, close database resources, and redirect the user back to the homepage `/`.

---

## Difficult Assignments

### Assignment 5: Recursive Crawler with Depth Limiter
#### Scenario
Search engine crawlers index web pages by recursively following hyperlinks on a page. You need to write a crawler that traverses links starting from a base URL up to a maximum depth limit, avoiding loops by tracking visited links.

#### Problem Description
Write a function `recursive_link_crawler(base_url, max_depth, max_links)`:
1. **State Tracking**:
   - Track visited URLs in a set to avoid loops.
   - Maintain a dictionary mapping each visited URL to a list of internal hyperlinks discovered on its page:
     `{url: [list_of_internal_links]}`.
2. **Recursion Details**:
   - Start crawling at `base_url` (Depth 0).
   - Follow discovered internal links recursively up to `max_depth` (Depth `max_depth` represents the last depth layer where links are parsed but not crawled further).
   - If the total number of unique visited URLs reaches `max_links`, stop crawling immediately.
3. **Page Scraper Rules**:
   - Fetch each page using `requests.get()` with custom `User-Agent` headers. Set a timeout threshold of `3.0` seconds. If a request fails, times out, or returns a non-200 status, log a warning and skip the URL.
   - Parse the page using BeautifulSoup and extract the `href` attribute of all `<a>` tags.
   - Clean and filter links:
     - If a link is relative (e.g. `"/about"`), convert it to absolute using `urllib.parse.urljoin(current_page, link)`.
     - Ignore any anchor links (starting with `#`) or mailto links.
     - **Domain Filter**: Only crawl and store links that belong to the **same domain (netloc)** as the `base_url`. (For example, if crawling `https://quotes.toscrape.com`, ignore links pointing to `https://github.com`).
4. **Return**: The dictionary of discovered links mapping.

#### Example Walkthrough
```python
# Limit crawl to a maximum depth of 1 and a maximum of 5 unique pages
crawler_map = recursive_link_crawler("https://quotes.toscrape.com/", max_depth=1, max_links=5)

for page, links in crawler_map.items():
    print(f"Page: {page} | Found {len(links)} internal links.")
```

---

### Assignment 6: Scrapy Database Pipeline and Product Crawler
#### Scenario
You are configuring a data pipeline for a web scraping project. In Scrapy, spiders crawl pages and yield scraped items, which are then passed through pipelines to be validated and saved to databases. You need to simulate this architecture in a single script.

#### Problem Description
Write a Python script that implements a Scrapy Spider class and a companion Database pipeline:
1. **Class `QuotesSpider` (inherits from `scrapy.Spider`)**:
   - Set properties:
     - `name = "quotes"`
     - `start_urls = ["https://quotes.toscrape.com/"]`
   - Implement the `parse(self, response)` method:
     - Iterate through quote container blocks on the page.
     - For each quote, extract the quote text and the author name.
     - Yield a dictionary containing: `{"text": <text_string>, "author": <author_string>}`.
     - Find the pagination `"Next"` page button link (`response.css('li.next a::attr(href)').get()`).
     - If it exists, yield a follow-up request to crawl it recursively:
       `yield response.follow(next_page, callback=self.parse)`.
2. **Class `SQLitePipeline`**:
   - Implement the standard Scrapy Pipeline interface:
     - **`__init__(self, db_name="quotes.db")`**: Accepts a database name.
     - **`open_spider(self, spider)`**: Establishes a connection to the database and creates a table named `quotes` if it does not exist: `id INTEGER PRIMARY KEY AUTOINCREMENT, text TEXT, author TEXT`.
     - **`process_item(self, item, spider)`**:
       - Receives the yielded item dict from the spider.
       - **Validation**: Check if `text` or `author` keys are empty. If either is missing or empty, raise Scrapy's built-in `DropItem` exception (import `DropItem` from `scrapy.exceptions`).
       - If valid, execute a parameterized SQLite query to insert the quote text and author into the `quotes` table. Commit the transaction and return the `item`.
     - **`close_spider(self, spider)`**: Closes the database connection cleanly.
3. Write a short mock test driver at the bottom of the script that instantiates `SQLitePipeline` and calls its methods using mock dictionary items to demonstrate that the database insertion and validation work.
