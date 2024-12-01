# dbr
A new way to do your daily bible reading

**Daily Bible Reading** is a collection of Python tools designed to assist students in building meaningful study habits. By randomly selecting a verse from the Bible and guiding users through a reflective process, it helps deepen understanding, connect ideas, and set personal goals.

This tool is designed to create meaningful daily Bible study habits, prompting introspection and spiritual growth.

## Features

- **Random Verse Selection**: Selects a random Bible verse each day for study.
- **Reflection Questions**: Provides a set of questions to encourage thoughtful engagement with the text:
  - What is this verse describing?
  - Why is that interesting?
  - What lesson can I learn from this?
  - What does this teach me about Jehovah?
  - What goal should I set based on this lesson?
- **Goal Setting**: Helps users create a personal, actionable goal inspired by the day's study.
- **Progress Logging**: Saves insights and goals to a file for future reference.
- **Extensible Framework**: Prepares for future enhancements, such as auto-fetching verses via web scraping.


## Getting Started

### Step 1: Set Up a Virtual Environment (Recommended)
To avoid conflicts with other Python projects, it's best to use a virtual environment.

1. Create a virtual environment:
   ```bash
   python -m venv dbr_env
   ```
2. Activate the virtual environment:
   - **On Windows**:
     ```bash
     dbr_env\Scripts\activate
     ```
   - **On Linux/macOS**:
     ```bash
     source dbr_env/bin/activate
     ```
3. Install the required libraries in the virtual environment:
   ```bash
   pip install -r requirements.txt
   ```

### Step 2: Add a Convenient `dbr` Command

To simplify running the script, you can add a `dbr` command to your terminal.

1. Locate the script's directory (where `main.py` is saved).
2. Edit your shell's startup file:
   - For **bash**:
     ```bash
     nano ~/.bashrc
     ```
   - For **zsh**:
     ```bash
     nano ~/.zshrc
     ```
3. Add the following alias to the file:
   ```bash
   alias dbr="python /path/to/main.py"
   ```
   Replace `/path/to/` with the full path to the directory containing `main.py`.
4. Save and close the file.
5. Apply the changes:
   ```bash
   source ~/.bashrc  # or source ~/.zshrc
   ```

Now, you can simply type `dbr` in your terminal to start the script!


## Configuration

- This project contains a file to store the structure of the Bible.
- Logs and goals are stored in the `datadir` (defaults to a user cache directory).


## Future Plans

- **Web Scraping**: Fetch verses and commentary directly from online sources.
- **Improved UX**: Add a GUI for a more user-friendly experience.
- **Multi-language Support**: Expand beyond English for global accessibility.


## Contact

For questions or suggestions, feel free to email: [josj@tegosec.com](mailto:josj@tegosec.com).
