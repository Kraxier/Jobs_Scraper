# Defining the Project Scope:

r'''
✅ 1. Define the Project Requirements
Before writing any code, answer these:
    What data do you need? (e.g., product prices, job listings)
    Where will you get it from? (specific websites? multiple?)
    How often do you need it? (once? daily? hourly?)
    How will you use/store the data? (CSV? Database? API?)
'''

# Goal of the Project:
r'''

(Future: Instrumentation Course and Data Engineer)

To identify the most in-demand hard skills for Mechatronics or Automation Engineer roles in the Philippines by scraping job listings from relevant local job websites.
    A. Collecting job listings related to Mechatronics and Automation Engineering.
    B. Extracting job titles, descriptions, and particularly required skills.
    C. Analyzing the frequency of specific hard skills (e.g., PLC programming, AutoCAD, MATLAB).
    D. Producing insights about which skills are most frequently demanded, helping guide skill development or hiring strategy.

    * What are the most frequently mentioned hard skills in job listings for Mechatronics or Automation Engineers?
    * Which companies or industries are hiring the most for these roles?
    * How do skill demands vary between locations or job levels?
    
    '''
# Data I Should Scrape Based on the Goal:
r'''
Defining What Things i should scrape: 
    Job title
    Company name
    Location (city, country, remote status)
    Posting date (e.g., “2 days ago”)
    Job description
    Employment type (full‑time, part‑time, contract)
    Salary range (if disclosed)
    Hard Skills and requirement
    Requirements/qualifications

    Optionals:        
        Application URL/link
        Tags/categories (e.g., Developer, Customer Service)
        Resume snippets or skill matrices
        Assessment results ()
        Employer ratings or chat metadata ()
'''

# I will Focus on This Website:https://ph.jora.com/ 

# I'm Done Defining the Scope of the Project i think 




############################### Determining Frequent or Once ##############################

# I Ask the Question in Chatgpt in Determining How Frequent Should i Scrape a Website like how often do i need the data?
# For my Things : I can Take things Slow in Doing my Website 
r'''
Based on the Research: 
🔁 When You Need to Scrape DAILY (or frequently):

1. Time-sensitive or rapidly changing data
    Examples
        Stock prices
        Flight or hotel prices
        Job listings
        E-commerce product prices
        Sports scores
        News headlines
2. Competitive Monitoring
    Examples:
        Monitoring rival pricing
        Tracking competitor features
        Watching product inventory
3. Alerting / Notification Systems
    New real estate listings
    New job openings
    Price drops

4. Building Time-Series Data
    Tracking how a product’s rating change
    Monitoring website metrics or changes

'''

# Why 🟢 Why Daily?
r'''

Businesses use this for market intelligence
Helps respond to price wars or stock changes
You need to react fast when something appears or changes
The data changes often
You want the latest version
You're tracking trends over time
'''

# Me is Once only: 
r'''
You're building a one-time dataset to analyze,  The Current trends in Mechatronics

'''


r'''
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