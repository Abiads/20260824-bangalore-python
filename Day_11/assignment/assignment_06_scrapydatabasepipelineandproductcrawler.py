"""
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
"""

def solve():
    # TODO: Implement your solution here
    pass

if __name__ == "__main__":
    solve()
