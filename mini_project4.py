"""
RECORD CHECK  -  my version
===========================

Name  : Nafidh Ally Mola
Lane  : AI
Date  : 2026-11-04

Run it:   python mini_project4.py

Reads server disk records (label,value,limit) from servers.txt, checks how
full each disk is, prints a report per server, writes each server's status
to disk_results.txt, and prints how many servers are OVER LIMIT.

File-not-found check: if servers.txt is missing, Python raises
    FileNotFoundError: [Errno 2] No such file or directory: 'servers.txt'
The program catches this, prints a clear message and carries on with an
empty list instead of crashing.
"""

# ================================================================= SETTINGS
DATA_FILE          = "servers.txt"
RESULTS_FILE       = "disk_results.txt"
OVER_LIMIT_PERCENT = 100.0
WARNING_PERCENT    = 90.0


# =================================================================== FUNCTIONS
def check_record(value, limit):
    """Return the difference (limit - value), percent used and status."""
    difference = limit - value
    percent = (value / limit) * 100
    if percent >= OVER_LIMIT_PERCENT:
        status = "OVER LIMIT"
    elif percent >= WARNING_PERCENT:
        status = "WARNING"
    else:
        status = "OK"
    return difference, percent, status


def print_report(label, value, limit, difference, percent, status):
    """Print one bordered disk report for a single server."""
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)
    print(f"  Used        : {value:>10.2f} GB")
    print(f"  Total       : {limit:>10.2f} GB")
    print(f"  Free        : {difference:>+10.2f} GB")
    print(f"  Percent     : {percent:>10.2f} %")
    print(f"  Status      : {status:>10}")
    print("=" * 34)


def print_summary(over_limit_count, results_path):
    """Print the OVER LIMIT count and where the results were saved."""
    print(f"\nServers OVER LIMIT: {over_limit_count}")
    print(f"Results written to: {results_path}")


def load_records(path):
    """Read label,value,limit lines from a file and return a list of dicts."""
    records = []
    with open(path) as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            label, value, limit = line.split(",")
            records.append({"label": label.strip(),
                            "value": float(value),
                            "limit": float(limit)})
    return records


def save_results(path, results):
    """Write one 'label, status' line per record to a file."""
    with open(path, "w") as file:
        for label, status in results:
            file.write(f"{label}, {status}\n")


# ====================================================================== STORE
try:
    records = load_records(DATA_FILE)
except FileNotFoundError:
    print(f"Error: data file '{DATA_FILE}' was not found - no records to check.")
    records = []


# =============================================================== PROCESS + OUTPUT
over_limit_count = 0
results = []

for record in records:
    difference, percent, status = check_record(record["value"], record["limit"])
    print_report(record["label"], record["value"], record["limit"],
                 difference, percent, status)
    results.append((record["label"], status))
    if status == "OVER LIMIT":
        over_limit_count += 1

save_results(RESULTS_FILE, results)
print_summary(over_limit_count, RESULTS_FILE)
