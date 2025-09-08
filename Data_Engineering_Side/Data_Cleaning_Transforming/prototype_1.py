# Goal Create a script where i can generally clean the data in the JSON, JSONL files:
r'''
Realization: 
Where to Clean the Data in terms of that what type of files?
    - The Top Choice for Cleaning and Post Processing is
    1. CSV (Comma Seperated Values) 
        - Most Common and Universal Choice for Tabular data.
        - Human Readaable
        - Wide Software Support 
        - Simple Structure that it force your JSON data into a flat tabular strucutre.
        which is often necessary for analysis and machine learning.
'''

r'''
To STORE RAW DATA for cleaning: JSONL is best. It's your immutable source.
To DO THE CLEANING: It happens in memory using a programming language (Python/Pandas). The file format is irrelevant at this stage; it's all about data structures.
To SAVE THE CLEANED RESULT: CSV (for most cases) or Parquet (for large, efficient datasets) is best.
'''

# Importing the Necessary Tools
import pandas as pd
import json


df = pd.read_json('Mechatronics_2025-08-30.jsonl', lines=True)
# df = pd.read_json('Mechatronics_2025-08-30.jsonl', lines=False) i got error if i did this
# df = pd.read_json('Mechatronics_2025-08-30.jsonl')+

# Display the first few rows to check the data
print(df.head())

r'''
My Question is what if the file are in different folders? 

* df = pd.read_json("data/2025/Mechatronics_2025-08-30.jsonl", lines=True)
C:/Users/Name/Documents/Mechatronics_2025-08-30.jsonl).

* lines=True: This is the crucial parameter that tells pandas the file is in JSON Lines format, 
where each line is a separate JSON object

* pd.read_json(): This is the pandas function for reading JSON files.
'''

# I Hear the Traceback in one of the Video and Figuring out What does it mean:
r'''
Traceback:
    1. Is one of the Asernal Tools of Debugging Skills that you have, it can let you know 
    where your program(which line broke) didn't work and why
    2. Root Cause Analysis, sometimes the bug isn't in the line itself but it is something 
    Traceback help you show the whole picture of things 
    3. Learning that over time , you can start recognizing the common errors and fix them faste

'''

r'''
1. Clean text by removing HTML, normalizing whitespace, and fixing encoding
'''

from bs4 import BeautifulSoup # For Removing the HTML in the Text
r'''
Currently Using the Playwright but let's say i use the HTML i can definitely do it
'''
def html_remover():
    r'''
    Remove the HTML
    '''
    # Remove HTML tags using BeautifulSoup
    text = BeautifulSoup(text, "html.parser").get_text()
    r'''
    Breaking line of the code:
        BeautifulSoup is to parse the HTML
        Text is something to get it into
        .get_text() is used to remove the html 
            html = "<p>Hello <b>World</b>!</p>"
            Turn it into: Hellow World
    
    Summary Extracting the  HTML Tag turning it into a Normal Text
    '''

# import re # A Regex Module or Regular Expression thing 
import re

def text_to_single_space_remover():
    text = re.sub(r'\s+', ' ', text)
    # Notice the inside of parenthesis there are "," to seperate things
    r'''
    re.sub(pattern, replacement, string)
        * re.sub() is a function from the re module (regular expressions).
            * It searches for all matches of pattern in string and replaces them with replacement.

        * The pattern: r'\s+'
            * \s means any whitespace character (space, tab, newline, etc.).
            * + means one or more occurrences.
            * So \s+ matches any sequence of whitespace (like " ", "\n\t", etc.).
            * Basically the \s is for white space, tab and newline
            * + for more occurence in a single text 
            * and all replace ment will be replace with a single space " "
        
        Example: text = "This   is \n   a   test."
        cleaned = re.sub(r'\s+', ' ', text)
        output : This is a test.
    '''

# In Terms of Playwright Libraries there are 2 things: Playwright’s .inner_text() / .text_content()
r'''
Quite Automatic at Things
'''

