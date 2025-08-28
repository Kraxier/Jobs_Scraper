
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

####### How to Write JSON Safely? ##########################
r'''
    * Always open files in UTF-8 encoding (encoding="utf-8") so special characters don’t break.
    * Use json.dumps(record, ensure_ascii=False) to keep text readable (accents, symbols).
    * Use indent=2 for human-friendly pretty files (slower, bigger).
    * Use compact form (no indent) for performance/space efficiency
'''


