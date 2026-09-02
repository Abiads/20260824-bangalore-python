"""
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
"""

def solve():
    # TODO: Implement your solution here
    pass

if __name__ == "__main__":
    solve()
