# How to Handle Error In Terms of Web Scrapping Strategically and not Blindly

# When you should wrap code in try/except
    # Think about impact and likelihood of failure:

# Web scraping actions → ✅ Definitely wrap them.
r'''
1. Why? Network delays, element not found, selector changes — all can break your code.
2. Examples: scrolling, clicking, hovering, extracting text, waiting for elements.
'''

# External file operations → ✅ Wrap them.
r'''
1. Writing to CSV, reading files, saving screenshots.
2. Why? You might have no permission, disk might be full, file might be locked.
'''

# Optional / non-critical steps → ✅ Wrap them.
r'''
If failure should not stop the entire program, protect it with try/except and log a warning.
'''

# When you don’t need try/except
    # For debugging during development — wrapping everything hides useful error messages.