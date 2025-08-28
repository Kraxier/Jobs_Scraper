
# 🧾 Fundamentals of Saving Scraped Data in JSON

# What is JSON?
r'''
. JSON is a structured text format
    * Stores data as key–value pairs (dict-like objects).
    * Preserves data types: numbers, strings, booleans, arrays, nested objects.
    * Makes it flexible for complex scraped data (e.g., job listings with tags, skills, requirements).
'''

# What is the 2 Main Styles of JSON? 

# a) Standard JSON (Array format)
r'''
Example: (.json)
[
  {"Role": "Engineer", "Company": "Acme"},
  {"Role": "Designer", "Company": "Beta"}
]
'''
r'''
* Whole dataset wrapped in an array ([...]).
* Needs to keep the entire list in memory until the file is closed.
* Good for small datasets or when exporting a single JSON file for sharing.
'''

# b) JSONL (JSON Lines / Newline-delimited JSON)
r'''
Example: (.json)
{"Role": "Engineer", "Company": "Acme"}
{"Role": "Designer", "Company": "Beta"}
'''
r'''
* Each line is an independent JSON object.
* Stream-friendly: write records one by one during scraping.
* Robust: if scraper crashes, file is still valid (all previous lines are fine).
* Best for long-running scrapers or big datasets.
'''

########################## How to Write JSON Safely? ##########################
r'''
    * Always open files in UTF-8 encoding (encoding="utf-8") so special characters don’t break.
    * Use json.dumps(record, ensure_ascii=False) to keep text readable (accents, symbols).
    * Use indent=2 for human-friendly pretty files (slower, bigger).
    * Use compact form (no indent) for performance/space efficiency
'''
########################## How to Handle Large Scrapes? ##########################
r'''
    * Don’t hold everything in memory → write incrementally (JSONL).
    * Rotate files daily (e.g., data_2025-08-29.jsonl) for very large jobs.
    * Optionally compress old files (.jsonl.gz) to save disk space.
'''

########################## How to Convet JSON to Different Files? ##########################
# JSON/JSONL is the best intermediate storage.
import pandas as pd
df = pd.read_json("data.jsonl", lines=True)
df.to_csv("data.csv", index=False)
df.to_excel("data.xlsx", index=False)
df.to_parquet("data.parquet", index=False)


# Fundamentals of Writing JSON in Python for Web Scraping


# 1. Standard JSON (Array Format)
import json

# Sample scraped data
scraped_data = [
    {"Role": "Engineer", "Company": "Acme", "Skills": ["Python", "SQL"]},
    {"Role": "Designer", "Company": "Beta", "Skills": ["Figma", "UI/UX"]}
]

# Write to file (good for small datasets)
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(scraped_data, f, ensure_ascii=False, indent=2)

# 2. JSONL (Recommended for Scraping)
import json

# Sample scraped data (one record at a time)
records = [
    {"Role": "Engineer", "Company": "Acme", "Skills": ["Python", "SQL"]},
    {"Role": "Designer", "Company": "Beta", "Skills": ["Figma", "UI/UX"]}
]

# Write to JSONL file (streaming-friendly)
with open("data.jsonl", "w", encoding="utf-8") as f:
    for record in records:
        json_line = json.dumps(record, ensure_ascii=False)
        f.write(json_line + "\n")

# How to Write JSON: writing with Error Handling: 
import json
import os
from datetime import datetime

def safe_scrape_and_save():
    # Create filename with timestamp
    filename = f"scraped_data_{datetime.now().strftime('%Y-%m-%d')}.jsonl"
    
    # Open file in append mode (so we can add to existing file if needed)
    with open(filename, "a", encoding="utf-8") as f:
        try:
            # Simulated scraping loop
            for page in range(1, 101):  # 100 pages to scrape
                # Simulate scraping a page
                scraped_items = scrape_page(page)
                
                for item in scraped_items:
                    # Add metadata
                    item["scraped_at"] = datetime.now().isoformat()
                    item["source_page"] = page
                    
                    # Write to JSONL
                    json_line = json.dumps(item, ensure_ascii=False)
                    f.write(json_line + "\n")
                    f.flush()  # Ensure data is written immediately
                    
        except Exception as e:
            print(f"Error during scraping: {e}")
            # File remains valid because we wrote complete JSON objects

def scrape_page(page_num):
    # Your scraping logic here
    # This would typically use requests/BeautifulSoup or Scrapy
    # Return a list of dictionaries with extracted data
    
    # Simulated return for example
    return [{"product": f"Item {page_num}_{i}", "price": 10*i} for i in range(3)]

# How to Reading JSONL Back
import json

def read_jsonl(filename):
    data = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            data.append(json.loads(line))
    return data

# Usage
records = read_jsonl("data.jsonl")
print(f"Loaded {len(records)} records")


###### How to Converting JSONL to Other Formats
import pandas as pd

# Convert JSONL to DataFrame
df = pd.read_json("data.jsonl", lines=True)

# Save to other formats
df.to_csv("data.csv", index=False, encoding="utf-8")
df.to_excel("data.xlsx", index=False)
df.to_parquet("data.parquet", index=False)


#### What is the Best Practice for JSON: 
r'''
Best Practices Summary
    1. Use JSONL for scraping - it's streaming-friendly and crash-resistant
    2. Always specify encoding - use encoding="utf-8" to handle special characters
    3. Use ensure_ascii=False - to preserve non-ASCII characters correctly
    4. Add metadata - include timestamps and source information
    5. Implement error handling - so your file remains valid even if scraping fails
    6. Flush regularly - use f.flush() to ensure data is written immediately
    7. Validate your JSON - occasionally check that your output is valid JSON
'''
