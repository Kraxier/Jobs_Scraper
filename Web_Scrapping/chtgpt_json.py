from playwright.sync_api import sync_playwright
from datetime import datetime
import json

def start_json_array_writer():
    date_str = datetime.now().strftime("%Y-%m-%d")
    filename = f"quote_{date_str}.json"
    f = open(filename, "w", encoding="utf-8")
    f.write("[\n")                     # start JSON array
    print(f"📁 Writing to: {filename}")  # inform where we write
    return f, True                     # True => next write is the FIRST record

def write_record(f, first, record):
    if not first:
        f.write(",\n")                 # comma before every record except the first
    f.write(json.dumps(record, ensure_ascii=False, indent=2))
    return False                       # after writing once, it's no longer the first

def close_json_array(f):
    f.write("\n]\n")                   # close JSON array
    f.close()

def extract_quote(page):
    # extract the first quote and author from the page
    # quote_text = page.locator(".quote .text").first.inner_text()
    # author_text = page.locator(".quote .author").first.inner_text()
    # print("Extracted:", quote_text, "-", author_text)
    # return {"Quote": quote_text, "Author": author_text}

    # quote_text = page.locator(".quote .text").inner_text()
    # author_text = page.locator(".quote .author").inner_text()
    # list_quote = []
    # list_author = []
    # for quotes in quote_text:
    #     print("Extracted:", quote_text, "-", author_text)
    #     return {"Quote": quote_text, "Author": author_text}

    quotes = page.locator(".quote") # The Author and Quote are all Under of Quote blocks 
    list_records = []

    # Counting How many Quotes are currently in the page
    for i in range(quotes.count()):
        quote_text = quotes.nth(i).locator(".text").inner_text()
        author_text = quotes.nth(i).locator(".author").inner_text()
        r'''
        quotes.nth(i)
            * .nth(i) picks out the i-th element from that collection.
            * i = 0 → first quote block
            * i = 1 → second quote block
        '''
        print("Extracted:", quote_text, "-", author_text)
        list_records.append({"Quote": quote_text, "Author": author_text})
    return list_records

    

def save_first_quote():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # set True to run headless
        page = browser.new_page(viewport={"width":1366, "height":768})
        page.goto("https://quotes.toscrape.com/js/", wait_until="domcontentloaded")

        f, first = start_json_array_writer()         # open file and mark "first"
        record = extract_quote(page)                 # scrape a quote (dict)
        first = write_record(f, first, record)       # write it into the JSON array
        close_json_array(f)                          # close the JSON array and file

        browser.close()
        print("✅ Saved successfully")

if __name__ == "__main__":
    save_first_quote()
