
# History or Timeline of What I currently Gonna do In "Project_Job_PH"
# Website i can Try: https://ph.jora.com/ 
# git rm -r --cached job_venv
#  .\job_venv\Scripts\activate

# Timeline/History:



# Defining the Finished Project: 
r'''
1. Raw HTML → structured format (CSV, JSON, database). # Create a Code for this 
2. UI or Simple Script that Automatically Clean the Data 
    * Data Cleaning, Data Wrangling
3. Build a config File What ever that means for Web Scrapping Project 
https://chatgpt.com/c/68af87be-74b4-832c-aa39-46714cf61aa1
4. Build a Proper README.md 
    * how to Run it 
5. Put it to a Google Sheet (Learn the API things)
6. Put it into a Mysql Database (Learn also the database)
7. Build a UI for Simple Showing Things 
8. Presentation of Portfolio 
    * GitHub repo: Clean code, requirements.txt, README with screenshots.
    * Case study / blog post: Explain the problem, your solution, and results.
    * Demo: Short Loom video walking through the project.

Go For Learning Data Cleaning and Transformaton 
File Handling and Storage 


'''
# 🔹 Components of a Good Web Scraping Project
r'''
1. Extraction (Core Scraper)
    * Navigating and requesting pages (requests, Scrapy, Selenium/Playwright for JS-heavy sites).
    * Handling pagination, filters, infinite scroll.
    * Respecting rate limits, headers, cookies.
    * CAPTCHAs (sometimes) → solving/bypassing gracefully.

2. Data Cleaning / Transformation
    * Parsing raw HTML → structured fields.
    * Cleaning text, trimming whitespace, handling encodings.
    * Normalizing data (e.g., dates, currencies, product variations).
    * Flattening nested data for CSV/Excel output.
    * Deduplication (e.g., avoid double entries with an id or hash).
3. File Handling / Storage (your focus now ✅)
    * JSONL/CSV/Excel/Google Sheets.
    * Database inserts (SQLite, MySQL, Postgres, MongoDB).
    * Cloud storage (Google Drive, AWS S3, etc.) if needed.

    Priority Task:
        1. Scraper outputs JSONL (append one JSON object per line) — streaming-safe, simple. 
        2. Local converters
            A. JSONL → CSV
            B. JSONL → Excel (.xlsx)
        3. Cloud / shareable output
            JSONL → Google Sheets (via Google Sheets API + service account)
        4. Database ingestion
            JSONL → SQLite / MySQL / PostgreSQL / MongoDB
        5. (Optional later) Parquet, BigQuery, S3, API push, etc.



4. Scheduling & Automation
    * Run scraper on a schedule (cron jobs, Airflow, Scrapy Cloud, GitHub Actions).
    * Automatic retries on failure.
    * Incremental scraping (only fetch new/updated records).

5. Error Handling & Logging
    * Save failed URLs, with reason (timeout, parsing error, captcha).
    * Retry with backoff.
    * Logs for monitoring what happened during the run.

6. Configurable Scripts (for clients)
    * Choose category, date range, keywords from a config file or CLI.
    * Example: python run.py --category "electronics" --format excel.
    * Makes your tool usable by non-developers.

7. Deployment / Delivery
    * Provide the client with:
    * A script they can run (python scraper.py --out data.xlsx).
    * A scheduled service (cloud run, VPS, Docker container).
    * Or just deliver ready-made Excel/CSV/Google Sheets reports.

8. (Optional but impressive) Dashboard / Visualization
    * Show results in a simple web dashboard (Streamlit, Flask, etc.).
    * Charts, filters → especially useful for e-commerce/lead gen scraping.
'''

# September 11:
r'''
After Exploring a little bit of the Data more on the standardization rather than cleaning white spaces because i already do it man 

1. Remove all Duplicates 
2. Find some Special Characters in each Column and try to Figure out What is common Special Characters
3. Standardization of Things 

So Far this is the Things i neeeded to do for data cleaning i think 

i Should Add Date In Extracting Data for Creating ISO Format
'''

