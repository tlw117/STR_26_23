
import csv
from pathlib import Path
from collections import Counter

folder = Path(__file__).parent

with open(
    folder / "candidate_locations.csv",
    encoding="utf-8-sig",
    newline=""
) as f:
    candidates = list(csv.DictReader(f))

# Choose column from structural report
report_column = "S208/108"

# Select possible matches and remove duplicate GlobalIds
unique = {}

for row in candidates:
    if row["Report_Name"] == report_column:
        global_id = row.get("IFC_GlobalId", "")

        if global_id:
            unique[global_id] = row

matches = list(unique.values())

# Sort by storey and coordinates
matches.sort(
    key=lambda r: (
        r.get("IFC_Storey", ""),
        float(r.get("Z_m") or 0),
        float(r.get("X_m") or 0),
        float(r.get("Y_m") or 0)
    )
)

print("Report column:", report_column)
print("Possible IFC columns:", len(matches))

print("\nColumns by storey:")
for storey, count in Counter(
    row["IFC_Storey"] for row in matches
).items():
    print(storey, ":", count)

# Save shortlist
output = folder / "review_S208.csv"

with open(
    output, "w", newline="", encoding="utf-8-sig"
) as f:
    if matches:
        writer = csv.DictWriter(
            f, fieldnames=list(matches[0].keys())
        )
        writer.writeheader()
        writer.writerows(matches)

print("\nCreated:", output.name)
