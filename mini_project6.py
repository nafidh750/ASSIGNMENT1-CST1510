"""
RECORD CHECK  -  my version
===========================

Name  : Nafidh Ally Mola
Lane  : AI
Date  : 2026-11-05

Run it:   python template.py
"""

import pandas as pd
import matplotlib.pyplot as plt

# ==================================================================== LOAD
# 1. Read your data file with pd.read_csv(). Make your own CSV, header row
#    plus at least 5 data rows: label,value,limit.

df = pd.read_csv("records_sample.csv")


# ================================================================= PROCESS
# 2. Add a "percent" column: (value / limit) * 100.
#    Add a "status" column using .apply() with a lambda - "OVER LIMIT" (100%+), 
#    "WARNING" (90%+), otherwise "OK".

df['percent'] = (df['value'] / df['limit']) * 100

df['status'] = df['percent'].apply(
    lambda x: "OVER LIMIT" if x >= 100 else ("WARNING" if x >= 90 else "OK")
)


# ================================================================== OUTPUT
# 3. Print the DataFrame.
#    Threshold : print it as-is, with the percent column.
#    Typical   : also filter to show only the rows that are not "OK"
#    Excellent : also group by "status" and print a count per group, save
#                the full DataFrame to a new CSV, and save a bar chart.

print("--- FULL DATAFRAME ---")
print(df)

print("\n--- ATTENTION REQUIRED (NOT 'OK') ---")
attention_df = df[df['status'] != 'OK']
print(attention_df)

print("\n--- STATUS COUNTS ---")
status_counts = df.groupby('status').size()
print(status_counts)

# Save the full DataFrame to a new CSV
df.to_csv("ai_metrics_processed.csv", index=False)

# Save one bar chart of the counts per status
status_counts.plot(kind='bar', color=['red', 'orange', 'green'])
plt.title("System Metrics Status")
plt.xlabel("Status")
plt.ylabel("Count")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("status_chart.png")

# ==========================================================================
# 4. Before you finish:
#    [x] Run it and check the percent/status columns by hand for one row
#    [x] Check you used & (not "and") if you combined more than one condition
#    [x] Check every column your code refers to actually exists - watch case