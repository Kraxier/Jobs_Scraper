# Studying and Learning how to Convert JSON, JSONL to Different Types of Format


# What JSON, JSONL, and Pandas expect


# JSON 
r'''
JSON (JSON (JavaScript Object Notation))(standard): a single JSON value. Common shapes:
    * array of objects: [{...}, {...}] — perfect for tables.
    * single object: {"a":1, "b":2} — becomes one row if you want a table.
[
  {
    "city": "Manila",
    "population": 17800000,
    "country": "Philippines"
  },
  {
    "city": "Paris",
    "population": 2100000,
    "country": "France"
  },
  {
    "city": "Tokyo",
    "population": 14000000,
    "country": "Japan"
  }
]
Pandas can directly read this into a DataFrame using pd.read_json().
JSON, in its standard form, expects a single, complete JSON value. The most common and useful structure for tabular data is an array of objects, 
where each object represents a row. This is the format a 
Pandas DataFrame naturally expects. A single object can also be a valid JSON, which Pandas will interpret as a single row.
'''


# JSONL (JSON Lines)
r'''
JSONL is a line-delimited format. It's a plain text file where each line is a self-contained JSON object, 
followed by a newline character. Unlike standard JSON, it's not a single JSON value, but rather a sequence of individual JSON values. This format is highly efficient for streaming data and processing large datasets line by line without having to load the entire file into memory.
Understanding: Basically you have a list of JSON in a list

{"city": "Manila", "population": 17800000, "country": "Philippines"}
{"city": "Paris", "population": 2100000, "country": "France"}
{"city": "Tokyo", "population": 14000000, "country": "Japan"}

'''

r'''
Pandas
The core of a Pandas DataFrame is a two-dimensional, 
mutable, tabular data structure with labeled axes (rows and columns). 
It's essentially a table. When you provide data to Pandas, it wants a structure that can be easily mapped to rows and columns.

    * A list of dictionaries list[dict] is the most intuitive format for Pandas, as it directly maps each dictionary to a row and the keys to columns.
    example of list of Dictionary: 
        data = [
    {'name': 'Alice', 'age': 30, 'city': 'New York'},
    {'name': 'Bob', 'age': 25, 'city': 'Los Angeles'},
    {'name': 'Charlie', 'age': 35, 'city': 'Chicago'}
    ]
    # Which can Pandas Read each of this line easily as you can see 

    * For nested JSON, where some values are themselves dictionaries or lists, 
    Pandas can't directly read it into a flat table. You need to use pd.json_normalize() 
    to flatten the nested structures into columns. This function is crucial for converting complex JSON into a usable DataFrame.

'''

# This is a Nested JSON
r'''
[
  {
    "id": 1,
    "name": "Jane Doe",
    "contact": {
      "email": "jane@example.com",
      "phone": "555-1234"
    }
  },
  {
    "id": 2,
    "name": "John Smith",
    "contact": {
      "email": "john@example.com",
      "phone": "555-5678"
    }
  }
]
'''

# Using the pd.json_normalize
import pandas as pd
import json

data = json.loads("""
[
  {
    "id": 1,
    "name": "Jane Doe",
    "contact": {
      "email": "jane@example.com",
      "phone": "555-1234"
    }
  },
  {
    "id": 2,
    "name": "John Smith",
    "contact": {
      "email": "john@example.com",
      "phone": "555-5678"
    }
  }
]
""")

df = pd.json_normalize(data)
# print(df)
r'''
Results:
   id        name     contact.email contact.phone
0   1    Jane Doe  jane@example.com      555-1234
1   2  John Smith  john@example.com      555-5678
'''
# Basically the Indentation at the bottom Thing
# Practising the json.load() vs. json.loads()
r'''
json.load()	File	Reading an external file
json.loads()	String	Parsing an in-memory string
'''
# record = json.loads() this is wrong because it is already 
type_1 = type(data)
length = len(data)
index_0 = data[0]
index_0_name = data[0]['name']
index_1 = data[1]['contact']['email']

print(type_1) # Output: <class 'list'>
print(length) # Output: 2
print(index_0) # Output:{'id': 1, 'name': 'Jane Doe', 'contact': {'email': 'jane@example.com', 'phone': '555-1234'}}
print(index_0_name) # Output: Jane Doe
print(index_1) # Output: john@example.com









r'''
When you see code, dissect it
Next time I (or a tutorial) give you code, don’t just run it.
Ask yourself:
What is each line doing?
Could I explain this to a beginner?
How would I rewrite it in my own words or slightly differently?
A good trick: retype the code from scratch, but without looking at the original after the first read. This shows what you’ve actually understood.
'''

r'''
Work on tiny projects with constraints
Fundamentals stick best when applied to real problems.
'''

r'''
Practice “fundamental-only” problem solving
Go to coding practice sites (LeetCode easy, HackerRank, Exercism).
Force yourself to solve problems without Googling.
'''

