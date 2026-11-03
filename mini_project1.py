"""
RECORD CHECK  -  my version
===========================

Name  : Nafidh Ally Mola
Course  :  DataScience and AI
Date  :  2026-11-03

Run it:   python template.py

Checks how full a server's disk is: asks for the hostname, GB used and
GB total, then reports free space, percent used and headroom before the
disk reaches the alert level.
"""

# ================================================================= SETTINGS
# Most monitoring tools raise a disk alert at 90% full. This is a policy
# choice, not something we can calculate, so it lives in one named place.
ALERT_PERCENT = 90.0

# ==================================================================== INPUT
hostname = input("Hostname  : ")
used_gb  = float(input("GB used   : "))
total_gb = float(input("GB total  : "))


# ================================================================== PROCESS
# Positive means space is still free; negative would mean over capacity.
free_gb      = total_gb - used_gb
percent_used  = (used_gb / total_gb) * 100

# Extra line: how many more GB can be written before the alert fires.
# Free space alone doesn't tell an admin when they'll get paged - this does.
alert_level_gb = total_gb * (ALERT_PERCENT / 100)
headroom_gb    = alert_level_gb - used_gb


# =================================================================== OUTPUT
print()
print("=" * 34)
print(f"  RECORD CHECK  -  {hostname}")
print("=" * 34)
print(f"  Used        : {used_gb:>10.2f}")
print(f"  Total       : {total_gb:>10.2f}")
print(f"  Free        : {free_gb:>+10.2f}")
print(f"  Percent     : {percent_used:>10.2f} %")
print(f"  To alert    : {headroom_gb:>+10.2f}   (at {ALERT_PERCENT:.0f}%)")
print("=" * 34)


# ==========================================================================
# Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and write the error in your journal
#    [ ] Check every variable name says what it holds
#    [ ] Show it to the person next to you