# .strip()
r'''
It’s a built-in Python string method
Removes leading and trailing whitespace (spaces, tabs, newlines) from a string.
    * Only at the End and Beginning 
    Examples: text = "   Hello world!   \n"
    Output: Hello world!

It's Differ from the re.sub because strip() clean the beginning and end (edges)
While the re.sub clean the middle one

text = "   Hello    world   \n  "

print("strip:", text.strip())  
# 'Hello    world'

print("re.sub:", re.sub(r'\s+', ' ', text))  
# ' Hello world '

'''


# Combining the 2 html remover and white space remover: 
def basic_clean_text(text,html):
    text = BeautifulSoup(html, "html.parser").get_text()
    text = re.sub(r'\s+', ' ', text).strip()


# 2. Type Conversion (parsers.py)
# Goal: Convert types to usable formats (float, date, bool).

def price_conversion(price_str):
    numbers = re.findall(r'[\d,]+', price_str)
    r'''
    re.findall(pattern, string) 
        * Scan the Wole String which is price_str
        * Returns a list of all matches for the regex pattern.
    The Pattern: r'[\d,]+'
        * + is if there are more pattern that are similar or occured in a string 
        * [] a Class as you can see putting it into the list of string
        * \d any digit (0–9).
        * , → a literal comma. for 12,000 Getting the Comma there 
        # 👉 So the pattern matches sequences of digits and commas.
    '''
    # if numbers: # if numbers there are no condition just if numbers exist

    #     Convert first number to float (e.g., "25,000" -> 25000.0)
    #     min_price = float(numbers[0].replace(',', ''))
    r'''
    numbers[0] get the first number in the regex 
    replace(',', '') # Replace the commas into no space sticking it into 25,000 to 25000
    float() Converting the Numbers into a float data type 1500 to 1500.0
    '''
    #     # If there's a second number, it's the max
    #     max_price = float(numbers[1].replace(',', '')) if len(numbers) > 1 else None
    #     return min_price, max_price
    r'''
    Same at the Top but the thing is if there are a second number exist 
    '''
    

price_str = "Kristian is a Programmer who owns 15,00 of debt in the bank" \
"12,00 debt in gcash account" \
"emergency fund is only at 5,000"

numbers = re.findall(r'[\d,]+', price_str)
print(numbers) # Output: ['15,00', '12,00', '5,000']

# Overall Summary:
r'''
Parsing the Price turning it into a float number or integer number it really depends
because in terms of like a job description like my thing i can get the numbers in there 
for the salary of things 

Getting a Numbers in a Sentence (String Format Data Type)
'''

# Assuming you get the date 
# date_str = "Sep 07, 2025" # There are many Different kind of dates but converting it into the iso format
# '2025-09-07'
from datetime import datetime # Importing the mOdule of Datetime working with dates 

def parse_date(date_str):
    try:
        # Parse a common date format
        return datetime.strptime(date_str, '%b %d, %Y').date().isoformat()
        r'''
        * datetime.strptime() = “string parse time”
        * It takes a text string (date_str) and a format pattern ('%b %d, %Y') and turns it into a Python datetime object.

        * The format here:
            * %b = abbreviated month name (Jan, Feb, … Dec)
            * %d = day of the month (01–31)
            * %Y = 4-digit year
        "Sep 07, 2025" → becomes a datetime.datetime(2025, 9, 7, 0, 0)

        * .date()
            * This takes the datetime object and extracts just the date portion (no time).
            * Example:
                * datetime(2025, 9, 7, 0, 0).date() → date(2025, 9, 7)
        '''
        # Why do this?
        # But for analysis, sorting, or storing in a database, you want a consistent, machine-friendly format (YYYY-MM-DD).
        
    except ValueError:
        return None  # Or log the error

# Summary Date and Time for  Conversion in a Machine readable way
# Converting the Price into a proper data format thing


# Standardization (normalizer.py) 
r'''
The idea of normalization is not limited to job titles at all. 
It’s a general data cleaning step where you take messy, inconsistent raw text and map it into a consistent, 
standardized label that your system can work with.
'''
# https://chatgpt.com/share/68bc9f28-83dc-8013-b903-6853574185f4
# Continue on this part 

