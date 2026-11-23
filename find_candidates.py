
import csv
from pathlib import Path

folder = Path(__file__).parent


def read_csv(filename):
    with open(folder / filename, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def number(value):
    try:
        return float(value)
    except (ValueError, TypeError):
        return None


def material_matches(expected, actual):
    expected = (expected or "").lower()
    actual = (actual or "").lower()

    if not expected or not actual or actual == "not specified":
        return False

    return expected in actual


def dimensions_match(report, ifc):
    rw = number(report.get("Width_mm"))
    rd = number(report.get("Depth_mm"))
    iw = number(ifc.get("Width_mm"))
    id_ = number(ifc.get("Depth_mm"))

    if None in (rw, rd, iw, id_):
        return False

    # Compare dimensions independently of orientation
    report_size = sorted([rw, rd])
    ifc_size = sorted([iw, id_])

    return all(
        abs(a - b) <= 1.0
        for a, b in zip(report_size, ifc_size)
    )


report_columns = read_csv("report_columns.csv")
ifc_columns = read_csv("ifc_columns.csv")

results = []

for report in report_columns:
    reference = report["Report_Name"]
    expected_material = report["Expected_Material"]

    has_dimensions = (
        number(report.get("Width_mm")) is not None
        and number(report.get("Depth_mm")) is not None
    )

    candidates = []

    if has_dimensions:
        for column in ifc_columns:
            same_material = material_matches(
                expected_material,
                column.get("Material")
            )

            same_dimensions = dimensions_match(
                report, column
            )

            if same_material and same_dimensions:
                candidates.append(column)

    if not has_dimensions:
        status = "INSUFFICIENT REPORT DATA"
    elif len(candidates) == 0:
        status = "NO CANDIDATE FOUND"
    else:
        status = "POSSIBLE MATCH - REVIEW REQUIRED"

    for column in candidates:
        results.append({
            "Report_Name": reference,
            "Source_Table": report["Source_Table"],
            "Status": status,
            "Candidate_Count": len(candidates),
            "IFC_GlobalId": column["GlobalId"],
            "IFC_Name": column["Name"],
            "IFC_Material": column["Material"],
            "IFC_Storey": column["Storey"],
            "IFC_Width_mm": column["Width_mm"],
            "IFC_Depth_mm": column["Depth_mm"],
            "Next_Check": "Verify position and identity"
        })

    if not candidates:
        results.append({
            "Report_Name": reference,
            "Source_Table": report["Source_Table"],
            "Status": status,
            "Candidate_Count": 0,
            "IFC_GlobalId": "",
            "IFC_Name": "",
            "IFC_Material": "",
            "IFC_Storey": "",
            "IFC_Width_mm": "",
            "IFC_Depth_mm": "",
            "Next_Check": (
                "Find report dimensions"
                if not has_dimensions
                else "Check model version and geometry"
            )
        })

output = folder / "candidate_matches.csv"

with open(output, "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.DictWriter(
        f, fieldnames=list(results[0].keys())
    )
    writer.writeheader()
    writer.writerows(results)

print("Candidate matching completed!")
print("Report records:", len(report_columns))
print("IFC columns:", len(ifc_columns))
print("File created:", output.name)

for report in report_columns:
    name = report["Report_Name"]
    table = report["Source_Table"]

    row = next(
        r for r in results
        if r["Report_Name"] == name
        and r["Source_Table"] == table
    )

    print(
        name,
        "|", row["Status"],
        "| Candidates:", row["Candidate_Count"]
    )
