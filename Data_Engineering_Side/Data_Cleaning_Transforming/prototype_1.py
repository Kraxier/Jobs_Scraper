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
'''