


# records = [
#     {"Role": "Engineer", "Company": "Acme", "Skills": ["Python", "SQL"]},
#     {"Role": "Designer", "Company": "Beta", "Skills": ["Figma", "UI/UX"]}
# ]
r'''
* This is a list of dictionaries (two scraped items).
* Each dictionary = one job posting. 
* Keys = "Role", "Company", "Skills". (The Column Thing)
* Values can be strings ("Engineer", "Acme") or even lists (["Python", "SQL"]).
* This simulates the kind of structured data you scrape.
'''

# with open("data.jsonl", "w", encoding="utf-8") as f:
r'''
* open() → built-in function to open files.
    * "data.jsonl" = filename (JSONL = JSON Lines format).
    * "w" = write mode → creates a new file, or overwrites if it exists.
    * encoding="utf-8" → ensures characters (like emojis or non-English text) save correctly.
* with ... as f: → context manager:
    * automatically opens the file.
    * ensures the file is closed when done (even if an error happens).
* f → the file object (like a "handle") that you use to write into.
'''

# for record in records:
r'''
Loops over each dictionary in the records list.
On the first loop: record = {"Role": "Engineer", "Company": "Acme", ...}
On the second loop: record = {"Role": "Designer", "Company": "Beta", ...}
'''
# json_line = json.dumps(record, ensure_ascii=False)
r'''json.dumps() → converts a Python object (dict, list, etc.) into a JSON string.'''

# Example: 
r'''
{"Role": "Engineer", "Company": "Acme"}  
→ '{"Role": "Engineer", "Company": "Acme"}'
ensure_ascii=False → allows non-ASCII characters to be written properly (e.g., "Málaga" instead of escaped "\u00e1").
'''

# f.write(json_line + "\n")
r'''
f.write() → writes text into the open file.
json_line is one JSON object, "...".
+ "\n" ensures each record is on its own line → that’s the JSONL format.
'''
# Example: 
r'''
{"Role": "Engineer", "Company": "Acme", "Skills": ["Python", "SQL"]}
{"Role": "Designer", "Company": "Beta", "Skills": ["Figma", "UI/UX"]}
'''


# ⚡ Fundamentals of file handling in Python

# Opening a file
# f = open("filename.txt", "w")  # "w" = write mode

r'''
Modes:
    "r" → read (default).
    "w" → write (overwrite).
    "a" → append (add to end).
    "b" → binary mode (e.g., images).
    "r+" → read/write.
'''


r'''Always close files'''
# f.close()

r'''
But better: use with open(...) as f: → auto-closes safely.
'''


# Reading

with open("filename.txt", "r") as f:
    data = f.read()          # whole file as string
    lines = f.readlines()    # list of lines


# Writing

with open("filename.txt", "w") as f:
    f.write("Hello\n")
    f.write("World\n")

r'''
✅ So the code you showed is a textbook example of:
open file for writing (with UTF-8)
loop through data
convert Python dict → JSON string
write one line per record (JSONL)
'''
