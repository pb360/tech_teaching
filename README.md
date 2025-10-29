# Tech Teaching: Jupyter Notebook Orientation

Welcome! This folder contains material for an introductory session on Jupyter notebooks tailored to professionals exploring law, litigation, and personal sovereignty. The goal is to help you feel comfortable launching JupyterLab, organizing knowledge, and capturing insights with minimal coding.

## Class Goals
- Understand how Jupyter notebooks can support research, case preparation, and knowledge management.
- Launch JupyterLab on Windows, macOS, or Linux and create your first notebook.
- Practice adding rich text (Markdown), LaTeX-style math, and attachments.
- Learn simple productivity boosters: table of contents generation, keyboard shortcuts, and version control with Git.
- Know how to save work locally and optionally publish it to a remote Git repository.

## Recommended Session Flow
1. **Tour the Interface**: Explore notebook cells, Markdown vs. code, and the command palette.
2. **Capture Notes**: Draft bullet points, legal citations, and personal checklists using Markdown formatting.
3. **Enhance Formatting**: Insert LaTeX snippets, tables, and embedded files for evidence or references.
4. **Organize with TOC Helper**: Run the provided helper to auto-build a table of contents.
5. **Share Your Work**: Save, export to PDF, and (optionally) push to a Git remote for collaboration.

## Prerequisites
- A computer running Windows 10/11, macOS 12+, or a modern Linux distribution.
- Internet access to download software.
- 3 GB of free disk space.
- Willingness to copy and paste a few commands into a terminal/PowerShell window (no coding experience required).
- Git installed so you can download (clone) class materials—see the quick guide below.

## Install Git (All Platforms)
Git is the tool we use to copy the class repository and keep it updated. Install it once, and you are good to go for future workshops.

- **Windows**: Visit <https://git-scm.com/download/win> and click the download button. Run the installer, accept the license, leave the defaults selected, and finish. After installation you will have *Git Bash* (a terminal) and Git integrated into Windows Terminal/PowerShell.
- **macOS**: Open Terminal and run `brew install git` (or install Homebrew first—see the macOS section). Alternatively, install Apple’s Command Line Tools by running `xcode-select --install`, which includes Git.
- **Linux**: Use your package manager, e.g., on Ubuntu/Debian run `sudo apt install git`.

Once Git is installed, you can clone this project whenever you like:

```bash
git clone https://github.com/pb360/tech_teaching.git
```

This creates a `tech_teaching` folder containing the notebook, helper script, and README.

## Setup: Windows
1. **Download Python 3**
   - Go to <https://www.python.org/downloads/windows/> and click the big yellow *Download Python 3.x* button.
   - When the installer opens, check the box labeled **Add Python to PATH** (very important) and click *Install Now*. Wait for it to finish, then close the window.
2. **Open a Terminal You Like**
   - Click *Start*, type `Windows Terminal` (or `PowerShell`), and press *Enter*. You can also use *Git Bash* if you prefer—everything below works there too.
3. **Create a Workspace Folder**
   - Choose where you want to keep class files and run:
     ```powershell
     cd %USERPROFILE%\Documents
     git clone https://github.com/pb360/tech_teaching.git
     cd tech_teaching
     ```
   - If you already cloned the project earlier, just `cd` into the folder instead of cloning again.
