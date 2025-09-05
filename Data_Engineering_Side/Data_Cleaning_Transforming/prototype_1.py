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

r"""
    Clean text by removing HTML, normalizing whitespace, and fixing encoding
"""
