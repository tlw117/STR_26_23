# A1: Forensic BIM

## Group

Group 23

## Focus Area

Structures

## Report

26-06-A-ClientReport-Anon  
Page number: 10

## Claim

The existing S206 steel columns may not have sufficient load-bearing capacity for the additional loads resulting from the proposed two-storey extension.

The Client Report identifies the S206 columns as 60 × 60 mm solid square steel columns and states that they will likely need to be replaced for the proposed construction.

## Investigation

The structural IFC model will be investigated to identify the S206 steel columns and examine their geometry, dimensions, and material properties.

The available BIM data will be assessed to determine whether sufficient information is available to verify the structural capacity of the columns under the proposed additional loading.

## Identified Issues

This issue is considered a design issue. The Client Report identifies the S206 steel columns as potentially inadequate for the increased loads from the proposed extension.

## Possible Solutions

One potential solution is to verify the axial capacity of the S206 steel columns and determine whether they can safely carry the increased loads resulting from the proposed extension.

An existing OpenBIM tool, "2520: IFC Column Axial Capacity Analysis", was identified as a possible basis for this investigation. The tool extracts column geometry and material information from an IFC model and uses this information to calculate the axial capacity of columns.

The tool could potentially be adapted to investigate the S206 steel columns and support the assessment of whether they need to be strengthened or replaced.

The tool is highly relevant to the issue, since it calculates axial capacity based on column geometry and material properties. However, because the current script appears to use concrete strength, it would need to be adapted to handle steel properties before it could be used to verify the capacity of the S206 steel columns.

## Conclusion

The investigation will determine whether the available IFC data is sufficient to assess the axial capacity of the S206 steel columns. If the required geometry and material properties are available, the existing OpenBIM tool could be adapted for steel columns and used to evaluate whether strengthening or replacement is necessary.
