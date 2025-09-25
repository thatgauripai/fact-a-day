import os

folder = "facts"
readme = "README.md"

# Collect fact files
fact_files = sorted(os.listdir(folder))

with open(readme, "w", encoding="utf-8") as f:
    f.write("# 🌱 Daily Science Facts\n\n")
    f.write("A collection of cool science facts I learn each day. 📚✨\n\n")
    f.write("## 📅 Facts\n\n")

    for file in fact_files:
        if file.endswith(".md"):
            date = file.replace(".md", "")
            f.write(f"- [{date}](facts/{file})\n")

print("✅ README updated with table of contents!")
