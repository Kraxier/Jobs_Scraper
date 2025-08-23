r'''
Phase 1: The "Can I Even Do This?" Check (Legal & Ethical)
This is the most critical phase. Always do this first.
robots.txt: Check https://<website.com>/robots.txt.
What to look for: Disallow rules. If the path you want to scrape is disallowed, you should respect it. It's a strong signal.
Your Example: Disallow: /click/ is fine. You're not scraping that path. You are "safe" from a robots.txt perspective.
Terms of Service (ToS): Find the website's Terms of Service or Acceptable Use Policy.

What to look for: Explicit clauses that forbid "scraping," "crawling," "data extraction," or "automated access." If it's forbidden, proceeding is a legal risk.

Data Sensitivity: Is the data you're scraping personal (user profiles, emails, phone numbers) or copyrighted (news articles, premium content)? Scraping personal data (especially in regions with laws like GDPR) is high-risk and often unethical.

Phase 2: Understanding the Website's Structure
How is the website built? This tells you what tools you'll need.

Static vs. Dynamic Content:

The Test: Right-click on the page and select "View Page Source". Search for the data you want (e.g., a job title or salary).

If you find it: The data is static. You can use simpler tools like requests and BeautifulSoup.

If it's missing: The data is loaded dynamically by JavaScript. You will need a tool that can run JS, like Playwright or Selenium.

Page Types & URL Patterns:

Identify Templates: Are you scraping a list of items (search results) and then individual detail pages? Note the URL structure.

Pagination: How does the site load more items? "Next" button? Does the URL change (?page=2)? Or does it load more data via a background API call (see Phase 3)?

Phase 3: Finding the Data Source (The Detective Work)
This is where Developer Tools become essential. Open the Network Tab before interacting with the site.

Look for a Hidden API (The Jackpot):

Process: Go to the Network Tab. Filter by XHR or Fetch. Now perform the action that loads the data you want (e.g., click "next page", search for a job).

What to look for: New requests appearing in the list. Click on them.

If you find one: Check the Headers tab to see the exact URL (Request URL) and method (GET/POST) needed to call it. Check the Preview or Response tab to see if it returns clean, structured JSON data. This is ideal and much easier to parse than HTML.

Headers & Cookies:

If you find an API or if even a simple requests.get() fails, you need to inspect headers.

In the Network Tab, click on any request (even the main document) and look at the Headers tab. Request Headers are what your browser sent.

Key Headers to replicate: User-Agent, Referer, and sometimes Accept-Language. Modern sites also use Sec-Fetch-* headers, which can be hard to fake but are sometimes important.

Phase 4: Planning the Extraction
Once you know where the data lives, figure out how to pull it out.

For HTML (Static or Rendered by Playwright):

Use the Elements Tab to inspect the data.

Right-click on the element containing the data and use Copy -> Copy selector or Copy XPath. Use these with BeautifulSoup or Playwright's query_selector().

Your <p> tag problem: You need to find a unique parent container for each job listing. Then, within that container, you can target the specific <p> tags or other elements reliably.

For JSON (from an API):

This is easier. You parse the JSON response (e.g., with response.json())

Phase 5: Avoiding Blocks (The Cat-and-Mouse Game)
Implement this after you have a basic scraper working.

Rate Limiting:

Always add delays between your requests (time.sleep()). Being polite is the best way to avoid detection.

Start with a 5-10 second delay. See how low you can go without getting blocked.

Mimicking a Real User:

Use realistic User-Agent strings.

Rotate user agents and other headers if you're making a lot of requests.

If using Playwright, use its built-in capabilities to mimic a real browser.

Proxies: If you are scraping at a very large scale, you will eventually need to rotate IP addresses using proxy servers to avoid IP bans.

'''