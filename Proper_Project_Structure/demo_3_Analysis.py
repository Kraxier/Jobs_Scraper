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
                write_job(writer, csv_file, [roles_of_jobs, company_name, company_location, type_of_work, description_extraction])

            except Exception as e:
                print(f"[ERROR] Skipping job {i} due to error: {e}")
                continue
    # Top Level if the extraction of Job Description are Failed
    except Exception as e:
        print(f"[ERROR] extraction_job_description() failed: {e}") 