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

import spacy

# Load the English model
nlp = spacy.load("en_core_web_sm")

# Text to analyze
doc = nlp("Apple is looking at buying U.K. startup for $1 billion.")

# Print named entities
for ent in doc.ents:
    print(ent.text, ent.label_)





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
