
# Assignment 4 – Tool

## Automated Comparison of Structural Information from IFC Models and Client Reports

**Course:** 41934 Advanced BIM  
**Group:** 23 – Structures  
**Focus Area:** Structures

---

## 1. Introduction

In Assignment 1, our group investigated a claim concerning the S206 steel columns in an existing building. The client report raised concerns about whether these columns would be sufficient to support a proposed two-storey extension.

During our investigation, we found that some of the information presented in the report could not be verified using the available IFC model. This made it difficult to assess the claim based on the available data.

Building on our previous assignments, we aim to develop a Python-based tool that compares structural information from a client report with data extracted from an IFC model.

The purpose is to identify missing information, inconsistencies, and limitations in the available data before carrying out further structural assessments.

## 2. Aim and Objectives

The main aim of this project is to develop a tool that helps users evaluate whether structural information presented in a client report is supported by the available IFC model.

The objectives are to:

- Extract relevant information about steel columns from an IFC model.
- Collect structural information and claims from a client report.
- Compare the information from the two sources.
- Identify missing, inconsistent, or unsupported information.
- Present the results in a clear and understandable format.

## 3. Tool Description

The proposed tool will consist of three main components.

### 3.1 IFC Data Extraction

The first component will use Python and IfcOpenShell to read an IFC model and extract relevant information about steel columns.

Depending on the available model data, this may include:

- Column identification and GlobalId
- Object type and classification
- Geometric information and dimensions
- Material information
- Relevant properties and property sets

The extracted information will be organized for further analysis.

### 3.2 Client Report Data Extraction

The second component will collect relevant structural information and claims from the client report.

The information may include reported column dimensions, material properties, structural assumptions, and other details relevant to the investigation.

The method used to extract this information will be determined during tool development.

### 3.3 Data Comparison and Validation

The third component will compare the extracted IFC data with the information collected from the client report.

The comparison will aim to identify:

- **Matching information:** Data that is consistent between the two sources.
- **Missing information:** Data required for verification but not available in the IFC model.
- **Conflicting information:** Data that differs between the two sources.
- **Unverified claims:** Statements that cannot be confirmed using the available information.

The results will help users understand the reliability and limitations of the available structural information.

## 4. Proposed Workflow

The planned workflow consists of the following steps:

1. Read the IFC model and identify relevant steel columns.
2. Extract available structural information from the IFC model.
3. Collect relevant information from the client report.
4. Compare the information from both sources.
5. Identify missing data and inconsistencies.
6. Generate a summary of the comparison results.

## 5. Model Requirements and IDS

The tool will require specific information from the IFC model to perform the intended comparisons.

An Information Delivery Specification (IDS) will be developed to define relevant information requirements for the structural elements.

The IDS will help identify whether the IFC model contains the required information.

The specific requirements will be defined during tool development.

## 6. Implementation

The tool will be developed in Python, using IfcOpenShell to access and process IFC model data.

The planned code structure includes:

- `extract_ifc.py` – Extract information from the IFC model.
- `extract_report.py` – Collect relevant information from the client report.
- `compare_data.py` – Compare the two datasets and identify differences.
- `main.py` – Run the overall workflow.

The implementation details will be updated as the tool is developed.

## 7. Results and Discussion

*This section will be completed after implementing and testing the tool.*

The results will present the comparison between the client report and the IFC model, highlighting matching information, missing data, and inconsistencies.

## 8. Limitations and Future Improvements

*This section will be completed during tool development.*

Potential limitations include incomplete IFC data, differences in naming conventions, and the availability of information in the client report.

## 9. References

*Relevant references and documentation will be added during development.*
