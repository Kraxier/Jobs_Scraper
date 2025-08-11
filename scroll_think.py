from playwright.sync_api import sync_playwright, Playwright
from urllib.parse import urljoin
import random
import time
from fake_useragent import UserAgent
from random_user_agent.user_agent import UserAgent as RandomUA
from random_user_agent.params import SoftwareName, OperatingSystem






# Goal of the Code: 
r'''
I needed it to Scroll while also Clicking for each Job Post

Algorithmic Thinking 
    1. Click the Job Post 
        Click 
        Wait for the Element to Load
        


    2. Extract the Job Description for That Job Post 
    3. Click on another Job Post 
    4. Extract the Job Description 

Algorithmic Thinking in Code 
'''

r'''
Investigating why my nth(2) is the 2 in Job Post it should be 3 because of index base 
'''

def extraction_job_description(page):
    # Clicking the Damn Job Post
    # job-link -no-underline -desktop-only show-job-description
    # page.click(".job-link.-no-underline.-desktop-only.show-job-description") 
    # page.locator(".job-link.-no-underline.-desktop-only.show-job-description").nth(0).click()
    # page.locator(".job-link.-no-underline.-desktop-only.show-job-description").nth(1).click()
    # page.locator(".job-link.-no-underline.-desktop-only.show-job-description").nth(2).click() # What does it mean by nth

    # locator = page.locator(".job-link.-no-underline.-desktop-only.show-job-description")
    # count = locator.count()
    # print(f"Found {count} matching elements:")
    # for i in range(count):
    #     text = locator.nth(i).inner_text()
    #     print(f"{i}: {text!r}")  # !r shows quotes for clarity
    r'''
    This Code Generate the Number of the Things in there 
        0: 'Senior Test Automation Engineer - Makati'
        1: 'System (Automation) Engineer'
        2: 'Energy Management System Specialist'
        3: 'System (Automation) Engineer'
        4: 'Plant Engineer - Mechatronics'
        5: 'Automation Engineer'
        6: 'Application Automation Engineer'
        7: 'Automation & Digitalization Support Engineer'
        8: 'Automation Engineer (UiPath) - 6290'
        9: 'Automation Engineer'
        10: 'ELECTRICAL & CONTROL ENGINEER'
        11: 'Mechatronics'
        12: 'Energy Management System Specialist'
        13: 'Automation Assistant Engineer (ME, Mechatronics, Automation, EE, COE, ECE)'
        14: 'PLC Technician - Operations, Sorting Center, SPX Express (Calamba, Laguna)'
    '''
    # locator = page.locator(".job-link.-no-underline.-desktop-only.show-job-description")
    # count_job_post = locator.count()
    # page.locator(".job-link.-no-underline.-desktop-only.show-job-description").nth(4).click()
    # value = page.locator(".job-link.-no-underline.-desktop-only.show-job-description").nth(4).inner_text()
    # print(value)

    r'''
    Why is it Automatically Scroll ?
        1. Finds the element in the DOM.
        2. Scrolls it into view automatically (because you can’t click something outside the visible viewport).
        3. Moves the mouse (virtually) over it.
        4. Sends the click event.

    This auto-scrolling comes from Playwright’s click actionability checks:
        The element must be visible
        The element must not be covered by another element
        The element must be in the viewport (Playwright will scrollIntoView for you)
    '''
    # locator = page.locator(".job-link.-no-underline.-desktop-only.show-job-description")
    # count_job_post = locator.count()
    
    # for i in range(count_job_post):
    #     time.sleep(random.uniform(0.8, 2.3))  # random delay
    #     locator.nth(i).hover()  # optional, simulates moving mouse
    #     time.sleep(random.uniform(0.2, 0.5))
    #     locator.nth(i).click()
    #     value = locator.nth(i).inner_text()
    #     print(f"{i}: {value}")
    r'''
    It Solve Every Problem that i have I don't need to automatic Scrolling Things in term of this 
    Question: 
        If It can Solve many things 
    '''


    locator = page.locator(".job-link.-no-underline.-desktop-only.show-job-description")
    count_job_post = locator.count()

    indexes = list(range(count_job_post))
    random.shuffle(indexes)  # randomize the order
    # job-description-container
    

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


    # description_extraction = page.locator(".job-description-container p").inner_text()
    # print(description_extraction)

    # description_extraction = page.locator(".job-description-container").inner_text()
    # print(description_extraction)
    r'''
    Use .inner_text() on the parent container
        * This grabs all visible text inside .job-description-container at once.
        * The output will include all <p> text in reading order.
    '''

    # Understanding : indexes = list(range(count_job_post))
    r'''
    * If count_job_post is 5, this gives:
    * range(0, 5) → represents 0, 1, 2, 3, 4
    The Output of this is: indexes = [0, 1, 2, 3, 4]
    Why?
        Because we want a list of indexes that correspond to .nth(i) for your locator elements.
    '''

    # Understanding : random.shuffle(indexes) 
    r'''
    What is Random.Shuffle:
        random.shuffle(...) takes a list and rearranges its items in-place into a random order.
    indexes = [0, 1, 2, 3, 4]
    random.shuffle(indexes)
    print(indexes)  
    # might print: [3, 1, 4, 0, 2]
    '''

    # I have all things that i need in terms of Scrolling and Stuff that can Automatically Handle for me and i don't need to engineer tings 
    r'''
    I need to Just
        1. Click
        2. Wait for the Elements to Load 
        3. Extract the Job Description 
        4. Click Again 
        Rinse and Repeat 
    '''
    



