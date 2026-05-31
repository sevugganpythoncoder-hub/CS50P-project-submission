# Python Command Line Interface (PCI)

#### Video URL: https://www.youtube.com/watch?v=EBXcY3K9-ms

## Personal Information
- **Name:** Sevuggan Arunachalam
- **Online Handle:** Kev1inmates
- **GitHub Account:** https://github.com/sevugganpythoncoder-hub
- **EdX Username:** sevuggan Arunachalam
- **Language Breakdown:** Python (100%)

---

## Project Overview
The Python Command Line Interface (PCI) is an advanced command-line interpreter built entirely from scratch using Python. It acts as a customized "CMD-Knockoff," replicating the core structural utilities of the traditional Windows Command Prompt while implementing a wide array of built-in features that standard shells lack(unique). 

Traditional command lines can feel slow and tedious, often requiring users to type out incredibly long directory pathways (such as `C:\Users\Name\AppData\Local\BasicFolder\`) just to navigate or perform routine file maintenance. Furthermore, standard system tools require users to bounce between separate graphical user interfaces—like Windows Defender or the Task Manager—to perform essential administrative tasks. PCI solves this friction by combining system navigation, security scanning, process management, and environment customization into a single, cohesive terminal application.

This project represents over 1000+ lines of pure Python code, developed, refined, and packaged over a rigorous two-month development cycle. While a portion of the advanced system hooks and optimization methodologies were inspired by community insights from Reddit and Python's official Discord platform, the architectural implementation and logic design are entirely original.

---

## Distinct and Exclusive Features
PCI stands apart from standard command prompts due to several exclusive, built-in features designed to streamline user workflows:

1. **Integrated System Security (pci-scan and pci-verify):** Instead of relying entirely on heavy background software, PCI introduces direct terminal-based scanning mechanisms to verify file integrity and check for local directory vulnerabilities right from the command prompt.

2. **Dynamic Command Aliasing (`aliases`):** Users can define, store, and execute custom shorthand shortcuts for repetitive tasks, drastically reducing typing time and simplifying deep directory navigation.

3. **Registry Optimization (`scan-reg`):** A specialized diagnostic feature designed to inspect registry paths, helping users keep track of system health in real-time.

4. **Enhanced Path Handling:** Native scripts to automatically parse, strip, and sanitize messy inputs, ensuring that accidental spacing or trailing backslashes never break a terminal command.

For deep documentation on basic operational commands, users can simply type the `help` command within the PCI shell interface to see a complete list of interactive operations.

---

## Architectural Breakdown of Core Functions
To comply with robust software design principles, the critical components of PCI are broken down into dedicated, modular functions. These core functions handle data sanitization, game/logic handling, and interface formatting, and are backed by an automated testing suite in `test_project.py`.

### 1. `clean_path_input`
The `clean_path_input` function is responsible for the terminal's path sanitization logic. When navigating file systems, users frequently copy and paste paths that contain accidental trailing spaces or awkward double backslashes (e.g., `"C:\Users\Sevuggan\   "`). This function strips out leading and trailing whitespaces and formats the string into a valid, standard directory path string. By protecting the system from malformed string errors, it allows commands like directory traversal to execute flawlessly without throwing unhandled exceptions.

### 2. `evaluate_toss`
To add unique utility and simulation features to the CLI environment, PCI includes built-in interactive modules. The `evaluate_toss` function processes user predictions against system-generated outcomes for randomized mini-games or decision-making functions (like a coin toss simulation). It takes the user's choice and the actual result as arguments, handles case-insensitive string comparisons, and outputs a standardized result state (such as `"Win"` or `"Loss"`). This showcases the CLI's capability to process game logic smoothly within a text-based environment.

### 3. `format_host_display`
User experience is highly dependent on clean interface aesthetics. The `format_host_display` function handles the normalization of the system host name or terminal prompt indicator. Operating systems often return hostnames in mixed or lowercase formats (e.g., `desktop-pci`). This function takes the raw host string, cleans up unnecessary characters, and applies strict capitalization styles (e.g., transforming it into `DESKTOP-PCI`). This ensures that the command line prompt looks uniform, professional, and visually consistent every time a new command line session is initialized.

---

## How to Run the Project and Tests
To launch the primary command line interface, execute the main Python file from your terminal:

python/py project.py
py/python test_project.py

another side note the functions mentioned above are stated for **pytest** so, Yeah Just wanted to clear that out.