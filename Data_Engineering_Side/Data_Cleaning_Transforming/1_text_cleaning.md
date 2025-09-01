# 🧹 Text Cleaning

## 1. Remove HTML
**Meaning:** Many web-scraped or copy-pasted texts contain HTML tags (like `<p>`, `<br>`, `<span>`, etc.). These tags are for formatting on web pages but are useless (and messy) for text analysis.

**Example before cleaning:**
```html
<p>We need a developer to build a website.</p><br>Contact us at: hello@company<span>.com</span>
```

**After removing HTML:**
```
We need a developer to build a website. Contact us at: hello@company.com
```

---

## 2. Newlines
**Meaning:** These are line breaks in text, represented by the escape sequence `
`. They make the text go to a new line (like pressing "Enter").

**Example before cleaning:**
```
Hello World!
This is a new line.
```

**Appears as:**
```
Hello World!
This is a new line.
```

**After cleaning:**
```
Hello World! This is a new line.
```

---

## 3. Extra Spaces
**Meaning:** Sometimes text contains multiple spaces, tabs (`	`), or leading/trailing spaces that aren’t useful.

**Example before cleaning:**
```
"   Urgently   Needed:   Web Dev    (PHP, JavaScript)!!!   "
```

**After cleaning:**
```
"Urgently Needed: Web Dev (PHP, JavaScript)!!!"
```

---

## 4. Normalize Encodings
**Meaning:** Text from different sources may contain weird/unreadable characters due to encoding issues (UTF-8, ASCII, etc.) or special representations of characters. Normalization converts them into a standard, consistent form.

**Examples:**
- Curly quotes → straight quotes:  
  `“Hello”` → `"Hello"`
- Non-breaking space (`&nbsp;`) → normal space
- Unicode variations (like `é`, `é` with accent as separate character) → `é`

This ensures the text looks clean and avoids problems when comparing or analyzing words.

---

## ✅ In short:
- **Remove HTML** → delete web formatting tags  
- **Newlines** → replace line breaks (`
`) with spaces  
- **Extra Spaces** → collapse multiple spaces into one  
- **Normalize Encodings** → make sure characters are stored/displayed consistently  

---

# 🔧 Tools for Text Cleaning

When you scrape text (with Playwright, Scrapy, or other tools), you usually end up with raw HTML and need to clean it. Here are the most common tools:

---

## 1. BeautifulSoup (bs4)
**What it does:** Parses HTML, removes tags, extracts only the text.

**Example:**
```python
from bs4 import BeautifulSoup

html = "<p>Hello <b>World</b></p>"
text = BeautifulSoup(html, "html.parser").get_text()
print(text)  # "Hello World"
```

✅ Best for removing HTML tags and getting readable text.

---

## 2. Regular Expressions (re module in Python)
**What it does:** Lets you search, replace, or match patterns in text (like spaces, newlines, emails, etc.).

**Example:**
```python
import re

text = "Hello     World

This is   messy"
text = re.sub(r'\s+', ' ', text)  # collapse spaces and newlines
print(text)  # "Hello World This is messy"
```

✅ Best for newlines, extra spaces, emails, phone numbers, etc.

**What is `re`?**  
It’s Python’s Regular Expressions library (built-in).  
Regular expressions are like patterns that match text.  

**Examples:**
- `\s+` → one or more spaces/newlines/tabs  
- `\d+` → one or more digits  
- `\w+` → one or more letters/numbers  

---

## 3. String Methods (built-in Python)
Sometimes you don’t need regex, just `.strip()`, `.replace()`, etc.

**Example:**
```python
text = "   Hello World!   "
print(text.strip())  # "Hello World!"
```

---

## 4. Scrapy (if you’re using it)
Scrapy has built-in selectors (xpath, css) that can pull text directly without HTML.

**Example:**
```python
response.css("p::text").getall()
```

✅ Can save you from needing BeautifulSoup in many cases.

---

## 5. Playwright
Playwright itself doesn’t have text-cleaning, but it can give you clean inner text directly.

**Example:**
```python
element = page.locator("p")
print(element.inner_text())
```

✅ Sometimes avoids extra cleaning.

---

## 6. Unidecode / ftfy (for encoding issues)
- **Unidecode** → converts weird characters to plain text.  
- **ftfy** (“fixes text for you”) → fixes messy Unicode issues.  

**Example:**
```python
from unidecode import unidecode

print(unidecode("“Héllo”"))  # "Hello"
```

---

# 🛠️ Which do you actually need?
- If you use **Scrapy** or **Playwright**, you can already grab plain text, but sometimes it still has line breaks, spaces, or encodings.  
- Use **BeautifulSoup** if you’re scraping with raw requests.  
- Use **re (regular expressions)** for cleanup of spaces, newlines, symbols, etc.  
