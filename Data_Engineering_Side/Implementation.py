import pandas as pd
import spacy
from spacy.matcher import PhraseMatcher
import sys
sys.stdout.reconfigure(encoding='utf-8')

nlp = spacy.load("en_core_web_sm")
hard_skills = [
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
df = pd.read_csv("mechatronics_jobs_2025-08-13.csv")
# job_description = df["Description"]
def extract_skills(text):
    doc = nlp(text)
    found = [skill for skill in hard_skills if skill.lower() in text.lower()]
    return found
df["extracted_skills"] = df["Description"].apply(extract_skills)


# Save new file
df.to_csv("mechatronics_jobs_2025-08-13_with_skills.csv", index=False)
# df.to_csv("mechatronics_jobs_2025-08-13.csv", index=False) This Overwrite the File which is not good at all
r'''
to_csv → writes the DataFrame back to a file.

"mechatronics_jobs_2025-08-13_with_skills.csv" → creates a new file with extracted skills.

index=False → prevents pandas from writing row numbers into the CSV.
'''
print("✅ Done Extracting Skills. Saved to new CSV file.")

r'''
My Files are currently at 2k kb and it taking a time to do all of it 
'''
################################################
########## Determining Output ##################
################################################
r'''
Option 1: List Format → ['PLC', 'Python']

✅ Pros
Perfect for pandas/Python:
    You can easily .explode() the list into separate rows.
    You can count frequencies directly.
    Keeps skills structured as a true data type (list of strings).
    Works well if you’ll keep analyzing inside Python.

❌ Cons
    If you open it in Excel → it looks messy (['PLC', 'Python']).
    Harder to filter/sort in Excel or BI tools.

Option 2: String Format → "PLC, Python"
✅ Pros
    Clean & human-readable in Excel, CSV, Tableau, Power BI.
    Easy to share with non-programmers.
    Looks like normal text (no brackets/quotes).

❌ Cons
    In Python, you lose the “list” structure:
    If you want to re-analyze, you need to split it back:
        df["extracted_skills"].str.split(", ")
⚖️ So which is better?
If you’re going to do most of your analysis in pandas/Python → keep it as a list (['PLC', 'Python']).
If you’re going to share/export to Excel, Tableau, Power BI → use a string ("PLC, Python").

or You can Keep both:
df["extracted_skills_list"] = df["Description"].apply(extract_skills)              # List format
df["extracted_skills_text"] = df["extracted_skills_list"].apply(lambda x: ", ".join(x))  # String format
extracted_skills_list: ['PLC', 'Python']
extracted_skills_text: PLC, Python
'''

###################### Wanting to See the Progress of the Extraction 
r'''
🚀 Recommendation
If you’re serious about analyzing big CSVs → use tqdm. 
It integrates with pandas, is lightweight, 
and gives you a real progress bar without changing much code.
'''

r'''
1. Use tqdm Progress Bar
from tqdm import tqdm
tqdm.pandas()  # adds .progress_apply to pandas

# Instead of apply()
df["extracted_skills"] = df["Description"].progress_apply(extract_skills)

100%|██████████████████████████| 5000/5000 [00:45<00:00, 110/s]
'''

r'''
2. Print Every N Rows (manual feedback)
def extract_skills_with_progress(text, idx=None, total=None):
    found = []
    for skill in hard_skills:
        if skill.lower() in str(text).lower():
            found.append(skill)
    if idx is not None and idx % 100 == 0:  # print every 100 rows
        print(f"Processed {idx}/{total}")
    return found

total_rows = len(df)
df["extracted_skills"] = [
    extract_skills_with_progress(text, idx, total_rows)
    for idx, text in enumerate(df["Description"])
]

Processed 0/5000
Processed 100/5000
Processed 200/5000
'''

# 3. Time Estimation
r'''
import time
start = time.time()

df["extracted_skills"] = df["Description"].progress_apply(extract_skills)

end = time.time()
print(f"✅ Done in {end - start:.2f} seconds")
'''

