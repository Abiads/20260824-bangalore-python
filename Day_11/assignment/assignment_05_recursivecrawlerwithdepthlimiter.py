"""
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
"""

def solve():
    # TODO: Implement your solution here
    pass

if __name__ == "__main__":
    solve()
