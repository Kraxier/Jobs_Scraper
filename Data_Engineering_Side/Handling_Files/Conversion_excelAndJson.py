import pandas as pd
# or, if you prefer xlsxwriter:
# pip install pandas xlsxwriter

# 1) Read existing CSV (or create DataFrame however you like)
df = pd.read_csv("data.csv")

# 2) Save to Excel (.xlsx)
# - engine "openpyxl" or "xlsxwriter" works
df.to_excel("data.xlsx", index=False, engine="openpyxl")   # index=False avoids writing the row index

# 3) Save to JSON (pretty)
df.to_json("data_pretty.json", orient="records", indent=4)  # orient="records" produces a list of objects

# 4) Save to newline-delimited JSON (good for large streaming/line-by-line ingestion)
df.to_json("data_lines.jsonl", orient="records", lines=True)  # .jsonl file (one JSON obj per line)

# 5) If you want compact (no whitespace) JSON:
df.to_json("data_compact.json", orient="records")

print("Saved: data.xlsx, data_pretty.json, data_lines.jsonl, data_compact.json")


