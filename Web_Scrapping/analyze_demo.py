# Goal of this File to Analyze the Demo Because i been Copy pasting the Damn Code

import csv
import random
import time
from datetime import datetime
from urllib.parse import urljoin
from playwright.sync_api import sync_playwright
from fake_useragent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem
from random_user_agent.user_agent import UserAgent as RandomUA

# The Idea of Mastry in Programming 
r'''
Due to my Incompetent Beginner, Cheater Mindset 
I been Copy Pasting Code Without Understanding the code properly and really relying on AI 
to do the work and not just really go for the Efficiency 

The Problem in that Mindset is i think it will be bad in the long run especially as it go complex
and AI can't solve it so i decided to analyze each of the damn code properly 
and learn the Fundamentals as i go on at things because there are many stuff 
This is Definitely the Hardwork and the Proccess is quite Gruelling
'''

# Using the AI as a Tool
r'''
Before Running the Code of AI 
    Reading it Line by Line
    ASking it What do i think this part Does?
    Why it might be written this way

The Tweak and Break Method:
    Renaming Variables, Changing Loops or Changing the Data Structure
    to Build Internal Map of the the Language and Logic Work

Reverse Engineering Method 
    Purely Writing it in memory to see what missed 

'''


# def start_csv_writer():
#     """Open a CSV for streaming writes during scraping."""
#     date_str = datetime.now().strftime("%Y-%m-%d")
#     filename = f"overall_automation_jobs_{date_str}.csv"

#     csv_file = open(filename, "w", newline="", encoding="utf-8")
#     writer = csv.writer(csv_file)
#     writer.writerow(["Role of Job", "Company Name", "Company Location", "Type of Work", "Description"])
#     print(f"📁 Streaming results to: {filename}")

#     return csv_file, writer

# Starting to Open the CSV Files
def start_csv_writer():
    # date_str variable
    # datetime.now() Get the Current Date
    # strftime is a method to format the date into the string format
    # %Y: Four-digit year
    # %m: Month as a zero-padded numbe
    # %d: Day of the month as a zero-padded number
    # %H: Hour (24-hour clock) as a zero-padded number (e.g., 15)
    # %I: Hour (12-hour clock) as a zero-padded number (e.g., 03)
    # %M: Minute as a zero-padded number (e.g., 34)
    # %S: Second as a zero-padded number (e.g., 57)
    # %A: Full weekday name (e.g., Thursday)
    # %B: Full month name (e.g., August)
    # %p: AM or PM
    # %c: Locale's appropriate date and time representation
    date_str = datetime.now().strftime("%Y-%m-%d") # To Produce the Output of:
    r'''
    2025-08-14
    '''

    # File naming 
    # f to Add the date_str so it automatically get the current date during scrapping 
    # f is basically adding the variable in a string format here
    filename = f"overall_automation_jobs_{date_str}.csv"


    csv_file = open(filename, "w", newline="", encoding="utf-8")
    # open() is it used to open a file and return a file object 
    # "w" stands for write 
        # it can overwrite the files
    # newline="" : Crucial for CSV files to not get inserted by a blank rows
        # basically prevent blank rows in your csv Files
    # encoding="utf-8", tf-8" is a universal and widely used encoding that can handle a vast range of characters
        # best practice to avoid issues in term of special character or text from non English languge
    # filename: 
    r'''
    filename that specifies the path, you are giving the name of the file while also 
    locate the files within a computer file system
    This Tell the Computer exactly where to find or create the File 
    
    e.g.
    file_path_windows = "C:\\Users\\JohnDoe\\Documents\\data.txt"

    # The r before the string makes it a "raw string" to avoid issues with backslashes
    file_path_windows_raw = r"C:\Users\JohnDoe\Documents\data.txt"

    with open(file_path_windows, "r") as file:
    content = file.read()
    print(content)

    Reading the COntent of the file(data.txt)
    '''

    # What is the Purpose of this code? 
    r'''
    It Create an Object designed to write CSV data because it is complexx
    '''
    writer = csv.writer(csv_file)
    # Opening a File Using $ open(filename, "w", ...) it only know how to write raw text
    # While $ csv.writer is a specialized tool for CSV 
    # csv.writer help you write in CSV files instead of manually to format each of the line

    # writer.writerow
    writer.writerow(["Role of Job", "Company Name", "Company Location", "Type of Work", "Description"])
    r'''Is a Method Call that instruct the csv.writer object to write in a single row
    "Role of Job", "Company Name", "Company Location", "Type of Work", "Description" a list of string represent the data for  the row 
    '''
    
    # Basically to Debug Things out if it Currently Saving or not 
    print(f"📁 Streaming results to: {filename}")

    # Why it Return?
    r'''
    A Function is responsbile for setting up the files and writer object
    But the Rest of the program(Scrapping a Website) needed to use the object to actually write the data
    which in my case the pagination part and by returning them you can use the function everywhere 
    '''
    return csv_file, writer

