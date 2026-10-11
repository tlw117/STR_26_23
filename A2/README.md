# Assignment 2 – Use Case

**Group:** 23  
**Focus Area:** Structures  
**Building:** #2606  
**Report:** 26-06-A-ClientReport-Anon

---

## A2a: About Our Group

### Python Coding Confidence

Our group's combined Python coding confidence score is **9 out of 12**.

Individual scores:
- Inga: 3 – Agree
- Sóley: 3 – Agree
- Þórdís: 3 – Agree

### Focus Area and Role

Our group's focus area is structures, specifically columns. We are investigating the existing S206 steel columns, which were identified in the previous report as potentially having insufficient load-bearing capacity for the proposed two-storey extension.

Our group takes the role of **analysts**, as our objective is to assess structural information and support engineering decisions using BIM data.

---

## A2b: Identify Claim

### Building

For our focus area, we will use Building #2606. The issue was identified in the Client Report prepared by Group 6 in Advanced Building Design 2026.

**Source:** 26-06-A-ClientReport-Anon, page 10.

### Claim

The existing S206 steel columns may not have sufficient axial load-bearing capacity to support the additional loads resulting from the proposed two-storey extension.

### Description

The Client Report (p. 10) states that the existing S206 steel columns may not have sufficient capacity for the additional loads caused by the proposed two-storey extension.

The report identifies the S206 columns as 60 × 60 mm solid square steel columns and states that they will likely need to be replaced for the proposed construction.

The aim of this investigation is therefore to identify the S206 columns in the structural IFC model, extract their geometry and material properties, and assess their axial load-bearing capacity.

### Justification

By focusing on the S206 steel columns, we can use the BIM model to investigate their geometry and material properties and assess whether they have sufficient axial capacity for the additional loads from the proposed extension.

This is relevant because the existing columns may need to be strengthened or replaced before the extension can be constructed.

The investigation can support the structural engineer in making an informed decision about whether the existing columns can be retained.

---

## A2c: Use Case

### How Would You Check This Claim?

The proposed investigation consists of the following steps:

1. **Identify the S206 steel columns in the structural IFC model.**
   - Locate the relevant column elements.
   - Extract the column dimensions and geometry.
   - Extract the available material properties.
   - Check whether the required information for a steel capacity calculation is available.

2. **Determine the design load acting on the S206 columns.**
   - Obtain the design axial load resulting from the existing structure and proposed two-storey extension.
   - The structural engineer is responsible for establishing the appropriate design loads.

3. **Calculate the axial load-bearing capacity of the columns.**
   - Use the extracted IFC geometry and relevant steel material properties.
   - Determine the cross-sectional area and the required steel design parameters.
   - Consider the influence of column length, buckling and stability where relevant.

4. **Compare the design load with the column resistance.**
   - Design axial load: N_Ed
   - Design axial resistance: N_Rd
   - Check whether N_Ed ≤ N_Rd.

5. **Evaluate the results.**
   - If the calculated resistance is sufficient, the existing column may be retained, subject to the remaining structural checks.
   - If the resistance is insufficient, strengthening or replacement should be investigated.
   - If required information is missing, the assessment cannot be completed without additional data.

6. **Generate an assessment report.**
   - Present the extracted IFC information.
   - Present the calculation results.
   - Identify missing information and assumptions.
   - Provide the results for review by the structural engineer.

### When Would This Claim Need to Be Checked?

The claim should be checked during the design phase, before the proposed two-storey extension is approved and detailed.

The capacity of the existing columns needs to be verified before additional loads are introduced to the structure.

### What Information Does This Claim Rely On?

The assessment relies on information about the S206 columns, including:

- Column identification and location.
- Column geometry and dimensions.
- Cross-sectional area.
- Column length.
- Material type and steel grade.
- Steel yield strength.
- Relevant buckling length and support conditions.
- Design axial load from the existing structure and proposed extension.

Some information may be available in the structural IFC model, while other information, particularly design loads and structural boundary conditions, may need to be provided separately by the structural engineer.

### What Phase Does the Use Case Belong To?

**Design phase.**

The structural capacity should be verified before the extension is constructed and before the final structural design is approved.

### What BIM Purpose Is Required?

The main BIM purpose is **Analyse**, because BIM information is used to assess the structural capacity of the existing S206 columns.

**Gather** is also relevant, since geometry and material information must first be extracted from the IFC model.

**Communicate** is relevant because the results will be presented in an assessment report to support structural design decisions.

### What BIM Use Case Is This Closest To?

