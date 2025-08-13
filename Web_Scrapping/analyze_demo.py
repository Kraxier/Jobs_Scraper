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



