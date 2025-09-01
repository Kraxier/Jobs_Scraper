# 1. Text Cleaning (clean_text())
# Goal: Remove HTML, newlines, extra spaces, and normalize encodings.



# 🔧 Core Cleaning Snippets (the 20% that do 80% of the job)

# 1. Remove HTML tags
from bs4 import BeautifulSoup

html = "<p>Hello <b>World</b></p><br>Contact us at <span>info@example.com</span>"
text = BeautifulSoup(html, "html.parser").get_text(separator=" ")
print(text)  
# "Hello World Contact us at info@example.com"

# 2. Collapse whitespace (newlines, tabs, multiple spaces)
import re

text = "Hello     World\n\nThis\tis   messy"
clean = re.sub(r'\s+', ' ', text).strip()
print(clean)  
# "Hello World This is messy"

# 3. Unescape HTML entities
import html

text = "Tom &amp; Jerry&nbsp;are here &#39;today&#39;"
clean = html.unescape(text)
print(clean)  
# "Tom & Jerry are here 'today'"

# 4. Normalize Unicode (consistent characters)
import unicodedata

text = "cafe\u0301 vs café vs caf\u00e9"  # different forms of "é"
clean = unicodedata.normalize("NFKC", text)
print(clean)  
# "café vs café vs café"

# 5. Fix curly quotes / dashes
text = "“Smart quotes” and an em–dash — like this."
replacements = {
    '\u2018': "'", '\u2019': "'", 
    '\u201c': '"', '\u201d': '"',
    '\u2013': '-', '\u2014': '-',
    '\xa0': ' '  # non-breaking space
}
for bad, good in replacements.items():
    text = text.replace(bad, good)

print(text)  
# "Smart quotes" and an em-dash - like this.

# 6. Trim spaces
text = "   Extra spaces around   "
print(text.strip())  
# "Extra spaces around"

# 🔍 Regex Cheat-Sheet Snippets
# 7. Extract numbers (e.g., salary/budget)
import re

budget = "₱25,000-30,000"
match = re.search(r'([^\d\s]+)?\s*([\d,]+)(?:\s*-\s*([\d,]+))?', budget)
if match:
    currency, low, high = match.groups()
    low = int(low.replace(",", "")) if low else None
    high = int(high.replace(",", "")) if high else None
    print(currency, low, high)
# ₱ 25000 30000

# 8. Find email addresses
import re

text = "Contact us at: hello.world123@example.co.uk"
email = re.search(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', text)
print(email.group() if email else None)
# hello.world123@example.co.uk

# 9. Remove non-printable characters
import re

text = "Hello\u0000World\u0007!"
clean = re.sub(r'[\x00-\x1F\x7F]+', '', text)
print(clean)  
# "HelloWorld!"

# 🌐 Scrapy & Playwright Built-ins
# 10. Scrapy extract clean text
# Inside a Scrapy spider
response.css("p::text").getall()
# Returns a list of text values without <p> tags

# 11. Playwright extract clean text
# Inside Playwright
element = page.locator("p")
print(element.inner_text())  
# Returns text content without HTML tags

# ✨ Optional Helpers # I really needed this UniDecode
# 12. Unidecode (normalize to plain ASCII)
from unidecode import unidecode

text = "Héllo, München!"
print(unidecode(text))  
# "Hello, Munchen!"

# 13. ftfy (fix Unicode issues automatically)
from ftfy import fix_text

text = "This text has mojibake: CafÃ©"
print(fix_text(text))  
# "This text has mojibake: Café"


# ✅ With just snippets 1–6 you’ll already handle 80% of messy text problems.
# Regex snippets (7–9) cover most structured extraction.
# Scrapy/Playwright shortcuts (10–11) help you skip HTML parsing when possible.
