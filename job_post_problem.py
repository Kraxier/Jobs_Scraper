

# Conclusion after the Research 
r'''
1. Extraction Stage:
    * Goal Extract the Entire Job Description 
    * Store it in a CSV Files
2. Clean Stage:
    * lowercase Everything 
    * Remove HTML tag if there are HRMl Tag
    * Remove Duplicate 
3. Structuring Stage:
    * Skills → keyword match + NLP (e.g., spaCy, SkillNER).
    * Salary → regex → numeric range.
    * Requirements → sentence filtering (“must have”, “degree in”, etc.).
    
'''
# Understanding the Goal:

r'''
What Data do I Actually want in a Job Post?
in term of a Job Post i want to know per Skills that we needed to learn 
like in term What is the Most Demand Skill in "Mechatronics"

Top Skills for Mechatronics
Job Salaries for Mechatronics
Skills Trend ? 
Health of Job of Mechatronics 

Considering Related to Mechatronics:
    1. Automation Engineer
    2. Instrumentation Engineer 
'''

r'''
Project Goal
To analyze job postings related to Mechatronics and closely related roles (e.g., Automation Engineer, Instrumentation Engineer) in order to identify:
1. Most in-demand hard skills.
2. High-demand locations for these roles.
3. Average salary ranges where available.
4. Common job requirements and qualifications.
5. Trends in skill demand over time.
6. Overall job market health for Mechatronics-related careers.
'''
# Data that I want:

r'''
Field	
    Why It Matters
Job Title	
    To classify roles and include related fields (Automation Engineer, Instrumentation Engineer, etc.).
Company Name	
    For context and possible employer analysis.
Location	
    To identify high-demand cities/countries.
Salary Range	
    For calculating average salaries.
Job Description	
    To mine for skills and responsibilities.
Skills Mentioned	
    To quantify the frequency of hard skills (e.g., PLC programming, CAD, robotics).
Requirements/Qualifications	
    To identify educational or certification trends.
Date Posted	
    To analyze demand trends over time.
Employment Type 
    (Full-time, contract, etc.)	For job type analysis.
'''


# Some Motivation for my Journey Towards Data Engineer 🛠️ or Even Data Analyst 📊

r'''
1. Data Engineer 🛠️
Focus: Building and maintaining data pipelines so data flows cleanly into systems.
Where you overlap:
    Web scraping is essentially building a data ingestion pipeline — a core Data Engineer skill.
    You’re designing how raw, messy data (job posts) gets collected, cleaned, and stored so it’s ready for analysis.
'''

r'''
2. Data Analyst 📊
Focus: Turning structured data into insights to answer business questions.
Where you overlap:
Once you’ve scraped and cleaned the job posts, you’ll analyze:

    Top 10 skills for Mechatronics
    Salary distribution by city
    Trends in demand for “PLC programming” over time
Creating visualizations: bar charts, heat maps, trend lines.
Example in your project:
    Grouping job posts by skill and counting occurrences.
    Calculating average salary per location.
    Making a skills heat map.

'''
r'''
 Web Scraping 🕷️
Focus: Extracting information from websites that don’t offer an API or downloadable dataset.
'''

# Roles that are Similar 
r'''
Robotics Engineer
Control Systems Engineer
Electromechanical Engineer
Process Control Engineer
Industrial Automation Specialist
Manufacturing Engineer (with automation focus)
Test & Commissioning Engineer
Maintenance Engineer (industrial/mechanical/electrical)
Embedded Systems Engineer
Electrical Design Engineer
Firmware Engineer (for industrial equipment)
Field Service Engineer (automation/instrumentation equipment)
System Integration Engineer
Production Engineer (automation-heavy industries)
Plant Engineer
SCADA Engineer
PLC Programmer
Instrumentation Technician
LabVIEW Developer
Process Instrumentation Specialist
Robotics Technician
Motion Control Engineer

'''
# Hard Skills 
r'''
PLC Programming (Siemens, Allen-Bradley, Omron, Schneider)
Distributed Control Systems (DCS)
SCADA & HMI Systems (Wonderware, Ignition, WinCC)
Robotics Programming (FANUC, ABB, KUKA, UR)
CAD Design (SolidWorks, AutoCAD, CATIA)
Mechanical Design & Manufacturing Processes
Electrical Circuit Design (Analog & Digital)
Embedded Systems (Arduino, Raspberry Pi, ARM)
Control Systems (PID tuning, feedback systems, cascade control)
MATLAB/Simulink
Python Programming
C/C++ Programming
Scripting Languages (Ladder Logic, Structured Text)
Sensors & Actuators (Proximity sensors, Servo motors, Stepper motors)
Motion Control Systems
Servo & VFD Drives Configuration
Vision Systems (Cognex, Keyence)
Industrial Networking (Modbus, PROFIBUS, PROFINET, Ethernet/IP, OPC-UA)
Process Measurement Devices (Pressure, Flow, Temperature, Level)
Instrument Calibration & Testing
P&ID Interpretation (Piping & Instrumentation Diagrams)
Signal Processing (Analog/Digital signals)
Industrial Safety Systems (SIL, ISO 13849)
Data Acquisition Systems (DAQ)
LabVIEW Development
Lean Manufacturing Principles
Six Sigma Methodology
'''
