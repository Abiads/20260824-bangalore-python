# Day 11 Practice Assignments: Web Scraping & Database Integration

## Objective
Combine web framework components with databases and crawl internet web pages to extract data elements.

---

### Exercise 1: HTML Element Scraper
Write a Python program using the `requests` and `BeautifulSoup` libraries:
1. Fetch the raw HTML content of the quotes website: `https://quotes.toscrape.com/`
2. Extract all quote texts and their corresponding authors.
3. Print the formatted quotes to the console or write them to a text file `scraped_quotes.txt`.

---

### Exercise 2: SQLite-powered Flask Web App
Build a Flask application that integrates with an SQLite database:
1. Database Setup: Create a database `library.db` with a table `books` (`id` integer primary key, `title` text, `author` text).
2. Web View: Create a route `/books` that fetches all books from the database and renders them in an HTML list.
3. Web Form: Create a form route `/add-book` that allows users to type in a book title and author, and insert them into the database upon submission.

---

### Exercise 3: Recursive Web Link Scraper
Write a program using BeautifulSoup that starts on a target webpage, extracts all hyperlinks (`<a>` tags), and prints those hyperlinks that belong to the same domain.

---

### Exercise 4: Scrapy Pagination Crawler
Create a Scrapy Spider class that extracts item titles from an e-commerce sandbox page and automatically crawls to the next pages by finding and following the `"Next Page"` link element.

---

### Exercise 5: Scrapy Database Pipelines
Write a Scrapy Pipeline class that receives item data from a spider (e.g., quote and author) and inserts the items directly into an SQLite database table instead of standard file output.

---

### Exercise 6: Wikipedia Table Extractor
Write a script using Pandas `pd.read_html()` or BeautifulSoup to scrape a demographic table from a static Wikipedia page and convert it into a structured CSV file.

---

### Exercise 7: User-Agent Custom Header Scraper
Write a scraping script using the `requests` library that adds a custom browser `User-Agent` string to the request headers to fetch and parse pages that block default automation headers.

---

### Exercise 8: Complete Web Scraper Dashboard
Build an integrated data scraper dashboard:
1. Write a scraping routine to extract headlines from a tech news site.
2. Store the scraped news headlines in an SQLite database.
3. Build a Flask homepage that displays these headlines in a neat, styled grid layout.