# September 10:
r'''
Its currently 6:30 PM which is pretty new to me but Let's do a small bit of programming 
'''

# September 7-9:
r'''
Building the Basics of Data Cleaning and Stuff in terms of the knowledge 
September: 9 is Categorizing and Standardization based on the data

Also I have a Goal in implementing the prototype_1.py
'''

# September 6: 
r'''
Building the basics script for data cleaning:

'''

# September 3:
r'''
Web Scraping Component and Projects 
1. Core Extraction 
	* Website Investigation
	* Playwright Skills
2. Data Cleaning and Transformation 
	* Regex
	* Pandas
	* Spacy 
'''

# September 2:
r'''
In a File, Determining where to Focus:
    Data Pipeline i should be focusing on the basic of things because my main core service is 
    Data Extraction, so Data Cleaning should be basics and stuff

    Focusing on Data Cleaning
'''

# September 1:
r'''

Storing the Data in the JSON, JSONL 
Converting JSON files to Excel, CSV 

'''

# August 31: 
r'''
Structuring the Learning stuff of copy pasting and learning the fundamentals and some rules into doing the stuff 
'''

# August 30:
r'''
Focusing in Creating a Code to Create a JSONL to save the data Thing 
And Creating the Config File 
Shipping the Project Thing
'''

# August 29: 
r'''
Creating a Code to Put Excel and JSON file Using Pandas

Research (Under 30 Minutes):
    1. JSON is the Best for Web Scrapping in terms of Getting the data and 
    converting it to different Format down later using pandas
    2. Fundamentals of Saving the Data Using JSON files
Research And Study (15 Minutes)    
1. "Learning JSON and  Fundamentals around it also the best practice for web scrapping

Implementing the JSON File in my Programming web Scrapping 
* Learning the Basic of File Handling and Working it to Function is a different experience for me

Feedback:
    1. In terms of Project Learning Approach: 
    * Should i Study after researching of what i research to make it understanding?
    

BACK TO THE FUCKING FUNDAMENTALS OF FILE HANDLING FOCUSING IN JSON STUFF 
'''

# August 28:
r'''
Realization: 
What is the Main Purpose of the Project?

To Showcase my Skills as a Web Scrapper to make a Script that are working for the Client but Right now after copy pasting the code in chatgpt the realization of 
that is not really mine and i don't have a sense of ownership and this feel like a chatgpt project more than me because the problem right now is i rush to finish the 
project and i want it to be done as soon as possible but right now i don't have a proper fundamentals in the tools that i used like spaCy and Pandas and Data Cleaning 
and even the playwright library that i been using 

To Learn something based on PrimeTime 
Give you a Component and from that Component is you need to Build Something out of that component and try do to something until you reach the final results 
What i do is Copy Paste the program which is the final results 

So Right now i have a Final Results from the Code i can analyze the Component of that and say i learn it but i feel like i'm missing something important 

After Asking this to Chatgpt: 
    1. Redo the Project Thing
    2. Or Analyze the Component and Breakdown the Fundamentals to Have a Cheat Sheet and Do another project is the best way of doing things 

The Next Thing I Supposed to do is 
    1. Do the Config File Thing 
    2. Google Sheet Saving Format Thing 

I'm Going to Ship the Project Thing
Why my Solution Worked 
What Problem Thing that i solve 

Read every error message completely
Use actual debuggers again
Write code from scratch
Read source code instead of asking AI

No AI for problems that you haven’t tried to understand first
Read and understand all AI-suggested solutions
Regular periods of coding without AI assistance
Focus on learning patterns, not just fixing immediate issues


Adding the Concept and Studying + Programming and Implementation of Things 
Adding the Rewriting the Code
Adding the Equation of how to Properly Integrate the AI
How to Do the Documentation 

'''

# August 27:
r'''
Analyze 

Demo_3.py MAIN FOCUS
    What Concept Did i Use? 
    Putting a Why instead of What
    Fix Everything (How to Clean the Data)
Analyze Component in Data Cleaning

Build Excel and JSON format 
Build a Google Sheet Saving Format 
Build a Config File

Putting everything in Project Strucure: 
Demo First 



'''

