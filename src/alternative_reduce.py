#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_paths',nargs='+',required=True)
parser.add_argument('--hashtags',nargs='+',required=True)
args = parser.parse_args()

# imports
import os
import json
from collections import Counter,defaultdict
import re
import matplotlib.pyplot as plt

# helper function

def extract_date_pattern(filename):
    match = re.search(r'\d{2}-\d{2}-\d{2}', filename)
    return match.group(0) if match else None

total = defaultdict(lambda: Counter())

for path in args.input_paths:
    date = extract_date_pattern(path)
    with open(path) as f:
        tmp = json.load(f)
        for hashtag in args.hashtags:
            if hashtag in tmp:
                total[date][hashtag] = sum(tmp[hashtag].values())

# Extract dates
dates = list(total.keys())

# Prepare plot data
hashtag_counts = {tag: [total[date].get(tag, 0) for date in dates] for tag in args.hashtags}

# Plot the data
plt.figure(figsize=(10, 5))

for tag, counts in hashtag_counts.items():
    plt.plot(dates, counts, marker='o', label=tag)

# Formatting
plt.xlabel("Date")
plt.ylabel("Count")
plt.title("Hashtag Frequency Over Time")
plt.xticks(rotation=45, fontsize=8)  # Smaller font size for date labels

# Only print a label every 20 dates
plt.xticks(dates[::20], rotation=45, fontsize=8)

plt.legend()
plt.grid(True)

# Save the plot as a PNG file
plt.savefig("hashtag_trend.png", dpi=300, bbox_inches="tight")

# Close the plot to free memory
plt.close()
