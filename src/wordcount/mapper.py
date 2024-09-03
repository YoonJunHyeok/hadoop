#!/usr/bin/env python3
import sys

for line in sys.stdin:
    values = line.strip().split(",")

    print(f"{values[7]}\t1")