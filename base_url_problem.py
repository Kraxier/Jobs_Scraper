from playwright.sync_api import sync_playwright, Playwright
from urllib.parse import urljoin
import random
import time
from fake_useragent import UserAgent
from random_user_agent.user_agent import UserAgent as RandomUA
from random_user_agent.params import SoftwareName, OperatingSystem
import csv # Working CSV 


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

        
        print("-" * 10)
        description_extraction = page.locator(".job-description-container").inner_text().lower()
        print(description_extraction)
        print("-" * 50)


        writer.writerow([roles_of_jobs, company_name, company_location, type_of_work, description_extraction])

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

def auto_search(page):
    r'''
    <input data-action="autocomplete-selectcomplete-&gt;hubble--keyword-autocomplete#track" data-url="/rpc/search_keywords/suggest" icon="search" icon-position="right" id="q" maxlength="512" name="q" placeholder="Job title, company, keyword" type="search" value="" autocomplete="off" aria-expanded="false" aria-owns="autocomplete_list_1" role="combobox">
    <button type="submit" class="search-jobs-button rounded-button -primary -size-lg -w-full"><span class="content">Search jobs</span></button>
    '''
    keywords = [
    "Mechatronics",
    "Robotics Engineer",
    "Control Systems Engineer",
    "Electromechanical Engineer",
    "Process Control Engineer",
    "Industrial Automation Specialist",
    "Manufacturing Engineer (with automation focus)",
    "Test & Commissioning Engineer",
    "Maintenance Engineer (industrial/mechanical/electrical)",
    "Embedded Systems Engineer",
    "Electrical Design Engineer",
    "Firmware Engineer (for industrial equipment)",
    "Field Service Engineer (automation/instrumentation equipment)",
    "System Integration Engineer",
    "Production Engineer (automation-heavy industries)",
    "Plant Engineer",
    "SCADA Engineer",
    "PLC Programmer",
    "Instrumentation Technician",
    "LabVIEW Developer",
    "Process Instrumentation Specialist",
    "Robotics Technician",
    "Motion Control Engineer"
    ]
    for term in keywords:
        page.fill('#q', term)
        page.click('button.search-jobs-button')
        page.wait_for_selector('.job-result-item')

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
        base_url = "https://ph.jora.com/"
        keywords = [
        "Mechatronics",
        "Robotics Engineer",
        "Control Systems Engineer",
        "Electromechanical Engineer",
        "Process Control Engineer",
        "Industrial Automation Specialist",
        "Manufacturing Engineer (with automation focus)",
        "Test & Commissioning Engineer",
        "Maintenance Engineer (industrial/mechanical/electrical)",
        "Embedded Systems Engineer",
        "Electrical Design Engineer",
        "Firmware Engineer (for industrial equipment)",
        "Field Service Engineer (automation/instrumentation equipment)",
        "System Integration Engineer",
        "Production Engineer (automation-heavy industries)",
        "Plant Engineer",
        "SCADA Engineer",
        "PLC Programmer",
        "Instrumentation Technician",
        "LabVIEW Developer",
        "Process Instrumentation Specialist",
        "Robotics Technician",
        "Motion Control Engineer"
        ]
        for term in keywords:
            print(f"Searching for: {term}")
            page.goto(base_url, timeout=60000)  # always start fresh
            page.fill('#q', term)
            page.click('button.search-jobs-button')
            page.wait_for_selector('.job-result-item')
            pagination(page, base_url, writer) 
        # extraction_job_description(page)

        
        browser.close()
    csv_file.close()  # close after done



if __name__ == "__main__":
    scrape_jora_title()


r'''
Problem where the fuck should i put the autosearch thing in  my code? 
the base url will be: 
    https://ph.jora.com/

i needed it to go back to base url and do the autosearch thing 
i should put autosearch at the beginning part because i'm starting in the baseurl:

in terms of Pagination thing after reaching the last page in mechatronics it will automatically go back to autosearch for the next thing 

Where i should put the thing in there ? 
'''