# Implementing the Prototype_1.py


# Goal: 
r'''
🎯 Project Goal

Build a full cleaning pipeline that takes your raw JSONL (Mechatronics_2025-08-30.jsonl) and produces a cleaned CSV file ready for analysis or ML.

✅ Step-by-Step Goals to Reinforce Learning
1. Load & Inspect
Load your raw JSONL into a DataFrame (pd.read_json(..., lines=True)).
Print df.info() and df.head() to understand the raw structure.

2. Text Cleaning (what you practiced)
Apply basic_clean_text() on:
Job titles
Descriptions
Company names (if they contain HTML/extra spaces)

3. Type Conversion
Parse salary fields (extract min/max salary as floats).
Parse dates (convert posted_date → ISO format).
Convert boolean-like fields (e.g., "remote"/"yes"/"no") into True/False.

4. Standardization
Normalize job titles into categories:
"Mechatronics Engineer", "Robotics Engineer" → "Engineer"
"Technician", "Maintenance Technician" → "Technician"
Normalize company industries (if available).

5. Deduplication
Generate unique IDs (hash(title + company + date)).
Remove duplicate job postings.

6. Output
Save cleaned dataset as:
Mechatronics_cleaned.csv (for easy viewing in Excel).
Optionally Mechatronics_cleaned.parquet (efficient for big data).

7. Stretch Goal (Reinforce Deeper)
Add logging (track how many duplicates removed, how many missing salaries, etc.).
Build a small modular pipeline (functions: clean_text(), convert_salary(), normalize_titles(), etc.).
Write a main() that runs everything step by step.

📌 1. JSONL is your raw storage
JSONL is best as your immutable source of truth.
You scrape → save raw JSONL → never overwrite it.
(In case your cleaning introduces errors, you can always go back to raw.)

📌 2. Cleaning happens in memory
You load JSONL into Pandas DataFrame (like you’re already doing).
Apply all your cleaning functions (basic_clean_text, price_conversion, parse_date, etc.).
The transformations live in Python, not in the raw JSONL file.

📌 3. Save cleaned version to a new file
After cleaning, save into another format:
cleaned.jsonl (if you want to keep JSONL structure).
cleaned.csv (good for Excel/analysis).
cleaned.parquet (efficient for big datasets).
'''

import pandas as pd
import json


df = pd.read_json('Mechatronics_2025-08-30.jsonl', lines=True)
# print(df.head()) # Load to Data Frame, I think all Pandas Core Parts i can do all of it here 
# print(df.info()) # Data Type are all object # What ever that means, Shoud i care ? 

# Data Exploration Part, before Post Proccessing Thing i Should Data Explore it First
column_1_role = df["Role"]
print(column_1_role)

# Basically go for Data Exploration First before Diving into the Data Cleaning, Maybe Try to Automate or Find a way to Find the Dirty Stuff like what is common instead of 
# manually Checking things out 