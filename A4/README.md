
# Assignment 4 – Tool

## Semi-Automated Comparison of Structural Reports and IFC Models

**Course:** 41934 Advanced BIM  
**Group:** 23 – Structures  
**Focus Area:** Structures

---

## 1. Introduction

In Assignment 1, our group investigated a claim concerning the S206 steel columns and their capacity to support a proposed two-storey extension. However, we discovered that these columns could not be identified in the available IFC model, which instead contained concrete columns.

This highlighted the challenges of verifying information between structural reports and BIM models. Therefore, we changed our focus to developing a **semi-automated BIM–Report Consistency Checker**.

The tool was developed and tested using one structural report and IFC model from Building 308. However, the workflow could be adapted to other structural reports and IFC models.

## 2. Aim and Objectives

The aim is to develop a Python-based tool that supports consistency checking between structural reports and IFC models.

The objectives are to:

- Extract structural column information from PDF reports and IFC models.
- Compare materials, dimensions and available element identifiers.
- Identify possible matching columns despite different naming conventions.
- Highlight missing information and ambiguous matches.
- Generate a CSV report for further engineering review.

## 3. Tool Description

The tool consists of three main components.

### 3.1 IFC Data Extraction

Using Python and IfcOpenShell, the tool extracts information about columns from the IFC model, including:

- GlobalId, name and type
- Material information
- Cross-section dimensions
- Building storey
- Placement coordinates (X, Y and Z)

The extracted data is exported to CSV files.

### 3.2 Structural Report Data Extraction

PyMuPDF is used to extract column information from the structural PDF report.

The current implementation focuses on two tables describing existing concrete columns:

- **Table 5.1:** Existing columns, loads and bearing capacities.
- **Table 5.4:** Reinforcement of existing columns.

The extracted information includes column references, available dimensions, material descriptions, loads, capacities and utilisation values.

The data is exported to `report_columns.csv`.

### 3.3 Data Comparison and Validation

Initially, we attempted to match columns directly using their identifiers (IDs). However, the structural report and IFC model used different naming conventions, making it difficult to identify corresponding elements.

Therefore, we developed an alternative approach to identify **possible matches** based on material information and cross-section dimensions, rather than relying only on column IDs.

The tool identifies:

- **Possible matches:** IFC columns with matching materials and dimensions.
- **Insufficient data:** Missing information required for comparison.
- **Multiple candidates:** Several columns meeting the same criteria.
- **Unmatched elements:** No corresponding candidate identified.

Storey information and IFC coordinates are included to support manual verification.

Since matching properties do not necessarily confirm element identity, the results are flagged for further review rather than treated as confirmed errors.

## 4. Workflow

The workflow consists of the following steps:

1. Extract concrete column information from the IFC model using IfcOpenShell.
2. Extract relevant data from the structural PDF report using PyMuPDF.
3. Export both datasets to CSV.
4. Attempt direct ID matching and identify possible matches based on material and dimensions.
5. Include IFC storey and coordinate information for further verification.
6. Flag missing information and ambiguous matches.
7. Generate a final review report.

The workflow is executed through `main.py`, which automatically runs the individual scripts.

## 5. Model Requirements and IDS

The tool requires structural elements classified as `IfcColumn` and relevant information such as GlobalId, dimensions, materials, storeys and placement.

These requirements could be formalised and checked using an Information Delivery Specification (IDS). However, separate IDS validation has not been implemented in the current version.

## 6. Implementation

The tool was developed in Python using IfcOpenShell, PyMuPDF and CSV processing.

| Script | Function |
|---|---|
| `main.py` | Runs the complete workflow |
| `ifc_to_csv.py` | Extracts IFC column data |
| `pdf_to_csv.py` | Extracts PDF report information |
| `check_locations.py` | Extracts IFC coordinates |
| `compare.py` | Compares data using identifiers or verified mappings |
| `find_candidates.py` | Finds possible matches by material and dimensions |
| `candidate_locations.py` | Adds coordinates to candidate matches |
| `final_review.py` | Generates the final CSV report |
| `test_checker.py` | Performs controlled comparison tests |

The main output is `final_review_report.csv`, which summarises the findings for engineering review.

## 7. Results and Discussion

The initial comparison based on column identifiers did not identify any direct matches between the structural report and IFC model. We therefore used material information and cross-section dimensions to identify possible corresponding elements.

The tool was tested using the Building 308 structural report and IFC model. A total of **211 IFC columns** and **25 structural report records** were extracted.

| Result | Number of report records |
|---|---:|
| Insufficient report data | 21 |
| Multiple possible IFC matches | 4 |
| **Total** | **25** |

For the four columns in Table 5.4, the tool identified **46 possible IFC candidates per report entry**, based on concrete material and 200 × 300 mm cross-section dimensions.

However, the corresponding elements could not be uniquely identified because several IFC columns shared the same properties.

### Testing

The comparison function was tested using two controlled examples: one with matching dimensions and one with a dimension mismatch. Both tests passed, confirming that the tool can identify dimensional differences when corresponding elements are known.

## 8. Limitations and Future Improvements

The main limitation is that the report and IFC model use different column identification systems, making direct matching difficult.

Additionally, some report entries lack sufficient dimensions, and IFC coordinates cannot be used for direct verification without corresponding location references from structural drawings.

The current PDF extraction is designed for specific tables in one structural report. **To use the tool with other reports, the extraction method would need to be adapted to their table structures and available information.** The general comparison workflow could then be reused.

Future improvements could include location-based matching, extraction from structural drawings and IDS validation.

## 9. Conclusion

A semi-automated BIM–Report Consistency Checker was developed using Python, IfcOpenShell and PyMuPDF.

The tool extracts structural information, attempts to match columns using their identifiers, and identifies possible corresponding elements based on materials and dimensions when direct matching is not possible.

It highlights missing or ambiguous data in a final CSV report for engineering review.

Although the tool cannot automatically confirm all element matches, it supports consistency checking and helps identify information requiring further investigation.

The tool was demonstrated using Building 308, but **the approach could be adapted to other structural projects and reports**.

## 10. References

- buildingSMART International. *Industry Foundation Classes (IFC)*.
- buildingSMART International. *Information Delivery Specification (IDS)*.
- IfcOpenShell. *Python API Documentation*.
- PyMuPDF. *Documentation*.
- Building 308. *Structural Report, 26-06-D-STR-Anon.pdf*.
