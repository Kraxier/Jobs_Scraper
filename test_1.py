
# Website i can Try: https://ph.jora.com/ 
# git rm -r --cached job_venv
#  .\job_venv\Scripts\activate
from playwright.sync_api import sync_playwright, Playwright
from urllib.parse import urljoin
import random
import time
from fake_useragent import UserAgent # Installing the pip install fake-useragent

# Fall Back System if fake_useragent didn't work
from random_user_agent.user_agent import UserAgent as RandomUA
from random_user_agent.params import SoftwareName, OperatingSystem
# pip install fake-useragent random-user-agent


def basic_search_extraction(page):
    # # Testing my Skill in CSS and Xpath Stuff 
    # page.wait_for_selector('a.job-link.-no-underline.-desktop-only.show-job-description')
    # # role_of_job = page.locator('a.job-link.-no-underline.-desktop-only.show-job-description').first.text_content()
    # # print(role_of_job)
    # # role_of_job = page.locator('a.job-link.-no-underline.-desktop-only.show-job-description').text_content()
    # roles_of_job = page.locator('a.job-link.-no-underline.-desktop-only.show-job-description').all_text_contents()
    # # for role in roles_of_job:
    # #     print(role)

    # # Practise Extracting Content on my Own Extracting the Name of a Company and Location 
    # company_name = page.locator('.job-company').first.text_content() # job-company
    # company_location = page.locator('.job-location.clickable-link').first.text_content() # job-location clickable-link
    # print(company_name)
    # print(company_location)

    # # A New Challenge: 
    # # company_description = page.locator('.job-abstract') # Which is the Parent Container for the Short Description of a Job
    # company_descriptions = page.locator('.job-abstract li').all_text_contents() # It Only Require Space to Move from the HTML Parent to a Child 
    # for company_description in company_descriptions:
    #     print(company_description.strip()) 
    #     print()
    #     # This Work Perfectly Fine in terms of Locating Things but the problem is Organizing per Each of things like a block of Information
    #     r'''
    #     The Output that i want is:
    #     Role_of_job
    #     Company_name
    #     Company_Location
    #     company_description 
    #     Rinse and Repeat in terms of Printing 

    #     But it Get Everything because of ".all_text_contents()"
    #     But i think i can work with it 

    #     '''
    roles_of_jobs = page.locator('a.job-link.-no-underline.-desktop-only.show-job-description').all_text_contents()
    company_names = page.locator('.job-company').all_text_contents()
    company_locations = page.locator('.job-location.clickable-link').all_text_contents()

    # First, get all job description containers
    description_blocks = page.locator('.job-abstract')

    all_descriptions = []
    for i in range(description_blocks.count()):
        # Find <li> items inside this specific job-abstract block
        lis = description_blocks.nth(i).locator('li').all_text_contents()
        all_descriptions.append(lis)  # list of bullet points for this job

    # Now zip all together
    for role, company, location, descriptions in zip(roles_of_jobs, company_names, company_locations, all_descriptions):
        print(f"Role: {role}")
        print(f"Company: {company}")
        print(f"Location: {location}")
        print("Description:")
        for desc in descriptions:
            print(f"  - {desc}")
        print("-" * 50)


    
    # Working Perfectly 
    # Analyzing 
    r'''
    Locating the Elements ican Defintely Do it 
    Analyzing the Description Part 
    And Analyzing the For Loops for Each of it 

    all_text_contents() Get all the Possible Data or return a list 
    for variable in zip()

    What is Zip? 
    Using zip() to iterate through lists together instead of For loops
    zip() will take one element from each list at the same index and return them as a tuple.
    All lists must be aligned — if the number of elements is different, zip() stops at the shortest list.
    '''

    ###################### Analyzing the Description Part ##################
    r'''
    1. description_blocks = page.locator('.job-abstract')
        * This creates a locator that targets all .job-abstract containers —
            one per job listing.
    2. for i in range(description_blocks.count()):
        This loop runs once for each job listing, using i as the index.
        We’re basically saying:
        “Look at the 1st .job-abstract container… now the 2nd… now the 3rd…”
    3. description_blocks.nth(i)
        .nth(i) selects only the i-th job description container.
        Example:
            nth(0) = first job’s .job-abstract
            nth(1) = second job’s .job-abstract
            and so on.
    4. .locator('li')
        Here’s the magic:
        Instead of searching the whole page for <li>,
        we’re searching inside only that job’s container.

        So you only get bullet points for the job you’re currently looping over.
    5. .all_text_contents()
        This gives you a list of strings, one for each <li>.
        Example:
            [
                "Bachelor's in Computer Science or related field required",
                "5+ years experience in software development or test automation",
                "Proficiency in Java, JavaScript, PL/SQL, and test automation tools"
            ]
    6. all_descriptions.append(lis)
        We add this list of bullet points to our all_descriptions list.
        That means all_descriptions becomes a list of lists:
            [
                ["Bullet1_job1", "Bullet2_job1", "Bullet3_job1"],
                ["Bullet1_job2", "Bullet2_job2"],
                ["Bullet1_job3", "Bullet2_job3", "Bullet3_job3", "Bullet4_job3"]
            ]
        Each sublist matches the job in the same index position in roles_of_jobs, company_names, etc.

    ✅ Why it works perfectly:
    You scoped your <li> search to each .job-abstract container instead of doing a global search — so each job’s bullets stay linked to that specific jo
    '''

    ##################### In CSS Selector: ###################
    # “Find a descendant of this element (at any depth, not just direct child).
    # In term of Space for example .job-abstract li
    r'''
    Start at any element with the class .job-abstract
    Find all <li> tags anywhere inside it (children, grandchildren, etc.)
    '''
    # Direct child vs descendant
    # If you only want direct children (no grandchildren), you’d use the > combinator:
    # .job-abstract > li # This means “li elements that are immediate children of .job-abstract”.
    # .job-abstract li → works (because <li> are descendants)
    r'''
    .job-abstract > li → does not match (because <li> are not direct children; <ul> is in between)
    '''
