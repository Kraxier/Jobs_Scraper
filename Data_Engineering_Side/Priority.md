# The Core Philosophy: During Scraping vs. Post-Processing

The key is to **strike a balance**. Your goal is to do just enough cleaning during scraping to make the data structured and manageable, saving the heavy lifting for a dedicated **post-processing pipeline**.

---

## 1. Cleaning **DURING Scraping** (The "First Pass")

**Goal:**  
Reduce memory/bandwidth usage, avoid storing huge HTML blobs, and get immediately usable, semi-structured data.

**When to Do It:**  
Right after you extract text from an element, before storing it in your dataset.

### Tools & Techniques (The "What"):

- **Playwright’s `.inner_text()`** → Your first and best choice for getting clean, human-readable text. It automatically handles hidden elements and collapses whitespace.

```python
# ✅ During scraping - BEST for visible text
title = page.locator('.job-title').inner_text()
# Result: "Web Developer (PHP)" instead of "  Web   Developer <!-- comment --> (PHP)  "
```

- **Lightweight Regex on Extracted Text** → Use simple patterns to extract structured data from the text you just got.

```python
# ✅ During scraping - Extract a price right away
price_text = page.locator('.price').inner_text() # e.g., "Price: $29.99"
price_match = re.search(r'\$(\d+\.\d{2})', price_text)
price = float(price_match.group(1)) if price_match else None  # Store 29.99, not the whole string
```

- **Basic String Methods** → Use `.strip()` and simple `.replace()` for obvious fixes.

```python
# ✅ During scraping - Quick clean
company = page.locator('.company-name').inner_text().strip()
```

### ❌ What to AVOID During Scraping:

- Don’t run **complex, multi-step cleaning functions** on every element (slows down your scraper).
- Don’t make **complex parsing decisions** that might fail and crash your scraper.  
  👉 If a date is in an unexpected format, just store the raw string and handle it later.

---

## 2. Cleaning **POST-PROCESSING** (The "Power Wash")

**Goal:**  
Standardize, validate, and transform the collected semi-structured data into a final, analysis-ready dataset.

**When to Do It:**  
After you’ve finished scraping and collected all your data (e.g., a list of dictionaries, a CSV file).

### Tools & Techniques (The "What"):

- **Pandas (`pandas`)** → The ultimate tool for this phase.  
  Load scraped data into a DataFrame (`pd.read_csv()`, `pd.DataFrame(your_list_of_dicts)`).

- **Apply Complex Functions:**  
  ```python
  df['column'].apply(your_cleaning_function)
  ```

- **Handle Missing Data:**  
  ```python
  df.dropna()
  df.fillna()
  ```

- **Deduplicate:**  
  ```python
  df.drop_duplicates()
  ```

- **Flatten Nested Data:**  
  ```python
  pd.json_normalize()
  ```

- **Custom Parsing Functions:**  
  - `parse_price`, `parse_date` → Complex logic for parsing budgets, dates, and ratings.  
  - Test thoroughly without the pressure of a live scraper.

- **Standardization with Dictionaries:**  
  - `job_title_mapping`  
  - `tag_mapping`  

- **Advanced Regex & Validation:**  
  - Comprehensive validation checks (e.g., `is_valid_email`).

---

## What Tools Should You Learn? (A Prioritized List)

1. **Playwright (or Similar):**  
   Master the scraper itself. Understand `.inner_text()` vs `.text_content()` cold.  
   → This is your data collection engine.

2. **Regular Expressions (Regex):**  
   Non-negotiable. Most powerful tool for both scraping and post-processing.  
   - Focus on: `re.findall()`, `re.search()`, `re.sub()`  
   - Learn patterns for **emails, prices, URLs, dates**.

3. **Pandas:**  
   Data manipulation powerhouse.  
   - Focus on: `DataFrame`, `apply()`, `json_normalize()`, `drop_duplicates()`, filtering.

4. **BeautifulSoup:**  
   When you need to parse stored HTML fragments. Perfect complement to Playwright.

5. **Python’s Core Libraries:**  
   - `datetime` → Parsing & formatting dates  
   - `hashlib` → Generating unique IDs for deduplication  

6. **Custom Functions & Dictionaries:**  
   Write modular, reusable, maintainable cleaning code.

---

## The Ideal Workflow

### Scraping Script
1. Use Playwright to navigate and locate elements.  
2. Extract text using `.inner_text()`.  
3. Apply lightweight regex and `.strip()` to structure data (dict with `title`, `price`, `raw_date`).  
4. Append each record to a list.  
5. Save list to JSON or CSV.

### Post-Processing Script (Separate File)
1. Read file into a Pandas DataFrame.  
2. Apply custom functions (`parse_date`, `normalize_job_title`) with `df.apply()`.  
3. Use `pd.json_normalize()` for nested data.  
4. Validate data quality.  
5. Save final DataFrame to **CSV** or **Parquet** for analysis.

---
