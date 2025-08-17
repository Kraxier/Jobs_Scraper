# Data Analysis of Skills 
# Inspiration by Datanerd Youtube Channel 
r'''
Focusing in Automation and Mechatronics
What is the Goal? 

Asking questions and finding patterns:
Descriptive stats → “What happened?”
Exploratory analysis → “What might be happening?”
Tools: Jupyter, SQL, Excel, Tableau, Power BI.
'''
# import pandas as pd
# import sys
# sys.stdout.reconfigure(encoding='utf-8')

# df = pd.read_csv("cleaned_data.csv")
# df_exploded = df.explode("extracted_skills")
# df_exploded.to_csv("exploded_data.csv", index=False, encoding="utf-8")
# print(df_exploded.head())
# skill_counts = df_exploded["extracted_skills"].value_counts()
# skill_counts_df = skill_counts.reset_index()
# skill_counts_df.columns = ["skill", "count"]

# # Save to CSV
# skill_counts_df.to_csv("skill_counts.csv", index=False, encoding="utf-8")
# print(skill_counts)

import pandas as pd
import sys
sys.stdout.reconfigure(encoding='utf-8')

df = pd.read_csv("cleaned_data.csv")

# 🔹 explode the skills list column into individual rows
df_exploded = df.explode("extracted_skills")

# 🔹 save exploded data
df_exploded.to_csv("exploded_data.csv", index=False, encoding="utf-8")
print(df_exploded.head())

# 🔹 count skills
skill_counts = df_exploded["extracted_skills"].value_counts()

# 🔹 convert to DataFrame
skill_counts_df = skill_counts.reset_index()
skill_counts_df.columns = ["skill", "count"]

# 🔹 save counts
skill_counts_df.to_csv("skill_counts.csv", index=False, encoding="utf-8")

print(skill_counts)

r'''
Figuring out what is the Top Skill for Mechatronics or Automation
What Location is the Demand thing 
'''

r'''
Realization After Scrapping Things i think There are so much to do man 

Role of the Job:
Company Name:
Company Location:  
Type of Work: 
Description:
Extracted Skills: 
'''

r'''
Maybe i Should do Data Cleaning First Before Analyzing Things
Maybe i Should Include the Date it Posted 
'''
