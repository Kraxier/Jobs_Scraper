import pandas as pd
import spacy 
from spacy.matcher import PhraseMatcher
import sys
sys.stdout.reconfigure(encoding='utf-8')

nlp = spacy.load("en_core_web_sm") 
r'''
Concept of nlp
spacy is a popular NLP (Natural Language Processing) library in Python.
"en_core_web_sm" is one of spaCy’s pre-trained English models:
    en → English
    core → general-purpose model
    web → trained on web text
    sm → small size (fast, lightweight, lower accuracy compared to larger models)

So, nlp becomes the processing pipeline object you can use to tokenize text, perform part-of-speech tagging, named entity recognition (NER), dependency parsing, etc.

English models
    * en_core_web_sm → small (~12MB, fast, less accurate)
    * en_core_web_md → medium (~40MB, includes word vectors)
    * en_core_web_lg → large (~800MB, most accurate, with full word vectors
    
'''

r'''
Why? 
This is the List of the Skills that i want to extract in the JOB description 
The Hard Skills of Mechatronics/Instrumentation 
'''
hard_skills = [
    # Robotics
    "abb robotics",
    "fanuc robotics",
    "kuka robotics",
    "machine vision systems",
    "motion control systems",
    "servo motor control",
    "robot operating system (ros)",

    # PLC, SCADA, DCS
    "plc",
    "programmable logic controller",
    "ladder logic",
    "rslogix",
    "studio 5000",
    "siemens tia portal",
    "scada",
    "supervisory control and data acquisition",
    "ignition scada",
    "wonderware intouch",
    "kepware opc server",
    "dcs",
    "distributed control system",
    "opc da",
    "opc ua",

    # Industrial Networking & Protocols
    "ethernet/ip",
    "modbus",
    "profibus",
    "foundation fieldbus",
    "hart protocol",
    "fieldbus protocols",
    "mqtt",
    "opc ua pub/sub",
    "industrial networking",
    "cybersecurity for industrial systems",

    # Instrumentation & Sensors
    "process instrumentation",
    "instrument calibration",
    "sensor integration",
    "proximity sensors",
    "flowmeters",
    "thermocouples",
    "rtd sensors",
    "i/o module configuration",
    "loop checking & commissioning",
    "signal conditioning",

    # Control Systems
    "pid control",
    "process safety systems",
    "sis",
    "control valves",
    "advanced control theory",
    "model predictive control",
    "state-space control",
    "adaptive control",

    # Embedded Systems & Programming
    "embedded systems",
    "arduino",
    "raspberry pi",
    "stm32 microcontroller",
    "c programming",
    "c++ programming",
    "python programming",
    "labview",
    "matlab",
    "simulink",

    # CAD/CAE & Simulation
    "autocad electrical",
    "eplan electric p8",
    "solidworks",
    "mechatronics design",
    "catia",
    "ptc creo",
    "fusion 360",
    "finite element analysis (fea)",
    "ansys",
    "comsol multiphysics",
    "abaqus",
    "digital twin technologies",
    "simscape",

    # Mechanical & Manufacturing Systems
    "cnc programming",
    "cnc machine operation",
    "hydraulics systems",
    "pneumatics systems design",
    "additive manufacturing (3d printing)",
    "vfd programming",

    # Safety & Standards
    "functional safety",
    "iec 61511",
    "iec 61508",
    "iso standards for automation",
]
#  Load the CSV file and putting it to dataframe and using that dataframe to do things 
df = pd.read_csv("mechatronics_jobs_2025-08-13.csv")
r'''
This means i can do multiple reading with different names and variables

df_1 = pd.read_csv("")
df_2 = pd.read_csv("")
df_3 = pd.read_csv("")

Other Alternative is you can do even
Excel → pd.read_excel("file.xlsx")
Database → pd.read_sql(query, connection)
JSON → pd.read_json("file.json")

Strength of Pandas is: 
you can load multiple datasets (multiple DataFrames) and then compare, merge, or analyze them.
You can do Side by Side Statistic, Combine and Compare, Column Comparison, Merging and Joining
'''

def extract_skills(text):
    doc = nlp(text) 
    r'''
    * This runs the text through spaCy’s pipeline (tokenizer, POS tagging, NER, etc.).
    * Using the doc it means i can do spaCy features
    * researching what are the spaCy Feature if i needed 
    '''
    found = [skill for skill in hard_skills if skill.lower() in text.lower()]
    r'''
    Shortened for List and For Loops 

    found = []
    for skill in hard_skills:
        if skill.lower() in text.lower():
            found.append(skill)
    '''
    return found

df["extracted_skills"] = df["Description"].apply(extract_skills)
r'''
df["Description"] → the column in your CSV with job descriptions.
.apply(extract_skills) → runs the function extract_skills on each row of that column.
df["extracted_skills"] → creates a new column containing the list of skills found per job posting.
'''

