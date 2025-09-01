1. Extract all emails from text

📌 Problem: You scraped a "Contact Us" page and need all emails.

import re

text = """
For inquiries contact us at support@example.com, or sales@example.co.uk.
"""

pattern = r"[\w\.-]+@[\w\.-]+\.\w+"
emails = re.findall(pattern, text)

print(emails)


✅ Solves: Finding all email addresses in messy text.

2. Extract all links (href) from HTML

📌 Problem: You want all links from an <a> tag.

import re

html = """
<a href="https://example.com">Home</a>
<a href="https://example.com/about">About</a>
"""

pattern = r'href="([^"]+)"'
links = re.findall(pattern, html)

print(links)


✅ Solves: Pulling URLs without a full HTML parser.

3. Extract prices

📌 Problem: Scraped product page with prices like $29.99.

import re

text = """
Our prices are $29.99, $49, and special offer $199.00!
"""

pattern = r"\$\d+(?:\.\d{2})?"
prices = re.findall(pattern, text)

print(prices)


✅ Solves: Finding dollar amounts (with or without decimals).

4. Extract dates (YYYY-MM-DD)

📌 Problem: You need structured dates from scraped text.

import re

text = """
Upcoming events: 2025-09-02, 2025-10-15, and 2026-01-01.
"""

pattern = r"\d{4}-\d{2}-\d{2}"
dates = re.findall(pattern, text)

print(dates)


✅ Solves: Getting ISO-style dates.

5. Extract numbers (views, likes, counts)

📌 Problem: You scraped a stats section with numbers like Views: 1200.

import re

text = """
This video has 1200 views, 89 comments, and 45 likes.
"""

pattern = r"\d+"
numbers = re.findall(pattern, text)

print(numbers)


✅ Solves: Extracting all integers from text.

6. Extract image sources

📌 Problem: Scraping <img> tags for image URLs.

import re

html = """
<img src="https://example.com/image1.jpg">
<img src="https://example.com/image2.png">
"""

pattern = r'<img[^>]+src="([^"]+)"'
images = re.findall(pattern, html)

print(images)


✅ Solves: Pulling image links for downloading.





🕷️ Web Scraping Regex Practice: The 20% You'll Actually Use! 🎯
Ready to practice the most useful regex patterns for web scraping? Let's dive in!

📋 The Challenge HTML
Imagine you scraped this messy HTML content and need to extract specific data:

html
<div class="products">
    <p>Contact us at support@example.com or sales@company.com for help.</p>
    
    <div class="product" data-price="$29.99">
        <h3>Awesome Widget</h3>
        <p>Price: $29.99 <span class="discount">Now $19.99!</span></p>
        <a href="https://example.com/product/123">View Details</a>
    </div>
    
    <div class="product" data-price="$149.50">
        <h3>Premium Gadget</h3>
        <p>Price: $149.50</p>
        <a href="/products/456">Learn More</a>
    </div>
    
    <p>Follow us on Twitter @example or visit https://example.com/social</p>
    <img src="https://example.com/images/banner.jpg" alt="Summer Sale">
</div>
🎯 Your Tasks & Solutions
1. Extract ALL Email Addresses
Pattern: [\w\.-]+@[\w\.-]+\.\w+

Matches:

support@example.com

sales@company.com

Why it works:

[\w\.-]+ → matches name part (letters, numbers, dots, hyphens)

@ → literal @ symbol

[\w\.-]+ → matches domain name

\. → literal dot

\w+ → matches TLD (com, org, net, etc.)

2. Extract ALL Prices (including the discounted one!)
Pattern: \$\d+(?:\.\d{2})?

Matches:

$29.99

$19.99

$149.50

Why it works:

\$ → literal dollar sign (escaped with )

\d+ → one or more digits

(?:\.\d{2})? → optional decimal point followed by exactly two digits

3. Extract ALL URLs (both absolute and relative)
Pattern: https?://[^\s"]+ (for absolute URLs)

Matches:

https://example.com/product/123

https://example.com/social

https://example.com/images/banner.jpg

For relative URLs too: (?:https?://)?[^\s"]+ would also match /products/456

4. Extract Image Source
Pattern: <img[^>]+src="([^"]+)"

Match: https://example.com/images/banner.jpg

Why it works:

<img → start of img tag

[^>]+ → any characters until >

src=" → literal src attribute start

([^"]+) → capture group for everything until closing quote

5. Extract Social Media Mention
Pattern: @\w+

Match: @example

Why it works:

@ → literal @ symbol

\w+ → one or more word characters

💡 Pro Tips for Real Web Scraping:
Combine regex with proper HTML parsing - use BeautifulSoup (Python) or Cheerio (JS) to isolate specific elements first, THEN apply regex to extract patterns from the text.

Test your patterns - use regex101.com or regexr.com to test patterns before implementing them.

Be specific - the more specific your pattern, the less likely you'll get false positives.

Handle errors - always assume the pattern might not match and handle those cases gracefully.