4. **Create and Activate a Virtual Environment**
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```
   - The prompt should now start with `(.venv)` to show the environment is active. If PowerShell blocks the command, run `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` once and try again.
5. **Install JupyterLab and Required Packages**
   ```powershell
   python -m pip install --upgrade pip
   pip install jupyterlab nbformat requests jupyter-server ipykernel
   ```
6. **Launch JupyterLab**
   ```powershell
   jupyter lab
   ```
   - Your default browser will open automatically. Choose *File → Open* and select `intro-class.ipynb` to begin exploring.

## Setup: macOS
1. **Install Homebrew** (skip if already installed)
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
   After installation, follow the on-screen `eval` command to add Homebrew to your shell.
2. **Install Git and Python 3**
   ```bash
   brew install git python
   ```
3. **Clone the Class Materials (or update them)**
   ```bash
   cd ~/Documents
   git clone https://github.com/pb360/tech_teaching.git
   cd tech_teaching
   ```
   If the folder already exists, use `cd tech_teaching` and `git pull` to grab updates instead of cloning again.
4. **Create a Virtual Environment**
   ```bash
   python3 -m venv ~/jupyter-env
   source ~/jupyter-env/bin/activate
   ```
5. **Install JupyterLab and Helpers**
   ```bash
   python -m pip install --upgrade pip
   pip install jupyterlab nbformat requests jupyter-server ipykernel
   ```
6. **Launch JupyterLab**
   ```bash
   jupyter lab
   ```
   A new browser tab opens; choose *File → New Notebook* to begin.

## Setup: Linux (Ubuntu/Debian)
1. **Update System Packages**
   ```bash
   sudo apt update
   sudo apt install -y git python3 python3-venv python3-pip
   ```
2. **Clone the Class Materials**
   ```bash
   cd ~
   git clone https://github.com/pb360/tech_teaching.git
   cd tech_teaching
   ```
   Already have the folder? Run `cd tech_teaching && git pull` instead.
3. **Create a Virtual Environment**
   ```bash
   python3 -m venv ~/jupyter-env
   source ~/jupyter-env/bin/activate
   ```
4. **Install JupyterLab and Helpers**
   ```bash
   python -m pip install --upgrade pip
   pip install jupyterlab nbformat requests jupyter-server ipykernel
   ```
5. **Launch JupyterLab**
   ```bash
   jupyter lab
   ```
   Copy the URL shown in the terminal into your browser if it does not open automatically.

## Working with the Table of Contents Helper
The starter notebook includes a helper that auto-generates an in-notebook table of contents, skipping headings below level three. To reuse it in other notebooks:

```python
from local_automation import generate_toc_nb

generate_toc_nb(skip_level=3)
```

Make sure `local_automation.py` sits in the same folder as your notebook (or in your Python path). Place the call in a code cell near the top of the notebook and run it after editing headings to refresh the table of contents.

## Tips for Non-Programmers
- **Markdown is your friend**: Use `**bold**`, `*italics*`, and bullet lists to structure arguments.
- **Keyboard shortcuts**: Press `Esc` then `H` in JupyterLab to see shortcut keys (e.g., `A` to add a cell above).
- **Autosave & checkpoints**: JupyterLab saves automatically, but you can create manual checkpoints via *File → Save and Checkpoint*.
- **Attachments**: Drag PDFs and images into Markdown cells to keep evidence alongside notes.
- **Exporting**: Use *File → Save and Export Notebook As → PDF* for sharing with courts or clients.
- **LaTeX math**: Wrap formulas in `$...$` for inline math or `$$...$$` for centered equations (e.g., `$P(\text{win}) = \frac{\text{favorable cases}}{\text{total cases}}$`).

## Optional: Create a GitHub Remote
1. Sign in to <https://github.com> and click **New repository**.
2. Set the repository name to `tech-teaching` (or similar) and create it **without** a README (we already have one locally).
3. Back in this folder, initialize Git and push:
   ```bash
   git init
   git add .
   git commit -m "Initial class materials"
   git branch -M main
   git remote add origin https://github.com/<your-username>/tech-teaching.git
   git push -u origin main
   ```
4. Share the repository link with participants so they can clone or download the materials.

## Next Steps
- Review the included notebook (`intro-class.ipynb`) before class and personalize the prompts.
- Consider recording a short screencast walking through the setup for participants who prefer video.
- Collect questions from your audience ahead of time and add them as discussion prompts in the notebook.

Enjoy guiding your group through the power of Jupyter notebooks!
