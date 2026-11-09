# Assignment 3 – Teach

## How to Organize and Document BIM Projects Using GitHub

This tutorial explains how to use GitHub to organize, document, and share BIM projects.
# Collaborating on IFC Models with GitHub, Bonsai and VS Code

## Summary
**Title:** Collaborating on IFC Models with GitHub, Bonsai and VS Code

**Description:** A step-by-step workflow for teams sharing one BIM project on GitHub: setting up a repository, branching, committing IFC changes from Bonsai, reviewing diffs in VS Code, and resolving merge conflicts without breaking the model.

**Video:** [YouTube link]

## About this tutorial
- **Focus area:** [your focus area]
- **BIM use:** [e.g. coordination / collaborative modelling]
- **Role and learning level:** [role], level [1/2/3]
- **Learning need owner:** [person/group who proposed the need]
- **Time needed:** ~[X] minutes

### Learning objectives
After this tutorial you will be able to:
1. Set up a shared GitHub repository for a BIM project
2. Commit and push IFC changes made in Bonsai using VS Code
3. Read an IFC diff to see what a teammate changed
4. Work on branches and merge them through pull requests
5. Avoid and resolve conflicts in a shared IFC model

## Prerequisites
- Blender [version] with Bonsai [version]
- VS Code
- Git installed and a GitHub account
- Python with IfcOpenShell (only for the optional script)

## Repository structure
```
project-repo/
├── README.md
├── .gitignore
├── model/
│   └── project.ifc        # the shared model (source of truth)
├── scripts/
│   └── check_ifc.py       # optional pre-commit check
├── docs/
│   ├── images/            # screenshots for this README
│   └── team-agreement.md  # copyable workflow contract
└── example-files/         # small sample IFC for practising
```

## Part 1: Set up the repository
### 1.1 Create the repo on GitHub and invite teammates
### 1.2 Clone it in VS Code
### 1.3 Add a .gitignore
```gitignore
*.blend1
*.blend
__pycache__/
```
### 1.4 Why we version the IFC, not the .blend

## Part 2: The daily workflow
### 2.1 Pull before you start
### 2.2 Edit the IFC in Bonsai and save
### 2.3 Stage, commit and push from VS Code
### 2.4 Writing useful commit messages

## Part 3: Reading changes
### 3.1 Opening the diff view in VS Code
### 3.2 What an IFC change looks like (worked example)

## Part 4: Branches and pull requests
### 4.1 Creating a branch per person or task
### 4.2 Opening a pull request on GitHub
### 4.3 Reviewing and merging

## Part 5: Merge conflicts
### 5.1 Demonstration: two people edit the same model
### 5.2 Preventing conflicts (split work by discipline/storey, communicate)
### 5.3 Resolving a conflict
### 5.4 Advanced: Bonsai's Git panel and ifcmerge (if your version supports it)

## Part 6 (optional): Python check before committing
```python
# scripts/check_ifc.py
# Checks that the IFC opens and reports element counts.
```

## Team workflow agreement
Template in `docs/team-agreement.md`: who edits what, branch naming, when to pull/push, who reviews PRs.

## Exercises
1. Clone the example repo and make your first commit
2. Create a branch, change a wall property, open a PR
3. Create and resolve a deliberate conflict with a partner

## Troubleshooting
| Problem | Fix |
|---|---|
| Push rejected | Pull first, then push again |
| Merge conflict in IFC | See Part 5.3 |

## Peer feedback
[Link to feedback form / summary of feedback received]

## Authors
[Names, group number]
