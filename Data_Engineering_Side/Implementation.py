import pandas as pd
import spacy
from spacy.matcher import PhraseMatcher
import sys
sys.stdout.reconfigure(encoding='utf-8')

df = pd.read_csv("mechatronics_jobs_2025-08-13.csv")
job_description = df['Description']


# print(job_description) 
# for x in job_description:
#     print(x)
r'''
In terms of Pandas the Difference in Output is in for loop it print everything 
from the start to the end while the printing it as "job_description = df['Description']"

0      work setup: hybrid (open to 2x a week in the o...
1      educational requirements:\nbachelor's degree i...
2      deliver predictive and intelligent delivery ap...
3      designing and developing robust and efficient ...
4      position summary:this position holder is respo...
                             ...
712    select how often (in days) to receive an alert...
713    join to apply for the devops engineer role at ...
714    your roleyou will be a member of a highly skil...
715    job description\n\n\nconceptualize design and ...
716    🔍 what we’re looking for:\n\n\n✅ college under...
Name: Description, Length: 717, dtype: object

In Some Organize Way
'''

nlp = spacy.load("en_core_web_sm")
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
matcher = PhraseMatcher(nlp.vocab, attr="LOWER")
patterns = [nlp.make_doc(t) for t in terms]
matcher.add("TECH_TERMS", patterns)


def extract_skills(text):
    doc = nlp(text)
    found = [skill for skill in skills_list if skill.lower() in text.lower()]
    return found




# Component from the Chatgpt:
r'''
import pandas as pd
import spacy
from collections import Counter # What is this Code? 


# Load model
nlp = spacy.load("en_core_web_sm")

# Example DataFrame
# In terms of DataFrame What does it mean by that ? 
# If i can Extract the Description(job_description by Doing this)

df = pd.DataFrame({
    "job_description": [
        "Looking for an engineer with PLC and Python experience.",
        "Must have SQL, Tableau, and data visualization skills."
    ]
})
# If i can access the description in my program this means i can do this? 
# my code is 
# df = pd.read_csv("mechatronics_jobs_2025-08-13.csv")
# job_description = df['Description']


# # print(job_description) 
# # for x in job_description:
# #     print(x)
# What does it mean by data frame?

# Simple skill extraction (dummy example)
skills_list = ["PLC", "Python", "SQL", "Tableau", "data visualization"]

def extract_skills(text):
    doc = nlp(text)
    found = [skill for skill in skills_list if skill.lower() in text.lower()]
    return found
    # I don't Understand the For Loop of this can you Simplified this? 
    # something like for skill in skill_list? 
    # What kind Writing is this part? 

# Apply function to each row
df["extracted_skills"] = df["job_description"].apply(extract_skills)
# Based on my Analyzing your code 
# Why df["extracted_skills"]
# Why df["job_description"].apply(extract_skills) 
# Explain me this line by line of this code

# Also this Code can you Explain this line by line 
# Analyze most common skills
all_skills = df["extracted_skills"].explode()
skill_counts = all_skills.value_counts()

print(df)
print(skill_counts)
'''



# Analyzing the code that Chatgpt give me: 
r'''
import pandas as pd
import spacy
from collections import Counter
'''
# pandas as pd → we import pandas, and give it the nickname pd (convention).

# spacy → loads the NLP library for text processing.

# Counter → comes from Python’s collections module. 
# It counts how many times each item appears. 
# (we didn’t use it directly here, but it’s often used for frequency analysis, 
#  like counting words or skills).

############## 

r'''nlp = spacy.load("en_core_web_sm")'''
# Loads a small English NLP model.

# With nlp(text), you turn text into a Doc object that 
# spaCy can analyze (tokens, POS tags, named entities, etc.).

############## 

r'''
What is DataFrame?
    Think of a spreadsheet in Python.
    Rows = entries (e.g., job postings).
    Columns = features (e.g., job description, salary, location).
'''
r'''
df = pd.read_csv("mechatronics_jobs_2025-08-13.csv")
job_description = df["Description"]
'''
# ✅ If you load your real CSV:

############## 

# This is a List Comprehension a Shortvut for a loop

r'''
def extract_skills(text):
    doc = nlp(text)
    found = [skill for skill in skills_list if skill.lower() in text.lower()]
    return found
'''
# Analyzing this based on my Understanding 
# an Extraction of Skills in a text 

r'''
[skill for skill in skills_list if skill.lower() in text.lower()]
'''
# Equivalent in a long form:
r'''
found = []
for skill in skills_list:
    if skill.lower() in text.lower():
        found.append(skill)
'''

############## 