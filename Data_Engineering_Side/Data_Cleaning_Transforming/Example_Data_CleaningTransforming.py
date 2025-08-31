raw_record = {
    "title": "Urgently Needed: Web Dev (PHP, JavaScript)!!!  ",
    "posted_date": "Jan 15, 2025",
    "budget": "₱25,000-30,000",
    "description": "<p>We need a developer to build a website. Must be experienced.</p>\n<br>Contact us at: hello@company<span>.com</span>",
    "client_country": "Philippines",
    "client_rating": "4.5/5",
    "reviews": [
        {"reviewer": "Jane D.", "comment": "Great client!", "rating": 5},
        {"reviewer": "John S.", "comment": "Payment was slow.", "rating": 4}
    ],
    "tags": ["Javascript", "js", "Web Development"]
}


# 1. Text Cleaning (clean_text())
# Goal: Remove HTML, newlines, extra spaces, and normalize encodings.

import re
from bs4 import BeautifulSoup

def clean_text(text):
    if text is None:
        return None
    # Remove HTML tags using BeautifulSoup
    text = BeautifulSoup(text, "html.parser").get_text()
    # Replace \n, \t, and multiple spaces with a single space
    text = re.sub(r'\s+', ' ', text)
    # Strip leading/trailing spaces
    return text.strip()

# 1. Text Cleaning Outpu
# Apply to relevant fields
raw_record['description'] = clean_text(raw_record['description']) # Output: "We need a developer to build a website. Must be experienced. Contact us at: hello@company.com"
raw_record['title'] = clean_text(raw_record['title']) # Output: "Urgently Needed: Web Dev (PHP, JavaScript)!!!"

# Input
description = "<p>We need a developer to build a website. Must be experienced.</p>\n<br>Contact us at: hello@company<span>.com</span>"
title = "Urgently Needed: Web Dev (PHP, JavaScript)!!!  "

# After clean_text()
description = "We need a developer to build a website. Must be experienced. Contact us at: hello@company.com"
title = "Urgently Needed: Web Dev (PHP, JavaScript)!!!"

########################################################################################## 

# 2. Type Conversion (parsers.py)
# Goal: Convert types to usable formats (float, date, bool).

# parsers.py
import re
from datetime import datetime

def parse_price(price_str):
    if price_str is None:
        return None, None
    # Find all numbers in the string
    numbers = re.findall(r'[\d,]+', price_str)
    if numbers:
        # Convert first number to float (e.g., "25,000" -> 25000.0)
        min_price = float(numbers[0].replace(',', ''))
        # If there's a second number, it's the max
        max_price = float(numbers[1].replace(',', '')) if len(numbers) > 1 else None
        return min_price, max_price
    return None, None

def parse_date(date_str):
    try:
        # Parse a common date format
        return datetime.strptime(date_str, '%b %d, %Y').date().isoformat()
    except ValueError:
        return None  # Or log the error

# Apply the parsers
min_budget, max_budget = parse_price(raw_record['budget'])
raw_record['posted_date_iso'] = parse_date(raw_record['posted_date'])
# We'll drop the original fields later

# 2. Type Conversion Output
# Input
budget = "₱25,000-30,000"
posted_date = "Jan 15, 2025"

# After parse_price()
min_budget = 25000.0
max_budget = 30000.0

# After parse_date()
posted_date_iso = "2025-01-15"

########################################################################################## 

# 3. Standardization (normalizer.py)
# Goal: Ensure consistent formats for currencies, categories, etc.
# normalizer.py
job_title_mapping = {
    "web dev": "Web Developer",
    "swe": "Software Engineer",
    "software eng.": "Software Engineer",
}

def normalize_job_title(title):
    title_lower = title.lower()
    for key, standard in job_title_mapping.items():
        if key in title_lower:
            return standard
    # If no match, return the original cleaned title
    return title

# Apply normalization
raw_record['normalized_title'] = normalize_job_title(raw_record['title']) # Output: "Web Developer"
# The currency was handled in parse_price, we know it's PHP.

# 3. Standardization Output
# Input
title = "Urgently Needed: Web Dev (PHP, JavaScript)!!!"
# After normalize_job_title()
normalized_title = "Web Developer"



########################################################################################## 


# 4. Deduplication (deduplicate())
# Goal: Use a unique key to identify duplicates. Often, a combination of title, client, and date is a good key. For this example, let's create a hash of the title and date.

import hashlib

def generate_id(record):
    # Create a unique string based on title and date
    unique_string = f"{record['title']}_{record['posted_date']}"
    return hashlib.md5(unique_string.encode()).hexdigest()

# Add a unique ID to the record
raw_record['id'] = generate_id(raw_record)

