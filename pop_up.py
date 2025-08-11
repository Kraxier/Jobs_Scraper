from playwright.sync_api import sync_playwright, Playwright
from urllib.parse import urljoin
import random
import time
from fake_useragent import UserAgent
from random_user_agent.user_agent import UserAgent as RandomUA
from random_user_agent.params import SoftwareName, OperatingSystem
import csv # Working CSV 




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
        description_extraction = page.locator(".job-description-container").inner_text()
        print(description_extraction)
        print("-" * 50)
 


def pagination(page, base_url):
    while True:
        page.wait_for_load_state("networkidle")
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
        # extraction_job_description(page)

        input()
        browser.close()

if __name__ == "__main__":
    scrape_jora_title()


r'''
<div class="modal-content"><form class="email-alert-form suggest-better-alert-form" id="suggest_better_alert_modal_new_email_alert" data-creation-method="suggest_better_alert_modal" action="/email_alerts" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="✓" autocomplete="off"><input type="hidden" name="authenticity_token" value="XWnkGam1JgdiiOKuS4vra8lthv73DmhLPqLwSxn0w_lcr7inN1n_2b31mSINikbA2vmoerVdgEgZqrNrbjSmZg" autocomplete="off"><div class="heading-with-icon"><svg class="icon icon-email" width="24" height="24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M3.87 5.5h16.26c.2 0 .37.168.37.382v12.236a.377.377 0 01-.37.382H3.87c-.2 0-.37-.168-.37-.382V5.882c0-.214.163-.382.37-.382z" stroke="#0e8136" stroke-miterlimit="10" stroke-linecap="round" stroke-linejoin="round"></path><path d="M3.5 5.775l8.5 7.647 8.5-7.647M9.45 11.128L3.5 16.481M20.5 16.481l-5.95-5.353" stroke="#0e8136" stroke-miterlimit="10" stroke-linecap="round" stroke-linejoin="round"></path></svg><h3 class="heading -size-xlarge -weight-700 -mb-0">Discover new jobs for this search</h3></div><p>Stay up to date with new jobs that match what you are looking for.</p><input autocomplete="off" type="hidden" name="email_alert[radius]" id="suggest_better_alert_modal_email_alert_radius"><input autocomplete="off" type="hidden" name="email_alert[job_type_id]" id="suggest_better_alert_modal_email_alert_job_type_id"><input autocomplete="off" type="hidden" name="email_alert[salary_min]" id="suggest_better_alert_modal_email_alert_salary_min"><input value="suggest_better_alert_modal" autocomplete="off" type="hidden" name="email_alert[creation_method]" id="suggest_better_alert_modal_email_alert_creation_method"><input value="desktop" autocomplete="off" type="hidden" name="email_alert[creation_device]" id="suggest_better_alert_modal_email_alert_creation_device"><input value="web" autocomplete="off" type="hidden" name="email_alert[creation_platform]" id="suggest_better_alert_modal_email_alert_creation_platform"><input value="true" autocomplete="off" type="hidden" name="email_alert[ignore_identical]" id="suggest_better_alert_modal_email_alert_ignore_identical"><div class="input-field -visible-label autocomplete-container keyword-input-field" data-controller="hubble--keyword-autocomplete" data-hubble--keyword-autocomplete-hubble--main-outlet="[data-controller='hubble--main']"><label for="suggest_better_alert_modal_email_alert_query">What</label><input type="search" maxlength="512" placeholder="Job title, company, keyword" icon="search" icon-position="right" data-url="/rpc/search_keywords/suggest" data-action="autocomplete-selectcomplete-&gt;hubble--keyword-autocomplete#track" size="512" value="Mechatronics" name="email_alert[query]" id="suggest_better_alert_modal_email_alert_query" autocomplete="off" aria-expanded="false" aria-owns="autocomplete_list_1" role="combobox"><ul hidden="" role="listbox" id="autocomplete_list_1"></ul><span class="visually-hidden" role="status" aria-live="assertive" aria-atomic="true">Begin typing for results.</span></div><div class="input-field -visible-label autocomplete-container -highlighted location-input-field"><label for="suggest_better_alert_modal_email_alert_raw_location">Where</label><input type="search" maxlength="64" placeholder="City, district, state" icon="location" icon-position="right" data-url="/rpc/search_locations/suggest" size="64" value="" name="email_alert[raw_location]" id="suggest_better_alert_modal_email_alert_raw_location" autocomplete="off" aria-expanded="false" aria-owns="autocomplete_list_2" role="combobox"><ul hidden="" role="listbox" id="autocomplete_list_2"></ul><span class="visually-hidden" role="status" aria-live="assertive" aria-atomic="true">No results found</span></div><div class="field-description -highlighted" icon="info" icon-size="small">Try to be as specific as you can with the location</div><div class="input-field -visible-label"><label for="suggest_better_alert_modal_email_alert_email">Email address</label><input placeholder="Enter your email" required="required" type="email" name="email_alert[email]" id="suggest_better_alert_modal_email_alert_email"></div><button type="submit" class="create-alert-button rounded-button -primary -size-lg -w-full" data-gtm="create-email-alert" data-ga4-on-click="true" data-ga4="{&quot;name&quot;:&quot;save_search__create&quot;,&quot;params&quot;:{&quot;trigger_source&quot;:&quot;serp&quot;,&quot;user_id&quot;:null,&quot;site_id&quot;:&quot;ph&quot;}}"><span class="content">Notify me with similar jobs</span></button><div class="privacy-statement font-xxsmall "><span class="branded-links">By creating an email alert, I agree to Jora's <a href="/cms/terms-of-service">Terms</a> and <a href="/cms/privacy">Privacy Policy</a> and can unsubscribe anytime. If I'm below legal age requirements, I have parental consent for Jora to process my data.</span></div></form></div>
'''