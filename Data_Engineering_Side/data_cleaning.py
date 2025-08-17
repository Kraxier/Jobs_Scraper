import pandas as pd
import sys
sys.stdout.reconfigure(encoding='utf-8')

# What is Data Cleaning?
r'''
Data cleaning (sometimes called data wrangling or data preprocessing) is the process of fixing, 
correcting, and organizing raw data so it can be used effectively for analysis or machine learning.
'''
# What does it mean by Raw Data:
r'''
Missing values
Duplicates
Wrong data types
Inconsistent formats
Outliers (values that don’t make sense)
'''

# Reflection of Mine:
r'''
Investigating if my Data is Messy First Figuring out Things to Do 
'''


df = pd.read_csv("mechatronics_jobs_2025-08-13_with_skills.csv")
# print(df)

# Data Exploration for Data Cleaning 
# head = df.head()
# print(head)
r'''
Output:
                           Role of Job  ...                                   extracted_skills
0  Automation Engineer (UiPath) - 6290  ...                                            ['sis']
1                       Scada Engineer  ...  ['plc', 'programmable logic controller', 'scad...
2      Application Automation Engineer  ...                                                 []
3         System (Automation) Engineer  ...  ['plc', 'programmable logic controller', 'scad...
4  Energy Management System Specialist  ...  ['plc', 'programmable logic controller', 'scad...
[5 rows x 6 columns]
The Upper Part of the Data good Overview of Things
'''

# info = df.info()
# print(info)
r'''
Output:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 717 entries, 0 to 716
Data columns (total 6 columns):
 #   Column            Non-Null Count  Dtype 
---  ------            --------------  ----- 
 0   Role of Job       717 non-null    object
 1   Company Name      701 non-null    object
 2   Company Location  717 non-null    object
 3   Type of Work      125 non-null    object
 4   Description       717 non-null    object
 5   extracted_skills  717 non-null    object
dtypes: object(6)
memory usage: 33.7+ KB
None

Reflection: 
RangeIndex is the Row of Data
I can see The Number of Columns also the 
What kind of Data Type: Object
The Name of the Columns 
Why is it Important for Memory Usage Thing? 
What does it mean by Non-Null Type?
Why is it Important to Know about the Missing Value Aka Non-Null (Correct me if I'm Wrong Here)

'''
# describe = df.describe()
# print(describe)
r'''
                   Role of Job  ... extracted_skills
count                      717  ...              717
unique                     373  ...               53
top     QA Automation Engineer  ...               []
freq                        20  ...              340

[4 rows x 6 columns]

Reflection:
Describe is i think is useful for finding pattern but how powerful it is? 
Basically Why i needed to know: 
count,unique,top, and Frequency
'''

df.drop_duplicates(keep=False, inplace=True)
df.to_csv("cleaned_data.csv", index=False)
print("DROPPING THE DUPLICATES")



#######################################################################
################### Chatgpt Explanation Part Data Exploration ##########################
#######################################################################

############# df.info() Output (Exploring Structure) #############

# 1. RangeIndex
# RangeIndex: 717 entries, 0 to 716
r'''
Tells you the dataset has 717 rows (records).
Index runs from 0 to 716.
Important because it confirms the size of your dataset before analysis.
'''
# 2. Columns + Dtypes
# Data columns (total 6 columns):
# 0   Role of Job       object
# 1   Company Name      object
r'''
Lists each column and its data type:
object → usually text (string), sometimes mixed types.
int64, float64 → numeric values.
datetime64 → dates.
Important: Sometimes numbers get read as text 
    (e.g., "1000" instead of 1000). 
    If you don’t fix this, calculations won’t work.
'''
# 3. Non-Null Count
# Company Name      701 non-null
# Type of Work      125 non-null
r'''
Shows how many non-missing values exist per column.
Example: Company Name has 701 values → means 16 are missing (717 - 701).
Type of Work is missing a lot (717 - 125 = 592 values missing!).

👉 Why it’s important:
If a column is missing too many values, it might be useless or require special treatment (like filling in or dropping).
Knowing missing values upfront helps you plan your cleaning strategy.
'''
# 4. Memory Usage
# memory usage: 33.7+ KB
r'''
Tells you how much RAM your dataset uses.

This matters when working with large datasets (millions of rows). Small datasets like this aren’t a problem, 
but for big data, optimizing memory can make your work faster.
'''
r'''
✅ So yes, "Non-Null" ≈ "Not Missing" values.
Missing values are a key problem in data cleaning because they can break calculations, 
distort statistics, or reduce model accuracy.
'''

############# 🔹 df.describe() Output (Exploring Distribution #############
r'''
Since all your columns are categorical (object), Pandas shows summary statistics for text data instead of numbers:
count   = total non-null entries
unique  = number of unique categories
top     = most frequent category
freq    = frequency of that top value

Example:
Role of Job  
count    717
unique   373
top      QA Automation Engineer
freq     20

373 unique job roles in 717 rows → lots of variety.
The most common role is QA Automation Engineer (20 times).
This gives a quick snapshot of distribution without plotting.
'''
# Why is describe() powerful?
r'''
For categorical data: helps spot dominant categories, rare values, and potential typos (like "USA" vs "U.S.A." vs "usa").
For numeric data (when you have numbers): it shows mean, median, min, max, standard deviation → crucial for spotting outliers.
'''
# 🔹 Why These Tools Matter

r'''
df.info() → structure, completeness, data types. (Good for spotting missing values + wrong data types).
df.describe() → distribution, uniqueness, common patterns. (Good for spotting trends + anomalies).

Together, they answer:
What do I have?
Is it clean or messy?
Where are the gaps?
What stands out?
'''


##########################################################################
################################## Data Cleaning #########################
##########################################################################

r'''
🔹 Components of Data Cleaning with Pandas

Here are the key steps you’ll typically work on:

Load the Data

Read data from CSV, Excel, SQL, JSON, etc.

import pandas as pd
df = pd.read_csv("data.csv")


Understand the Data (Exploration)

Look at rows, columns, and data types.

df.head()
df.info()
df.describe()


Handle Missing Data

Find missing values (NaN) and decide whether to fill them in or remove them.

df.isnull().sum()
df.fillna(0, inplace=True)   # fill missing values
df.dropna(inplace=True)      # remove missing values


Fix Data Types

Ensure columns have correct types (numbers, dates, categories, etc.).

df['date'] = pd.to_datetime(df['date'])
df['price'] = df['price'].astype(float)


Remove Duplicates

df.drop_duplicates(inplace=True)


Handle Inconsistent Data / Formatting

Standardize categories, fix typos, or adjust case.

df['city'] = df['city'].str.strip().str.lower()


Handle Outliers

Detect values that are unusually high/low.

df[df['age'] > 100]   # check unrealistic ages


Feature Engineering (optional)

Create new useful columns from existing data.

df['full_name'] = df['first_name'] + " " + df['last_name']


Save the Cleaned Data

df.to_csv("cleaned_data.csv", index=False)
'''