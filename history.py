
# History or Timeline of What I currently Gonna do In "Project_Job_PH"
# Website i can Try: https://ph.jora.com/ 
# git rm -r --cached job_venv
#  .\job_venv\Scripts\activate

# Timeline/History:


# August 16 
r'''
Targeted Things i needed to do:
    1. Let the Scrapper Run While Studying how to Extract the Skills
    2. Study the Extraction part 

Welp I needed to Study spaCy and i learning some of the concepts here and there 
And i also need to study or Relearn the Pandas and Combining them Both which is think is necessary to extract some of the files


'''

# August 15:
r'''
Forgotten to Write in August 14 but in terms of August 15:
I just learned the Try and Except in python 


'''
# Reflection for the Project (August 15)
r'''
July 29 Started so it's been 2 Weeks since i Started 

i can Scrape the Jobs and do the Web Scrapping Thing which is the main goal for the project is to Demonstrate my skills 
The Next Thing is Something like an Additional in terms of the Project is which for Data Engineering 
    I needed to Extract Properly the Keywords in terms of Skills 
    I also need to Clean it While Doing it 
The Last Part is Data Analysis: 
    Where i will Show the Output of the Work that i do

In Terms of Skills:
    1. Improve the Investigation of the Website i needed a Workflow for that 
    2. Deciding What tool i needed to use either Playwright or BS4 
    3. Lacking in Developer Tools i needed a plan to quite master that stuff 
    4. Clearly Defining the Project Scope of Things
    5. Learning more about the Project Structure of the Code
    6. What will be The Public and Private in terms of my Coding because i'm so Transparent at Things 
    7. Creating a Demo or a Prototype in the Project 
        Defining the Critical of What is really needed 
            Examples:
                1. Scrapping the Single Page 
                2. Scrapping in terms of Multiple Pages
                3. Proper Set up for CSV files 
                4. Human Interaction Things 
    Needed a System for These 

    Starting a Project 
        * Clearly Defining the Scope of the Project 
        * Setting up the Project 
            * Installing Things BS4, Request, Playwright, Scrapy, Pandas
            * Setting Up the Project Structure: 
                * README.md → The first thing a client sees. It sells the project and tells them exactly how to use it.
                * requirements.txt → Makes it easy to install dependencies with pip install -r requirements.txt.
                * config.py → Keeps URLs, credentials, and constants separate from code so they can be changed without editing core scripts.
                * main.py → A single, simple entry point to run the scraper.
                * scraper/ → Keeps scraping logic modular and organized by responsibility.
                * data/ → Shows you actually produce something useful, not just run code.
                * logs/ → Professional touch that shows you thought about monitoring/debugging.
                * tests/ → Tells clients your scraper isn’t brittle and you care about quality.
        * Web Scrapping Skills:
            * Investigation of Website:
                A. Reading or Automating the Robot.txt
                B. Reading the Terms of the Website
                C. Finding API if there are an API
                D. Finding the Security of the Website:
            * Writing the Pseudocode:
            * CSS Selector and Xpath Selector 
            *
        
'''

# Beginner to Intermediate Layer of Skills:

r'''
1. Website Investigation & Compliance (what you already have)
robots.txt & Terms of Service — know what’s legally/ethically allowed
Security analysis — is there login required, hidden APIs, CAPTCHAs?
JavaScript rendering detection — inspect network requests, look for “XHR” calls, check if HTML is empty without JS
Anti-bot protection detection — Cloudflare, rate limits, honeypot fields


2. Locating & Targeting Data (what you already have)
CSS selectors — classes, IDs, attribute selectors
XPath selectors — absolute vs relative paths, advanced filters
Understanding HTML structure — nesting, sibling relationships, hidden elements
Identifying reusable patterns — pagination buttons, “next” links, repeating divs

3. Extraction Methods (how to actually get the data)
Static HTML scraping — using requests + BeautifulSoup or similar
Dynamic JS scraping — using Selenium, Playwright, or Puppeteer
Direct API calls — sometimes the site’s frontend fetches JSON you can use directly
Handling authentication — cookies, session tokens, headers

4. Data Cleaning & Processing
Removing HTML tags, extra spaces, or encoding issues
Normalizing formats (dates, prices, currencies)
Handling missing or malformed data
Converting extracted lists/tables into structured formats (pandas DataFrames)

5. Data Storage
Local files — CSV, JSON, Excel
Databases — SQLite, PostgreSQL, MongoDB for larger projects
Understanding basic CRUD (Create, Read, Update, Delete) in storage

6. Automation & Scalability
Loops & pagination — scraping many pages
Rate limiting — time.sleep() or async queues to avoid bans
Retry logic — handling failed requests gracefully
Scheduled runs — using cron, Windows Task Scheduler, or cloud functions

7. Anti-Detection Techniques (when allowed)
Rotating user agents
Proxies / VPNs
Headless browsing detection bypass
Randomized timing between requests

8. Debugging & Troubleshooting
Interpreting HTTP status codes (200, 403, 404, 429…)
Capturing and replaying network requests
Logging errors & partial data saves

9. Documentation & Maintenance
Writing clear code comments
Keeping track of changes in the target site’s structure
Making your scraper easy to update if selectors break
'''

