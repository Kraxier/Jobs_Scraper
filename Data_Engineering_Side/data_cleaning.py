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

info = df.info()
print(info)
r'''
Output:

'''
# print()
# df.describe()