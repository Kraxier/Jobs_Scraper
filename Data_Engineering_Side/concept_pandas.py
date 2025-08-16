# Relearning the Pandas 
import pandas as pd
import sys
sys.stdout.reconfigure(encoding='utf-8')

df = pd.read_csv("mechatronics_jobs_2025-08-13.csv")

head = df.head()  
print(head)

# What is the Goal of Pandas?
# I think this is Data Cleaning and Transformation 
# Combining it to spaCy to Extract Some Hard Skill in Job Description for example "PLC"
# And create a  another Column where i can store it 

# Data Analysis 
# Calculating What is the Most Demand Skill in the Data Stuff


r'''
First is i need to Access a Certain Columns
and then for each column (For Loops) run the spaCy thing where it Extract things 
and then my pandas store that in a new column thing 
'''

################################################################################################################
############################################ Concepts of Pandas ################################################
################################################################################################################

# What is Pandas?
r'''
Pandas is a Python library for working with tabular data (like spreadsheets, SQL tables, CSV files).

Series → 1D labeled array (like a column)
DataFrame → 2D labeled table (like a spreadsheet)
'''

# How To Import Pandas?
r'''
import pandas as pd

The convention is always pd.
'''

# How to Create a Data?
r'''
You can create data from Python lists, dictionaries, or external files.

Examples:
# Series
s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])

# DataFrame from dict
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['NY', 'LA', 'Chicago']
})

'''

# How to Read and Write the Data?
r'''
# Read from CSV
df = pd.read_csv('data.csv')

# Save to CSV
df.to_csv('output.csv', index=False)

# Other formats: Excel, JSON, SQL
df.to_excel('data.xlsx', index=False)

'''

# How to Explore the Data:
r'''
df.head()      # First 5 rows
df.tail()      # Last 5 rows
df.shape       # (rows, columns)
df.columns     # Column names
df.info()      # Data types & non-null counts
df.describe()  # Summary statistics
'''

# How to Select the Data?
r'''
# Column
df['Name']            # Series
df[['Name', 'Age']]   # Multiple columns

# Row by index
df.loc[0]             # By label/index
df.iloc[0]            # By position

# Row + Column
df.loc[0, 'Name']     # First row, "Name" column
'''
# How to Filter the Data?
r'''
# Filter by condition
df[df['Age'] > 30]

# Multiple conditions
df[(df['Age'] > 25) & (df['City'] == 'NY')]
'''
# How to Modify the Data?
r'''
# Add new column
df['Age in 5 Years'] = df['Age'] + 5

# Update values
df.loc[df['Name'] == 'Alice', 'Age'] = 26

# Drop column/row
df.drop(columns=['City'], inplace=True)
df.drop(index=0, inplace=True)
'''

# How to Aggregate and Group the Data?
r'''
df['Age'].mean()    # Average age
df.groupby('City')['Age'].mean()  # Avg age per city
'''
#  How to Sort the Data?
r'''
df.sort_values(by='Age', ascending=False)
df.sort_index()
'''

# How to Handle Missing Data?
r'''
df.isna()           # Check missing
df.fillna(0)        # Replace missing with 0
df.dropna()         # Drop missing rows
'''

# How to Merge? 
r'''
pd.merge(df1, df2, on='ID')      # SQL-style join
pd.concat([df1, df2], axis=0)    # Stack rows
'''

# What kind of job can pandas fulfill?
r'''
Pandas is designed for data manipulation, cleaning, and analysis.
It’s not a “job” in itself but a tool that powers many job roles, such as:

    * Data Analyst – analyzing trends, creating reports, making dashboards.
    * Data Scientist – preparing datasets for machine learning, statistical analysis.
    * Business Analyst – turning raw business data into insights.
    * Financial Analyst – processing stock data, sales reports, or budgets.
    * Researcher – cleaning survey data, preparing datasets for experiments.
    * Engineer (ETL/Data Engineer) – moving and transforming data between systems.

Basically: if your work involves structured data (tables, CSVs, Excel, SQL), pandas can help.
'''
# Who Uses pandas? 
r'''
You’ll find pandas in use by:

    * Tech companies – for log analysis, A/B testing results, user analytics.
    * Banks/Finance – for time-series stock data, risk modeling, fraud detection.
    * Healthcare – for patient records, trial data, medical research datasets.
    * Government & NGOs – census data, economic reports, social research.
    * Academia – data cleaning & statistical prep for scientific studies.
    * E-commerce – product sales analytics, customer behavior analysis.

Pandas is like Excel for programmers, so anywhere Excel is used, pandas can often replace or enhance it.
'''


# What i can do With Pandas? 
r'''
Data Cleaning
    * Remove duplicates
    * Fill in missing values
    * Rename or reorder columns
    * Fix wrong data types

Data Transformation
    * Merge/join multiple datasets
    * Group data and summarize it (totals, averages, counts)
    * Pivot and reshape tables
    * Apply custom functions to each row or column

Data Analysis
    * Calculate statistics (mean, median, std, correlations)
    * Find trends over time (time-series analysis)
    * Identify outliers
    * Filter specific conditions

Data Input/Output
    * Read/write CSV, Excel, JSON, SQL, Parquet, and more
    * Handle millions of rows much faster than Excel
    * Automate repetitive reporting

Visualization (with help from matplotlib/seaborn)
    * Quick charts (bar, line, scatter)
    * Time-series plots
    * Histograms
'''