# Data Life Cycle or The Pyramid Thing:

r'''
Data Generation / Collection
Where it starts: Sensors, user interactions, transactions, web scraping, APIs, logs, etc.
In web scraping: your scraper outputs raw HTML or JSON.
Main concerns: completeness, reliability, and legal/ethical compliance.

2. Data Ingestion
Getting data into your system:
Batch ingestion → loading files at intervals
Streaming ingestion → capturing data in real time
Tools: Apache Kafka, AWS Kinesis, or just Python scripts + databases for small projects.

3. Data Storage
Where you put it for later use:
Raw layer (unprocessed, “data lake”)
Processed layer (cleaned, structured data warehouse)
Formats: CSV, Parquet, JSON, SQL tables
Tools: PostgreSQL, Snowflake, BigQuery, S3, etc.

4. Data Cleaning & Transformation
Making it usable: removing duplicates, handling missing values, standardizing formats.
Transformation includes joining datasets, aggregating, or reshaping data.
Tools: Pandas, PySpark, dbt, ETL pipelines.

5. Data Enrichment
Adding more value:
Combining with external datasets
Doing calculations (e.g., revenue growth %)
Geocoding addresses, sentiment analysis on text, etc.

6. Data Analysis / Exploration
Asking questions and finding patterns:
Descriptive stats → “What happened?”
Exploratory analysis → “What might be happening?”
Tools: Jupyter, SQL, Excel, Tableau, Power BI.

7. Data Visualization & Reporting
Telling the story through charts, dashboards, reports.
The goal is to make the insight understandable and actionable.

8. Decision Making / Action
The top of the pyramid — turning insight into real-world actions, product changes, or business strategies.
'''

# To Do List:
r'''
1. Run the Scrapper Scrapping the Website and Getting the Data While Learning, Working and Experiencing Things
    - Reflect and Adjust if the Scrapper Fail to do their Job 
2. Learn the Basic/Core of Data Cleaning and Proccessing in the Website Extracting things to Create Insights
3. Clean the Damn Data to Create Insights
4. Data Cleaning the Proccess 
5. Data Analysis and Exploration and Data Visualization and Reporting
'''


# August 13:
r'''
I been Rushing things that i left to Chatgpt and even Deepseek do the Work that i didn't study it properly so i needed to fix that stuff for me and 
to understand the damn code man i been basically Cheating things 

I didn't write the code this day and i didn't even bother debugging it myself so that is a mistake so i needed to fix my mistake 
'''


# August 12:

# New goal:
r'''
Instead of Manually Typing the Things i should automate it because i'm a freaking programmer
https://ph.jora.com/
    Starting from this Website i should do things properly
'''

