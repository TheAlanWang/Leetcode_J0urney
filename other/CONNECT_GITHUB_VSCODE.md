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
## Branch
### Create new branch and switch
1. Create a branch (does not switch)
```zsh
git branch new-branch-name
```
2. Switch to the branch
```zsh
git checkout new-branch-name
```

Short cut: create and switch
```zsh
git checkout -b new-branch-name
```

3. make changes, then commit
```zsh
git checkout branch1
git add .
git commit -m "Finish feature X"
git push -u origin branch1
```

### Merge
#### Method 1: Submit a Pull Request (Recommended for teamwork)
1. After push feature branch to remote
`git push -u origin branch-name`

2. Open a Pull Request on GitHub/GitLab
- base: `main`
- compare: `branch-name`
- Fill in title and description (what feature/fix this branch adds).

3. **Get the PR reviewed and tested** → Click **Merge** button.

4. Update your local main branch
```zsh
git checkout main
git pull origin main
```

#### Method2: local merge
1. Make sure you’re on `main` and up to date
    `git checkout main git pull origin main`
2. Merge your feature branch locally
```zsh
git merge branch-name
```
    - If no conflicts → Git creates a merge commit automatically.   
    - If conflicts → resolve them manually, then `git add . && git commit`.
        
3. Push the updated `main` branch to remote
```zsh
git push origin main
```

### Remove file already in github
#### 1. add file in `.gitignore`
`.DS_Store`

#### 2.Remove `.DS_Store` from Git tracking
```zsh
git rm --cached .DS_Store 
git commit -m "Remove .DS_Store" 
git push
```

### Delete branch
```zsh
# Safe delete (only if branch is fully merged)
git branch -d branch-name

# Force delete (even if not merged)
git branch -D branch-name
```