# import csv
# import random
# import time
# from datetime import datetime
# from urllib.parse import urljoin
# from playwright.sync_api import sync_playwright

# # Always import JSON 
# import json

# # Why there are OS right now 
# import os

# def start_jsonl_writer():
#     date_str = datetime.now().strftime("%Y-%m-%d")
#     filename = f"quote_{date_str}.jsonl"
#     f = open(filename, "w", encoding="utf-8")
#     print("📁 Writing JSONL to:", filename)
#     # Where is f.write("[\n")   
#     return f # Why there are no True? 

# def write_jsonl_record(f, record, flush=True):
#     f.write(json.dumps(record, ensure_ascii=False) + "\n")
#     # Starting from the if why there are Error Handling
#     if flush:
#         f.flush()
#         try:
#             os.fsync(f.fileno())
#         except Exception:
#             pass 

# # Should i Still do this ? 
# def close_json_array(f):
#     # Should i still do this ? 
#     f.write("\n]\n")                   # close JSON array
#     f.close()

# def extract_quote(page):
#     quotes = page.locator(".quote") # The Author and Quote are all Under of Quote blocks 
#     list_records = []

#     # Counting How many Quotes are currently in the page
#     for i in range(quotes.count()):
#         quote_text = quotes.nth(i).locator(".text").inner_text()
#         author_text = quotes.nth(i).locator(".author").inner_text()
#         r'''
#         quotes.nth(i)
#             * .nth(i) picks out the i-th element from that collection.
#             * i = 0 → first quote block
#             * i = 1 → second quote block
#         '''
#         print("Extracted:", quote_text, "-", author_text)
#         list_records.append({"Quote": quote_text, "Author": author_text})
#     return list_records

# def save_first_quote():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)  # set True to run headless
#         page = browser.new_page(viewport={"width":1366, "height":768})
#         page.goto("https://quotes.toscrape.com/js/", wait_until="domcontentloaded")

#         # Why did you remove the first? 
#         f, first = start_jsonl_writer()         # open file and mark "first"
#         record = extract_quote(page)                 # scrape a quote (dict)
#         write_jsonl_record(f, record)
#         close_json_array(f)                          # close the JSON array and file

#         browser.close()
#         print("✅ Saved successfully")

# if __name__ == "__main__":
#     save_first_quote()


r'''
Short answers to each inline question you asked

1. f.write("[\n") — where is it?
That line is only for JSON arrays. JSONL (a.k.a. .jsonl) is not a JSON array. Each line is a standalone JSON object, so you don’t write a [ at the start. That’s why start_jsonl_writer() does not write [\n.

2. return f # Why there are no True?
The True flag you used earlier (for arrays) tracks "is this the first object?" so we can insert commas. JSONL doesn’t need comma bookkeeping, so you don’t need to return a first boolean. Returning just f is correct.

3. if flush: and error handling around os.fsync
f.flush() pushes Python's internal buffer to the operating system.
os.fsync(f.fileno()) asks the OS to flush the OS buffers to disk (stronger guarantee).
We wrap os.fsync in try/except because fsync can sometimes fail or be unavailable in some environments (or raise permission errors). It’s safe to ignore that error; it’s only a best-effort durability measure.

4. Should i still do this? (close_json_array)
No, you should remove close_json_array in the JSONL flow. That function writes ]\n (closing bracket) which is only for JSON arrays. For JSONL you only need to f.close() when finished. (If you want, create close_writer(f) that just f.close(); not necessary but OK.)

5. Why did you remove the first?
Because we switched to JSONL, comma-tracking isn’t needed. So start_jsonl_writer() should return a single f (no first). Your current save_first_quote() still expects (f, first) — that’s the bug causing a crash.

6. record = extract_quote(page) returns a list
Your extract_quote returns list_records (i.e., multiple quotes). write_jsonl_record expects a single dict. You must either:
change extract_quote to return a single record, or
iterate through the list and call write_jsonl_record once per record (this is the common choice when scraping all quotes on a page).
'''


import json
import os
from datetime import datetime
from playwright.sync_api import sync_playwright

# ---------- JSONL helpers ----------
def start_jsonl_writer():
    """Open a .jsonl file and return the file handle."""
    date_str = datetime.now().strftime("%Y-%m-%d")
    filename = f"quote_{date_str}.jsonl"
    f = open(filename, "w", encoding="utf-8")
    print("📁 Writing JSONL to:", filename)
    return f

def write_jsonl_record(f, record, flush=True):
    """
    Write a single dict as one JSON line.
    - record: Python dict
    - flush: whether to flush to disk (f.flush() + os.fsync())
    """
    f.write(json.dumps(record, ensure_ascii=False) + "\n")
    if flush:
        # push Python buffer to OS, then try to sync to disk
        f.flush()
        try:
            os.fsync(f.fileno())
        except Exception:
            # Not critical if fsync isn't available or fails
            pass

def close_writer(f):
    """Close the file handle (JSONL doesn't need array brackets)."""
    f.close()

# ---------- Extraction helper ----------
def extract_all_quotes(page):
    """Return a list of dicts for all quotes on the current page."""
    quotes = page.locator(".quote")
    records = []
    count = quotes.count()
    for i in range(count):
        q = quotes.nth(i)
        quote_text = q.locator(".text").inner_text()
        author_text = q.locator(".author").inner_text()
        print("Extracted:", quote_text, "-", author_text)
        records.append({"Quote": quote_text, "Author": author_text})
    return records