r'''
I have a Script to Scrape the Things that i want what is the next thing i supposed to do 
1. Run the Script to gather Data 
While Running the Script 
    In terms of Running the Sript 
    Overall Goal of the Project I needed to Rethink this stuff

    I Should Automate this Stuff in terms of Autosearching in the terms of searching things like inputting in the field

    My Script can run on the Website for 
    Mechatronics 
    Robotics Engineer
    Control Systems Engineer
    Electromechanical Engineer
    Process Control Engineer
    Industrial Automation Specialist
    Manufacturing Engineer (with automation focus)
    Test & Commissioning Engineer
    Maintenance Engineer (industrial/mechanical/electrical)
    Embedded Systems Engineer
    Electrical Design Engineer
    Firmware Engineer (for industrial equipment)
    Field Service Engineer (automation/instrumentation equipment)
    System Integration Engineer
    Production Engineer (automation-heavy industries)
    Plant Engineer
    SCADA Engineer
    PLC Programmer
    Instrumentation Technician
    LabVIEW Developer
    Process Instrumentation Specialist
    Robotics Technician
    Motion Control Engineer


2. I should Study the How to Extract and Read things While Studying at my things 
    How to Extract the Keywords and Stuff 

3. I'm Thinking should i lowercase everything but based on chatgpt he said during scrapping i should keep the original format if i'm not sure in terms of collection 
so in terms of description that is the lowercase of things 
'''

r'''
1. Re learning the CSV (Done)
2. RE Learning how to store a damn data in a CSV (Done)
3. Handling the Pop up Menu (Done)
4. Somehow Extract the Necessary Data In term of Scrapping (Done) 
5. 
'''

# August 11:
r'''
I Just Figure out that Clicking in a certain Elements playwright can automatically scroll it 
I can just fix this part to make it more Human thing because my current stuff is more on randomize but still 
a human behaviour in a project
'''

# August 10:
r'''
Re Practice the clicking Part in the Things 
'''

# To Do List
r'''
Inspiration for the Project: https://datanerd.tech/

1. Build a Clicking Thing in my Project that click a Job Post 
2. Extract After Clicking the Thing Extracting the Entire Text
3. Create a not so Complex Human Scrolling and Even Clicking and Addign Delays
4. Store all of the Job Description in a CSV Files
5. Cleaning Stage Most likely the Pandas Thing 
    * Lower Casing Everything 
    * removing Duplicate in the Projects
    * Removing the Unnecessary Stuff such as the HTML Tags 
6. Structuring Stage:
    * Skills → keyword match + NLP (e.g., spaCy, SkillNER).
    * Salary → regex → numeric range.
    * Requirements → sentence filtering (“must have”, “degree in”, etc.).
'''
# Motivation for the Project 
r'''
I can do a Role of Data Analyst, Data Engineer and Web Scrapping in this Project
'''
r'''
Got a Bit of problem and Starting a New Structure of the Code 
'''
# Project Structure 
r'''
README.md → The first thing a client sees. It sells the project and tells them exactly how to use it.
requirements.txt → Makes it easy to install dependencies with pip install -r requirements.txt.
config.py → Keeps URLs, credentials, and constants separate from code so they can be changed without editing core scripts.
main.py → A single, simple entry point to run the scraper.
scraper/ → Keeps scraping logic modular and organized by responsibility.
data/ → Shows you actually produce something useful, not just run code.
logs/ → Professional touch that shows you thought about monitoring/debugging.
tests/ → Tells clients your scraper isn’t brittle and you care about quality.
'''

# August 9:
r'''

I Learned i can See the damn History of my Commit which is very Nice 
1. Working Demo 
2. I can Scale the Damn Code
3. I can Do Switching User Agent Thing 

Next Thing 
1. Delays a Randomize Delays
2. Human Behaviour 
    Randomize CLicking 
    Randomize Scrolling Thing 
3. Maybe Finger Printing 
4. Lastly Going to Big Description Thing The Final Boss of the Project thing 
    What i want to do is text parsing + keyword extraction + categorization.
    1. Extracting relevant sections (e.g., “Qualifications”, “Requirements”, “Skills”)
2. Identifying and categorizing keywords (hard skills, soft skills, nice-to-haves)
3. Counting keyword occurrences (like “PLC” frequency for mechatronics career tracking)



Reflection I'm Still Dependable in AI and there are Concept and Practice i needed to learn 
1. Zip 
2. Next Page Thing 
3. Handling Exception and Error in my Code for more Robustness 
4. Skills In CSS and Xpath thing 
5. How to Commit Things


'''

# August 8:
r'''
Forgot to Put Something in August 7 

But In August 8 I think i needed to Do some Research on What is a Timeline in Creating a Project in Webscrapping a Realistic Timeline and i will try to do it fast enough
Because i have a Whole Day of Doing it and i needed to proccess the Information Faster and Create Something for myself in that 

I'm Going to Start to Work Right now: 
1. Devfining the PRoject Scope 

# I learn that Why do i need a Frequent or Once in term of Web Scrapping 
# In Terms of Demand i will putmyself where there are Currently needed which is the Frequent thing to do

'''

