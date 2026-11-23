
import ifcopenshell
from pathlib import Path

folder = Path(__file__).parent
model = ifcopenshell.open(str(folder / "B308X (1).ifc"))

references = [
    "S202",
    "S211",
    "S208/108",
    "S210a",
    "S216"
]

print("Searching all IFC entities...\n")

for reference in references:
    matches = []

    for entity in model:
        if reference.upper() in str(entity).upper():
            matches.append(entity)

    print(reference, "- Matches:", len(matches))

    for entity in matches[:5]:
        print("  IFC type:", entity.is_a())
        print("  IFC ID:", entity.id())
        print("  Details:", str(entity)[:200])

    print()