r'''
Standardization is something putting it in a category for example i have an infinix phone and oppo Phone instead of putting the data 
Inifinix Phone and Oppo Phone we replace it with --> Phone to categorize the items or standardization the items 
'''

category_mapping = {
    "cell phone": "Smartphone",
    "mobile phone": "Smartphone",
    "iphone": "Smartphone",
    "laptop pc": "Laptop",
    "notebook": "Laptop",
    "fridge": "Refrigerator",
    "refrigerator": "Refrigerator",
}

# Why Use Dictionary in Standardization: 
r'''
category mapping is just a name or i should just name it standardization of things 
The Whole thing is a Dictionary 
    * Keys ("cell phone", "iphone", etc.) → possible raw values you might scrape from websites.
    * Values ("Smartphone", "Laptop", "Refrigerator") → the standardized labels you want in your dataset.
    * When you normalize, you take any messy variant and map it to one consistent category.
'''

# This is Replacing the Thing to put it into the category parts of the things
def normalize_category(category): # Defines a function named normalize_category that accepts one argument category (expected to be a string)  
    category_lower = category.lower()   # Lowering the letters if there are the case of Upper cases 
    for key, standard in category_mapping.items():
        r'''
        Iterates over each (key → standard) pair in category_mapping.
        Example key: "cell phone", standard: "Smartphone".
        In Dictionary we Use Keys and the standard is the value of the key something like Key Value Pairs 
        '''
        if key in category_lower:
            '''
            Checks whether the key (like "cell phone") appears anywhere inside the category_lower string.
            This is a substring check. If the key is present, the condition is True.
            This make Sense because we are lowering the files in there 
            '''
            return standard # If the if is True, the function immediately returns the standardized label (e.g., "Smartphone"). The loop stops.
    return category # If none of the keys were found, return the original category string unchanged.

r'''
Important caveats / edge-cases

category may be None or non-string → .lower() will raise AttributeError.
F   ix: check if not category: return category or if not isinstance(category, str): ....
Substring false positives
    Example: if key = "phone", then "microphone" contains "phone" and would match incorrectly.
Order matters:
    If you have both "phone" and "iphone" as keys, whichever key appears first in the dict iteration will match first. For correctness prefer matching longer keys first.
Punctuation & typos: 
    "Cell-Phone" or "cell phone!!!" may work, but "cellphone" (no space) won’t match "cell phone". You may want to normalize punctuation/whitespace first.
Scalability:
    For a small mapping, this is fine. For hundreds/thousands of keys you should precompile patterns (or build trie/regex) for speed.

Components (what a robust normalize_category needs)

1. Input validation
Reject or handle None, non-strings, empty strings to avoid crashes.

2. Unicode normalization
Normalize accents and composed characters so “café” and “café” match the same way.

3. Case normalization
Lowercasing so matching is case-insensitive.

4. Noise removal / token cleaning
Remove/replace punctuation, collapse multiple spaces, handle hyphens, parentheses, trailing punctuation.

5. Key-preparation / ordering
Prefer longer keys first (so "iphone" matches before "phone"). This avoids short-key preemption.

6. Match strategy
* Exact substring? word boundaries (\b)? regex patterns? fuzzy matching for typos?
* For most cases, word-boundary regex is safer than raw substring (avoids matching "microphone" if key is "phone").

7. Precompilation
* Compile regexes once (not every call) for speed.

8. Fallback behavior
* If no mapping found, return a cleaned version, or None, or the original — choose what fits your downstream code.

9. Logging / metrics (optional)
* Count unmapped categories for later mapping expansion.

10. Caching (optional)
If you see the same strings a lot, cache results for speed.

11. Optional fuzzy layer
Use a fuzzy library (e.g., rapidfuzz) only when exact/regex fails. Slower but catches misspellings
'''

normalize_category("Latest Apple iPhone 14 Pro Max")
# → "Smartphone"
normalize_category("Brand New Laptop PC, i7")
# → "Laptop"
normalize_category("Big Capacity Fridge 300L")
# → "Refrigerator"


