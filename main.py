

import ifcopenshell
import ifcopenshell.util.element
import csv
from pathlib import Path

# Colums from modle to csv file
def analyse(model):
    columns = model.by_type("IfcColumn")
    print("Total columns:", len(columns))

    results = []

    for column in columns:
        material = ifcopenshell.util.element.get_material(column)
        storey = ifcopenshell.util.element.get_container(column)
        column_type = ifcopenshell.util.element.get_type(column)

        results.append({
            "GlobalId": column.GlobalId,
            "Name": column.Name,
            "Tag": column.Tag,
            "Type": column_type.Name if column_type else "",
            "Material": str(material.Name) if material and material.is_a("IfcMaterial") else "Not specified",
            "Storey": storey.Name if storey else "Not specified"
        })

    output = Path(__file__).parent / "ifc_columns.csv"

    with open(output, "w", newline="", encoding="utf-8-sig") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["GlobalId", "Name", "Tag", "Type", "Material", "Storey"]
        )

        writer.writeheader()
        writer.writerows(results)

    print("CSV file created:", output.name)


if __name__ == "__main__":
    ifc_file = Path(__file__).parent / "B308X (1).ifc"

    model = ifcopenshell.open(str(ifc_file))
    analyse(model)

