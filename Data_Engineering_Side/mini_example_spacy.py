# python mini_example_spacy.py
import spacy
from spacy.matcher import PhraseMatcher
import pandas as pd
import sys
sys.stdout.reconfigure(encoding='utf-8')

nlp = spacy.load("en_core_web_sm")
# terms = ["PLC", "HMI", "SCADA", "ladder logic"]
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

print(matcher) # output: <spacy.matcher.phrasematcher.PhraseMatcher object at 0x000002566DDFEB90>
print()
print(patterns) # Output: terms(the List)

doc = nlp("We program PLCs and design HMI for SCADA, using ladder logic.")
for match_id, start, end in matcher(doc):
    r'''
    matcher(doc) runs the PhraseMatcher on your processed text (doc).
    It returns a list of tuples in the form:
        (match_id, start, end)

1. match_id → An integer ID for the match’s label (like "TECH_TERMS").
You convert this back to a string later.
2. start → The index of the first matched token in doc.
3. end → The index after the last matched token in doc (Python-style slicing).
    '''
    print(doc[start:end].text, nlp.vocab.strings[match_id])
    # doc[start:end].text
    r'''
    doc[start:end] slices the Doc to create a Span — basically the chunk of text that matched.

    .text converts that span to a string

    Example:
    If start=3 and end=4 and the 4th token is "PLC", then doc[start:end].text = "PLC".
    '''
    # nlp.vocab.strings[match_id]
    r'''
    Since match_id is just an integer, you use nlp.vocab.strings[...] to get its string label back.

    This will give you "TECH_TERMS" (or whatever you named your matcher rule).
    '''
    # Putting it Together: 
    r'''
    If you matched "PLC" in the text:

    match_id → integer (e.g., 12345678)

    start → 3

    end → 4

    doc[start:end].text → "PLC"

    nlp.vocab.strings[match_id] → "TECH_TERMS"
    '''


r'''
Creates a PhraseMatcher, a fast rule-based matcher for exact phrases (sequences of tokens).
'''
matcher = PhraseMatcher(nlp.vocab, attr="LOWER") # It shares your pipeline’s vocabulary (nlp.vocab) so matches use the same lexicon/tokenization as your Doc.
# attr="LOWER" means “match on the lowercased form of tokens,” so "PLC", "plc", and "Plc" all match the same pattern.
# (If you omit this, matching is case-sensitive. Other options include "ORTH" exact text, "LEMMA" lemma, "NORM" normalized text.)


patterns = [nlp.make_doc(t) for t in terms]
# Turns each string in your terms list (e.g., ["PLC", "HMI", "SCADA", "ladder logic"]) into a Doc using spaCy’s tokenizer only.
# Multi-word terms like "ladder logic" become a two-token Doc, so the matcher will look for that exact token sequence in your text.

matcher.add("TECH_TERMS", patterns)
r'''
Registers all those Docs as patterns under the rule name "TECH_TERMS".
Internally, that name is mapped to an integer match_id; when you iterate matches you can recover the name with nlp.vocab.strings[match_id]. # What do you mean by this part?
You can call add multiple times with different names to group different sets of phrases (e.g., "HARDWARE_TERMS", "SOFTWARE_TERMS"). # Also on this part 
'''