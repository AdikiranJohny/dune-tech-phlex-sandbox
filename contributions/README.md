# Contributions

Each participant has one folder here, named after their GitHub username. If you only
work in your own folder, nobody's pull request can conflict with anyone else's.

```
contributions/
├── README.md        <- this file
├── _template/       <- copy this to start your folder
├── _stretch/        <- optional: a C++ algorithm to add to your folder
└── <your-username>/ <- your work
```

Folders that start with `_` are examples. Copy them; don't edit them.

At the end of the session, `tools/word-cloud.py` collects the "One word for today" from every
merged README and makes a word cloud for the room.

## How to contribute

1. **Fork** this repository on GitHub (the Fork button, top right).
2. **Clone your fork** and make a branch:
   ```bash
   git clone https://github.com/<you>/phlex-india-sandbox.git
   cd phlex-india-sandbox
   git switch -c my-first-contribution
   ```
3. **Copy the template** into your own folder:
   ```bash
   cp -r contributions/_template contributions/<you>
   ```
4. Do the work, and fill in `contributions/<you>/README.md`.
5. **Commit** with a message that says what the change does, then **push** to your fork:
   ```bash
   git add contributions/<you>
   git commit -m "Add my first Phlex workflow: 20 spills, sum only"
   git push -u origin my-first-contribution
   ```
6. On GitHub, open a **pull request** from your branch to `main` of
   `nuRiceLab/phlex-india-sandbox`. Fill in the checklist in the description.
7. Ask someone to review it. When it's approved, an instructor merges it.

**No terminal?** You can do all of this in the browser. On your fork, go to `contributions/`,
click **Add file → Create new file**, type `<you>/README.md` as the name, write your README,
and pick **Create a new branch** when you commit. GitHub then offers to open the pull request.

## Review checklist

Reviewing is as important as writing the code. On DUNE, nothing is merged until someone
else has read it. When you review, open the **Files changed** tab and check:

- [ ] **Only one folder.** Every changed file is inside `contributions/<author>/`.
- [ ] **A useful README.** It says what the work does, how to run it (a command someone
      else can copy), and what output to expect.
- [ ] **Clear commit messages.** Each message says what changed. "stuff" or "fix" doesn't.
- [ ] **No build products or personal files.** No `CMakeCache.txt`, `.so`, `.root`,
      `build/`, notes or passwords.
- [ ] **Code and configuration agree.** Names in the `.jsonnet` match the plugin and
      products in the code.
- [ ] **The code makes sense.** Comments match what the code does. Checks (`assert`) test
      the right thing.

To comment on a line, hover over it and click the blue **+**. To propose an exact fix, click
the ± icon to add a `suggestion` block. When you're done, click **Review changes** and choose
**Comment**, **Approve** or **Request changes**.

Be kind and specific. "Could you add the command you ran to the README?" helps more than
"README bad".

## Answering a review

You don't open a new pull request. Fix the problem in the same branch, commit and push
again. The pull request updates by itself, and the reviewer can see the new commit.