# August 26:
r'''
Deadline is This August Only
    1. Create the README.md
        - Study the Concept of README.md (DONE)
        - Properly Implement Things (DONE)
    2. Create the Case Study for the Project (DONE) 
    3. Python Files:
        A. Put Python Files in the Proper Places (Proper Structure of Project)
        B. Understand the Code:
            1. Meaningful Names:
            2. Write the Why of Things (Why something it Done)
            3. Clean Code
            4. Write a Code that will save in JSON format
            5. Write a Code that will save in Excel Format 
            6. Write a Code that will save in MYSQL database and Google Sheet
            7. Write a code that have a Config files for the whole thing
            8. Write a Code for UI (Optional I think)
            9. History of the Code and the Thought Proccess and Reflection
            10. Find out what is the Reusable of Things in the Code that i can reuse
            11. Template for the Things that i want to Build 
                A. Data Cleaning 
                B. Data Extracting 
                C. Investigation in the Website 
    4. Create a Demo Video for the Things in here
'''

# August 24:
r'''
FOCUSING ON PUTTING THE ENTIRE CONCEPT IN THE THINGS THAT I CREATED 

Why i do i do this again ? 
Focus in Applying the learning that i forgotten how important the concept is 

Additional Concept 
    1. CSV Writing 
    2. Try and Except Blocks 
    3. Function 
    4. Pandas Library and Core Concepts and Fundamentals
    5. Data Exploration and Data Cleaning Concept 
    6. spacy
    7. 


AS i learning the concepts and some of it are already applied at things there are things that i must 
do it better next time but the thing is i'm constructing the workflow while also learning which is 
quite nice of things 


Concepts in Investigation in Website
1. I try to Experiment some of the concept some are definitely working but in terms of scrolling it didn't 
update it sometime like facebook and instagram
2. AS i Scroll and checking in Developer Tools network Request it keeps pumping things, also not just scrolling
i can do interaction in the website and it continously call in the network request thing and i see some data there 

'''

# August 23:
r'''
Compile all the Learning and Studying Part of things
'''


# August 22:
r'''
Priority for the Goal:
    1. Create a Proper Proffessional Project:
        a. Proper Project Structure 
    2. Mastery in Web Scrapping 
        a. Workflow for Investigating a Website:
            1. Legality of Scrapping 
            2. Terms and Services
            3. Robot.txt
            4. Security of the Website 
            5. Developer Tools Mastery
        b. Workflow for Anchor Project Learning + Studying Concept
        c. Workflow in building a Scrapper
            1. What Tools i needed to Use? (API,BS4/Request,Playwright,Scrapy)
            2. Building a Anti Bot Detection
            3. Single Page Data Extraction (Focusing on the Core Extraction of the Project)
            5. Multiple Page Data Extraction
        d. 
           
'''

# August 21:
r'''
Collecting Resource on how to Write in README.md
'''


# To Do List:
r'''
1. README.md Fix the Damn Thing 
2. Study this why? 
├── scraper/              # core logic
│   ├── __init__.py
│   ├── spiders/          # scraping logic, possibly multiple sources
│   ├── parsers/          # clean extraction, parsing, validation
│   ├── pipelines/        # process/save scraped data
│   ├── utils.py          # helper functions
│   └── proxy_manager.py  # if rotating proxies
and This Part Also 
├── logs/
│   └── scraper.log
│
├── tests/
│   ├── test_scraper.py
│   └── test_parsers.py
3. Proper Learning Things 
    1. Project Approach + Concept 
    2. Fixing the Concept using the Coding Sloth Thing 
    3.  The Goal of the Project is for me to learned the concept and implement it properly
    4. From the Start Fixing all the Concept that i did and Sharing the Damn Code of things
    5. Using the Proper learning Approach Creating a System for Learning

'''