# August 4 -6
r'''
Pure Writing and Searching about "Meta" like getting experience and stuffl like
that and not actually working at things but after the term Test i will hit this project hard 
But right now at least i want to create a commit to get streak in the github

its like i'm working in this project in a Indirect Way of how i should do things here 

'''

# August 3
r'''
* Learning the DevTools More about things that are Important for Web Scrapping 
There are a lot of Things in Dev Tools That are Quite Important i thank my past self for learning API 
i have some idea on how to do things in there man 
'''

# August 2, 2025: 
r'''
    1. Learning to Investigate a Website First Before Touching  a code
        A. Understanding robot.txt (Done)
        B. Can i somehow Read the robot.txt or automate it in python? 
        C. Understanding Incognito and Browser Investigation in Website
        D. Learning the Dev Tools for Furthermore Investigation of the Website
Learning to Investigate or Recon of the Website before touching the code to know how to do the Workflow (Medium - High Energy Level)
    This Means i can Do it in the Morning or Afternoon for Energy Management 
    
        
        '''

# August 1, 2025:
r'''
    1. Trying the BS4 and Request 
    2. Sticking to Playwright BS4 and REquest DIdn't work 
'''

# July 31, 2025 
r'''
I want to Learn and Analyze a Website in terms of Legality whether i can scrape it or not 

'''

# July 30, 2025
r'''

Learning the Gray Area of Web Scrapping and The Legality of Web Scrapping 
    1. Scrapping a Third Party Website : "Jora" Similar to the other Website like Jobstreet or Even Linkdiln because i had no idea how to navigate things in terms of legality
    2. 

Fixing the Github of Why i can't just upload things in there 
    "
    💡 Only push your code and essential files to GitHub. 
    Keep large or system-specific folders (like venv/) out using .gitignore. Use requirements.txt to share your environment.
    " 
    # Requirment of Learning Things in here 
'''

