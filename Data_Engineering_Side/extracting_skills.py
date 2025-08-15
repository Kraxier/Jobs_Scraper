# python extracting_skills.py

# Installing:
r'''
pip install spacy
'''
# Download Language Model:
# python -m spacy download en_core_web_sm
r'''
The model name means:
    en = English

    core = general-purpose
    web = trained on web text
    sm = small size (fast, less accurate than medium/large)
'''

# For Heavier Proccessing 
r'''
python -m spacy download en_core_web_md   # medium
python -m spacy download en_core_web_lg   # large
'''

# # Importing spaCy
# import spacy

# # Imports spaCy’s PhraseMatcher, a fast rule-based matcher for finding exact phrases (token sequences) in a Doc.
# from spacy.matcher import PhraseMatcher

# Importing Pandas in my Script 
import pandas as pd

import sys
sys.stdout.reconfigure(encoding='utf-8')


# 1. Load your CSV file
df = pd.read_csv("mechatronics_jobs_2025-08-13.csv")
# print(df) Printing out the csv file thing 

# 2. Load spaCy model
nlp = spacy.load("en_core_web_sm")

# 3. Define the keywords you want to find
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



# 4. Create the PhraseMatcher
# matcher = PhraseMatcher(nlp.vocab, attr="LOWER")
# patterns = [nlp.make_doc(t) for t in terms]
# matcher.add("TECH_TERMS", patterns)



######################################### Concepts ###############################

# Why Choose spaCy?
r'''
Pick spaCy as your core tool — it can scale from a simple predefined skill 
list matcher to an advanced NLP-based extractor.
'''

# What is spaCy?
r'''
spaCy is an open-source library for Natural Language Processing (NLP)
basically, it helps computers work with human language in a structured, intelligent way.
'''

# Characteristic:
r'''
Tokenization – splitting text into words, punctuation, etc. (What i needed)
Part-of-speech tagging – identifying nouns, verbs, adjectives, etc.
Named entity recognition (NER) – finding entities like names, places, dates, currencies.
Dependency parsing – figuring out how words relate grammatically.
Lemmatization – reducing words to their root form.
Text similarity & word vectors – measuring how similar two pieces of text are.
'''
# What does it mean by Natural Language Proccessing?
r'''
Natural Language Processing (NLP) is the field of computer science and 
AI that focuses on enabling computers to understand, interpret, and generate human language — whether spoken or written.

In other words, NLP is about teaching machines to work with natural (human) languages instead of programming languages.
'''

# What NLP can Do?
r'''
What NLP can do

Some common tasks in NLP include:
    Text classification – sorting messages as spam or not spam.
    Sentiment analysis – figuring out if a review is positive, negative, or neutral.
    Machine translation – translating between languages (e.g., English ↔ Spanish).
    Speech recognition – turning spoken words into text.
    Named entity recognition (NER) – finding names, dates, places, etc., in text.
    Chatbots & virtual assistants – understanding your questions and responding.
    Summarization – condensing large documents into shorter summaries
'''

# What is Pandas in python?
r'''
is a powerful open-source data analysis and manipulation library.
It’s built on top of NumPy and is designed to make working with structured data (like tables, spreadsheets, or databases) easier.
'''
# What are Key Things about Pandas?
r'''
Name origin: It comes from “Panel Data,” a term for multidimensional structured datasets in statistics.

Core objects:
    Series → A one-dimensional labeled array (like a column in Excel).
    DataFrame → A two-dimensional labeled data structure (like a spreadsheet or SQL table).
'''

# What are Feature of Pandas?
r'''
Features:
    * Reading/writing data from CSV, Excel, SQL, JSON, etc.
    * Data cleaning (handling missing values, renaming columns, dropping duplicates).
    * Powerful data selection and filtering (loc, iloc).
    * Grouping, aggregating, and summarizing data.
    * Time series handling.
'''

# How to Install Pandas?
r'''
pip install pandas
'''



# Simple Program:
# Importing spaCy
# import spacy

# Load the English model
# nlp = spacy.load("en_core_web_sm")

# # Text to analyze
# doc = nlp("Apple is looking at buying U.K. startup for $1 billion.")

# # Print named entities
# for ent in doc.ents:
#     print(ent.text, ent.label_)