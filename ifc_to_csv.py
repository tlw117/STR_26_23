
import ifcopenshell
import ifcopenshell.util.element
import ifcopenshell.util.unit
import csv
import re
from pathlib import Path


# Extract material name
def get_material_name(column):
    materials = ifcopenshell.util.element.get_materials(column)

    names = [m.Name for m in materials if m.Name]
    return ", ".join(dict.fromkeys(names)) if names else "Not specified"


# Extract cross-section dimensions
def get_dimensions(column, model):
    material = ifcopenshell.util.element.get_material(column)

    # First try reading the IFC material profile
    if material:
        if material.is_a("IfcMaterialProfileSetUsage"):
            profile_set = material.ForProfileSet
        elif material.is_a("IfcMaterialProfileSet"):
            profile_set = material
        else:
            profile_set = None

        if profile_set:
            for item in profile_set.MaterialProfiles or []:
                profile = item.Profile

                if profile and profile.is_a("IfcRectangleProfileDef"):
                    scale = ifcopenshell.util.unit.calculate_unit_scale(model)
                    width = profile.XDim * scale * 1000
                    depth = profile.YDim * scale * 1000

                    return (
                        round(width, 1),
                        round(depth, 1),
                        "IFC profile"
                    )

    # If unavailable, try the column type name
    column_type = ifcopenshell.util.element.get_type(column)

    text = column_type.Name if column_type and column_type.Name else ""

    match = re.search(r"(\d+)\s*x\s*(\d+)\s*mm", text, re.I)

    if match:
        return (
            float(match.group(1)),
            float(match.group(2)),
            "Type name"
        )

    return "", "", "Not available"


# Export IFC columns to CSV
def analyse(model):
    columns = model.by_type("IfcColumn")
    print("Total columns:", len(columns))

    results = []

    for column in columns:
        material_name = get_material_name(column)
        storey = ifcopenshell.util.element.get_container(column)
        column_type = ifcopenshell.util.element.get_type(column)

        width, depth, source = get_dimensions(column, model)

        results.append({
            "GlobalId": column.GlobalId,
            "Name": column.Name,
            "Tag": column.Tag,
            "Type": column_type.Name if column_type else "",
            "Material": material_name,
            "Storey": storey.Name if storey else "Not specified",
            "Width_mm": width,
            "Depth_mm": depth,
            "Dimension_Source": source
        })

    output = Path(__file__).parent / "ifc_columns.csv"

    with open(output, "w", newline="", encoding="utf-8-sig") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "GlobalId", "Name", "Tag", "Type",
                "Material", "Storey", "Width_mm",
                "Depth_mm", "Dimension_Source"
            ]
        )

        writer.writeheader()
        writer.writerows(results)

    print("CSV file created:", output.name)

    extracted = sum(
        1 for row in results if row["Width_mm"] != ""
    )
    print("Columns with dimensions:", extracted)


if __name__ == "__main__":
    ifc_file = Path(__file__).parent / "B308X (1).ifc"
    model = ifcopenshell.open(str(ifc_file))
    analyse(model)