# def extract_Job_Description_old(page):

#     scrolling_attempt_max = 15 
#     scrolling_attempt_page = 0 
#     # This Code is For the termination Part:
#     initial_counting_job = len(page.locator("a.job-link.-no-underline.-desktop-only.show-job-description").all()) 
#     scrolling_max_termination = 5
#     scrolling_fail_buffer = 0

#     while scrolling_attempt_max > scrolling_attempt_page:
  
        
#         # Job Post Cards      
#         cards = page.locator('a.job-link.-no-underline.-desktop-only.show-job-description')

#         count = cards.count()
#         print(f"How many Jobs are There: {count}")
#         for i in range(initial_counting_job):
#             cards.click()
#             print("cards get Clicked")
           
#         initial_height_page = page.evaluate("document.body.scrollHeight")
#         print(f'Intial Height of the Page{initial_height_page}')
#         scrolling_profiles = {
#             "scroll_magnitude":(200.0, 768.0), # Scroll Magnitude right to the max for range
#             "scroll_timing": (0.2, 1.5),
#             "scroll_think": (3.0, 8.0)
#         }
#         # Scrolling Method that are Based on Viewport Height
#         viewport_height = page.viewport_size["height"] 
#         min_px, max_px = scrolling_profiles["scroll_magnitude"]
#         scroll_amount_px = random.uniform(min_px, max_px)
#         max_scroll = viewport_height * 0.8
#         scroll_amount = min(scroll_amount_px, max_scroll)
#         page.mouse.wheel(0, scroll_amount)
#         # Time Delay for Every Scroll 
#         min_scroll_delay, max__scroll_delay = scrolling_profiles["scroll_timing"] # For Short Term Scrolling 
#         min_scroll_think, max_scroll_think = scrolling_profiles["scroll_think"] # For Longer Interval of Thinking 
#         time_delay = random.uniform(min_scroll_delay, max__scroll_delay)
#         print(f"Time Delay: {time_delay}secods")
#         time.sleep(time_delay)

#         if random.random() < 0.25:  # 25% chance
#             think_min, think_max = scrolling_profiles["scroll_think"]
#             time_delay_long = random.uniform(think_min, think_max)
#             print(f"Long Thinking Scrolling {time_delay_long}seconds")
#             time.sleep(time_delay_long)
#                 # time.sleep(random.uniform(think_min, think_max))

#             # ||||||||||| Scroll Amount Going up for 30% Chance |||||||||||
#         direction = 1  # Default down
#         if random.random() < 0.3:  # 30% chance to scroll up
#             direction = -1
#             print(f"Scrolling Up (30% Chance)")
#         scroll_amount *= direction
#         page.mouse.wheel(0, scroll_amount)

#         counting_job = len(page.locator("a.job-link.-no-underline.-desktop-only.show-job-description").all())
#         print(f"Counting How many Jobs: {counting_job}")
#          #||||||||||| Second Termination: Counting The Quotes ||||||||| 
#         if counting_job == initial_counting_job:
#             scrolling_fail_buffer += 1
#             # print(f"No new quotes found. Fail count: {scrolling_fail_buffer}")
#             if scrolling_fail_buffer == scrolling_max_termination:
#                 break
#         else:
#             scrolling_fail_buffer = 0
#             initial_counting_job = counting_job

#             # print(f"There are New Quotes Found so It will Reset to: {scrolling_fail_buffer}")
#             # print(f" New Number for the Comparison counting_quotes and initial_count_quotes not 10 anymore: {initial_count_quotes}")
        
#         r'''
#         Putting a "Why" instead of What is really a necessary thing in Doing things 
#         Second Termination is the Best Way 
#         '''
#         scrolling_attempt_page += 1 #
#         print(f"How many attempt currently  {scrolling_attempt_page}")
#         # In Attempt 10 is Enough for the Maximum Scroll of the Page


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


        extraction_job_description(page)


        input()
        browser.close()

if __name__ == "__main__":
    scrape_jora_title()


############### Website anti-bot signals ############### 

r'''
Some sites track:
    How fast you scroll/click
    Whether the click coordinates look human
    How long you spend reading before interacting
    If all clicks happen in one viewport session without hesitation
'''