
import csv
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

source = Path(__file__).parent / "compare.py"


def write_csv(path, rows):
    with open(path, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def run_test(folder, ifc_depth, expected_status):
    report = [{
        "Report_Name": "TEST-S208",
        "Source_Table": "TEST",
        "Expected_Material": "Concrete",
        "Width_mm": "200",
        "Depth_mm": "300"
    }]

    ifc = [{
        "GlobalId": "TEST_GLOBAL_ID_001",
        "Name": "Concrete Column Test",
        "Tag": "TEST",
        "Type": "Concrete 200x250",
        "Material": "DTU_Concrete_Generic_Natural_Mat",
        "Storey": "Ground Floor",
        "Width_mm": "200",
        "Depth_mm": str(ifc_depth),
        "Dimension_Source": "Test data"
    }]

    mapping = [{
        "Report_Name": "TEST-S208",
        "Source_Table": "TEST",
        "IFC_GlobalId": "TEST_GLOBAL_ID_001"
    }]

    write_csv(folder / "report_columns.csv", report)
    write_csv(folder / "ifc_columns.csv", ifc)
    write_csv(folder / "column_mapping.csv", mapping)

    run = subprocess.run(
        [sys.executable, str(folder / "compare.py")],
        cwd=folder,
        capture_output=True,
        text=True
    )

    if run.returncode != 0:
        raise RuntimeError(run.stdout + run.stderr)

    with open(
        folder / "discrepancy_report.csv",
        encoding="utf-8-sig",
        newline=""
    ) as f:
        result = list(csv.DictReader(f))[0]

    actual = result["Status"]

    print("Expected:", expected_status)
    print("Actual:  ", actual)

    assert actual == expected_status, (
        f"Test failed: expected {expected_status}, got {actual}"
    )

    print("PASS\n")


if __name__ == "__main__":
    if not source.exists():
        raise FileNotFoundError("compare.py not found")

    with tempfile.TemporaryDirectory() as temp:
        folder = Path(temp)
        shutil.copy2(source, folder / "compare.py")

        print("TEST 1: Dimension mismatch")
        run_test(
            folder,
            ifc_depth=250,
            expected_status="DIMENSION MISMATCH - REVIEW"
        )

        print("TEST 2: Matching dimensions")
        run_test(
            folder,
            ifc_depth=300,
            expected_status="MATCHED REFERENCE"
        )

    print("ALL CONTROLLED TESTS PASSED")
