# Regex Concept: 


# September 4 
# What is Regex?
r'''
A Regular Expression (Regex) is a sequence of characters that defines a search pattern. It's like a super-powered "Find" or "CTRL+F" function that doesn't just look for exact text, but for patterns.
It's a language: Regex has its own syntax and rules for defining these patterns.
It's a tool: You use it within other programming languages (like Python, JavaScript, etc.).
'''

r'''
Regex is a searching pattern for finding things 
It's have an own Syntax and rule and it is a tool for many different programming language lke python and javascript
'''

# What is the Relevance of that in Web Scrapping?
r'''
In Web Scraping: It's the tool you use to find and extract specific,
 predictable sequences of text from the messy HTML you've downloaded. 
 For example, the pattern for an email address is something@something.anything.
'''

r'''
In terms of web scrapping you are finding the text from the messy html that have pattern like email
'''

# Why is this Important? 
r'''
Web scraping is not just about getting data; it's about getting clean, 
usable data. Websites are built for humans, not machines. 
The data you want is often buried inside:
    * Lots of HTML tags: <div>, <span>, <p>, etc.
    * Inconsistent formatting.
    * Unrelated text and "noise".
Regex is important because it allows you to cut through that noise and pluck out the precise data you need from the text. It turns a messy string of characters into structured information.
'''
r'''
Web Scrapping is all about getting data but data should be clean and usable and a lot of that is buried inside the html tags and inconsistent formatting 
and Regex can help that by extracting specific thing in that 
'''

# Why should i learn this?
r'''
1. Precision Extraction: You can extract very specific data (prices, emails, IDs, dates) that would be incredibly tedious to get any other way.

2. Data Validation: You can check if the data you scraped is in the right format before you save it to your database (e.g., "Does this string look like a valid email?").

3. Efficiency: A single line of regex can often replace dozens of lines of looping and conditional logic.

4. Universal Application: Regex is not just for Python or web scraping. It's a standard tool used in nearly every programming language, text editor (like VSCode, Sublime), and command-line tools (like grep). Learning it is an investment that pays dividends across your entire programming career.
'''

r'''
In terms of Precision and Extraction thing in web scrapping and also the data cleaning part of it which is very important thing too man 

i can check the data before saving it to the database because regex is a pattern and reading thing 

And Regex is a universal application in terms of programming and can pay dividends in programming career 
'''

# How Powerful Regex is in term of web Scrapping?

r'''
For Parsing the HTML don't Rely too Much in Regex, Use the Standard Library

Why is it still used? 

1. Data Cleaning and Extraction within the Text
You've used BeautifulSoup to extract a block of text, but that text contains the specific data you need mixed with junk.

2. Validating Extracted Data:
Ensure the data you scraped matches an expected pattern before saving it to your database.

3. Parsing Non-HTML Content:
APIs (JSON): Modern websites often load data dynamically via APIs that return JSON. While you should use a JSON parser, sometimes you might need regex to find the API URL itself within the HTML or a JavaScript file.

JavaScript Files: Data can be embedded within JavaScript variables or objects. You can extract the JavaScript code with your HTML parser and then use regex to find specific patterns within it (e.g., productData: {...}).

CSV, Log Files, or Custom Formats: If you're scraping data from other text-based sources, regex is the ideal tool.
'''

# How about in terms of Data Cleaning? 
r'''
 When it comes to data cleaning in the web scraping pipeline, Regex transforms from a "risky tool to use with caution" into an absolutely essential and powerful workhorse.

1. Standardizing Text Formats
You've extracted text, but it's in various formats that need to be normalized.

Phone Numbers:

Raw Data: "(555) 123-4567", "555.123.4567", "5551234567", "+1-555-123-4567"

Goal: Standardize to a single format, e.g., 555-123-4567.

Regex Use: Use re.sub() to remove all non-digit characters first (r'[^\d]'), then use a capturing groups to reformat the string into the desired pattern. 
1. Standardizing Text Formats
You've extracted text, but it's in various formats that need to be normalized.

Phone Numbers:

Raw Data: "(555) 123-4567", "555.123.4567", "5551234567", "+1-555-123-4567"

Goal: Standardize to a single format, e.g., 555-123-4567.

Regex Use: Use re.sub() to remove all non-digit characters first (r'[^\d]'), then use a capturing groups to reformat the string into the desired pattern.

Dates:

Raw Data: "2023-10-26", "10/26/2023", "26th Oct 2023", "Oct 26, 2023"

Goal: Identify and convert all these to a standard ISO format (YYYY-MM-DD).

Regex Use: Write patterns to match each known format, parse the components (day, month, year), and then output them in the standard order.

2. Extracting Specific Patterns from Unstructured Text
This is perhaps the most common use case. You have a large block of text and need to pluck out very specific pieces of information.

Email Addresses:

python
import re

text = "Contact support@company.com or sales@other.org for help."
emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
print(emails) # Output: ['support@company.com', 'sales@other.org']
Prices and Currency:

python
text = "The price was $19.99, now on sale for £15.50. Special offer: 5.99€."
prices = re.findall(r'\$?\d+\.\d{2}', text) # Simple example for $ and basic format
print(prices) # Output: ['$19.99', '15.50', '5.99']
# A more robust pattern would handle different currencies and thousand separators.
Hashtags or Mentions:

python
text = "Loving the new features! #WebScraping #Python @regexfan"
hashtags = re.findall(r'#(\w+)', text)
mentions = re.findall(r'@(\w+)', text)
print(hashtags) # Output: ['WebScraping', 'Python']
print(mentions) # Output: ['regexfan']
3. Removing Unwanted Characters and Noise
Often, extracted text comes with extra whitespace, line breaks, HTML entities, or other junk.

Extra Whitespace:

python
messy_text = "   This    text   has   too   many   spaces.   "
clean_text = re.sub(r'\s+', ' ', messy_text).strip()
print(clean_text) # Output: "This text has too many spaces."
Removing Non-Printable/Non-ASCII Characters:

python
text = "This text… has “smart” quotes and a dash – and emoji 🚀."
# Keep only common printable ASCII (simplified example)
clean_text = re.sub(r'[^\x20-\x7E]', '', text)
print(clean_text) # Output: "This text has smart quotes and a dash  and emoji ."
# Note: This is a blunt instrument. For complex Unicode, consider `unicodedata` module.
Cleaning Leftover HTML:
Sometimes, the parser might leave behind HTML entities.

python
text = "This product is &quot;the best&quot; &amp; it&#39;s cheap."
clean_text = re.sub(r'&(#?\w+);', lambda m: html.unescape(m.group(0)), text)
# While the `html` module is better for this, regex can help find the patterns.
4. Validating Data Integrity
Before inserting scraped data into a database, you can use regex to validate it, ensuring it meets expected criteria.

Is this a valid email? re.match(email_pattern, extracted_string)

Does this product SKU follow our expected format? (e.g., ABC-12345)

Is this field a valid zip code? (5 digits, or 5+4 format)

This allows you to flag or log records with invalid data for manual review instead of polluting your database.

5. Splitting Complex Strings
The standard .split() string method is useful but limited. Regex provides much more powerful splitting capabilities.

Splitting on Multiple Delimiters:

python
text = "apple, banana; cherry|date fig"
items = re.split(r'[,\s;|]+', text)
print(items) # Output: ['apple', 'banana', 'cherry', 'date', 'fig']
'''







 
# What is Regex? 

# What are the Core Building Block? 
#  What are the MetaCharacters? 
# What is Quantifiers? 
# What is Characters Classess?
# What is Groups & Capturing? 