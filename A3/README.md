# Assignment 3 – Teach

## How to Organize and Document BIM Projects Using GitHub

# Adding Files and Writing READMEs on GitHub

## Summary
**Title:** Adding Files and Writing READMEs on GitHub

**Description:** A beginner's guide to working in a shared GitHub repository: adding files and folders, committing changes, and writing clear README files in Markdown with headings, images, links, code blocks and tables.

**Video:** [YouTube link]

## Why we made this tutorial
When our group started using GitHub for the course, we struggled with the basics. We weren't sure what a repository was, we couldn't find the "Add file" button, and we didn't know how to create a folder for each assignment. Writing READMEs in Markdown was also new to us.

Every group in the course has to submit their work through GitHub, but there wasn't a simple tutorial covering these first steps. We made this tutorial so other students can skip the confusion we went through.

[Add your own experiences here: what was hardest, what you wish you had known at the start.]

## About this tutorial
- **Focus area:** [your focus area]
- **BIM use:** [how GitHub supports your BIM work, e.g. sharing models, scripts and reports]
- **Role and learning level:** [role], level [1/2/3]
- **Learning need owner:** [person/group who proposed the need]

### Learning objectives
After this tutorial you will be able to:
1. Add, upload and edit files in a shared GitHub repository
2. Create folders to organise your assignments
3. Commit changes with clear commit messages
4. Write a README in Markdown with headings, lists, links, images, code blocks and tables

## Prerequisites
- A free GitHub account
- Access to a repository (as owner or invited collaborator)

## Key terms
| Term | What it means |
|---|---|
| Repository (repo) | A project folder on GitHub that keeps a full history of every change |
| Commit | A saved snapshot of your changes, with a short message describing them |
| Collaborator | A person who has been given permission to edit a repo |
| README | The text file GitHub shows on a folder's page, used to describe the work |
| Markdown | A simple way of formatting text using symbols like `#` and `*` |

---

## Part 1: Working on GitHub

### 1.1 Adding a file
1. Make sure you are **signed in** to GitHub.
2. Open your repository's main page.
3. Click the **Add file** button (next to the green **Code** button) and choose **Create new file**.
4. Type a name for your file in the box at the top, e.g. `notes.md`.
5. Write the content of your file in the large text box.
6. Click the green **Commit changes...** button (see 1.5 for what to write).

> If you can't see the **Add file** button, you are either not signed in or not a collaborator on the repo. See Troubleshooting.

### 1.2 Creating a folder
GitHub can't create empty folders, so you make a folder by creating a file inside it.

1. Click **Add file → Create new file**.
2. In the filename box, type the folder name followed by a slash, e.g. `A3/`.
3. GitHub turns `A3` into a folder automatically. Now type the filename, e.g. `README.md`, so the full path reads `A3/README.md`.
4. Add some content and click **Commit changes...**.

To create a file inside a folder that already exists, open that folder first, then click **Add file**.

### 1.3 Uploading files
Use this for images, PDFs, IFC models, Python scripts and other files you already have on your computer.

1. Open the folder you want to upload to (e.g. `A3`).
2. Click **Add file → Upload files**.
3. Drag your files into the page, or click **choose your files** to browse.
4. Write a commit message, e.g. "Add screenshots for A3".
5. Click **Commit changes**.

Tip: keep images in their own folder, e.g. `A3/images/`. To do that, upload them from inside the `images` folder (create it first with a placeholder file, as in 1.2).

### 1.4 Editing a file
1. Click on the file to open it.
2. Click the **pencil icon** (Edit this file) at the top right of the file.
3. Make your changes.
4. Click **Commit changes...**.

### 1.5 Committing and writing good commit messages
Every change you make on GitHub is saved as a **commit**. When you click **Commit changes...**, a window appears:

1. **Commit message:** a short line describing what you changed.
2. **Extended description** (optional): more detail if needed.
3. Leave **Commit directly to the main branch** selected.
4. Click **Commit changes**.

Good commit messages tell your teammates what happened without opening the file:

| Bad | Good |
|---|---|
| `update` | `Add learning objectives to A3 README` |
| `asdf` | `Fix broken image link in A2` |
| `changes` | `Upload IFC model for structural analysis` |

You can see every commit by clicking **Commits** on the repo's main page. This shows who changed what and when.

---

## Part 2: Writing a README in Markdown

A file called `README.md` is shown automatically on its folder's page. The `.md` ending means it is written in **Markdown**, a simple way to format text using symbols. The examples below show what you type on the left and what it looks like once it's displayed.

### 2.1 Headings
Use `#` symbols. More `#` means a smaller heading.

```markdown
# Main title
## Section
### Subsection
```

Leave a space after the `#` and a blank line before each heading.

### 2.2 Bold, italic and lists
```markdown
**bold text**
*italic text*

- bullet point
- another bullet point

1. first step
2. second step
```

Leave a blank line before a list, or it may not display correctly.

### 2.3 Links
```markdown
[text people see](https://www.example.com)
```

You can also link to another file in your repo:

```markdown
[See our A2 work](../A2/README.md)
```

### 2.4 Images
1. Upload the image to your repo (see 1.3), e.g. to `A3/images/`.
2. In your README, write:

```markdown
![Short description of the image](images/screenshot.png)
```

The path is relative to the README. If the README is in `A3` and the image is in `A3/images`, the path is `images/screenshot.png`. Filenames are case sensitive, so `Screenshot.PNG` and `screenshot.png` are different.

### 2.5 Code blocks
For a short piece of code inside a sentence, use single backticks: `` `print("hello")` ``.

For several lines, use three backticks before and after, and add the language name for colour highlighting:

````markdown
```python
import ifcopenshell
model = ifcopenshell.open("model.ifc")
print(model.by_type("IfcWall"))
```
````

### 2.6 Tables
```markdown
| Name | Role |
|---|---|
| Anna | Modeller |
| Ben | Analyst |
```

The second line (`|---|---|`) is required. It tells Markdown the first line is the header.

### 2.7 Checking your work with Preview
1. While editing a file, click the **Preview** tab at the top of the editor.
2. Check that headings, lists, images and tables look right.
3. Switch back to **Edit** to fix anything, then commit.

---

## Troubleshooting
| Problem | Fix |
|---|---|
| No "Add file" button | You're not signed in, or not a collaborator. Ask the repo owner to invite you under **Settings → Collaborators** |
| Can't create an empty folder | GitHub doesn't allow empty folders. Create a file inside it, e.g. `A3/README.md` |
| Image doesn't show in README | Check the path is relative to the README, the image is uploaded, and the filename matches exactly (including capitals) |
| Formatting looks wrong | Check the Preview tab, and leave a blank line before lists and headings |
| Heading shows as `#Title` | Add a space after the `#` |
