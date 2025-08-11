from playwright.sync_api import sync_playwright, Playwright
from urllib.parse import urljoin
import random
import time
from fake_useragent import UserAgent
from random_user_agent.user_agent import UserAgent as RandomUA
from random_user_agent.params import SoftwareName, OperatingSystem
import csv # Working CSV 

r'''
Problem 
    I have 2 Way of Extracting a Website 
        1. Overview of a Job Post 
            * Role 
            * Company 
            * Short Description of the Job 
        2. A Full Stack of Job Post 
            * I can Scrape the Description 
Based on the csv File i needed to somehow fix this part
    1. Problem is the Randomization of the Full Stack Thing
    2. How i can Connect the 2? 
    3. Should i even Connect the 2? 

Should i Seperate the 2? 
    1. Because in Terms of Saving the File
    2. Maybe that a lot of Work at Cleaning so i should not seperate it 

Solution:
    1. In term of the Overview and Full Stack Post 
        * I Should Scrape the Role, Company and Connect the 2 of those in a 1 CSV files
        * I Should Create a Demo in Terms of Just Scrapping the  Full Stack thing because that is the most critical thing i should focus on 

Full Stack of Job Post Scrape the:
    Role: job-title heading -size-xxlarge -weight-700
    Company: class="company"
    Location: 
        <span class="location">Makati City, Metro Manila</span>
    Type of Work:
        <div class="content">Hybrid</div>
'''



# Creating CSV files for this 
def saving_csv_understanding():
    csv_file = open("data_1.csv", "w", newline="", encoding="utf-8")
    ############# Concept of the Line of Code ##############
    # "data.csv" → The file name you’re creating (or overwriting if it already exists).
    # "w" → Write mode. This means
        # If the file exists → It will be overwritten.
        # If it doesn’t exist → It will be created.
    # newline="" → Prevents Python from adding extra blank lines between rows in Windows. 
        # Without it, you might get a weird double-line spacing in your CSV.
    # encoding="utf-8" → Ensures the file can store special characters (e.g., accents, emojis) without corruption.
    writer = csv.writer(csv_file)
    ############# Concept of the Line of Code ##############
    # csv.writer() → Creates a writer object that knows how to turn Python lists
        # (e.g., ["Title", "Price"]) into properly formatted CSV rows.
    # This writer is tied to csv_file, so every writer.writerow() call writes directly to that file.
    r'''
    writer.writerow(["Column1", "Column2", "Column3"])
    '''
    writer.writerow(["Column1", "Column2", "Column3"])
    r'''
    Code for CSV Files:
    csv_file = open("job_data_1.csv", "w", newline="", encoding="utf-8")
    writer = csv.writer(csv_file)
    writer.writerow(["Role of Job", "Company Name", "Company Location", "Type of Work", "Description"])
    '''
    ############# Concept of the Line of Code ##############
    # writer.writerow() → Writes one row to the CSV file.
    # Here, we’re writing the headers — the column names that appear at the top of the CSV.

def saving_csv():
    csv_file = open("data_1.csv", "w", newline="", encoding="utf-8")
    writer = csv.writer(csv_file)
    writer.writerow(["Role of Job", "Company Name", "Company Location", "Type of Work", "Description"])
    return csv_file, writer  # return so other functions can use them,  Return both the csv_file and writer so other functions can use them:


def extraction_job_description(page, writer):
    locator = page.locator(".job-link.-no-underline.-desktop-only.show-job-description")
    count_job_post = locator.count()
    indexes = list(range(count_job_post))
    random.shuffle(indexes) 


    for i in indexes:
        time.sleep(random.uniform(0.8, 2.3))
        locator.nth(i).hover()
        time.sleep(random.uniform(0.2, 0.5))
        locator.nth(i).click()
        value = locator.nth(i).inner_text()
        page.wait_for_selector(".job-description-container", state="visible")
        print(f"{i}: {value}")
        roles_of_jobs = page.locator('.job-title.heading.-size-xxlarge.-weight-700').inner_text()
        company_name = page.locator('.company').inner_text()
        company_location = page.locator('.location').inner_text()
        type_of_work = page.locator('.badge.-work-arrangement-badge .content').first.inner_text()
        print(f"Role of the Job: {roles_of_jobs}")
        print(f"Company Name: {company_name}")
        print(f"Company Location: {company_location}")
        print(f"Type of Work(Full Time, Hybrid, PartTime): {type_of_work}")
        
        # elements = page.locator('.badge.-work-arrangement-badge .content')
        # for i in range(elements.count()):
        #     print(elements.nth(i).inner_text())

        
        print("-" * 10)
        description_extraction = page.locator(".job-description-container").inner_text().lower()
        print(description_extraction)
        print("-" * 50)
        # print(f"{i}: {value}")

        writer.writerow([roles_of_jobs, company_name, company_location, type_of_work, description_extraction])
        r'''
        writer.writerow(["roles_of_jobs", "company_name", "company_location", "type_of_work", "description_extraction"])
        '''

def basic_search_extraction(page):
    roles_of_jobs = page.locator('a.job-link.-no-underline.-desktop-only.show-job-description').all_text_contents()
    company_names = page.locator('.job-company').all_text_contents()
    company_locations = page.locator('.job-location.clickable-link').all_text_contents()

    description_blocks = page.locator('.job-abstract')
    all_descriptions = []
    for i in range(description_blocks.count()):
        lis = description_blocks.nth(i).locator('li').all_text_contents()
        all_descriptions.append(lis)  

    for role, company, location, descriptions in zip(roles_of_jobs, company_names, company_locations, all_descriptions):
        print(f"Role: {role}")
        print(f"Company: {company}")
        print(f"Location: {location}")
        print("Description:")
        for desc in descriptions:
            print(f"  - {desc}")
        print("-" * 50)


def pagination(page, base_url, writer):
    while True:
        # Wait for the current page to fully load jobs
        page.wait_for_load_state("networkidle")

        # ✅ Call your extraction here for the *current* page
        # basic_search_extraction(page)
        extraction_job_description(page,writer)

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

def scrape_jora_title():
    csv_file, writer = saving_csv()  # create CSV here
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        ua_string = get_user_agent()
        context = browser.new_context(
            user_agent=ua_string, 
            viewport={"width": 1366, "height": 768}   
            )
        page = browser.new_page()
        base_url = "https://ph.jora.com/j?sp=homepage&trigger_source=homepage&q=Mechatronics&l="
        page.goto(base_url, timeout=60000)
        pagination(page, base_url, writer) 
        # extraction_job_description(page)

        input()
        browser.close()
    csv_file.close()  # close after done

if __name__ == "__main__":
    scrape_jora_title()


