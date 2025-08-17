import ast
import pandas as pd
from collections import Counter

r'''
ast → lets us safely convert a string like "['plc','scada']" into a real Python list.
pandas → for handling the CSV file and dataframe operations.
Counter → helps count occurrences of each skill easily.
'''

# load
df = pd.read_csv("cleaned_data.csv")

# list of terms you're interested in (use the one you provided)
terms = [
    "abb robotics","arduino","autocad electrical","control valves","cnc programming","daq",
    "data acquisition systems","dcs","distributed control system","eplan electric p8",
    "embedded systems","ethernet/ip","fanuc robotics","fieldbus protocols","flowmeters",
    "foundation fieldbus","hart protocol","hmi","human-machine interface","hydraulics systems",
    "ignition scada","industrial networking","instrument calibration","i/o module configuration",
    "kepware opc server","kuka robotics","ladder logic","loop checking & commissioning",
    "machine vision systems","matlab","simulink","mechatronics design","modbus",
    "motion control systems","opc da","opc ua","pid control","plc",
    "programmable logic controller","pneumatics systems design","process instrumentation",
    "process safety systems","sis","profibus","proximity sensors","rslogix","studio 5000",
    "rtd sensors","raspberry pi","scada","supervisory control and data acquisition",
    "sensor integration","servo motor control","signal conditioning","siemens tia portal",
    "solidworks","stm32 microcontroller","thermocouples","vfd programming","wonderware intouch"
]

# normalize search terms (lower + strip)
terms = [t.lower().strip() for t in terms]
terms_set = set(terms)
r'''
I already normalize it to small letter: 
Converts every term to lowercase and stripped of spaces (so " PLC " becomes "plc").
terms_set is a faster lookup set (optional optimization).

Short Way of Writing Things: terms = [t.lower().strip() for t in terms]
'''

# helper to parse each row into a Python list of strings
def parse_skills_cell(cell):  

    # Basically return an empty list if it is empty in a row? 
    if pd.isna(cell):
        return []
    r'''
    If the cell is empty (NaN), return an empty list → prevents errors.
    what is "isna"

    '''

    # if already a Python list (rare in csv), return normalized items
    if isinstance(cell, list):
        items = cell
    else:
        s = str(cell).strip()
        # try literal_eval for "['plc','ladder logic']" style strings
        r'''
        If the cell is already a Python list (rare in CSVs), use it directly.
        Otherwise, convert the cell into a string.
        
        in terms of If Statement why use "list"
        what does it mean by items = cell

        in Else part i don't understand it
        '''

    ## 
        try:
            parsed = ast.literal_eval(s)
            if isinstance(parsed, (list, tuple)):
                items = list(parsed)
            else:
                # fallback: treat as single string
                items = [str(parsed)]
        except Exception:
            # fallback: comma-separated string
            items = [item.strip() for item in s.split(",") if item.strip() != ""]
    
    
    # normalize each item to lowercase and strip
    return [str(i).lower().strip() for i in items]

# create a new column with parsed lists
df['skills_list'] = df['extracted_skills'].apply(parse_skills_cell)

# ---- A. Raw occurrence counts (counts duplicates if skill appears multiple times across rows)
all_tokens = [tok for lst in df['skills_list'] for tok in lst]
occurrence_counter = Counter(all_tokens)

# Keep only the terms we care about (others may exist)
occurrence_counts_for_terms = {term: occurrence_counter.get(term, 0) for term in terms}

# ---- B. Row counts (how many rows mention the term at least once)
row_counts = {}
for term in terms:
    # count rows where term is present in the list
    row_counts[term] = df['skills_list'].apply(lambda lst: term in lst).sum()

# ---- C. Make a DataFrame of results and sort by whichever metric you want
results = pd.DataFrame({
    'term': terms,
    'occurrences': [occurrence_counts_for_terms[t] for t in terms],
    'rows_with_term': [row_counts[t] for t in terms]
})

# sort by rows_with_term (descending) to see which skill appears in most rows
results_sorted_by_rows = results.sort_values('rows_with_term', ascending=False).reset_index(drop=True)

# also show top by total occurrences
results_sorted_by_occ = results.sort_values('occurrences', ascending=False).reset_index(drop=True)

# print / save
print("Top 20 skills by number of rows containing the skill:")
print(results_sorted_by_rows.head(20))

print("\nTop 20 skills by raw occurrences:")
print(results_sorted_by_occ.head(20))

# optionally save to csv for further inspection
# results_sorted_by_rows.to_csv("skill_counts_by_rows.csv", index=False)
# results_sorted_by_occ.to_csv("skill_counts_by_occurrences.csv", index=False)


import matplotlib.pyplot as plt

# ---- Top N skills by number of rows ----
top_n = 15  # adjust how many top skills you want to display

top_rows = results.sort_values('rows_with_term', ascending=False).head(top_n)

plt.figure(figsize=(10,6))
plt.barh(top_rows['term'], top_rows['rows_with_term'])
plt.gca().invert_yaxis()  # highest skill at the top
plt.title(f"Top {top_n} Skills by Number of Rows Containing the Skill")
plt.xlabel("Number of Rows (Job Posts)")
plt.ylabel("Skill")
plt.tight_layout()
plt.show()

# ---- Top N skills by raw occurrences ----
top_occ = results.sort_values('occurrences', ascending=False).head(top_n)

plt.figure(figsize=(10,6))
plt.barh(top_occ['term'], top_occ['occurrences'])
plt.gca().invert_yaxis()
plt.title(f"Top {top_n} Skills by Raw Occurrences")
plt.xlabel("Total Occurrences")
plt.ylabel("Skill")
plt.tight_layout()
plt.show()