import pandas as pd
import sys
sys.stdout.reconfigure(encoding='utf-8')
from spacy.matcher import PhraseMatcher



# Focusing on Config file in here instead off Hard Coding it 
# File to be Read:
# df = pd.read_csv("")


# Drop the Duplicate in the Files 
# df.drop_duplicates(keep=False, inplace=True)
# df.to_csv("cleaned_data.csv", index=False)
# print("DROPPING THE DUPLICATES")


# Hard Skills that supposed to be extract
# hard_skills = [
#     # Robotics
#     "abb robotics",
#     "fanuc robotics",
#     "kuka robotics",
#     "machine vision systems",
#     "motion control systems",
#     "servo motor control",
#     "robot operating system (ros)",

#     # PLC, SCADA, DCS
#     "plc",
#     "programmable logic controller",
#     "ladder logic",
#     "rslogix",
#     "studio 5000",
#     "siemens tia portal",
#     "scada",
#     "supervisory control and data acquisition",
#     "ignition scada",
#     "wonderware intouch",
#     "kepware opc server",
#     "dcs",
#     "distributed control system",
#     "opc da",
#     "opc ua",

#     # Industrial Networking & Protocols
#     "ethernet/ip",
#     "modbus",
#     "profibus",
#     "foundation fieldbus",
#     "hart protocol",
#     "fieldbus protocols",
#     "mqtt",
#     "opc ua pub/sub",
#     "industrial networking",
#     "cybersecurity for industrial systems",

#     # Instrumentation & Sensors
#     "process instrumentation",
#     "instrument calibration",
#     "sensor integration",
#     "proximity sensors",
#     "flowmeters",
#     "thermocouples",
#     "rtd sensors",
#     "i/o module configuration",
#     "loop checking & commissioning",
#     "signal conditioning",

#     # Control Systems
#     "pid control",
#     "process safety systems",
#     "sis",
#     "control valves",
#     "advanced control theory",
#     "model predictive control",
#     "state-space control",
#     "adaptive control",

#     # Embedded Systems & Programming
#     "embedded systems",
#     "arduino",
#     "raspberry pi",
#     "stm32 microcontroller",
#     "c programming",
#     "c++ programming",
#     "python programming",
#     "labview",
#     "matlab",
#     "simulink",

#     # CAD/CAE & Simulation
#     "autocad electrical",
#     "eplan electric p8",
#     "solidworks",
#     "mechatronics design",
#     "catia",
#     "ptc creo",
#     "fusion 360",
#     "finite element analysis (fea)",
#     "ansys",
#     "comsol multiphysics",
#     "abaqus",
#     "digital twin technologies",
#     "simscape",

#     # Mechanical & Manufacturing Systems
#     "cnc programming",
#     "cnc machine operation",
#     "hydraulics systems",
#     "pneumatics systems design",
#     "additive manufacturing (3d printing)",
#     "vfd programming",

#     # Safety & Standards
#     "functional safety",
#     "iec 61511",
#     "iec 61508",
#     "iso standards for automation",
# ]


# df = pd.read_csv("File Naming")
# # job_description = df["Description"]
# Extracting the Skills in the Job Description Thing
# def extract_skills(text):
#     doc = nlp(text)
#     found = [skill for skill in hard_skills if skill.lower() in text.lower()]
#     return found
# df["extracted_skills"] = df["Description"].apply(extract_skills)

# Save new file
# df.to_csv("New Naming Things", index=False)
# print("✅ Done Extracting Skills. Saved to new CSV file.")