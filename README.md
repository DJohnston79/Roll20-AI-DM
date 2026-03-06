### # Roll20 AI Dungeon Master 

A local, private D&D 5e Dungeon Master powered by **Llama 3.2** and **Ollama**. This tool acts as a bridge between a local Large Language Model and your Roll20 tabletop sessions, featuring automated session logging and a random monster manual selector.

### ### 1. Overview

This script allows you to run a private AI DM on your own hardware. It features **Short-term memory** (the AI remembers the current session) and **Long-term storage** (every word is saved to a local text file).

### ### 2. Prerequisites & Setup

1. **Ollama:** Install from ollama.com and run `ollama pull llama3.2` in your terminal.
2. **Python Libraries:** Inside your virtual environment `(venv)`, you must install the required tools:
`pip install ollama pymupdf`
3. **The Book:** You must place your own `Monster_Manual.pdf` directly into the `Roll20_DM` folder for the randomizer to work.

### ### 3. Session Persistence

* **Live Memory:** The AI remembers your current session as long as the terminal window stays open.
* **Hard Copy:** every action, DM response, and dice roll is automatically saved to `session_history.txt` with a timestamp.
* **To Continue a Story:** Open your log file, copy the last paragraph of the previous session, and paste it as the "Starting Location" when you restart the script.

### ### 4. The Monster Manual (PDF Integration)

Each time you start a new session, the script performs the following:

1. It randomly selects 4 pages from your `Monster_Manual.pdf`.
2. It loads those specific stats into the AI's "Brain" for combat reference.
3. It displays the page numbers in your terminal so you can refer to the artwork or lore in your own copy of the book.

### ### 5. Dice Rolling Mechanics

* **Players:** Players roll their own dice on Roll20. The DM simply enters the result into the prompt (e.g., "Fighter hits with a 15").
* **Enemies:** The AI handles enemy math. The DM triggers this by starting a line with 'roll' followed by the dice and the action (e.g., 'roll 1d20+2 The Orc attacks').

### ### 6. Privacy & Security

Your `session_history.txt` and `Monster_Manual.pdf` are automatically ignored by Git (via the `.gitignore` file). This means your code remains public on GitHub, but your personal game notes and copyrighted books stay private on your local machine.

---

### **Final Step for your Terminal:**
