import csv # Why: To Save the File in the CSV format 
import random # Why: To Randomize the Human Interaction in the website even though it's not needed
import time # Why: To Add Time in Saving the File, Randomize the Pausing Time of the Program like waiting it, Adding Time of Scrapping 
from datetime import datetime # Why: Adding the Date in the Files 
from urllib.parse import urljoin # Why: To Paginate between pages using the URL 
from playwright.sync_api import sync_playwright # Why: 
from fake_useragent import UserAgent # Why: To Randomize the USeragent Online 
from random_user_agent.params import SoftwareName, OperatingSystem # Why: To Randomize the USeragent Online 
from random_user_agent.user_agent import UserAgent as RandomUA # Why: To Randomize the USeragent Online 


# Why: To Save the File in the CSV thing
def start_csv_writer(): # 
    r"""Open a CSV for streaming writes during scraping."""
    date_str = datetime.now().strftime("%Y-%m-%d") # Getting the Current Date  
    filename = f"automation_{date_str}.csv" # Adding the Date for the Historical Analysis/historical logs and (you won’t overwrite old CSVs). 
    r'''You Won't Overwrite the old CSV files '''


    csv_file = open(filename, "w", newline="", encoding="utf-8") 
    r'''
    * Opens the CSV file in write mode ("w").
    * newline="" ensures rows don’t get extra blank lines (important for CSVs on Windows).
    * encoding="utf-8" makes sure text (like non-English characters) is saved correctly.
    * Stores the file object in csv_file.
    '''


    writer = csv.writer(csv_file)
    r'''
    * Creates a CSV writer object tied to the csv_file.
    * This object (writer) is what you’ll use to actually add rows to the file.
    '''
    writer.writerow(["Role of Job", "Company Name", "Company Location", "Type of Work", "Description"]) # Here the The Top Column in the Things
    r'''
    Writes the header row (the column names) into the CSV file.
    So the first line of the CSV looks like:
    '''
    print(f"📁 Streaming results to: {filename}") # For Debugging if it currently saving things 

    return csv_file, writer
    r'''
    csv_file → the file object (so you can later .close() it when finished).
    writer → the CSV writer (so you can call writer.writerow([...]) to add more rows).
    writer to save the next data which is the Job Post Thing 
    '''
    # Summary: Prepare the CSV files and Writing the Date thing 



def write_job(writer, csv_file, job_data):
    r'''
    3 Arguments 
    writer: the CSV writer object (so it can write a row),
    csv_file → the open file object (so it can flush it),
    job_data → a list or tuple with the job info, e.g.:
    '''
    """Write a single job row and flush immediately."""
    writer.writerow(job_data)
    r'''
    # must be a list-like object (list or tuple)
    job_data = [
    "Backend Developer", 
    "Netflix", 
    "Los Gatos, CA", 
    "Hybrid", 
    "Work on streaming services"
    ]
    '''
    csv_file.flush()  # 💾 flush() forces Python to immediately write all buffered data to disk.
    r'''
    You’re scraping and want to make sure progress is saved even if the program crashes.
    '''

