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
# df_exploded = df.explode("extracted_skills")

# 🔹 save exploded data
# df_exploded.to_csv("exploded_data.csv", index=False, encoding="utf-8")
# print(df_exploded.head())

# 🔹 count skills
# skill_counts = df_exploded["extracted_skills"].value_counts()

# 🔹 convert to DataFrame
# skill_counts_df = skill_counts.reset_index()
# skill_counts_df.columns = ["skill", "count"]

# 🔹 save counts
# skill_counts_df.to_csv("skill_counts.csv", index=False, encoding="utf-8")
# print(skill_counts)

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


r'''
Let's Focus on the Key Things 
    1. Per Row there are List:
        ['plc', 'programmable logic controller', 'scada', 'supervisory control and data acquisition', 'dcs', 'distributed control system', 'modbus', 'cybersecurity for industrial systems', 'sis']
        ['plc', 'ladder logic', 'sis', 'c programming']
        ['plc', 'scada', 'dcs', 'ethernet/ip', 'modbus', 'profibus', 'c programming', 'matlab', 'simulink']

Using Pandas i want to Count how many "plc" in a certain File

df = pd.read_csv("cleaned_data.csv")
skill = df['extracted_skills'] # Name of the Column that have this ['plc', 'ladder logic', 'sis', 'c programming']

# Using the for loop for each row i will extract that have "plc" in the row and count it and note not just plc but for every "term"
terms = [
    "abb robotics",
    "arduino",
    "autocad electrical",
    "control valves",
    "cnc programming",
    "daq",
    "data acquisition systems",
    "dcs",
    "distributed control system",
    "eplan electric p8",
    "embedded systems",
    "ethernet/ip",
    "fanuc robotics",
    "fieldbus protocols",
    "flowmeters",
    "foundation fieldbus",
    "hart protocol",
    "hmi",
    "human-machine interface",
    "hydraulics systems",
    "ignition scada",
    "industrial networking",
    "instrument calibration",
    "i/o module configuration",
    "kepware opc server",
    "kuka robotics",
    "ladder logic",
    "loop checking & commissioning",
    "machine vision systems",
    "matlab",
    "simulink",
    "mechatronics design",
    "modbus",
    "motion control systems",
    "opc da",
    "opc ua",
    "pid control",
    "plc",
    "programmable logic controller",
    "pneumatics systems design",
    "process instrumentation",
    "process safety systems",
    "sis",
    "profibus",
    "proximity sensors",
    "rslogix",
    "studio 5000",
    "rtd sensors",
    "raspberry pi",
    "scada",
    "supervisory control and data acquisition",
    "sensor integration",
    "servo motor control",
    "signal conditioning",
    "siemens tia portal",
    "solidworks",
    "stm32 microcontroller",
    "thermocouples",
    "vfd programming",
    "wonderware intouch"
]

The Output that i want for every term i want to see What is the most Skill are needed basically counting what is the highest Skills 

'''