# Pagination for myself 
# def pagination(page, base_url):
#     while True:
#         page.wait_for_selector('.next-page-button', timeout=5000) # Wait for the Selector
#         next_page = page.locator('.next-page-button').get_attribute('href')
#         print(next_page)
#         go_to_next_page = urljoin(base_url, next_page)
#         page.goto(go_to_next_page)
#         if not next_page:
#             print("No next page found")
#             return
    # Creating Condition for Stopping the Pagination 
        # We Coudn't Find any Stuff 
        # Next Page is gone
def pagination(page, base_url):
    page.wait_for_load_state("networkidle") 
    while True:
        try:
            page.wait_for_selector('.next-page-button', timeout=5000) 
            button = page.locator('.next-page-button')
            if not button.count():
                print("No next page found.")
                break

            next_page = button.get_attribute('href')
            if not next_page:
                print("Next page button exists, but no href found.")
                break

            go_to_next_page = urljoin(base_url, next_page)
            print(f"Going to: {go_to_next_page}")
            page.goto(go_to_next_page)

        except Exception as e:
            print(f"Error or no more pages: {e}")
            break
 
# Next Goal is the Anti Blocking Toolkit i needed to Implement


def extract_Job_Description(page):
    # Build a Clicking Thing in my Project that click a Job Post 
    # Build a Human Mimicing Behavior for Scrolling
    
    # cards = page.locator('div.job-card.result.sponsored-job.premium-job.spon-top')
    # count = cards.count()
    # print(count)
    # for i in range(count):
    #     cards.nth(i).click()
    #     print(f"Clicking the Job {i}")

    # What is i need in term of Scrolling?
    r'''
    1. Viewport (Done)
    2. Scrolling Profile for the Properties of Scrolling (Done)
    3. Scrolling (Done)
    4. Delaying the Scroll (Done)
    5. Initial 25% of going up (Done)
    6. Termination Program (Done)
    7. Looping Things (Done)
    8. Clicking and Scrapping Things right now 
    '''
    scrolling_attempt_max = 15 
    scrolling_attempt_page = 0 
    # This Code is For the termination Part:
    initial_counting_job = len(page.locator("a.job-link.-no-underline.-desktop-only.show-job-description").all()) 
    scrolling_max_termination = 5
    scrolling_fail_buffer = 0

    while scrolling_attempt_max > scrolling_attempt_page:
        initial_height_page = page.evaluate("document.body.scrollHeight")
        print(f'Intial Height of the Page{initial_height_page}')
        scrolling_profiles = {
            "scroll_magnitude":(200.0, 768.0), # Scroll Magnitude right to the max for range
            "scroll_timing": (0.2, 1.5),
            "scroll_think": (3.0, 8.0)
        }
        # Scrolling Method that are Based on Viewport Height
        viewport_height = page.viewport_size["height"] 
        min_px, max_px = scrolling_profiles["scroll_magnitude"]
        scroll_amount_px = random.uniform(min_px, max_px)
        max_scroll = viewport_height * 0.8
        scroll_amount = min(scroll_amount_px, max_scroll)
        page.mouse.wheel(0, scroll_amount)
        # Time Delay for Every Scroll 
        min_scroll_delay, max__scroll_delay = scrolling_profiles["scroll_timing"] # For Short Term Scrolling 
        min_scroll_think, max_scroll_think = scrolling_profiles["scroll_think"] # For Longer Interval of Thinking 
        time_delay = random.uniform(min_scroll_delay, max__scroll_delay)
        print(f"Time Delay: {time_delay}secods")
        time.sleep(time_delay)

        if random.random() < 0.25:  # 25% chance
            think_min, think_max = scrolling_profiles["scroll_think"]
            time_delay_long = random.uniform(think_min, think_max)
            print(f"Long Thinking Scrolling {time_delay_long}seconds")
            time.sleep(time_delay_long)
                # time.sleep(random.uniform(think_min, think_max))

            # ||||||||||| Scroll Amount Going up for 30% Chance |||||||||||
        direction = 1  # Default down
        if random.random() < 0.3:  # 30% chance to scroll up
            direction = -1
            print(f"Scrolling Up (30% Chance)")
        scroll_amount *= direction
        page.mouse.wheel(0, scroll_amount)

        counting_job = len(page.locator("a.job-link.-no-underline.-desktop-only.show-job-description").all())
        print(f"Counting How many Jobs: {counting_job}")
         #||||||||||| Second Termination: Counting The Quotes ||||||||| 
        if counting_job == initial_counting_job:
            scrolling_fail_buffer += 1
            # print(f"No new quotes found. Fail count: {scrolling_fail_buffer}")
            if scrolling_fail_buffer == scrolling_max_termination:
                break
        else:
            scrolling_fail_buffer = 0
            initial_counting_job = counting_job

            # print(f"There are New Quotes Found so It will Reset to: {scrolling_fail_buffer}")
            # print(f" New Number for the Comparison counting_quotes and initial_count_quotes not 10 anymore: {initial_count_quotes}")
        
        r'''
        Putting a "Why" instead of What is really a necessary thing in Doing things 
        Second Termination is the Best Way 
        '''
        scrolling_attempt_page += 1 #
        print(f"How many attempt currently  {scrolling_attempt_page}")
        # In Attempt 10 is Enough for the Maximum Scroll of the Page