The use case is closest to **Structural Analysis**, specifically the example **"2520: IFC Column axial capacity analysis"**.

This example extracts information about columns from an IFC model and uses it to calculate their axial capacity.

Our use case extends this idea by focusing specifically on existing S206 steel columns and comparing their calculated resistance with the design load from the proposed extension.

The existing example appears to use concrete material strength and would therefore need to be adapted to handle steel properties and appropriate steel design calculations.

### BPMN Diagram – Overall Workflow

The following BPMN diagram illustrates the proposed workflow for investigating the structural capacity of the S206 steel columns.

It includes the structural engineer, the IFC model and the analysis tool, as well as the information exchange and decision-making process.

![A2c – Overall BPMN Workflow](IMG/A2c_workflow.svg)

---

## A2d: Scope the Use Case

The proposed Python tool will focus on the part of the overall workflow where information about the S206 steel columns is extracted from the IFC model and used to calculate their axial load-bearing capacity.

The tool should:

1. Identify the relevant S206 steel columns in the structural IFC model.
2. Extract their available geometry and material information.
3. Check whether the required information is available.
4. Determine the cross-sectional area.
5. Obtain or accept the required steel strength and other calculation parameters.
6. Calculate the axial resistance of the columns.
7. Generate an assessment output for the structural engineer.

The tool will use **Python and IfcOpenShell** to access and process IFC data.

### Scope Limitations

Determining the complete structural loading from the proposed extension and redesigning or replacing the columns are outside the main scope of the Python tool.

The design load must therefore be provided separately.

A complete structural verification may also require buckling calculations, connection checks and other stability assessments. If the necessary information is unavailable, the tool should identify this limitation rather than conclude that a column is structurally safe.

The tool is intended to support the structural engineer and does not replace a complete structural design assessment.

### BPMN Diagram – Python Tool Scope

The diagram below highlights the activities that are intended to be implemented or supported by the Python tool.

The highlighted steps represent the new script or functions needed for the use case.

![A2d – Highlighted Python Tool Scope](IMG/A2d_tool_scope.svg)

---

## A2e: Tool Idea

### Proposed OpenBIM Tool

Our proposed tool is a Python-based OpenBIM tool developed using **IfcOpenShell**.

The tool will identify the S206 steel columns in the structural IFC model and extract relevant information such as geometry, cross-sectional dimensions, column length and material properties.

The extracted information will then be used to calculate the axial load-bearing capacity of the columns, using relevant steel design parameters.

The tool will build upon the existing example **"2520: IFC Column axial capacity analysis"**, adapting the calculation approach to steel columns.

The calculated resistance can be compared with a design load provided by the structural engineer to support the assessment of whether the existing columns may be retained or require further investigation.

The tool should also identify missing information and clearly communicate any assumptions or limitations.

### Proposed Tool Workflow

The proposed workflow is:

1. Open the structural IFC model using IfcOpenShell.
2. Identify the relevant S206 column elements.
3. Extract geometry and available material information.
4. Check the completeness of the required data.
5. Calculate the cross-sectional area and axial resistance using the appropriate parameters.
6. Present the calculated resistance and relevant assumptions.
7. Generate an output report for review by the structural engineer.

### Business Value

The tool can reduce the amount of manual work required when assessing existing structural elements and make better use of information already available in BIM models.

Automated data extraction can reduce the risk of transcription errors and make structural assessments more transparent, consistent and repeatable.

The tool could also be adapted to assess other steel columns in future projects, potentially saving time during structural investigations and renovation projects.

### Societal Value

From a societal perspective, the tool can support the reuse of existing structures by helping engineers assess whether existing structural elements can safely remain in use instead of being unnecessarily replaced.

Retaining suitable structural elements can reduce material consumption, construction waste and embodied carbon.

The tool can therefore contribute to more resource-efficient renovation and extension projects.

### BPMN Diagram – Tool Idea

The following BPMN diagram summarises the proposed Python tool, including its main inputs, processing steps and expected outputs.

![A2e – Proposed Python Tool](IMG/A2e_tool_idea.svg)

---

## A2f: Information Requirements

To assess the axial load-bearing capacity of the S206 steel columns, information must be obtained from the structural IFC model and, where necessary, from external structural design documentation.

The following table identifies the required information, its possible location in IFC, and how it could be accessed using IfcOpenShell.

