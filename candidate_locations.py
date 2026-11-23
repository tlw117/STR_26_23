
import csv
from pathlib import Path

folder = Path(__file__).parent


def read_csv(filename):
    with open(folder / filename, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


candidates = read_csv("candidate_matches.csv")
locations = read_csv("ifc_locations.csv")

# Match by unique IFC GlobalId
location_lookup = {
    row["GlobalId"]: row
    for row in locations
}

results = []

for candidate in candidates:
    global_id = candidate.get("IFC_GlobalId", "")
    location = location_lookup.get(global_id, {})

    results.append({
        **candidate,
        "X_m": location.get("X_m", ""),
        "Y_m": location.get("Y_m", ""),
        "Z_m": location.get("Z_m", "")
    })


output = folder / "candidate_locations.csv"

with open(output, "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.DictWriter(
        f,
        fieldnames=list(results[0].keys())
    )
    writer.writeheader()
    writer.writerows(results)

print("Candidate locations created!")
print("Total rows:", len(results))
print("File:", output.name)
