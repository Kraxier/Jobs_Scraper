# Implementing the Prototype_1.py


# Goal: 
r'''
🎯 Project Goal

Build a full cleaning pipeline that takes your raw JSONL (Mechatronics_2025-08-30.jsonl) and produces a cleaned CSV file ready for analysis or ML.

✅ Step-by-Step Goals to Reinforce Learning
1. Load & Inspect
Load your raw JSONL into a DataFrame (pd.read_json(..., lines=True)).
Print df.info() and df.head() to understand the raw structure.

2. Text Cleaning (what you practiced)
Apply basic_clean_text() on:
Job titles
Descriptions
Company names (if they contain HTML/extra spaces)

3. Type Conversion
Parse salary fields (extract min/max salary as floats).
Parse dates (convert posted_date → ISO format).
Convert boolean-like fields (e.g., "remote"/"yes"/"no") into True/False.

4. Standardization
Normalize job titles into categories:
"Mechatronics Engineer", "Robotics Engineer" → "Engineer"
"Technician", "Maintenance Technician" → "Technician"
Normalize company industries (if available).

5. Deduplication
Generate unique IDs (hash(title + company + date)).
Remove duplicate job postings.

6. Output
Save cleaned dataset as:
Mechatronics_cleaned.csv (for easy viewing in Excel).
Optionally Mechatronics_cleaned.parquet (efficient for big data).

7. Stretch Goal (Reinforce Deeper)
Add logging (track how many duplicates removed, how many missing salaries, etc.).
Build a small modular pipeline (functions: clean_text(), convert_salary(), normalize_titles(), etc.).
Write a main() that runs everything step by step.

📌 1. JSONL is your raw storage
JSONL is best as your immutable source of truth.
You scrape → save raw JSONL → never overwrite it.
(In case your cleaning introduces errors, you can always go back to raw.)

📌 2. Cleaning happens in memory
You load JSONL into Pandas DataFrame (like you’re already doing).
Apply all your cleaning functions (basic_clean_text, price_conversion, parse_date, etc.).
The transformations live in Python, not in the raw JSONL file.

📌 3. Save cleaned version to a new file
After cleaning, save into another format:
cleaned.jsonl (if you want to keep JSONL structure).
cleaned.csv (good for Excel/analysis).
cleaned.parquet (efficient for big datasets).
'''

import pandas as pd
import json


df = pd.read_json('Mechatronics_2025-08-30.jsonl', lines=True)
# print(df.head()) # Load to Data Frame, I think all Pandas Core Parts i can do all of it here 
# print(df.info()) # Data Type are all object # What ever that means, Shoud i care ? 

# Data Exploration Part, before Post Proccessing Thing i Should Data Explore it First
# column_1_role = df["Role"]
# print(column_1_role)

# Basically go for Data Exploration First before Diving into the Data Cleaning, Maybe Try to Automate or Find a way to Find the Dirty Stuff like what is common instead of 
# manually Checking things out 

r'''
"Focusing on Exploring the Dataset Instead of manual the goal is to figure out what is dirty creating a program to find the dirty data in the set off columns thing"
'''

########################## Location Data ##########################################
# column_2_role = df["Location"]
# print(column_2_role)
# Terms of Location i can do the Standardization, Picking Between Luzon, Visayas and Mindanao
r'''
Also i can concentrated Area of things Metro Manila, Or Calabarzon
Also i just know , how many Words that are Repeated in the things, to make it Some sort Concetrating in terms of locations 
'''

########################## Company Data ############################################
# column_3_role = df["Company"]
# print(column_3_role)
r'''
What Company is always Hiring i think in terms of this, maybe Create a Standardization of the company that are currently hiring 
'''

# column_4_role = df["Type"]
# print(column_4_role)

# In terms of Column no. 5 i can extract skills, which i already Do which is quite nice so It is really doesn't matter anymore man
# column_5_role = df["Description"]
# print(column_5_role)


r'''
After Exploring a little bit of the Data more on the standardization rather than cleaning white spaces because i already do it man 

1. Remove all Duplicates 
2. Find some Special Characters in each Column and try to Figure out What is common Special Characters
3. Standardization of Things 

So Far this is the Things i neeeded to do for data cleaning i think 

i Should Add Date In Extracting Data for Creating ISO Format
'''


df_csv = pd.read_csv('mechatronics_jobs_2025-08-13_with_skills.csv')
# print(df_csv.head())
# print(df_csv.info())


duplicates = df_csv.duplicated()
print(duplicates)
# print(duplicates.sum())  # Count duplicates
# Data Frame Look like This: 
r'''
	A	B
0	1	x
1	1	x
2	2	y
3	2	z
4	3	z

0    False   # first (1, 'x') → not a duplicate yet
1     True   # second (1, 'x') → duplicate of row 0
2    False   # (2, 'y') → new combination
3    False   # (2, 'z') → new combination
4    False   # (3, 'z') → new combination

print(duplicates.sum()) # Since True counts as 1 and False counts as 0, .sum() counts the number of duplicates.
 
So This Means in the 183 There are Similar in a Row which is i can remove it properly because if there are similar in a row it really have a duplicate at things
'''


# duplicate_rows = df_csv[df_csv.duplicated()]
# print(duplicate_rows)
# print(duplicate_rows.head(10))


# Experience in Doing the 
r'''
In terms of Doing things 
I should Install the Pykernel but that will take up time to set up the Environment so i needed some Things i needed to think about 

'''

# Understanding the Duplicates:
r'''
Based on the Duplicates it state that even if they have in same Columns but they are different in others columns it didn't count as duplicates
but if they all have the same data in all columns it means it consider a duplicate 

	* If two rows both have "Automation Engineer (UiPath) - 6290" as Job Title, and "Cambridge University Press & Assessment" as Company Name, and "Manila, Metro Manila" as Company Location, and the same Description, and the same extracted_skills list, etc. → ✅ they are duplicates.
	* If only the extracted_skills column matches (['sis']) but other columns differ (like different company name or job description), → ❌ they are not considered duplic
The duplicates you’re seeing now are full-row duplicates — entire rows that are 100% identical across all columns.
'''


# Remove all duplicate rows
# duplicate_rows = df_csv[df_csv.duplicated()] 
# duplicate_count = df_csv.duplicated().sum()
# print(duplicate_count)



# df_no_duplicates = df_csv.drop_duplicates(keep=False)
# df_no_duplicates = df_csv[df_csv.duplicated()]
# print(df_no_duplicates.head(10)) # Printing if it is drop 


# DataFrame Concepts 
r'''
Based on dropping it only in the data frame which is the memory of python but in the file of the csv itself it didn't drop anything 
'''


# # 1. Count duplicates
# print("Duplicates before dropping:", df_csv.duplicated().sum())

# # 2. Drop duplicates (keep first occurrence)
# df_no_duplicates = df_csv.drop_duplicates(keep='first')

# # 3. Count duplicates after
# print("Duplicates after dropping:", df_no_duplicates.duplicated().sum())