r'''
Reflection in Clicking:

viewport can matter when clicking
Automatically scroll the element into view before clicking.
Wait for it to be visible and enabled before clicking.

Scrolling is the next Step i should do 
'''

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
    

def extract_job_description():
    # page.wait_for_selector(".quote", state="attached")
    # description = page.locator(".quote .text").all()
    # Extracting the Side Part 
    pass

def scrape_jora_title():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        ua_string = get_user_agent()
        # print(f"[INFO] Using UA: {ua_string}")
        context = browser.new_context(
            user_agent=ua_string, # Implementing User Agent thing
            viewport={"width": 1366, "height": 768}   # Changing Viewport thing for the Scrolling part 
            ) 
        page = browser.new_page()
        base_url = "https://ph.jora.com/j?sp=homepage&trigger_source=homepage&q=Mechatronics&l="
        page.goto(base_url, timeout=60000)
        extract_Job_Description(page)

        # basic_search_extraction(page)
        # Extract the title tag content
        # page_title = page.title()
        # print("Page Title:", page_title)
        # pagination(page, base_url) # This is Working Perfectly
        input()
        browser.close()

if __name__ == "__main__":
    scrape_jora_title()

# Finally it's working 




############ Reflection ##################
r'''
In Terms of Extracting Things:
1. My Skills in CSS Selector Ignoring the Xpath(Advance Cases) i completely Forgot how to Extract Content 
2. In terms of ".first.text_content()" i use this line of code after the page.locator 
3. My Debugging Skills Needed to Work like i had no idea that it's working but i got lazy in terms of Reading it 

Problem:
role_of_job = page.locator('a.job-link.-no-underline.-desktop-only.show-job-description').text_content()
# Problem of the Code is it Matches 15 other Things which is the Complete Stuff in the First Pagination 
# Identifying Why is it 15 Matches Element Reading the Terminal
    i think i Figure it out:
    playwright._impl._errors.Error: Locator.text_content: Error: strict mode violation: locator("a.job-link.-no-underline.-desktop-only.show-job-description") resolved to 15 elements:

    also Adding the 
    10) <a data-rank="8" target="_blank" rel="nofollow noopener" class="job-link -no-underline -desktop-only show-job-description"
    1-10 even though it is 15

Question:

    1. In terms of BS4: Every Request i can be Detected but in terms of Playwright does page.locator can detect me 
    Answer is:
'''