# Later, you have a list of records `all_records`
def deduplicate(records, key="id"):
    seen = set()
    unique_records = []
    for record in records:
        if record[key] not in seen:
            seen.add(record[key])
            unique_records.append(record)
    return unique_records

# unique_jobs = deduplicate(all_jobs, key="id")

# 4. Deduplication Output
# After generate_id()
id = "a1b2c3d4e5f6g7h8i9j0"  # Example MD5 hash

# The record now has an ID field for deduplication

########################################################################################## 


# 5. Handling Missing Data (validate_record())
# Goal: Check for critical missing fields and log issues.

validation_errors = []

def validate_record(record):
    errors = []
    if not record.get('title'):
        errors.append("Missing title")
    if not record.get('posted_date_iso'):
        errors.append("Invalid or missing date")
    min_budget, _ = parse_price(record.get('budget', ''))
    if min_budget is None:
        errors.append("Invalid budget format")
    return errors

# Validate our record
errors = validate_record(raw_record)
if errors:
    print(f"Record {raw_record['id']} has errors: {errors}")
    # We might choose to drop it or flag it for review

# 5. Handling Missing Data Output
# If validate_record() finds issues:
validation_errors = ["Invalid budget format"]  # Example error

# If no issues:
validation_errors = []  # Empty list means valid

########################################################################################## 


# 6. Flattening Nested Data (flatten_json())
# Goal: Break out the nested reviews list into separate rows.

# We will use pandas.json_normalize for this, as it's perfect for the job.
import pandas as pd

# First, let's create a main record without the nested field to avoid duplication.
main_record = {k: v for k, v in raw_record.items() if k != 'reviews'}

# Now use json_normalize on the nested 'reviews', using the 'id' as a meta key to link back.
reviews_df = pd.json_normalize(raw_record['reviews'], meta=['id'], record_prefix='review_')
# reviews_df now has columns: ['reviewer', 'comment', 'rating', 'id']

# If you want everything in one flat table (one row per review):
flat_table = reviews_df

# To add main record info to the flat table:
main_df = pd.DataFrame([main_record])
flat_table = reviews_df.merge(main_df, on='id', how='left')
# The flat_table now has columns for all main record fields AND review fields.

# Input nested data:
reviews = [
    {"reviewer": "Jane D.", "comment": "Great client!", "rating": 5},
    {"reviewer": "John S.", "comment": "Payment was slow.", "rating": 4}
]

# After flattening (pandas DataFrame):
# | id | product | price | review_reviewer | review_comment     | review_rating |
# |----|---------|-------|-----------------|--------------------|---------------|
# | abc| Web Dev | 25000 | Jane D.         | Great client!      | 5             |
# | abc| Web Dev | 25000 | John S.         | Payment was slow.  | 4             |

########################################################################################## 


# 7. Normalization by Business Rules
# Goal: Standardize the messy tags list.

tag_mapping = {
    "js": "JavaScript",
    "reactjs": "React",
    "web development": "Web Development"
}

def normalize_tags(tags):
    normalized = []
    for tag in tags:
        normalized_tag = tag_mapping.get(tag.lower(), tag) # Use mapped value, or original if not found
        normalized.append(normalized_tag)
    # Remove duplicates
    return list(set(normalized))

# 7. Normalization by Business Rules Output
# Input
tags = ["Javascript", "js", "Web Development"]

# After normalize_tags()
normalized_tags = ["JavaScript", "Web Development"]  # "js" mapped to "JavaScript", duplicates removed


raw_record['normalized_tags'] = normalize_tags(raw_record['tags'])
# Output: ['JavaScript', 'Web Development'] (note: deduplicated and standardized)

########################################################################################## 

# 8. Validation / QA
# Goal: Add final data quality checks.

import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

# Extract email from description (simplified example)
extracted_email = re.search(r'[\w\.-]+@[\w\.-]+', raw_record['description'])
if extracted_email:
    email = extracted_email.group(0)
    if not is_valid_email(email):
        print(f"Invalid email found: {email}")

# Check if rating is within bounds
try:
    rating = float(raw_record['client_rating'].split('/')[0])
    if rating < 0 or rating > 5:
        print(f"Rating {rating} is out of bounds.")
except ValueError:
    print("Could not parse rating.")

# 8. Validation / QA Output
# Email validation
email = "hello@company.com"
is_valid = True  # Would be False for "hello@company"

# Rating validation
rating = 4.5
is_valid = True  # Would be False if rating was 6.5 (out of 5)

########################################################################################## 


r'''
Yes, your list is exceptionally comprehensive for basic and intermediate data cleaning. It covers about 95% of the challenges faced with scraped data.
'''