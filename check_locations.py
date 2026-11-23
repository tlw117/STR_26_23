
import ifcopenshell
import ifcopenshell.util.placement
import ifcopenshell.util.unit
import csv
from pathlib import Path

# Open IFC model
folder = Path(__file__).parent
ifc_file = folder / "B308X (1).ifc"

model = ifcopenshell.open(str(ifc_file))
scale = ifcopenshell.util.unit.calculate_unit_scale(model)

# Find all columns
columns = model.by_type("IfcColumn")
results = []

for column in columns:

    if column.ObjectPlacement:
        placement = ifcopenshell.util.placement.get_local_placement(
            column.ObjectPlacement
        )

        # Convert model coordinates to metres
        x = placement[0, 3] * scale
        y = placement[1, 3] * scale
        z = placement[2, 3] * scale

        results.append({
            "GlobalId": column.GlobalId,
            "Name": column.Name,
            "X_m": round(x, 3),
            "Y_m": round(y, 3),
            "Z_m": round(z, 3)
        })

# Export locations to CSV
output = folder / "ifc_locations.csv"

with open(output, "w", newline="", encoding="utf-8-sig") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=["GlobalId", "Name", "X_m", "Y_m", "Z_m"]
    )

    writer.writeheader()
    writer.writerows(results)

print("Total IFC columns:", len(columns))
print("Columns with location:", len(results))
print("CSV created:", output.name)
