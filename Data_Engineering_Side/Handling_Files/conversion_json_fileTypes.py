#!/usr/bin/env python3
"""
json_to_many.py

Usage:
    python json_to_many.py input.json
    python json_to_many.py input.json --out-dir exports --no-parquet

This reads a JSON (array of objects) or JSONL file and exports to:
 - CSV
 - Excel (.xlsx)
 - newline-delimited JSON (.jsonl)
 - pretty JSON (.json)
 - compact JSON (.json compact)
 - Parquet (.parquet) [optional]
 - HTML table (.html)
 - SQLite database (table named 'data') (.sqlite)
"""

# import argparse
# import os
# import sys
# import json
# import pandas as pd

# try:
#     from pandas import json_normalize
# except Exception:
#     # fallback
#     from pandas import json_normalize  # will raise ImportError if pandas not installed

# def read_json_file(path):
#     """
#     Detects if file is JSONL (one JSON object per line) or a normal JSON array/object.
#     Returns a list of dicts (records).
#     """
#     with open(path, "r", encoding="utf-8") as f:
#         first = f.read(1024).lstrip()
#         f.seek(0)
#         # Heuristic: if file starts with '[' or '{' => standard JSON
#         if first.startswith("[") or first.startswith("{"):
#             data = json.load(f)
#             # if it's a single object (dict), convert to list
#             if isinstance(data, dict):
#                 # If dict maps top-level keys to objects, we can't reliably tabularize them;
#                 # assume user meant a list wrapped in a dict under a key 'data' if present.
#                 # But here we convert single dict to a one-row record.
#                 return [data]
#             elif isinstance(data, list):
#                 return data
#             else:
#                 raise ValueError("Unsupported JSON root type: " + str(type(data)))
#         else:
#             # JSONL: parse line by line
#             records = []
#             for i, line in enumerate(f, start=1):
#                 line = line.strip()
#                 if not line:
#                     continue
#                 try:
#                     obj = json.loads(line)
#                 except json.JSONDecodeError as e:
#                     raise ValueError(f"Invalid JSON at line {i}: {e}")
#                 records.append(obj)
#             return records

# def normalize_records(records):
#     """Flatten nested JSON (dicts/arrays) into columns using pandas.json_normalize"""
#     # If empty, return empty DataFrame
#     if not records:
#         return pd.DataFrame()
#     try:
#         df = json_normalize(records, sep=".")
#     except Exception:
#         # fallback to DataFrame constructor
#         df = pd.DataFrame(records)
#     return df

# def write_outputs(df, basepath, out_dir, write_parquet=True, sqlite_table="data"):
#     os.makedirs(out_dir, exist_ok=True)

#     # CSV
#     csv_path = os.path.join(out_dir, basepath + ".csv")
#     df.to_csv(csv_path, index=False)
#     print("Wrote:", csv_path)

#     # Excel
#     xlsx_path = os.path.join(out_dir, basepath + ".xlsx")
#     # use openpyxl as engine (ensure it's installed)
#     df.to_excel(xlsx_path, index=False, engine="openpyxl")
#     print("Wrote:", xlsx_path)

#     # Pretty JSON (records)
#     pretty_json_path = os.path.join(out_dir, basepath + "_pretty.json")
#     df.to_json(pretty_json_path, orient="records", indent=4)
#     print("Wrote:", pretty_json_path)

#     # Compact JSON
#     compact_json_path = os.path.join(out_dir, basepath + "_compact.json")
#     df.to_json(compact_json_path, orient="records")
#     print("Wrote:", compact_json_path)

#     # JSONL (newline-delimited)
#     jsonl_path = os.path.join(out_dir, basepath + ".jsonl")
#     # Using orient="records" and lines=True
#     df.to_json(jsonl_path, orient="records", lines=True)
#     print("Wrote:", jsonl_path)

#     # Parquet (optional)
#     if write_parquet:
#         parquet_path = os.path.join(out_dir, basepath + ".parquet")
#         # pandas will use pyarrow or fastparquet if available
#         df.to_parquet(parquet_path, index=False)
#         print("Wrote:", parquet_path)

#     # HTML table
#     html_path = os.path.join(out_dir, basepath + ".html")
#     df.to_html(html_path, index=False, justify="left")
#     print("Wrote:", html_path)

#     # SQLite - save into a single-table DB
#     try:
#         import sqlite3
#         sqlite_path = os.path.join(out_dir, basepath + ".sqlite")
#         conn = sqlite3.connect(sqlite_path)
#         df.to_sql(sqlite_table, conn, if_exists="replace", index=False)
#         conn.close()
#         print("Wrote:", sqlite_path, "(table name:", sqlite_table + ")")
#     except Exception as e:
#         print("Skipping SQLite export (sqlite3 not available or error):", e, file=sys.stderr)

