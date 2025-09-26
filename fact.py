# -*- coding: utf-8 -*-

import os
from datetime import date

folder = "facts"
today = date.today().strftime("%Y-%m-%d")
filename = f"{folder}/{today}.md"

if not os.path.exists(folder):
    os.makedirs(folder)

if not os.path.exists(filename):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# Science Fact of the Day - {today}\n\n")
        f.write("✨ **Fact:** \n\n")
        f.write("🧠 **Why it's cool:** \n\n")

print(f"✅ File ready: {filename}. Go drop your fact!")