# August 20 Wednesday:
r'''
1. Fix Some of the Concept in the History and put it in Proper Place
2. Implement the Basic of Data Cleaning and Transformation

Rebuild from Scratch:
    A. implementation.py in Data Engineering Side:
    B. data_cleaning.py in Data Engineering Side:
    C. Reflection on Everything from Data Cleaning and Transformation to Data Analysis and Data Visualization and how the Project i will be Moving forward 
    because right now i think i achieve the Goal and i wonder what to do next
'''


#  August 19 Tuesday 
r'''
What is the Current Focus of Things? 
I have a project i can somehow an incomplete project honestly but i think it can do 70% of the job even if it is not Done

I can Somehow Categorize the Company Location: 
    1. Clear Some of Special Characters that are in there (Data Cleaning)
    2. Categorizing the Role of the Job (Data Transformation)
    3. Extraction of the URL (Data Extraction )
    4. Adding Programming Language in the Things (Data Transformation)

Fixing the Proper Project Structure of Things 
Creating a Script where i can Replicate things My Own Damn Script instead 
'''



# To Do List: 
r'''

💡 Your Workflow Summary
Define 15-min task needing the tool
Research ≤25 mins – only what’s essential for this task
Implement immediately (errors = learning anchors)
Customize only when the task demands it
Ship at 70% completion → Start new micro-project


Strategic Approach to Project Demands & Emerging Concepts
1. Anchor Your Current Phase (Stop Jumping)
Diagnosis: You're experiencing "concept overwhelm" - discovering related but non-urgent requirements (data engineering/analysis) mid-task.
Action: Freeze your project at ONE logical checkpoint:
"I will complete scraping ALL target data FIRST before considering cleaning/visualization."
→ This is your ANCHOR: "Fully scraped raw dataset"

2. The Expansion Trigger Principle
Only move to the next concept when:
Your current micro-project (scraping) reaches 70% completion (e.g., data from 7/10 sites scraped)
AND a new skill becomes blocker for current work
(e.g., if dirty data prevents saving files → learn minimal cleaning)

Define the MINIMAL required action:
"I need Pandas to remove null values from column X in my scraped.csv"
(NOT "Learn all Pandas")

Apply the 15-Minute Rule:
🕒 15-min task: "Drop rows with null values in 'price' column"
🔍 Research ONLY: pandas.read_csv() + df.dropna(subset=['price'])
⚠️ Ignore: Data types, optimizations, advanced methods


Critical Mindset Shifts
✅ "Concepts serve projects, not vice-versa"
(Learn data engineering ONLY when dirty data blocks your scraping)
✅ "Projects grow branches, not forests"
(Visualization is a NEW branch, not part of scraping trunk)
❌ Kill: "While I'm here I should also learn..."
'''


# August 18:
r'''
Thinking the to do List 
    1. Analyzing the Data 
I just Copy Pasting Code from the Chatgpt and analyzing line by line to see how the code works and i think it is Shallow way of learning things because i don't see it in real time


Copy-pasting code and reading it line by line isn’t “bad” — it can give you surface-level familiarity — 
but you’re right that if you never test, tweak, or build with it, the learning stays shallow. It’s like reading about swimming without ever getting in the water.

The Next Question is Since When i copy pasting Things?
Ask “what if?”
    Instead of only asking what this line does, try what would happen if I remove/modify this line?
    This builds causal understanding instead of just memorization.

Rebuild from scratch
    After analyzing, close the original code and try to write it again without looking.
    You’ll quickly discover what you really understood and what you only skimmed over.

Apply to a tiny project
    Take the same concepts and use them in a simple project (calculator, to-do list, scraper, game, etc.).
    Application forces you to understand why the code exists, not just what it does.
'''

# August 17:
r'''
Create a Analyze Component(Combining spaCy and Pandas)
I finally can extract the job description skills while also i can add the component of progression in terms of extracting skills because it really take a time to do things so i think we are going to data analysis
'''
r'''
Learning about the Data Analysis
'''


# August 16 or 17:
r'''
1. Properly Study the Damn spaCy 
2. Relearn the Necessary Tools in Pandas 
3. Try to Combine the Both Extracting Skills and Creating a Table for that

'''

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
