# file_automation.py
# Simple automation: renaming files in a folder

import os

# Example file list
files = ["report1.txt", "report2.txt", "report3.txt"]

# Rename files
for i, file in enumerate(files):
    new_name = f"file_{i+1}.txt"
    print(f"Renaming {file} to {new_name}")
    # Uncomment the line below to actually rename files on your computer
    # os.rename(file, new_name)

print("Automation complete!")