# def main():
#     p = argparse.ArgumentParser(description="Convert one JSON file into multiple formats.")
#     p.add_argument("input", help="Input JSON or JSONL file")
#     p.add_argument("--out-dir", "-o", default="exports", help="Output directory")
#     p.add_argument("--base-name", "-b", default=None, help="Base filename for outputs (without ext). If omitted uses input file stem.")
#     p.add_argument("--no-parquet", action="store_true", help="Do not write Parquet file")
#     p.add_argument("--sqlite-table", default="data", help="Table name to use when writing to SQLite")
#     args = p.parse_args()

#     inpath = args.input
#     if not os.path.isfile(inpath):
#         print("Input file not found:", inpath, file=sys.stderr)
#         sys.exit(2)

#     # Read
#     try:
#         records = read_json_file(inpath)
#     except Exception as e:
#         print("Failed reading JSON:", e, file=sys.stderr)
#         sys.exit(3)

#     # Normalize -> DataFrame
#     df = normalize_records(records)

#     # If columns contain lists or nested dicts still, convert them to JSON strings so CSV/SQLite don't break
#     def safe_serialize(val):
#         if isinstance(val, (dict, list)):
#             return json.dumps(val, ensure_ascii=False)
#         return val

#     # Apply safe_serialize to problematic columns
#     for col in df.columns:
#         if df[col].apply(lambda x: isinstance(x, (dict, list))).any():
#             df[col] = df[col].apply(safe_serialize)

#     # Output basename
#     base = args.base_name or os.path.splitext(os.path.basename(inpath))[0]

#     write_outputs(df, base, args.out_dir, write_parquet=not args.no_parquet, sqlite_table=args.sqlite_table)
#     print("Done. Exported files are in:", os.path.abspath(args.out_dir))

# if __name__ == "__main__":
#     main()


#!/usr/bin/env python3
"""
json_to_csv_xlsx.py
Simple: read a JSON or JSONL file and write CSV and Excel (.xlsx).

Usage:
    python json_to_csv_xlsx.py input.json
    python json_to_csv_xlsx.py input.json -o exports -b basename
"""

# import argparse
# import json
# import os
# import pandas as pd
# from pandas import json_normalize

# def read_json_or_jsonl(path):
#     """Return a list of records parsed from JSON array/object or JSONL."""
#     with open(path, "r", encoding="utf-8") as f:
#         sample = f.read(2048).lstrip()
#         f.seek(0)
#         # Standard JSON (array or object)
#         if sample.startswith("[") or sample.startswith("{"):
#             data = json.load(f)
#             if isinstance(data, dict):
#                 # single object -> one-row record
#                 return [data]
#             elif isinstance(data, list):
#                 return data
#             else:
#                 raise ValueError("Unsupported JSON root type: " + str(type(data)))
#         else:
#             # JSONL: parse line-by-line
#             records = []
#             for i, line in enumerate(f, start=1):
#                 line = line.strip()
#                 if not line:
#                     continue
#                 try:
#                     obj = json.loads(line)
#                 except json.JSONDecodeError as e:
#                     raise ValueError(f"Invalid JSON on line {i}: {e}")
#                 records.append(obj)
#             return records

# def records_to_dataframe(records):
#     """Flatten nested objects and return a pandas DataFrame."""
#     if not records:
#         return pd.DataFrame()
#     try:
#         df = json_normalize(records, sep=".")
#     except Exception:
#         df = pd.DataFrame(records)
#     # Convert any remaining list/dict cells into JSON strings to keep CSV/Excel clean
#     def safe_serialize(v):
#         if isinstance(v, (list, dict)):
#             return json.dumps(v, ensure_ascii=False)
#         return v
#     for col in df.columns:
#         if df[col].apply(lambda x: isinstance(x, (list, dict))).any():
#             df[col] = df[col].apply(safe_serialize)
#     return df

# def write_csv_and_excel(df, out_dir, base_name):
#     os.makedirs(out_dir, exist_ok=True)
#     csv_path = os.path.join(out_dir, base_name + ".csv")
#     xlsx_path = os.path.join(out_dir, base_name + ".xlsx")
#     df.to_csv(csv_path, index=False)
#     # Requires openpyxl (pip install openpyxl)
#     df.to_excel(xlsx_path, index=False, engine="openpyxl")
#     return csv_path, xlsx_path

# def main():
#     p = argparse.ArgumentParser(description="Convert JSON/JSONL -> CSV & Excel")
#     p.add_argument("input", help="Input JSON or JSONL file")
#     p.add_argument("-o", "--out-dir", default="exports", help="Output directory")
#     p.add_argument("-b", "--base-name", default=None, help="Base filename (without extension)")
#     args = p.parse_args()

#     if not os.path.isfile(args.input):
#         raise SystemExit(f"Input file not found: {args.input}")

#     records = read_json_or_jsonl(args.input)
#     df = records_to_dataframe(records)

#     base = args.base_name or os.path.splitext(os.path.basename(args.input))[0]
#     csv_path, xlsx_path = write_csv_and_excel(df, args.out_dir, base)

#     print("Wrote CSV:", csv_path)
#     print("Wrote Excel:", xlsx_path)
#     print("Rows:", len(df), "Columns:", len(df.columns))

# if __name__ == "__main__":
#     main()