# July 29 2025
r'''
    Measurable: 
         I think in terms of History i will measure it but i lacking of Time for this 

        Phase: 
            1. Defining The Objective
            2. Target Website: "Jobstreet.ph"
            3. Careful Experimenting to not Get blocked


    Actionable: 
        # I'm currently Thinking that should i always write the SMARTER goal for every Project The Heck 
   1. Putting VENV :  python -m venv job_venv
   job_venv\Scripts\activate
   2. Installing the Playwright: 
        a. pip install playwright ✅ 2. Install Playwright
        b. playwright install # ✅ 3. Install the required browser binaries

    3. Defining What Things i should scrape: 
        Job title
        Company name
        Location (city, country, remote status)
        Posting date (e.g., “2 days ago”)
        Job description
        Employment type (full‑time, part‑time, contract)
        Salary range (if disclosed)
        Application URL/link
        Requirements/qualifications
        Tags/categories (e.g., Developer, Customer Service)
        On some platforms (e.g., Kalibrr, OnlineJobs.ph), you might also scrape:
        Resume snippets or skill matrices
        Assessment results (Kalibrr)
        Employer ratings or chat metadata (Bossjob)

    4. Goal Statement:
        To identify the most in-demand hard skills for Mechatronics or Automation Engineer roles in the Philippines by scraping job listings from relevant local job websites.
            A. Collecting job listings related to Mechatronics and Automation Engineering.
            B. Extracting job titles, descriptions, and particularly required skills.
            C. Analyzing the frequency of specific hard skills (e.g., PLC programming, AutoCAD, MATLAB).
            D. Producing insights about which skills are most frequently demanded, helping guide skill development or hiring strategy.
    You said:

    🧭 Process to Define and Achieve the Goal
    Here’s how you define and implement this project step-by-step:

    1. Clarify Your Research Questions (Define Goal Precisely)
        * Break your broad idea into concrete questions:
        * What are the most frequently mentioned hard skills in job listings for Mechatronics or Automation Engineers?
        * Which companies or industries are hiring the most for these roles?
        * How do skill demands vary between locations or job levels?

    2. Identify Target Websites for Scraping
        Find Philippine-based job portals that list engineering jobs:
        JobStreet Philippines (https://www.jobstreet.com.ph/)
        Indeed Philippines (https://ph.indeed.com/)
        Kalibrr (https://www.kalibrr.com/)
        LinkedIn Jobs (PH location filtered)

    3. Determine Data to Collect (Data Fields)
        For each job listing, collect:
            Job Title
            Company Name
            Location
            Posted Date
            Job Description
            Skills / Requirements (Key Field!)
            Employment Type (optional)
            Seniority Level (optional)

    4. Store the Data
        Store the scraped data in:
        A local CSV or JSON file for initial analysis
        Or a database like SQLite or MongoDB for scalability
     
    5. Clean and Parse the Data
    Focus especially on:
        Cleaning messy text
        Tokenizing and extracting hard skills from job descriptions
        Example: using keyword matching (e.g., ["PLC", "AutoCAD", "SCADA", "Python", "SolidWorks"]) or NLP

    6. Analyze the Data
        Use Pandas or SQL to count frequencies of skills
        Plot using Matplotlib or Seaborn

    7. Interpret & Visualize Results
        Create visual insights like:
        Bar chart of Top 10 In-Demand Skills
        Word cloud from job descriptions
        Time-series if you scrape over weeks/months

            
'''
r'''
July 28 2025:
    1. Starting to Create "history.py" to document what i'm going to do in Project_Job_PH
    2. Why i created this project? 
        * To Showcase my Skill in Playwright and overall Web Scrapping Skills 
        * For Personal use to Determine what is the current Demand on Job in the Philippines targeting the specific Career Path and their Hard Skills, Location, and information 
            - for Example "Mechatronics Engineer or Mechatronics Technician" The Average Salary, What hard Skills are Needed, What Location are Currently finding it? 
    3. My Implementation or my "Meta Proccess"
        * Jumping with an Uncofident in my Skills in terms of the Foundation or Core in "Playwright"
        * Implementing the Project Learning Approach in this Case
    4. Let's Define a SMARTER Goal:
        S Specific:
            Scrape a Mechatronics Areas
                1. Industrial Automation / Control Systems
                    Roles: Automation Engineer, PLC Programmer, Control Systems Engineer
                    Skills: PLCs (Siemens, Allen Bradley), SCADA, HMI, sensors, actuators, PID control
                    Industries: Manufacturing, oil & gas, automotive, packaging
                2. Robotics
                    Roles: Robotics Engineer, Robot Programmer, Maintenance Engineer
                    Skills: Kinematics, dynamics, ROS (Robot Operating System), microcontrollers, C++/Python
                    Industries: Automotive (e.g. assembly lines), medical robotics, aerospace

                3. IoT (Internet of Things)
                    Roles: IoT Developer, Embedded Systems Engineer
                    Skills: Arduino, Raspberry Pi, wireless communication (BLE, Zigbee, MQTT), sensors, cloud (AWS/ThingsBoard)
                    Industries: Smart homes, agriculture, logistics, healthcare

                4. Embedded Systems / Firmware Development
                    Roles: Embedded Systems Engineer, Firmware Developer
                    Skills: C/C++, microcontrollers (STM32, PIC), RTOS, circuit design
                    Industries: Consumer electronics, medical devices, automotive

                5. Product Design & Development
                    Roles: Mechatronics Designer, R&D Engineer
                    Skills: CAD (SolidWorks, Fusion 360), prototyping, 3D printing, simulations
                    Industries: Consumer goods, industrial tools, startups

                6. Maintenance & Field Engineering
                    Roles: Mechatronics Technician, Maintenance Engineer
                    Skills: Troubleshooting, diagnostics, machine maintenance, wiring, hands-on skills
                    Industries: Manufacturing, energy, rail, defense
                7. Artificial Intelligence + Mechatronics
                    Roles: AI Robotics Engineer, Machine Vision Engineer
                    Skills: Python, OpenCV, TensorFlow, AI/ML for robotics
                    Industries: Automation, autonomous vehicles, smart robotics
            What is the Current Demand 
        M Measurale
            Basing the History and the Work i will be Doing 
        A Actionable
        R Relevance
        T Timebound
        E 
        R  
'''
