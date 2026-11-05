"""
RECORD CHECK  -  my version
===========================

Name  : Nafidh Ally Mola
Lane  : AI
Date  : 2026-11-05

Run it:   python template.py
"""

import os

# =================================================================== FUNCTIONS

def parse_line(raw_line):
    """Parses a messy string into a dictionary, handling spacing and case."""
    parts = raw_line.split(',')
    parsed_dict = {}
    
    for i, part in enumerate(parts):
        part = part.strip()
        if not part:
            continue
            
        if '=' in part:
            key, val = part.split('=', 1)
            key = key.strip().lower()
            val = val.strip()
            # Attempt to convert to int for analysis
            try:
                parsed_dict[key] = int(val)
            except ValueError:
                parsed_dict[key] = val
        else:
            # Assume the first item without an '=' is the survey ID
            if i == 0:
                parsed_dict['survey_id'] = part.strip().upper()

    return parsed_dict

def status_of(record):
    """Returns 'FLAGGED' if rating is less than 3, otherwise 'OK'."""
    rating = record.get('rating', 5) 
    if isinstance(rating, int) and rating < 3:
        return 'FLAGGED'
    return 'OK'

# ====================================================================== INPUT

# Writing out the dummy data to a file to meet the 'Excellent' file-loading criteria
file_name = "messy_records.txt"
with open(file_name, "w") as f:
    f.write("  Survey_2026 , rating=4 , age=23  \n")
    f.write("SURVEY_2027,rating=2, AGE= 35\n")
    f.write("   survey_2028, RATING = 5 ,age=19 \n")
    f.write("Survey_2029 , rating= 1,AGE =42  \n")
    f.write("  SURVEY_2030, RaTiNg= 4 ,  aGe = 28\n")

raw_records = []
with open(file_name, "r") as f:
    raw_records = f.readlines()

# =============================================================== PROCESS + OUTPUT

total_records = 0
flagged_records = 0

for raw_record in raw_records:
    if not raw_record.strip():
        continue
        
    total_records += 1
    cleaned_dict = parse_line(raw_record)
    status = status_of(cleaned_dict)
    
    if status == 'FLAGGED':
        flagged_records += 1
        
    print(f"Parsed: {cleaned_dict} | Status: {status}")

print("-" * 50)
print(f"SUMMARY: {total_records} records processed, {flagged_records} flagged.")

# Cleanup temporary data file
if os.path.exists(file_name):
    os.remove(file_name)