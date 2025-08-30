import csv
import random
import time
from datetime import datetime
from urllib.parse import urljoin
from playwright.sync_api import sync_playwright
from fake_useragent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem
from random_user_agent.user_agent import UserAgent as RandomUA


import json
import os


def jsonl_writer():
    date_str = datetime.now().strftime("%Y-%m-%d")
    filename = f"Mechatronics_{date_str}.jsonl"
    f = open(filename, "w", encoding="utf-8")
    print("📁 Writing JSONL to:", filename)
    r'''
    Why i need to "return f"
    basically i needed to return the "f" to let other function write it
    '''
    return f

r'''Writing the Record or the Scrape Material
    Why "f" so it can write things 
    "record" is where the data will go
    flush=True is a python to immediately push things to the file 
    not just in memory because if the program crash we have still a file
'''
def write_jsonl_record(f, record, flush=True):
    f.write(json.dumps(record, ensure_ascii=False) + "\n")
    r'''
    * json.dumps(...) turn a python object into a JSON string
    record = {"Quote": "你好", "Author": "Li"}
    json.dumps(record, ensure_ascii=False)

    👉 becomes (JSON file)
    '{"Quote": "你好", "Author": "Li"}'
    * ensure_ascii=False [keeps characters as they are (like 你好) instead of converting them to]

    * + "\n"     Adds a newline character at the end.
    {"Quote": "Hello", "Author": "Alice"}
    {"Quote": "World", "Author": "Bob"}

    f.write(...) Actually writes the text into the open file (f).
    '''

    if flush:
        # push Python buffer to OS, then try to sync to disk
        f.flush()
        r'''
        f.flush()
            * f.write: Write it only in the memory for performance thing 
            * f.flush Push the Memory into the file itself 
            * f.flush() forces Python to push everything in that buffer to the operating system.
        '''
        try:
            os.fsync(f.fileno())
            r'''
            * Even after flushing, the OS itself may still buffer the data before writing to the physical disk.
            * os.fsync(...) forces the OS to actually save it to disk immediately.
            * f.fileno() just gives the OS-level “file number” for the file f.
            '''
        except Exception:
            # Not critical if fsync isn't available or fails
            r'''
            * try/except block
            * Not all environments (or OS’s) support fsync.
            * If it fails, we just ignore the error (pass) because it’s not fatal — the file will still usually be saved eventually.
            '''
            pass
def close_writer(f):
    """Close the file handle (JSONL doesn't need array brackets)."""
    f.close()

# def start_csv_writer():
#     """Open a CSV for streaming writes during scraping."""
#     date_str = datetime.now().strftime("%Y-%m-%d")
#     filename = f"automation_{date_str}.csv"

#     csv_file = open(filename, "w", newline="", encoding="utf-8")
#     writer = csv.writer(csv_file)
#     writer.writerow(["Role of Job", "Company Name", "Company Location", "Type of Work", "Description"])
#     print(f"📁 Streaming results to: {filename}")

#     return csv_file, writer

r'''
From my Question in start_csv_writer why there are no "with" is because with is used 
to close the file after using it but right now in terms of web scrapping we keep it open
as we scrapping things 
'''


# def write_job(writer, csv_file, job_data):
#     """Write a single job row and flush immediately."""
#     writer.writerow(job_data)
#     csv_file.flush()  # 💾 force save to disk immediately



# def extraction_job_description(page,write_jsonl_record,jsonl_writer): 
# def extraction_job_description(page, f, writer):
def extraction_job_description(page, f):
    r'''
    * page → scrape from Playwright
    * f → the open file handle (from jsonl_writer())
    * writer → the save function (e.g., write_jsonl_record)
    '''
    r'''
    🔑 Why not jsonl_writer as an argument?
    Because jsonl_writer() is only called once at the start to open the file.
    You don’t need to pass the function around — just pass its result (f).
    '''
    try:
        locator = page.locator(".job-link.-no-underline.-desktop-only.show-job-description")
        count_job_post = locator.count()

        if count_job_post == 0:
            print("[WARNING] No job posts found on this page.")
            return

        indexes = list(range(count_job_post))
        random.shuffle(indexes)

        for i in indexes:
            try:
                time.sleep(random.uniform(0.8, 2.3))

                # Hover safely
                try:
                    locator.nth(i).hover(timeout=3000)
                except Exception as e:
                    print(f"[WARNING] Could not hover over job {i}: {e}")
                    continue

                time.sleep(random.uniform(0.2, 0.5))

                # Click safely
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
                # write_job(writer, csv_file, [roles_of_jobs, company_name, company_location, type_of_work, description_extraction])

                # This is where i needed to Write the Damn Thing:
                # return {
                #     "Role": roles_of_jobs,
                #     "Company": company_name,
                #     "Location": company_location,
                #     "Type": type_of_work,
                #     "Description": description_extraction,
                # }
                write_jsonl_record(f, {
                    "Role": roles_of_jobs,
                    "Company": company_name,
                    "Location": company_location,
                    "Type": type_of_work,
                    "Description": description_extraction,
                })
            except Exception as e:
                print(f"[ERROR] Skipping job {i} due to error: {e}")
                continue

    except Exception as e:
        print(f"[ERROR] extraction_job_description() failed: {e}")

