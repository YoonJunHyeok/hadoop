#!/usr/bin/env python3
import sys

first_line = True

for line in sys.stdin:
    if first_line:
        first_line = False
        continue

    values = line.strip().split(",")

    print(f"{values[7]}\t1")