# Extracting the Content from the Site:
def extraction_job_description(page, writer, csv_file): 
    try:
        # Wraps the whole routine in a top-level try to catch unexpected failures.
        # count() counts how many matching elements exist right now
        locator = page.locator(".job-link.-no-underline.-desktop-only.show-job-description")
        count_job_post = locator.count()

        # Early Exit of the Function if there are no Job Post in the Current Page
        # Way to Handle the Error Properly
        if count_job_post == 0:
            print("[WARNING] No job posts found on this page.")
            return

        # For Each Job Post it Randomly Mix it
        r'''
        Why?
            To Look like a Human Behaviour doing it Thing in there 
        '''
        indexes = list(range(count_job_post))
        random.shuffle(indexes)
        
        
        for i in indexes: # For Each Job Post Loop it 
            try:
                time.sleep(random.uniform(0.8, 2.3)) # Adding a Humanish Delay Before Interacting

                # Hover safely
                # Attempts to hover the i-th job (some sites reveal buttons/details on hover).
                # If hovering fails (detached node, overlay, etc.), logs and skips this job.
                try:
                    locator.nth(i).hover(timeout=3000)
                except Exception as e:
                    print(f"[WARNING] Could not hover over job {i}: {e}")
                    continue

                time.sleep(random.uniform(0.2, 0.5)) # For Delaying Humanish Bot

                # Click safely # Opening the Job by Clicking it the same nth(i) element.
                # On failure, logs and goes to the next jo
                try:
                    locator.nth(i).click(timeout=5000)
                except Exception as e:
                    print(f"[WARNING] Could not click job {i}: {e}")
                    continue

                # Get job title text safely 
                try:
                    value = locator.nth(i).inner_text(timeout=5000)
                except Exception as e:
                    print(f"[WARNING] Could not get text for job {i}: {e}")
                    value = "Unknown"

                # Wait for job description container
                if not page.wait_for_selector(".job-description-container", state="visible", timeout=5000):
                    print(f"[WARNING] No job description loaded for job {i}")
                    continue

                # Extract safely
                # Helper that returns inner text for a CSS selector or "N/A" if it fails—keeps the flow tidy.
                # If it Missing i can "N/A"
                def safe_text(sel):
                    try:
                        return page.locator(sel).inner_text(timeout=3000)
                    except Exception:
                        return "N/A"

                roles_of_jobs = safe_text('.job-title.heading.-size-xxlarge.-weight-700')
                company_name = safe_text('.company')
                company_location = safe_text('.location')
                type_of_work = safe_text('.badge.-work-arrangement-badge .content')

                print(f"{i}: {value}")
                print(f"Role of the Job: {roles_of_jobs}")
                print(f"Company Name: {company_name}")
                print(f"Company Location: {company_location}")
                print(f"Type of Work: {type_of_work}")
                print("-" * 10)

                try:
                    description_extraction = page.locator(".job-description-container").inner_text(timeout=5000).lower()
                except Exception:
                    description_extraction = "No description found."

                print(description_extraction)
                print("-" * 50)

                # ✅ Use the new write_job function
                write_job(writer, csv_file, [roles_of_jobs, company_name, company_location, type_of_work, description_extraction])

            except Exception as e:
                print(f"[ERROR] Skipping job {i} due to error: {e}")
                continue
    # Top Level if the extraction of Job Description are Failed
    except Exception as e:
        print(f"[ERROR] extraction_job_description() failed: {e}") 


software_names = [SoftwareName.CHROME.value, SoftwareName.FIREFOX.value]
r'''
SoftwareName is an Enum (presumably). .value gets the actual value (like "chrome" or "firefox").

software_names becomes a list of the software/browser names you want the UA rotator to pick from.
'''
operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]
r'''
Same idea for OS enum values (e.g. "Windows", "Linux"). These tell the rotator which OS strings to include in generated user agents.
'''
fallback_ua_rotator = RandomUA(software_names=software_names,
                               operating_systems=operating_systems,
                               limit=100)
r'''
RandomUA(...) instantiates a rotator object (custom class or third-party) that can supply random user-agent strings.

software_names and operating_systems restrict which parts the rotator will vary.

limit=100 probably controls how many UAs the rotator will pre-generate / cache or the pool size. (Exact meaning depends on the RandomUA implementation.)
'''
def get_user_agent():
    try:
        ua = UserAgent()
        return ua.random
    except Exception as e:
        print(f"[WARNING] fake_useragent failed: {e}")
        return fallback_ua_rotator.get_random_user_agent()
r'''
get_user_agent() tries to use UserAgent() (commonly from the fake_useragent package) to get a random, realistic user agent via ua.random.

If that fails (network, package error, bad cache, etc.), it prints a warning and falls back to fallback_ua_rotator.get_random_user_agent() — i.e., the RandomUA instance you created earlier.

This makes the function resilient: if fake_useragent is unavailable, your scraper still gets a UA string instead of crashing.
'''
# Basically Get the Headers or User Agent in Scrapping THings