# More Complicated Code:
import re
import unicodedata

# Example mapping
category_mapping = {
    "cell phone": "Smartphone",
    "mobile phone": "Smartphone",
    "iphone": "Smartphone",
    "laptop pc": "Laptop",
    "notebook": "Laptop",
    "fridge": "Refrigerator",
    "refrigerator": "Refrigerator",
}

# Precompile patterns: sort keys by length to prefer longer matches (avoids 'phone' capturing before 'iphone')
compiled = []
# for key in sorted(category_mapping.keys(), key=len, reverse=True):
#     pattern = re.compile(r'\b' + re.escape(key.lower()) + r'\b')
#     compiled.append((pattern, category_mapping[key]))

# def normalize_category_safe(category):
#     if not category or not isinstance(category, str):
#         return category

#     # Unicode normalize, lowercase, strip
#     cat = unicodedata.normalize('NFKD', category).lower().strip()
#     # Replace punctuation with spaces, collapse whitespace
#     cat = re.sub(r'[^\w\s-]', ' ', cat)
#     cat = re.sub(r'\s+', ' ', cat).strip()

#     for pat, standard in compiled:
#         if pat.search(cat):
#             return standard

#     return category  # fallback
######################################################################################################
######################################################################################################


# 4. Deduplication (deduplicate())
# Goal: Use a unique key to identify duplicates. Often, a combination of title, client, and date is a good key. For this example, let's create a hash of the title and date.
r'''
Basically the  Goal of this is to avoid duplicates and mostly do in post proccessing thing

Duplicates affect 
    * inflates counts (wrong statistics, wrong analysis),
    * pollutes training data (if you’re using it for ML/AI),
    * and wastes storage.
'''

raw_records = [
    {"title": "Software Engineer", "posted_date": "2025-09-09"},
    {"title": "Software Engineer", "posted_date": "2025-09-09"},  # duplicate
    {"title": "Web Developer", "posted_date": "2025-09-09"},
]

import hashlib
r'''
* Imports Python’s hashlib module, which provides hash functions (MD5, SHA-1, SHA-256, etc.).

* Why: we use a hash to produce a short, fixed-length identifier from a (possibly long) string.
'''

def generate_id(record): # Defines a function named generate_id that expects a record (a dict in this context).

    # Create a unique string based on title and date
    unique_string = f"{record['title']}_{record['posted_date']}"
    r'''
    * Builds a single string from the title and posted_date fields of the record.

    * Why: we need a deterministic string that (ideally) uniquely represents that record. The underscore _ is a simple separator.
    '''


    return hashlib.md5(unique_string.encode()).hexdigest()
    r'''
    * unique_string.encode() turns the Python string into bytes (UTF-8 by default).

    * hashlib.md5(...).hexdigest() computes the MD5 hash of those bytes and returns a 32-character hex string (e.g. "a1b2c3...").

    * Why: the hex hash is compact, fixed-size, and reproducible — convenient as an ID.
    '''

# Add a unique ID to the record
raw_records['id'] = generate_id(raw_records)
r'''
* Calls generate_id and stores the resulting hash in the record under key 'id'.

* Note/caution: generate_id expects the record to have title and posted_date; 
if missing this will raise a KeyError. Also variable name mismatch: earlier you used raw_record singular; here you used raw_records — be consistent.
'''
# Later, you have a list of records `all_records`
def deduplicate(records, key="id"):
    r'''
    Defines a function deduplicate which takes a list records and an optional key name (default "id"). It will remove duplicates based on the value at record[key].
    '''
    seen = set()
    unique_records = []
    r'''
    seen is a set() of keys we’ve observed.

unique_records is the list we’ll return containing only the first occurrence of each unique key.
    '''


    for record in records:
        
        if record[key] not in seen:
            seen.add(record[key])
            unique_records.append(record)
    return unique_records

r'''
For each record: check its record[key].

If not seen before → add the key to seen and append the record to unique_records.

If already seen → skip it (this removes duplicates).

Returns the filtered list preserving first-occurrence order.
'''