# Going Back to Basics
# Why Use Function and return statement 
r'''Function is a reusable code that perform a specific task, it break down the program
into a smaller,manageable pieces which my code is easier to read, debug and maintain'''
r''' is a way for a function to send value or values back to the part of the code that called it
'''



# Purpose of the Function:
r'''
When i try to run my program it sometimes crashes midway during running and the files are not saved so i want to fix that 
'''
# Function: def write_job(writer, csv_file, job_data)
r'''
I understand the writer and csv_file in terms of using the past files but in terms of 
job_data: is kinda i don't i needed to think about it but one thing i know is it should be the job_data which is in my pagination function
'''
def write_job(writer, csv_file, job_data):
    
    """Write a single job row and flush immediately."""
    writer.writerow(job_data) # I know this already writing the Line of Row of things 

    csv_file.flush()  # ensures data is saved to disk right away
    r'''
    The .flush() method forces the data you've written to the file to be saved from the computer's memory (RAM) to the hard drive or disk immediately. 💾
    '''

# this is Tricky for me in Some Sense in terms of Why it write the way it Write so I needed to Learn more about this stuff but i think it is quite simple 
# # --- Scraper integration example ---
# csv_file, writer = start_csv_writer()

# try:
#     # Your real scraping loop goes here:
#     for job in scrape_jobs():  # <- Replace with your actual scraping function
#         # job must be a list like: [role, company, location, work_type, description]
#         write_job(writer, csv_file, job)

# finally:
#     csv_file.close()
#     print("✅ CSV file closed.")
###################################################################################### 


# Understanding the Try and Except Blocks
# I Didn't even Notice there are Nested Function inside my Function

# extraction_job_description:
r'''
What Exactly it can do?
    * Locate the Jobs in terms of in the Side and Randomly getting things (For Non Human Thing)
    * Hovering and Clicking the Jobs that are Random based on the Index 
    * Safely Get the Proper Things in there Jobs Description, Role of the Job, Company Name, and Type of Work
'''

# extraction_job_description 
# page is for getting the page in the main thing, Writer is for the csv files 
# I think i should add write_job in terms of the things
# My Understanding in the Concept of the Function are kinda vague so i needed to fix that 

# Going Back to the Basics of Try and Except Blocks 
r'''
In Python, try and except are used for exception handling—they let you run code that might cause an error without stopping your whole program.
try block → put code that might fail.
except block → what to do if it fails.

You Can do Multiple Exception Depending on the Error 

'''

r'''Catching Multiple Exceptions'''
# try:
#     num = int("abc")  # This will fail
#     result = 10 / num

# except ValueError:
#     print("That was not a number.")
# except ZeroDivisionError:
#     print("You can't divide by zero.")
r'''Catching Any Exception [it Catches any Error the problem is debugging things]'''
# try:
#     print(10 / 0)
# except Exception as e:
#     print("An error occurred:", e)
r'''else and finally
    * else → runs if no error happens.
    * finally → always runs (good for cleanup).
'''
# try:
#     x = int(input("Enter a number: "))
# except ValueError:
#     print("Invalid number.")
# else:
#     print("Good! You entered:", x)
# finally:
#     print("This always runs.")
r'''
Summary:
💡 In short:
    * try → Attempt risky code
    * except → Handle errors
    * else → Runs if no error
    * finally → Runs no matter what
'''