# ---------- Orchestration ----------
def save_all_quotes_jsonl():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # set True to run headless
        page = browser.new_page(viewport={"width": 1366, "height": 768})
        page.goto("https://quotes.toscrape.com/js/", wait_until="domcontentloaded")

        # open writer
        f = start_jsonl_writer()

        try:
            # extract all quotes on the page (list of dicts)
            records = extract_all_quotes(page)

            # write each record as one JSON line
            for rec in records:
                write_jsonl_record(f, rec)

        finally:
            # ensure file is closed even if we get interrupted inside the try block
            close_writer(f)
            browser.close()
            print("✅ Done (file closed)")

if __name__ == "__main__":
    save_all_quotes_jsonl()


r''''
Nice — here’s a focused, no-fluff summary of the fundamentals and core you need to know about saving JSON from scrapers (and small code patterns you’ll actually use). Read it once, then keep it as your quick reference.

Core concepts

JSON data shapes

Objects (dicts): {"k": "v"}

Arrays (lists): [{"a":1}, {"a":2}]

Nested combinations (dicts with lists, lists of dicts).
Choose the shape that matches how you want to consume the data later.

Two main saving strategies

Batch JSON array — one big JSON array written at the end (human-friendly, pretty):
[{...}, {...}, ...]
Requires holding or carefully streaming with bracket/comma management.

JSONL / NDJSON (recommended for scrapers) — one JSON object per line:
{"..."}\n{"..."}\n
Stream-friendly, appendable, robust to interruptions.

Python json API

json.dump(obj, file, ensure_ascii=False, indent=2) → directly write JSON to file.

json.dumps(obj, ensure_ascii=False, indent=None) → produce JSON string.

ensure_ascii=False keeps Unicode readable; indent=2 pretty-prints.

File modes

"w" → overwrite / create file.

"a" → append (useful for JSONL or continuing previous runs).

Always set encoding="utf-8".

Durability

f.write() → Python buffer.

f.flush() → flush Python → OS.

os.fsync(f.fileno()) → ask OS to persist to disk (wrap in try/except).

Use these when you may interrupt the process and need less data loss.

Safety & correctness

For JSON arrays you must handle commas (no comma before first item) and write closing ]. Use a first flag or a helper class. If interrupted before ], file is invalid.

JSONL avoids comma/closing problems — each line is independent valid JSON.

Use try/finally to ensure close() runs for arrays if you require a valid final file.

Atomic writes

To avoid partial files when writing a complete file in one shot: write to a temp file then os.replace(temp, final) (atomic on most OSes).

Reading back

For arrays: data = json.load(open("file.json", "r", encoding="utf-8")).

For JSONL: iterate lines for line in f: record = json.loads(line).

When to use which

Short-run, small scrapes and need pretty output → JSON array.

Long-running scrapes, streaming, frequent interruptions, or very large data → JSONL.

Minimal code patterns
1 — Save one object (one-off)
import json
with open("quote.json", "w", encoding="utf-8") as f:
    json.dump({"Quote": "text", "Author": "name"}, f, ensure_ascii=False, indent=2)

2 — Save list-of-records at the end (batch)
records = [...]  # list of dicts collected in memory
with open("quotes.json", "w", encoding="utf-8") as f:
    json.dump(records, f, ensure_ascii=False, indent=2)

3 — Stream to JSONL (recommended)
import json, os
def start_jsonl(filename):
    return open(filename, "a", encoding="utf-8")  # use "a" to append across runs

def write_jsonl_record(f, record, flush=True):
    f.write(json.dumps(record, ensure_ascii=False) + "\n")
    if flush:
        f.flush()
        try: os.fsync(f.fileno())
        except Exception: pass

def close_writer(f):
    f.close()

# usage:
f = start_jsonl("quotes.jsonl")
write_jsonl_record(f, {"Quote":"q","Author":"a"})
close_writer(f)

4 — Stream a single JSON array incrementally (if you must)
import json
def start_array(filename):
    f = open(filename, "w", encoding="utf-8")
    f.write("[\n")
    return f, True  # True => next write is first item

def write_array_record(f, first, record):
    if not first:
        f.write(",\n")
    f.write(json.dumps(record, ensure_ascii=False, indent=2))
    return False

def close_array(f):
    f.write("\n]\n")
    f.close()

5 — Atomic write for final file
import json, tempfile, os
def atomic_write_json(filename, obj):
    dirn = os.path.dirname(filename) or "."
    with tempfile.NamedTemporaryFile("w", delete=False, dir=dirn, encoding="utf-8") as tf:
        json.dump(obj, tf, ensure_ascii=False, indent=2)
        tmpname = tf.name
    os.replace(tmpname, filename)  # atomic replace

Practical tips & best practices

Prefer JSONL for scrapers: easy to append, robust to crashes, fast to stream.

Use "a" mode for JSONL if you want to resume and append across runs. If you want fresh file each run, use "w".

If you need pretty/human-readable output, create a separate conversion step from JSONL → pretty JSON array after scraping (small script).

Avoid storing extremely large lists in memory. Stream to disk (JSONL) instead.

Test your selectors and extraction in a quick script that prints results before writing files.

When debugging file writes, open the file in a text editor to ensure lines are complete JSON objects.

Short decision flow (one-sentence cheat)

Want streaming, resume/append, or robust to interruption? → JSONL.

Want pretty, single JSON file and dataset small enough to hold in memory? → JSON array.

Need atomic overwrite? → write to temp + replace.

If you want, I can now:

Convert your current scraper to JSONL with append mode and pagination; or

Give you a tiny JsonlWriter class that wraps start/write/close and handles flush/fsync for you.
'''