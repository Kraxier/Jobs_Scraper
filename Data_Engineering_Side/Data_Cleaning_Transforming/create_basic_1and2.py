# Implementing the Concept of 1_clean_basic.py 

r'''
Goal is to Create a script where i needed to create a cleaning or proccessing the files after the scrapping things 

During Scraping for keeps memory/IO low, avoids storing huge raw HTML blobs, and gives usable data quickly.
Remove tags by extracting text nodes (use inner_text() / ::text / .get_text(separator=' ')).
Trim and collapse obvious whitespace.
Extract structured fields (email, price, date) with lightweight regex so you get structured data immediately.
'''

# Playwright Script for Scrapping while also cleaning 
# Bs4 Script for Scrapping while also Cleaning 
# General Script for Cleaning 
r'''
General Script is a (post-processing pipeline): 
'''

# During Scrapping Cleaning 
# Playwright Synch Version 
def extracting_elements(page):
    ############### .inner_text() ###############
    r'''
    What it is: A Playwright method that extracts the visible text of an element
        * Returns only the text that's actually visible to users in the browser
        * Automatically collapses whitespace (multiple spaces become single spaces)
        * Excludes text from hidden elements (with display: none or visibility: hidden)
        * Respects CSS styling (like text transformed with text-transform)
    '''
    # HTML: <div>  Hello   <span style="display:none">Hidden</span>  World  </div>
    text = element.inner_text()
    # Result: "Hello World" (collapsed whitespace, hidden text excluded)

    ############### .text_content() ###############
    r'''
    What it is: A Playwright method that extracts all text content of an element
        * Returns all text nodes within an element, regardless of visibility
        * Includes text from hidden elements
        * Preserves original whitespace formatting
        * Doesn't collapse whitespace automatically
    '''
    # HTML: <div>  Hello   <span style="display:none">Hidden</span>  World  </div>
    text = element.text_content()
    # Result: "  Hello   Hidden  World  " (preserves all whitespace and hidden text)

    ############### .strip() ###############
    r'''
    What it is: A Python string method for removing whitespace
        What it does:
        * Removes leading (beginning) and trailing (end) whitespace characters
        * Whitespace includes spaces, tabs, newlines (\n), and carriage returns (\r)
        * Does NOT affect whitespace between words
    '''
    text = "   Hello World   \n"
    cleaned = text.strip()
    # Result: "Hello World" (only beginning/end spaces removed)

    ############### .split() ############### 
    r'''
    What it is: A Python string method for splitting text into parts
        What it does:
        * By default, splits on any whitespace (spaces, tabs, newlines)
        * Returns a list of words/parts
        * When used without parameters, it also removes empty strings from the result
    '''
    raw_text = "   Hello    World\nFrom   Python   "
    words = raw_text.split()  # Split on any whitespace
    # Result: ['Hello', 'World', 'From', 'Python']

    # Then join with single spaces to collapse whitespace:
    cleaned_text = ' '.join(words)
    # Result: "Hello World From Python"

    # Implementation
    element = page.locator('h1')

    # Extracting things 
    inner_h1 = element.inner_text()
    inner_h1 = element.text_content()

    # Deep Cleaning 
    clean_from_content = ' '.join(inner_h1.split()).strip() 




    


