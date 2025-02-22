# Automated Browser Tab Opener in Python
This repository contains two Python scripts for automating the opening of multiple browser tabs using Google Chrome. These scripts are designed to enhance productivity by quickly accessing frequently used websites.

**Scripts Overview:**
1. Predefined Website Version (auto_browser_opener.py):
- This version has a predefined list of websites embedded directly in the code.
- Automatically opens the same websites each time the script is run, ideal for setting up a daily work environment.

2. Manual Website Input Version (auto_browser_opener_with_input.py):
- This version prompts the user to input a list of websites manually after the program is executed.
- Useful for dynamic scenarios where the list of websites may vary each time.

**HOW TO USE:**
1. Clone the repo or download the script
2. Ensure that your browser (Google, Firefox, etc) is installed and the path is correctly set in the code for smooth execution.
3. Run the desired script using any Python environment.

**AUTOMATE THE USEAGE TO RUN ON BOOTUP:**
1. Convert the script (.py) to executable file (.exe):
- pip install -U pyinstaller
#Open a command prompt/shell window, and navigate to the directory where your .py file is located, then build your app with the following command:
- pyinstaller your_script.py
your bundled application should now be available in the dist folder.

2. Run the exe on bootup:
- press "win+r"
- search "shell:startup"
- copy and paste the .exe file into that folder/directory.
