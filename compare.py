
import csv
import re
from pathlib import Path
from collections import Counter

folder = Path(__file__).parent

report_file = folder / "report_columns.csv"
ifc_file = folder / "ifc_columns.csv"
mapping_file = folder / "column_mapping.csv"
output = folder / "discrepancy_report.csv"


def read_csv(filename):
    with open(filename, encoding="utf-8-sig", newline="") as file:
        return list(csv.DictReader(file))


def normalize(value):
    return str(value or "").strip().upper()


def to_number(value):
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def find_matches(reference, ifc_columns):
    matches = []

    # Only match complete identifiers in Name or Tag.
    # Combined references must be mapped manually.
    if "/" in reference:
        return matches

    pattern = (
        r"(?<![A-Za-z0-9])"
        + re.escape(reference)
        + r"(?![A-Za-z0-9])"
    )

    for column in ifc_columns:
        for field in ["Name", "Tag"]:
            value = column.get(field) or ""

            if re.search(pattern, value, re.IGNORECASE):
                matches.append(column)
                break

    return matches


def check_material(report_row, ifc_row):

    expected = normalize(report_row["Expected_Material"])
    actual = normalize(ifc_row.get("Material"))

    if not actual or actual == "NOT SPECIFIED":
        return "MISSING DATA"

    if expected == "CONCRETE":
        if "CONCRETE" in actual:
            return "MATCH"
        return "REVIEW MATERIAL"

    return "REVIEW REQUIRED"


def check_dimensions(report_row, ifc_row):

    rw = to_number(report_row["Width_mm"])
    rd = to_number(report_row["Depth_mm"])

    iw = to_number(ifc_row.get("Width_mm"))
    id_ = to_number(ifc_row.get("Depth_mm"))

    if rw is None or rd is None:
        return "NOT IN REPORT"

    if iw is None or id_ is None:
        return "NOT IN IFC"

    # Width and depth may be reversed
    report_dimensions = sorted([rw, rd])
    ifc_dimensions = sorted([iw, id_])

    if all(
        abs(a - b) <= 1.0
        for a, b in zip(report_dimensions, ifc_dimensions)
    ):
        return "MATCH"

    return "MISMATCH"


def main():

    report = read_csv(report_file)
    ifc = read_csv(ifc_file)

    # Optional manually verified ID mappings
    mapping = {}

    if mapping_file.exists():
        for row in read_csv(mapping_file):
            key = (
                normalize(row.get("Report_Name")),
                normalize(row.get("Source_Table"))
            )

            if row.get("IFC_GlobalId"):
                mapping[key] = row["IFC_GlobalId"].strip()

    ifc_by_id = {
        row["GlobalId"]: row
        for row in ifc
        if row.get("GlobalId")
    }

    results = []

    for row in report:

        name = row["Report_Name"].strip()
        table = row["Source_Table"].strip()

        key = (normalize(name), normalize(table))

        mapped_id = mapping.get(key)

        if mapped_id:
            matched = (
                [ifc_by_id[mapped_id]]
                if mapped_id in ifc_by_id
                else []
            )
            method = "VERIFIED GLOBALID MAPPING"

        else:
            matched = find_matches(name, ifc)
            method = "NAME/TAG SEARCH"

        result = {
            "Report_Name": name,
            "Source_Table": table,
            "Status": "",
            "Match_Method": method,
            "IFC_GlobalId": "",
            "IFC_Name": "",
            "Report_Material": row["Expected_Material"],
            "IFC_Material": "",
            "Material_Check": "",
            "Report_Dimensions": "",
            "IFC_Dimensions": "",
            "Dimension_Check": ""
        }

        if row["Width_mm"] and row["Depth_mm"]:
            result["Report_Dimensions"] = (
                row["Width_mm"] + "x" + row["Depth_mm"]
            )

        if len(matched) == 0:
            result["Status"] = "UNMATCHED - REVIEW REQUIRED"

        elif len(matched) > 1:
            result["Status"] = "AMBIGUOUS - REVIEW REQUIRED"

        else:
            column = matched[0]

            material_result = check_material(row, column)
            dimension_result = check_dimensions(row, column)

            result["IFC_GlobalId"] = column["GlobalId"]
            result["IFC_Name"] = column["Name"]
            result["IFC_Material"] = column["Material"]
            result["Material_Check"] = material_result
            result["Dimension_Check"] = dimension_result

            result["IFC_Dimensions"] = (
                str(column.get("Width_mm", ""))
                + "x"
                + str(column.get("Depth_mm", ""))
            )

            if dimension_result == "MISMATCH":
                result["Status"] = "DIMENSION MISMATCH - REVIEW"

            elif material_result == "REVIEW MATERIAL":
                result["Status"] = "MATERIAL DIFFERENCE - REVIEW"

            elif material_result == "MISSING DATA":
                result["Status"] = "MISSING DATA - REVIEW"

            else:
                result["Status"] = "MATCHED REFERENCE"

        results.append(result)

    fieldnames = list(results[0].keys())

    with open(output, "w", newline="", encoding="utf-8-sig") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)

    print("Comparison completed!")
    print("Report records:", len(report))
    print("IFC columns:", len(ifc))
    print("CSV created:", output.name)

    print("\nResults:")
    for status, count in Counter(
        row["Status"] for row in results
    ).items():
        print(status, ":", count)


if __name__ == "__main__":
    main()