# In Term of def extraction_job_description:
r'''
It Uses to Catch The Error anything at the End of the Stuff:
    * Catching Any Exception
Basically the Goal of this is to Catch the Error so my Web scrapping still do the job Thing
'''
# I quite Notice that everything in here is using : except Exception as e which is kinda good i think


def extraction_job_description(page, writer):
    # It Uses to Catch The Error anything at the End of the Stuff:
    try:
        # Basically Get the Numbers of things 
        locator = page.locator(".job-link.-no-underline.-desktop-only.show-job-description")
        count_job_post = locator.count()


        # If Statement that Return:
        if count_job_post == 0:
            print("[WARNING] No job posts found on this page.")
            return
        r'''
        * Here, return means: stop running this function right now and go back to where it was called.
        * This is not just skipping one loop — it stops the entire extraction_job_description function.

        The Next Question is if it Early Exit will still it Paginate? 
        because if Extraction_job_description stop i think it will still paginate maybe i needed to experiment that 
        '''
        ###################################
        indexes = list(range(count_job_post))
        random.shuffle(indexes)

        for i in indexes:
            try:
                time.sleep(random.uniform(0.8, 2.3))

                # Hover safely
                try:
                    locator.nth(i).hover(timeout=3000)
                except Exception as e:
                    print(f"[WARNING] Could not hover over job {i}: {e}")
                    continue

                time.sleep(random.uniform(0.2, 0.5))

                # Click safely
                try:
                    locator.nth(i).click(timeout=5000)
                except Exception as e:
                    print(f"[WARNING] Could not click job {i}: {e}")
                    continue
                r'''
                Contiue means: skip the rest of this loop iteration and go directly to the next item in the loop.
                It means going to the next Job Post because it don't click anything
                '''
                ##########################################################

                # Get job title text safely
                try:
                    value = locator.nth(i).inner_text(timeout=5000)
                except Exception as e:
                    print(f"[WARNING] Could not get text for job {i}: {e}")
                    value = "Unknown"

                # Wait for job description container
                if not page.wait_for_selector(".job-description-container", state="visible", timeout=5000):
                    print(f"[WARNING] No job description loaded for job {i}")
                    continue

                # Extract safely
                def safe_text(sel): #  sel → A string representing a CSS selector for a web elemen

                    try:
                        return page.locator(sel).inner_text(timeout=3000)
                        r'''
                        Inside the try block, it:
                            * Finds the element with page.locator(sel).
                            * Gets its text content using .inner_text() with a 3-second timeout.
                        '''
                    except Exception:
                        return "N/A"
                    r'''
                    If anything goes wrong (element missing, selector wrong, timeout, etc.):
                        * It catches the error in the except block.
                        * Returns "N/A" instead of crashing.
                    '''
                # Calling the function for different data
                roles_of_jobs = safe_text('.job-title.heading.-size-xxlarge.-weight-700')
                company_name = safe_text('.company')
                company_location = safe_text('.location')
                type_of_work = safe_text('.badge.-work-arrangement-badge .content')
                r'''
                Calls safe_text with a different CSS selector.
                Gets the text for that element (or "N/A" if it fails).
                Stores it in a descriptive variable.                
                '''


                print(f"{i}: {value}")
                print(f"Role of the Job: {roles_of_jobs}")
                print(f"Company Name: {company_name}")
                print(f"Company Location: {company_location}")
                print(f"Type of Work: {type_of_work}")
                print("-" * 10)
                ######################################################################

                try:
                    description_extraction = page.locator(".job-description-container").inner_text(timeout=5000).lower()
                except Exception:
                    description_extraction = "No description found."

                print(description_extraction)
                print("-" * 50)

                writer.writerow([roles_of_jobs, company_name, company_location, type_of_work, description_extraction])

            except Exception as e:
                print(f"[ERROR] Skipping job {i} due to error: {e}")
                continue

    except Exception as e:
        print(f"[ERROR] extraction_job_description() failed: {e}")

# Concepts:
r'''
return = “No jobs at all? Okay, I’m going home and stopping work entirely.”
continue = “This specific job listing is broken. I’ll skip it and move to the next one.”
'''

# I think i Understand the Rest of THe Code For Understanding the Try and Except blocks thing 
