# Day 10 Morning: Quick Steps

Use the **PowerShell terminal in VS Code** for these steps.

1. In VS Code, open your current folder: `C:\Users\abcd\OneDrive\Desktop\Week2`. Open **Terminal > New Terminal**.

2. Check that Python and Git are installed:

   ```powershell
   py --version
   git --version
   ```

3. Run the inventory app and try its menu. Choose **6** to save and exit:

   ```powershell
   py ".\Day10\Morning_task\A1_CLI_Inventory_PR\inventory_cli.py"
   ```

4. Clone the GitHub repository into a separate folder. Your current `Week2` folder is not a Git clone:

   ```powershell
   Set-Location "$HOME\OneDrive\Desktop"
   git clone https://github.com/shahkritika/Week2.git Week2-git
   Set-Location ".\Week2-git"
   ```

5. Create a feature branch:

   ```powershell
   git switch -c feature/day10-cli-inventory
   ```

   If that branch already exists, use `git switch feature/day10-cli-inventory` instead.

6. If the task folder is missing from the clone, copy it from your original folder:

   ```powershell
   New-Item -ItemType Directory -Force ".\Day10\Morning_task" | Out-Null
   Copy-Item "$HOME\OneDrive\Desktop\Week2\Day10\Morning_task\A1_CLI_Inventory_PR" ".\Day10\Morning_task\" -Recurse
   ```

7. Review and commit the task:

   ```powershell
   git status
   git add ".\Day10\Morning_task\A1_CLI_Inventory_PR"
   git diff --cached
   git commit -m "feat: add CLI inventory manager"
   ```

8. Push your branch:

   ```powershell
   git push -u origin feature/day10-cli-inventory
   ```

9. On GitHub, open the Week2 repository and create a pull request from `feature/day10-cli-inventory` into `main`. Review the changed files, then create the pull request.

If `py` is not recognized, try `python` instead. Do not force-push or discard changes you need.
