import csv
import random
import time
from datetime import datetime
from urllib.parse import urljoin
from playwright.sync_api import sync_playwright
from fake_useragent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem
from random_user_agent.user_agent import UserAgent as RandomUA



def start_csv_writer():
    """Open a CSV for streaming writes during scraping."""
    date_str = datetime.now().strftime("%Y-%m-%d")
    filename = f"automation_{date_str}.csv"

    csv_file = open(filename, "w", newline="", encoding="utf-8")
    writer = csv.writer(csv_file)
    writer.writerow(["Role of Job", "Company Name", "Company Location", "Type of Work", "Description"])
    print(f" Streaming results to: {filename}")

    return csv_file, writer


def write_job(writer, csv_file, job_data):
    """Write a single job row and flush immediately."""
    writer.writerow(job_data)
    csv_file.flush() 


def extraction_job_description(page, writer, csv_file): 
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


                try:
                    locator.nth(i).hover(timeout=3000)
                except Exception as e:
                    print(f"[WARNING] Could not hover over job {i}: {e}")
                    continue

                time.sleep(random.uniform(0.2, 0.5))

   
                try:
                    locator.nth(i).click(timeout=5000)
                except Exception as e:
                    print(f"[WARNING] Could not click job {i}: {e}")
                    continue

                try:
                    value = locator.nth(i).inner_text(timeout=5000)
                except Exception as e:
                    print(f"[WARNING] Could not get text for job {i}: {e}")
                    value = "Unknown"

         
                if not page.wait_for_selector(".job-description-container", state="visible", timeout=5000):
                    print(f"[WARNING] No job description loaded for job {i}")
                    continue

  
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

       
                write_job(writer, csv_file, [roles_of_jobs, company_name, company_location, type_of_work, description_extraction])

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
def pagination(page, base_url, writer, csv_file):
    while True:

        page.wait_for_load_state("networkidle")

        extraction_job_description(page, writer, csv_file)

        try:
            page.wait_for_selector('.next-page-button', timeout=5000)
            button = page.locator('.next-page-button')

    
            if not button.is_visible():
                print("No next page found.")
                break

            next_page = button.get_attribute('href')
            if not next_page:
                print("Next page button exists, but no href found.")
                break


            go_to_next_page = urljoin(base_url, next_page)
            print(f"Going to: {go_to_next_page}")
            page.goto(go_to_next_page, timeout=60000)
            try:
   
                close_button = page.locator("#suggest-better-alert-modal .dismiss")
                
                if close_button.is_visible(timeout=2000):  
                    close_button.click()
                    print("Closed popup")
                else:
                    print("Popup detected but close button not visible")
            except Exception as e:
                print(f"No popup detected or error closing popup: {e}")


        except Exception as e:
            print(f"Error or no more pages: {e}")
            break
    
def scrape_jora_title():
    csv_file, writer = start_csv_writer()  
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        ua_string = get_user_agent()
        context = browser.new_context(
            user_agent=ua_string,
            viewport={"width": 1366, "height": 768}
        )
        page = context.new_page()

        base_url = "https://ph.jora.com/"
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

        
        for index, term in enumerate(keywords, start=1):
            print(f"\n🔍 [{index}/{len(keywords)}] Searching for: {term}")

            page.goto(base_url, timeout=60000)
            page.fill('#q', term)
            page.click('button.search-jobs-button')

            pagination(page, base_url, writer, csv_file)

            print(f"✅ Finished: {term}")

        browser.close()
    csv_file.close()

if __name__ == "__main__":
    scrape_jora_title()