software_names = [SoftwareName.CHROME.value, SoftwareName.FIREFOX.value]
operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]
fallback_ua_rotator = RandomUA(software_names=software_names,
                               operating_systems=operating_systems,
                               limit=100)
def get_user_agent():
    try:
        ua = UserAgent()
        return ua.random
    except Exception as e:
        print(f"[WARNING] fake_useragent failed: {e}")
        return fallback_ua_rotator.get_random_user_agent()
# def pagination(page, base_url, writer, csv_file):
def pagination(page, base_url, f):
    while True:
        # Wait for the current page to fully load jobs
        page.wait_for_load_state("networkidle")

        # ✅ Call your extraction here for the *current* page
        # basic_search_extraction(page)
        # extraction_job_description(page,writer)

        # ✅ Pass csv_file so flushing works
        # extraction_job_description(page, writer, csv_file)
        extraction_job_description(page, f)

        try:
            # Wait for the "next page" button
            page.wait_for_selector('.next-page-button', timeout=5000)
            button = page.locator('.next-page-button')

            # If no next page button exists
            if not button.is_visible():
                print("No next page found.")
                break

            # Get the link to the next page
            next_page = button.get_attribute('href')
            if not next_page:
                print("Next page button exists, but no href found.")
                break

            # Navigate to next page
            go_to_next_page = urljoin(base_url, next_page)
            print(f"Going to: {go_to_next_page}")
            page.goto(go_to_next_page, timeout=60000)
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

        except Exception as e:
            print(f"Error or no more pages: {e}")
            break
    
# def scrape_jora_title():
#     # csv_file, writer = start_csv_writer()  

#     f = jsonl_writer()   

#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)
#         ua_string = get_user_agent()
#         context = browser.new_context(
#             user_agent=ua_string,
#             viewport={"width": 1366, "height": 768}
#         )
#         page = context.new_page()

#         base_url = "https://ph.jora.com/"
#         # ✅ Your keyword list
#         keywords = [
#             # "Mechatronics",
#             # "Instrumentation Technician",
#             # "Instrumentation Engineer"
#             # "Robotics Engineer",
#             # "Control Systems Engineer", Due to 5,k Jobs i Stop this Midway I'm Going to Continue this later
#             # "Electromechanical Engineer", Not this Part more on Mechanical and electrical 
#             # "Process Control Engineer",
#             # "Industrial Automation Specialist",
#             # "Manufacturing Engineer (with automation focus)",
#            #  "Test & Commissioning Engineer",
#             # "Maintenance Engineer (industrial/mechanical/electrical)",
#             # "Embedded Systems Engineer",
#             # "Electrical Design Engineer", # I Stop Mid Here there are 2k Jobs are like this 
#            #  "Firmware Engineer (for industrial equipment)",
#             # "Field Service Engineer (automation/instrumentation equipment)",
#             "System Integration Engineer",
#             "Production Engineer", #  (automation-heavy industries)
#             # "Plant Engineer",
#             "SCADA Engineer",
#             "PLC Programmer",
#             "LabVIEW Developer",
#             "Process Instrumentation Specialist",
#             "Robotics Technician",
#             "Motion Control Engineer"
#         ]

        
#         for index, term in enumerate(keywords, start=1):
#             print(f"\n🔍 [{index}/{len(keywords)}] Searching for: {term}")

#             page.goto(base_url, timeout=60000)
#             page.fill('#q', term)
#             page.click('button.search-jobs-button')

#             pagination(page, base_url, writer, csv_file)

#             print(f"✅ Finished: {term}")
        
#         finally:
#             # tidy up resources even when interrupted
#             try:
#                 context.close()
#             except Exception:
#                 pass
#                 browser.close()
    

def scrape_jora_title():
    # open output once (JSONL recommended)
    f = jsonl_writer()   # returns file handle

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        try:
            ua_string = get_user_agent()
            context = browser.new_context(
                user_agent=ua_string,
                viewport={"width": 1366, "height": 768}
            )
            page = context.new_page()
            base_url = "https://ph.jora.com/"

            keywords = [
                # "System Integration Engineer",
                # "Production Engineer",
                "SCADA Engineer",
                "PLC Programmer",
                "LabVIEW Developer",
                "Process Instrumentation Specialist",
                "Robotics Technician",
                "Motion Control Engineer"
            ]

            for index, term in enumerate(keywords, start=1):
                print(f"\n🔍 [{index}/{len(keywords)}] Searching for: {term}")

                page.goto(base_url, timeout=60000)
                page.fill('#q', term)
                page.click('button.search-jobs-button')

                # wait for results to render — replace selector with a real one if needed
                try:
                    page.wait_for_selector(".job-listing, .search-results, .job-card", timeout=10000)
                except Exception:
                    # fallback: wait for DOM load, but prefer selector wait
                    page.wait_for_load_state("domcontentloaded")

                # pass the writer function and file handle to pagination so it can call writer(f, record)
                # pagination(page, base_url, write_jsonl_record, f)
                pagination(page, base_url, f)

                print(f"✅ Finished: {term}")

        finally:
            # tidy up resources even when interrupted
            try:
                context.close()
            except Exception:
                pass
            browser.close()
            close_writer(f)   # close the JSONL file

if __name__ == "__main__":
    scrape_jora_title()