##### Understanding the BS4 and Playwright In term of Detection

# BS4:
r'''
BS4 making a raw HTTP Request which site can easily detect you 
    No Javascript Execution
    No Cookes/Sessions
    HTTP Headers are Bot 
'''

# Playwright:
r'''
It Run on Full Browser
Execute Javascript like a real User 
Send Normal Browser Header and Cookies 
Behave much closer to human 

It can Detect you if 
You use the default Playwright browser without tweaks (some JS checks can detect “headless” mode).
You run too fast or scrape too many pages without pauses.
You don’t interact in a human-like way (no scrolling, instant clicks, etc.).

I plan on Doing Just Locate all the Elements and move to the next page HAHHAHA 

'''

# In terms of Extracting Components in CSS Selectors i notice i will quite use .class always but i think there are more ways to do this stuff
# 
# 

################################# Concept for User Agent ########################################

# 2 Types of User Agent
# 1. fake_useragent	 	Fetches latest UAs online, It need to Internet, can Break if the Site is Down, But give you Fresh List 
# 2. random_user_agent Use 	Uses static internal UA list, No need for Internet but great at Fallback System

# random_user_agent
# from random_user_agent.user_agent import UserAgent as RandomUA
# from random_user_agent.params import SoftwareName, OperatingSystem
#  pip install fake-useragent random-user-agent

# fake_useragent
# from fake_useragent import UserAgent
# pip install fake-useragent

r'''
fake-useragent → Primary source of fresh UAs (updates online).
random-user-agent → Fallback with local UA database (no network needed).
'''

########################################## Concept of Delays in Playwright vs BS4 #############################S
# Delays in BS4/Request
r'''
Avoid rate limiting, respect robots.txt, prevent IP ban
Solution: Fixed or random sleep between requests (e.g.,time.sleep(random.uniform(1, 3)))
Server sees an IP making 100 GET request in 10 Seconds
'''
# Delays in Playwright Means:
r'''
Look human, avoid bot detection, give JS time to load content
Server sees: browser making clicks, scrolling, navigating pages → looks more human if done right.
Solution for this is: Random pauses, scrolling, typing delays, realistic click timing
'''
# Conclusions:
r'''
Playwright delays → about mimicking human interaction + letting JavaScript-rendered content load.
BS4 delays → about pacing HTTP requests so you don’t trip anti-scraping measures.
'''
# Reflection and Connection for my Project
r'''
Based on the Information if i want to do Mimicking Human Interaction the goal of that is to let the 
javascript rendered but what if the data that i want is already at place and i don't need a interaction
should i still add the delay thing because in my case i don't need to do "Scrolling" and go to the next page after locating 
the things that i want? 
'''
r'''
Chatgpt Answer to my Question:
If Data is Fully present when the page load is i don't need to do human interaction behaviour
i just need to wait the elements and then scrape it

When to do Human Interaction
    1. Content is load as you interact with it 
    2. The Site has behavioural bot Detection that monitor mouse movement, Timing 
    3. Trying to avoid Suspicion on a heavily protected site 

Just do this 
    1. Navigate to the page 
    2. Wait until the content is in the DOM 
    3. Scrape Immediately 
'''