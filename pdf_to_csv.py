
import csv
import re
from pathlib import Path
import pymupdf

folder = Path(__file__).parent
pdf_file = folder / "26-06-D-STR-Anon.pdf"
output = folder / "report_columns.csv"

fields = [
    "Report_Name", "Source_Table", "Report_Page",
    "Expected_Material", "Width_mm", "Depth_mm",
    "Height_m", "NEd_kN", "Capacity_Old_kN",
    "Util_Old_pct", "Capacity_New_kN",
    "Util_New_pct", "Notes"
]

id_pattern = re.compile(
    r"^S\d{3}[a-z]?(?:/(?:S)?\d{3}[a-z]?)?$",
    re.IGNORECASE
)

number_pattern = re.compile(r"^\d+(?:\.\d+)?$")


def extract_table(page, title, end_marker, count, table_number):

    text = page.get_text("text")

    start = text.find(title)
    if start == -1:
        raise ValueError(f"Could not find Table {table_number}")

    end = text.find(end_marker, start)
    if end == -1:
        raise ValueError(f"Could not find end of Table {table_number}")

    lines = [
        line.strip()
        for line in text[start:end].splitlines()
        if line.strip()
    ]

    results = []

    for i, line in enumerate(lines):

        if not id_pattern.fullmatch(line):
            continue

        values = lines[i + 1:i + 1 + count]

        if len(values) != count:
            continue

        if not all(number_pattern.fullmatch(v) for v in values):
            continue

        row = {field: "" for field in fields}

        row["Report_Name"] = line
        row["Source_Table"] = table_number
        row["Expected_Material"] = "Concrete"

        if table_number == "5.1":

            row["Report_Page"] = "10"
            row["NEd_kN"] = values[0]
            row["Capacity_Old_kN"] = values[1]
            row["Util_Old_pct"] = values[2]
            row["Notes"] = "Existing concrete column"

        elif table_number == "5.4":

            row["Report_Page"] = "11"
            row["Width_mm"] = "200"
            row["Depth_mm"] = "300"
            row["NEd_kN"] = values[0]
            row["Capacity_Old_kN"] = values[1]
            row["Util_Old_pct"] = values[2]
            row["Capacity_New_kN"] = values[3]
            row["Util_New_pct"] = values[4]
            row["Notes"] = "Existing section 200x300 mm"

        results.append(row)

    return results


def main():

    with pymupdf.open(pdf_file) as document:

        # PDF page indices start at 0
        table_51 = extract_table(
            document[11],
            "Table 5.1: Existing columns, loads and bearing capacities",
            "5.1.2",
            3,
            "5.1"
        )

        table_54 = extract_table(
            document[12],
            "Table 5.4: Reinforcement of existing columns",
            "5.2.2",
            5,
            "5.4"
        )

    if not table_51 or not table_54:
        raise ValueError("One or more tables could not be extracted.")

    results = table_51 + table_54

    with open(output, "w", newline="", encoding="utf-8-sig") as file:

        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(results)

    print("Table 5.1 columns:", len(table_51))
    print("Table 5.4 columns:", len(table_54))
    print("Total report records:", len(results))
    print("CSV created:", output.name)


if __name__ == "__main__":
    main()