| Required information | Possible IFC location | Availability | IfcOpenShell approach |
|---|---|---|---|
| S206 column identification | `IfcColumn`, `IfcColumnType`, `Name`, `Tag` | To be verified | Identify columns using `by_type("IfcColumn")` and inspect names, tags and types |
| Column geometry | `IfcProductDefinitionShape` and geometric representations | To be verified | Inspect column geometry and representations |
| Cross-sectional dimensions | `IfcProfileDef`, profile representations or geometry | 60 × 60 mm stated in Client Report; IFC verification required | Extract profile dimensions or derive dimensions from geometry |
| Column length | Geometric representation and object placement | To be verified | Extract geometry and calculate column length |
| Material | `IfcMaterial` and material associations | To be verified | Use `ifcopenshell.util.element.get_material()` |
| Steel grade and strength | Material properties or custom IFC property sets | To be verified | Inspect material information and property sets |
| Design axial load | Structural analysis data or external calculations | Not confirmed in IFC | Obtain from structural engineer or external documentation |
| Buckling length and support conditions | Structural analysis information or external documentation | Not confirmed in IFC | Obtain and validate the necessary structural parameters |

### Is the Required Information Available in the Model?

The Client Report identifies the S206 columns as 60 × 60 mm solid square steel columns.

However, the availability of the required information in the structural IFC model has not yet been fully verified.

During the development of the tool, the model must be inspected to determine whether the S206 columns can be identified and whether their geometry, dimensions and material properties can be extracted.

Steel grade, yield strength, buckling length, support conditions and design loads may not be included in the IFC model and may need to be provided separately.

If the required information is unavailable, the tool should report the missing data rather than produce an unsupported capacity assessment.

### Do We Know How to Extract the Information Using IfcOpenShell?

IfcOpenShell provides Python functions for opening IFC files, identifying IFC elements and accessing their attributes, properties, materials and geometry.

We plan to use functions such as:

- `ifcopenshell.open()` to open the IFC model.
- `model.by_type("IfcColumn")` to identify column elements.
- `ifcopenshell.util.element.get_psets()` to access available property sets.
- `ifcopenshell.util.element.get_material()` to retrieve material associations.
- IFC geometry utilities to inspect the column dimensions and cross-sectional geometry.

The exact extraction method will depend on how the structural IFC model represents the S206 columns.

### What Do We Need to Learn?

To implement the tool successfully, we need to develop our understanding of:

1. Identifying specific structural elements in an IFC model using Python and IfcOpenShell.
2. Extracting geometric information and cross-sectional dimensions.
3. Retrieving material properties and steel grade information.
4. Handling missing or incomplete IFC information.
5. Adapting an existing axial capacity calculation tool from concrete to steel.
6. Implementing appropriate steel axial resistance calculations and understanding the influence of buckling.
7. Comparing calculated resistance with externally provided design loads.
8. Generating a clear and reproducible assessment report.

These learning requirements will also be recorded in the course's Teams Excel file.

---

## A2g: Software Licence

### Selected Licence: MIT Licence

We propose to use the **MIT Licence** for our Python-based OpenBIM tool.

The MIT Licence is a permissive open-source software licence that allows other users to use, modify, distribute and further develop the code, provided that the original copyright and licence notice are included.

### Justification

The MIT Licence is appropriate for our project because the tool is intended to support an open and reusable BIM workflow.

It allows other students, researchers and industry professionals to adapt the tool for different structural elements and IFC models.

This supports collaboration, transparency and further development of the tool.

The licence also allows the software to be used in both academic and commercial contexts.

Any reused code or external libraries must continue to comply with their respective software licences.

---

## Conclusion

This assignment presents a proposed OpenBIM workflow for investigating the axial load-bearing capacity of existing S206 steel columns in Building #2606.

The investigation is based on an issue identified in the Client Report, where the columns were considered potentially insufficient for the additional loads resulting from a proposed two-storey extension.

The proposed Python tool will use IfcOpenShell to extract relevant structural information from the IFC model and support an axial capacity assessment.

The main objective is to create a transparent and repeatable workflow that can assist structural engineers in evaluating existing columns and identifying whether further structural investigation, strengthening or replacement may be necessary.

The workflow and tool scope defined in this assignment will provide the basis for implementation in the following assignment.

---

## References

1. Group 6, Advanced Building Design (2026). *26-06-A-ClientReport-Anon*, p. 10.
2. DTU, Advanced Building Information Modelling (41934). *Assignment 2 – Use Case*.
3. OpenBIM tool example: *2520 – IFC Column axial capacity analysis*.
4. IfcOpenShell documentation: https://docs.ifcopenshell.org/
5. MIT Licence: https://opensource.org/license/mit
