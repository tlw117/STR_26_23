
from pathlib import Path
import subprocess
import sys

# BIM Report Consistency Checker
# A4 - Forensic BIM

folder = Path(__file__).parent


steps = [
    ("Extract IFC columns", "ifc_to_csv.py"),
    ("Extract PDF report data", "pdf_to_csv.py"),
    ("Extract IFC locations", "check_locations.py"),
    ("Compare report and IFC", "compare.py"),
    ("Find possible matches", "find_candidates.py"),
    ("Add candidate locations", "candidate_locations.py"),
    ("Generate final review report", "final_review.py"),
]



def main():
    print("\nBIM REPORT CONSISTENCY CHECKER")
    print("=" * 45)

    for description, script in steps:
        print(f"\nSTEP: {description}")

        script_path = folder / script

        if not script_path.exists():
            print(f"ERROR: Missing file {script}")
            sys.exit(1)

        result = subprocess.run(
            [sys.executable, str(script_path)],
            cwd=folder
        )

        if result.returncode != 0:
            print(f"\nERROR running {script}")
            sys.exit(result.returncode)

    print("\n" + "=" * 45)
    print("ANALYSIS COMPLETED!")
    print("=" * 45)

    print("\nOutput files:")
    print("- ifc_columns.csv")
    print("- report_columns.csv")
    print("- ifc_locations.csv")
    print("- discrepancy_report.csv")
    print("- candidate_matches.csv")
    print("- candidate_locations.csv")

    print("\nReview possible matches manually.")
    print("Unmatched columns are not confirmed errors.")


if __name__ == "__main__":
    main()
