# Connect VS Code with GitHub

This guide explains how to connect Visual Studio Code (VS Code) with GitHub step by step.

---

## 1. Install Requirements
- Install [Git](https://git-scm.com/downloads)  
  ```bash
  git --version
  ```
- Install VS Code extension: **GitHub Pull Requests and Issues**
- Have a GitHub account and repository ready

---

## 2. Sign in to GitHub in VS Code
1. Open VS Code
2. Go to bottom-left **Accounts** icon → **Sign in to GitHub**
3. Authorize in browser → return to VS Code

---

## 3. Clone a Repository
- Open Command Palette (`Ctrl+Shift+P` / `Cmd+Shift+P` on Mac)  
- Run:
  ```
  Git: Clone
  ```
- Paste repository URL, choose folder location

---

## 4. Push Local Project to GitHub
If you already have local code but no GitHub repo connected:

```bash
git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/<USERNAME>/<REPO>.git
git push -u origin main
```

---

## 5. Use Source Control in VS Code
- Open **Source Control** tab (branch icon on sidebar)
- Stage changes (+ button)
- Write commit message
- Click ✓ to commit
- Push to GitHub

---

## 6. Verify Connection
```bash
git remote -v
```
You should see your GitHub repository URL.  
Go to GitHub webpage to confirm your code is uploaded.

---

✅ Now your VS Code is connected with GitHub!

## Branch
### create new branch and switch
1. create new branch
```zsh
git branch new-branch-name
```
2. change to new branch
```zsh
git checkout new-branch-name
```

create change to new branch
```zsh
git checkout -b new-branch-name
```

merge branch to main
```zsh
git checkout main
git merge branch1
```

in branch1 push to branch1
```zsh
git checkout branch1
git add .
git commit -m "Finish feature X"
git push -u origin branch1
```

### Merge
Method1: 
	switch to github, apply PR
Method2:
```zsh

```