# Next button Things
def pagination(page, base_url, writer, csv_file):
    while True:
        # Wait for the current page to fully load jobs so it can do it thing 
        # (Note: this can still return before dynamic content is rendered.)
        page.wait_for_load_state("networkidle")

        # ✅ Pass csv_file so flushing works
        extraction_job_description(page, writer, csv_file)

        try:
            # Wait for the "next page" button
            page.wait_for_selector('.next-page-button', timeout=5000)
            button = page.locator('.next-page-button')

            # If no next page button exists 
            # The Loop will stop 
            if not button.is_visible():
                print("No next page found.")
                break

            # Get the link to the next page
        
            next_page = button.get_attribute('href')
            if not next_page:
                print("Next page button exists, but no href found.")
                break

            # Navigate to next page like page 2 to scrape everything in the sute 
            go_to_next_page = urljoin(base_url, next_page)
            print(f"Going to: {go_to_next_page}")
            page.goto(go_to_next_page, timeout=60000)

            # To Handle the Random Pop Up when Paginating per page
            try:
                # Adjust the selector for your modal's close/dismiss button
                close_button = page.locator("#suggest-better-alert-modal .dismiss")
                
                if close_button.is_visible(timeout=2000):  # waits up to 2 seconds
                    close_button.click()
                    print("Closed popup")
                else:
                    print("Popup detected but close button not visible")
            except Exception as e:
                print(f"No popup detected or error closing popup: {e}")

            # input("Paused. Press Enter to continue...")
        # Top-level except catches any wait/navigation errors and breaks the loop.
        except Exception as e:
            print(f"Error or no more pages: {e}")
            break
r'''
Recommendation: 
1. button.is_visible() can raise if the locator matches multiple elements or gets detached.
* Prefer checking button.count() or use button.first and locator.wait_for() for stable behavior.

2. Infinite loop risk / stuck on same page
If navigation fails or the site returns the same URL, you may loop forever. Keep a visited set or max_pages counter.

'''



def scrape_jora_title(): # The Top Leve l Function 
    # Opens a dated CSV and returns both file and CSV writer (so you can write rows and later close/flush).
    csv_file, writer = start_csv_writer()  
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        ua_string = get_user_agent()

        context = browser.new_context(
            user_agent=ua_string,
            viewport={"width": 1366, "height": 768}
        )
        page = context.new_page()
        r'''
        Creates a browser context with a random user agent and a viewport size, then a page in that context.
        Getting the USer Agent and Using that as a browser context of things
        '''


        base_url = "https://ph.jora.com/" # The site root used for URL joins and navigation.
        # ✅ Your keyword list
        keywords = [
            # "Mechatronics",
            # "Instrumentation Technician",
            # "Instrumentation Engineer"
            # "Robotics Engineer",
            # "Control Systems Engineer", Due to 5,k Jobs i Stop this Midway I'm Going to Continue this later
            # "Electromechanical Engineer", Not this Part more on Mechanical and electrical 
            # "Process Control Engineer",
            # "Industrial Automation Specialist",
            # "Manufacturing Engineer (with automation focus)",
           #  "Test & Commissioning Engineer",
            # "Maintenance Engineer (industrial/mechanical/electrical)",
            # "Embedded Systems Engineer",
            # "Electrical Design Engineer", # I Stop Mid Here there are 2k Jobs are like this 
           #  "Firmware Engineer (for industrial equipment)",
            # "Field Service Engineer (automation/instrumentation equipment)",
            "System Integration Engineer",
            "Production Engineer", #  (automation-heavy industries)
            # "Plant Engineer",
            "SCADA Engineer",
            "PLC Programmer",
            "LabVIEW Developer",
            "Process Instrumentation Specialist",
            "Robotics Technician",
            "Motion Control Engineer"
        ]

        # For each in key words and putting it in a search button and doing that
        r'''
        logs the term,

        navigates to the homepage,

        fills the search box #q with the term and clicks the search button,

        calls pagination() to crawl all pages for that search, passing writer and csv file to be written/flushed,

        and logs completion.
        '''
        for index, term in enumerate(keywords, start=1):
            print(f"\n🔍 [{index}/{len(keywords)}] Searching for: {term}")

            page.goto(base_url, timeout=60000)
            page.fill('#q', term)
            page.click('button.search-jobs-button')

            pagination(page, base_url, writer, csv_file)

            print(f"✅ Finished: {term}")

        # Closes the browser and then closes the CSV file when everything finish
        browser.close()
    csv_file.close()

