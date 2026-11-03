"""
RECORD CHECK  -  my version
===========================

Name   : Nafidh Ally Mola
Lane   : AI
Date   : 2026-11-04

Run it:   python mini_project3.py

Checks how full each server's disk is. For every server it asks for the
hostname, GB used and GB total, then reports the free space, percent used
and a status. Type "quit" as the hostname to stop; the number of servers
that came back OVER LIMIT is printed at the end.
"""

# ================================================================= SETTINGS
# Policy thresholds - chosen, not calculated, so they live in one place.
OVER_LIMIT_PERCENT = 100.0
WARNING_PERCENT    = 90.0


# ================================================================ FUNCTIONS
def status_of(percent):
    """Return "OVER LIMIT", "WARNING" or "OK" for a percent-used figure."""
    if percent >= OVER_LIMIT_PERCENT:
        return "OVER LIMIT"
    elif percent >= WARNING_PERCENT:
        return "WARNING"
    else:
        return "OK"


def check(value, limit):
    """Return the free space (limit - value) and the percent used."""
    difference = limit - value
    percent = (value / limit) * 100
    return difference, percent


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


# ===================================================================== MAIN
over_limit_count = 0

while True:
    # ================================================================ INPUT
    hostname = input("\nHostname (or 'quit') : ")
    if hostname.strip().lower() == "quit":
        break

    used_gb  = float(input("GB used              : "))
    total_gb = float(input("GB total             : "))

    # ============================================================== PROCESS
    free_gb, percent_used = check(used_gb, total_gb)
    status = status_of(percent_used)

    if status == "OVER LIMIT":
        over_limit_count += 1

    # =============================================================== OUTPUT
    print_report(hostname, used_gb, total_gb, free_gb, percent_used, status)

# ======================================================================= END
print(f"\nServers OVER LIMIT: {over_limit_count}")
