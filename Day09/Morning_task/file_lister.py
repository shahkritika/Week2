# A2: List files by extension, print today's date, and run a directory command

import os
import sys
import datetime
import subprocess

print("Today's date:", datetime.date.today())

folder = "."
files_by_extension = {}

print(f"\nFiles in {os.path.abspath(folder)}, grouped by extension:")
for filename in os.listdir(folder):
    path = os.path.join(folder, filename)
    if os.path.isfile(path):
        extension = os.path.splitext(filename)[1].lower() or "(no extension)"
        files_by_extension.setdefault(extension, []).append(filename)

for extension, filenames in sorted(files_by_extension.items()):
    print(f"\n{extension}:")
    for filename in filenames:
        print(f"  {filename}")

print("\nHere is the folder listing from your computer:")
if sys.platform == "win32":
    command = ["cmd", "/c", "dir"]
else:
    command = ["ls", "-la"]

result = subprocess.run(command, capture_output=True, text=True)
if result.returncode != 0:
    print(f"Could not list the folder: {result.stderr}")
else:
    print(result.stdout)