# Standard Python entrypoint: run the function when the script is executed.
if __name__ == "__main__":
    scrape_jora_title()



r'''
Reusing a single user_agent for entire run: You pick one UA string at start. That’s OK, but rotating UA per search or periodically can reduce pattern detection. Don’t change UA per request too frequently or produce invalid UAs.
Page state reset: You call page.goto(base_url) before each search; good for resetting but you might want to context.clear_cookies() or recreate context if the site tracks sessions.

Before Interacting: 
Use wait_for_selector() or locator.wait_for() before interacting.
'''

r'''
Top priorities (do these first)

Guarantee resource cleanup (CSV & browser)

Why: Prevent corrupted CSVs and leaked browser processes on errors.

What to do: Use try/finally (or context managers) to always close() the CSV and browser. You already use with sync_playwright() — ensure CSV close is in an outer finally.

One-line fix: wrap scrape_jora_title() body in try/finally and call csv_file.close() in finally. (Your hardened refactor has this.)

Create and reuse UserAgent() once

Why: UserAgent() can be slow and error-prone if created per call.

What to do: Initialize once at module import and reuse; fallback to RandomUA when it fails. Add optional locking for threads.

Example:

try:
    _FAKE_UA = UserAgent()
except Exception:
    _FAKE_UA = None

def get_user_agent():
    if _FAKE_UA:
        try: return _FAKE_UA.random
        except Exception: pass
    return fallback_ua_rotator.get_random_user_agent()


Protect Playwright operations with robust waits

Why: time.sleep() races and wait_for_selector raises on timeout — both lead to brittle scrapers.

What to do: Prefer locator.wait_for(state="visible", timeout=...), element_handle snapshotting for lists, and try/except around waits to handle TimeoutError specifically.

Avoid index drift: snapshot element handles for loop

Why: Clicking can change DOM order, causing locator.nth(i) to point at the wrong element or a detached node.

What to do: Use element_handles() once per page, shuffle handles, and operate on handles (hover/click) instead of re-querying by index.

Make pagination robust (click instead of href, visited set, max_pages)

Why: Href-less JS pagination, loops, and stuck navigation.

What to do: Prefer next_button.click() when possible; maintain visited URL set and max_pages guard.

Reliability & robustness (next items)

Flush + close file safely; consider csv.DictWriter

Keep using flush() to avoid data loss; optionally csv.DictWriter for readability/column safety.

Add per-job and per-search counters / logging

Track pages scraped, rows written, fallback UA usage. Helps debug blocking or scale issues.

Trim/limit enormous text when logging

Print only first ~300 chars of descriptions to keep console readable.

Handle modals/popups gracefully

Use locator.first and wait_for(state="visible") then click() inside try/except to dismiss.

Add polite jitter and rate-limits

Random sleeps between interactions and between searches (you already do some). Consider await/time.sleep ranges tuned to the site.

Maintainability & architecture (medium term)

Encapsulate scraper into a class

Put writer, csv_file, UA, counters into a JoraScraper class. Cleaner state management and easier unit tests.

Make configuration explicit

Move constants (selectors, timeouts, UA rotation flag, max_pages) to a config object or top of file.

Return statistics from functions

Let pagination() return (pages_scraped, rows_written) and aggregate per search. Makes monitoring simpler.

Add resume capability

Save progress (e.g., last keyword index) to a small JSON checkpoint file so you can resume after interruption.

Add tests & dry-run mode

Unit test small parts (parsing, safe_text), and a dry-run mode that runs on a saved sample HTML page.

Scalability & performance (later)

Parallelize cautiously

If you later do parallel searches, open separate browser contexts per worker, and write to separate CSVs or synchronize writes.

Consider saving long descriptions separately

If descriptions are very large, consider saving them to files (or compressed columns) and refer by id in CSV.

Monitoring / alerting

Log to a file and optionally report when fallback UA used > X times or when scraping stops prematurely.

Safety, ethics & legal

Respect robots.txt and terms of service

Make sure the site allows scraping. If unsure, ask for permission or throttle to be polite.

Be prepared for CAPTCHAs

If the site uses bot detection, consider back-off strategies or avoid scraping at scale.
'''