#!/usr/bin/env python3
"""Check data/species-master-list.csv for duplicate scientific names.

Exit code 0 = no duplicates, 1 = duplicates found (useful as a pre-commit hook).
"""
import csv
import os
import sys
from collections import Counter

CSV_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "species-master-list.csv")

def main():
    with open(CSV_PATH, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    names = [r["Scientific Name"].strip() for r in rows if r.get("Scientific Name")]
    dupes = {n: c for n, c in Counter(names).items() if c > 1}
    total = len(names)
    unique = len(set(names))
    print(f"Species rows: {total} | unique scientific names: {unique}")
    if dupes:
        print("DUPLICATES FOUND:")
        for n, c in sorted(dupes.items()):
            print(f"  {n}: listed {c} times")
        sys.exit(1)
    print("No duplicate species found. Inventory is clean.")

if __name__ == "__main__":
    main()
