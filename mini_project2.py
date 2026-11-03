"""
RECORD CHECK  -  my version
===========================

Name  : Nafidh Ally Mola
Lane  : AI 
Date  :  2026-11-04

Run it:   python mini_project2.py

Checks how full each server's disk is. For every server it asks for the
hostname, GB used and GB total, then reports the free space, percent used
and a status. Type "quit" as the hostname to stop; the number of servers
that came back OVER LIMIT is printed at the end.
"""

# ================================================================= SETTINGS
# Policy thresholds - chosen, not calculated, so they live in one place.
OVER_LIMIT_PERCENT = 100.0
WARNING_PERCENT    = 90.0

over_limit_count = 0

while True:
    # ================================================================ INPUT
    hostname = input("\nHostname (or 'quit') : ")
    if hostname.strip().lower() == "quit":
        break

    used_gb  = float(input("GB used              : "))
    total_gb = float(input("GB total             : "))

    # ============================================================== PROCESS
    # Positive = space still free; negative = over capacity.
    free_gb      = total_gb - used_gb
    percent_used = (used_gb / total_gb) * 100

    if percent_used >= OVER_LIMIT_PERCENT:
        status = "OVER LIMIT"
        over_limit_count += 1
    elif percent_used >= WARNING_PERCENT:
        status = "WARNING"
    else:
        status = "OK"

    # =============================================================== OUTPUT
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {hostname}")
    print("=" * 34)
    print(f"  Used        : {used_gb:>10.2f} GB")
    print(f"  Total       : {total_gb:>10.2f} GB")
    print(f"  Free        : {free_gb:>+10.2f} GB")
    print(f"  Percent     : {percent_used:>10.2f} %")
    print(f"  Status      : {status:>10}")
    print("=" * 34)

# ======================================================================= END
print()
print(f"Servers OVER LIMIT: {over_limit_count}")
