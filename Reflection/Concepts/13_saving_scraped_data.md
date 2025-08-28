# 📄 Q&A: Saving Scraped Data

------------------------------------------------------------------------

## ❓ Q1. What's the easiest file format to save while scraping?

✅ **Answer: JSONL (newline-delimited JSON).**

-   Each line is a full JSON object.\
-   You can write one record at a time while scraping.\
-   It's safe if your program crashes --- previous lines remain valid.\
-   Very easy to convert later into CSV, Excel, or Parquet.

------------------------------------------------------------------------

## ❓ Q2. Why not just use CSV?

✅ **Answer:** Use CSV if your data is flat (no nested structures) and
you need maximum compatibility with tools like Excel, Google Sheets,
etc.

But:\
- CSV can't store nested lists/objects.\
- Bad at preserving data types (everything becomes text).\
- Errors if commas/line breaks appear in fields (though quoting helps).

------------------------------------------------------------------------

## ❓ Q3. Is Excel good for saving scraped data directly?

✅ **Answer: No, not for streaming.**

-   Excel (`.xlsx`) must be written via a library (`openpyxl`,
    `xlsxwriter`).\
-   Entire workbook stays in memory until saved → risky for large
    scrapes.\
-   Great for stakeholders who want a spreadsheet, but inefficient for
    raw scraping.

👉 Use JSONL or CSV for scraping, then convert to Excel at the end.

------------------------------------------------------------------------

## ❓ Q4. What's the difference between JSON and JSONL?

✅ **Answer:**

**JSON (array style):**

``` json
[
  {"name": "Alice"},
  {"name": "Bob"}
]
```

-   Needs the full list in memory before closing → not
    streaming-friendly.

**JSONL:**

``` json
{"name": "Alice"}
{"name": "Bob"}
```

-   Each line is a record → streaming-friendly (append as you scrape).

------------------------------------------------------------------------

## ❓ Q5. What if I need efficiency for big data analysis?

✅ **Answer: Parquet is best for huge datasets.**

-   Columnar storage: compressed & fast to query.\
-   Perfect for analytics (Pandas, Spark, Athena).\
-   But: not human-readable, not streaming-friendly → you usually
    batch-save.

------------------------------------------------------------------------

## ❓ Q6. Which format is "safest" for scraping?

✅ **Answer: JSONL.**

-   Write one record at a time.\
-   If your scraper crashes, you lose at most one row.\
-   Works well with incremental appends.

------------------------------------------------------------------------

## ❓ Q7. How do I convert JSONL into other formats later?

✅ **Answer: With pandas:**

``` python
import pandas as pd

df = pd.read_json("data.jsonl", lines=True)
df.to_csv("data.csv", index=False)         # CSV
df.to_excel("data.xlsx", index=False)      # Excel
df.to_parquet("data.parquet", index=False) # Parquet
```

------------------------------------------------------------------------

## ❓ Q8. If I want one file format only, which should I pick?

✅ **Answer:**

-   For scraping + flexibility → **JSONL**\
-   For quick use in Excel/Sheets → **CSV**\
-   For large-scale analytics → **Parquet**

👉 If you don't know yet: always pick **JSONL**.\
It's safest, simplest, and you can transform it later.

------------------------------------------------------------------------

## ❓ Q9. Can I save simultaneously to multiple formats?

✅ **Answer: Yes.**\
You can open CSV, Excel, and JSONL writers at the same time and write
each record to all three.

But:\
- It's slower, more code, and usually unnecessary.\
- Better: scrape once to JSONL, then convert.

------------------------------------------------------------------------

## ❓ Q10. What's the fastest workflow in practice?

✅ **Answer:**

1.  **Scrape → write to JSONL (streaming).**\
2.  **Convert JSONL → CSV/Excel/Parquet** depending on your need.

👉 So the *"one format to rule them all"* is **JSONL**.\
It's streamable, safe, flexible, and easy to convert.

------------------------------------------------------------------------
