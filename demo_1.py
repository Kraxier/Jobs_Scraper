from playwright.sync_api import sync_playwright, Playwright
from urllib.parse import urljoin
import random
import time
from fake_useragent import UserAgent
from random_user_agent.user_agent import UserAgent as RandomUA
from random_user_agent.params import SoftwareName, OperatingSystem



def extraction_job_description(page):
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
        description_extraction = page.locator(".job-description-container").inner_text()
        print(description_extraction)
        print("################## Another Job Description #####################")
        print(f"{i}: {value}")

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


def pagination(page, base_url):
    while True:
        # Wait for the current page to fully load jobs
        page.wait_for_load_state("networkidle")

        # ✅ Call your extraction here for the *current* page
        basic_search_extraction(page)
        extraction_job_description(page)

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
        pagination(page, base_url) 



        input()
        browser.close()

if __name__ == "__main__":
    scrape_jora_title()


