import csv
import sys
from pathlib import Path

# Usage
if len(sys.argv) != 2:
    print("python3 csv2pleco.py <input.csv>")
    sys.exit(1)

# Input
input_path = Path(sys.argv[1])

if not input_path.exists():
    print(f"File not found: {input_path}")
    sys.exit(1)

rows = []

# Read CSV
with open(input_path, newline="", encoding="utf-8") as f:
    reader = csv.reader(f)

    # Skip header row
    next(reader, None)

    for row in reader:
        # Skip incomplete rows
        if len(row) < 3:
            continue

        word = row[0].strip()
        pinyin = row[1].strip()
        english = row[2].strip()

        rows.append((word, pinyin, english))

if not rows:
    print("CSV is empty")
    sys.exit(1)

first_word = rows[0][0]

# Output Path
txt_dir = input_path.parent.parent / "txt"

if txt_dir.exists():
    output_path = txt_dir / f"{first_word}.txt"
else:
    output_path = input_path.with_name(f"{first_word}.txt")

# Write TSV
with open(output_path, "w", encoding="utf-8") as f:
    f.write(f"//{first_word}\n")

    for word, pinyin, english in rows:
        f.write(f"{word}\t{pinyin}\t{english}\n")

print(f"Saved: {output_path}")
