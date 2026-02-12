#!/usr/bin/env python3
import sys

text = sys.argv[1:]

if len(text) == 0:
    print("none")
else:
    for w in text:
        if not w.endswith("nd"):
            print(w + "nd")