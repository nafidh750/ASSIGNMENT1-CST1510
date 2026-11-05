"""
RECORD CHECK  -  my version
===========================

Name  : Nafidh Ally 
Lane  : AI
Date  : 2026-11-04

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
"""

# ====================================================================== CLASS
class Record:
    """Represents an individual metric record with a label, value, and limit."""
    
    # Class-level running total for how many records have exceeded their limit
    over_limit_count = 0

    def __init__(self, label, value, limit):
        """Initializes a Record instance with a label, value, and limit."""
        self.label = label
        self.value = float(value)
        self.limit = float(limit)

    def status(self):
        """Evaluates and returns the status based on the value relative to the limit."""
        if self.value >= self.limit:
            Record.over_limit_count += 1
            return "OVER LIMIT"
        elif self.value >= (self.limit * 0.9):
            return "WARNING"
        else:
            return "OK"


# ==================================================================== RECORDS
def load_records(path):
    """Reads label, value, limit lines from a file and returns a list of Record objects."""
    record_list = []
    try:
        with open(path, "r") as file:
            for line in file:
                line = line.strip()
                if line:  # Skip empty lines
                    parts = line.split(",")
                    if len(parts) == 3:
                        label, value, limit = parts
                        record_list.append(Record(label.strip(), value.strip(), limit.strip()))
    except FileNotFoundError:
        print(f"Error: The file '{path}' was not found.")
    return record_list

# Load records from the external data file
records = load_records("records.txt")


# ==================================================================== OUTPUT
for record in records:
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)

    # Report lines
    print(f"  Value : {record.value}")
    print(f"  Limit : {record.limit}")
    print(f"  Status: {record.status()}")

    print("=" * 34)

# Print final summary report for records that went over the limit
print()
print(f"Total records exceeding limit: {Record.over_limit_count}")


# ==========================================================================
# 4. Before you finish:
#
#    [X] Run it and check every record's numbers by hand
#    [X] Check every method only reads/changes its OWN object (self) -
#        nothing reaches outside itself (except class-level tracking)
#    [X] Check every method and __init__ has a one-line docstring