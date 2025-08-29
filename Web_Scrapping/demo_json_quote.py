import csv
import random
import time
from datetime import datetime
from urllib.parse import urljoin
from playwright.sync_api import sync_playwright

# Always import JSON 
import json

r'''
Goal is to Build a JSON format in gathering the Data in the Quote to Scrape
That are Streaming Similar to the demo_stuff 
'''


# Define the Function to Open a Big JSON File and prepare it to store things 
def start_json_array_writer(): 
    # Get the Today Date 
    date_str = datetime.now().strftime("%Y-%m-%d")
    filename = f"quote_{date_str}.json"
    r'''
    Opens the file for writing ("w" mode).
    utf-8 ensures all characters (like é, ü, 汉字) are stored correctly.
    ''' 
    f = open(filename, "w", encoding="utf-8")
    f.write("[\n")
    r'''
    * Writes the opening bracket of a JSON array.
    * So the file now starts with:

        [

    '''
    return f, False  # file handle + flag for first record
    r'''
    * The file handle (f) so you can keep writing to the file.
    * A boolean flag (False) that will help track whether we’re writing the first record or not.
    '''
    r'''
    Summary we Preparing the JSON file to Store it by Doing all of this 
    '''

# This function writes a single JSON object (record) into the open array file.
def write_record(f, first, record):
    r'''
    * f: the file handle.
    * first: a boolean flag (if True, it’s the first record; if False, we must prepend a comma).
    * record: the Python dict to save.
    '''
    if not first:
        f.write(",\n")  # add comma before next record
    r'''
    If it’s not the first record → write a comma + newline ,\n before writing the new JSON object.
    This is required for valid JSON arrays, e.g.:

    [
        {"Role": "Engineer"},
        {"Role": "Designer"}   <-- must have a comma before this
    ]
    '''
    f.write(json.dumps(record, ensure_ascii=False, indent=2))
    r'''
    Converts the Python dict (record) into a JSON-formatted string.
    ensure_ascii=False → keeps Unicode characters as they are (é instead of \u00e9).
    indent=2 → pretty-prints with indentation.
    '''
    return False  # after first write, always False
def close_json_array(f):
    f.write("\n]\n")
    r'''
    Writes the closing bracket ] for the JSON array.
    '''
    f.close()

r'''
Why the boolean flag is needed
When you stream/write incrementally:
    * The first record → must not have a comma before it.
    * Every subsequent record → must start with a comma.
If we didn’t track this, you’d either:
    * accidentally put a comma before the first record (invalid JSON), or
    * forget to put commas between records (invalid JSON).
'''


# python demo_json_quote.py
def extract_quote(page):
    quote = page.locator(".quote .text").first
    quote_text = quote.inner_text()
    print(quote_text)
    author = page.locator(".author").first
    author_text = author.inner_text()
    print(author_text)
    # return {
    #     "Quote": quote_text,
    #     "Author": author_text
    # }
    return {"Quote": quote_text, "Author": author_text}

# https://quotes.toscrape.com/js/
def quote_to_scrape():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(
            viewport={"width": 1366, "height": 768}
        )
        page = context.new_page()

        base_url = "https://quotes.toscrape.com/js/"
        page.goto(base_url)
        extract_quote(page)
        browser.close()


if __name__ == "__main__":
    quote_to_scrape()