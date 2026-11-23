
import csv
from pathlib import Path
from collections import defaultdict

# A4 - BIM Report Consistency Checker
# Final review report

folder = Path(__file__).parent


def read_csv(filename):
    with open(folder / filename, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


report = read_csv("report_columns.csv")
candidates = read_csv("candidate_locations.csv")

# Group candidate columns by report reference and table
groups = defaultdict(list)

for row in candidates:
    key = (row["Report_Name"], row["Source_Table"])
    groups[key].append(row)


results = []

for item in report:
    name = item["Report_Name"]
    table = item["Source_Table"]
    key = (name, table)

    rows = groups.get(key, [])

    # Keep unique IFC elements
    unique = {
        row["IFC_GlobalId"]: row
        for row in rows
        if row.get("IFC_GlobalId")
    }

    matches = list(unique.values())
    count = len(matches)

    # Report information
    material = item.get("Expected_Material", "")
    width = item.get("Width_mm", "")
    depth = item.get("Depth_mm", "")

    missing = []

    if not material:
        missing.append("Material")

    if not width or not depth:
        missing.append("Dimensions")

    # Decide review status
    if "Dimensions" in missing:
        status = "INSUFFICIENT DATA"
        issue = "Missing cross-section dimensions in report"
        action = "Find dimensions in structural documentation"

    elif count == 0:
        status = "NO CANDIDATE"
        issue = "No IFC column matches material and dimensions"
        action = "Check model version and other properties"

    elif count == 1:
        status = "SINGLE CANDIDATE - REVIEW"
        issue = "One possible match, identity not verified"
        action = "Verify column location and identity"

    else:
        status = "MULTIPLE CANDIDATES - REVIEW"
        issue = f"{count} possible IFC columns found"
        action = "Verify storey, position and column identity"

    # Available locations of candidate IFC elements
    storeys = sorted({
        row.get("IFC_Storey", "")
        for row in matches
        if row.get("IFC_Storey")
    })

    locations_available = sum(
        1 for row in matches
        if all(row.get(field) not in ("", None)
               for field in ["X_m", "Y_m", "Z_m"])
    )

    results.append({
        "Report_Column": name,
        "Source_Table": table,
        "Expected_Material": material,
        "Report_Width_mm": width,
        "Report_Depth_mm": depth,
        "Possible_IFC_Matches": count,
        "IFC_Storeys": "; ".join(storeys),
        "Candidates_With_Location": locations_available,
        "Status": status,
        "Issue": issue,
        "Recommended_Action": action,
        "Verification": "NOT VERIFIED"
    })


# Export final report
output = folder / "final_review_report.csv"

fields = [
    "Report_Column",
    "Source_Table",
    "Expected_Material",
    "Report_Width_mm",
    "Report_Depth_mm",
    "Possible_IFC_Matches",
    "IFC_Storeys",
    "Candidates_With_Location",
    "Status",
    "Issue",
    "Recommended_Action",
    "Verification"
]

with open(output, "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    writer.writerows(results)


print("\nFINAL BIM CONSISTENCY REVIEW")
print("=" * 45)
print("Report records:", len(report))
print("Final review records:", len(results))
print("Output:", output.name)

print("\nStatus summary:")

summary = {}

for row in results:
    status = row["Status"]
    summary[status] = summary.get(status, 0) + 1

for status, count in summary.items():
    print(f"{status}: {count}")

print("\nManual verification is required.")
print("Candidate matches are not confirmed element identities.")
