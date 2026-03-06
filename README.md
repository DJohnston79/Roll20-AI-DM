# Roll20 AI Dungeon Master

A local, private D&D 5e Dungeon Master powered by Llama 3.2 and Ollama. This tool acts as a bridge between a local Large Language Model and your Roll20 tabletop sessions, featuring automated session logging and a random monster manual selector.
### 1. Overview

This script allows you to run a private AI DM on your own hardware. It features short-term memory (the AI remembers the current session) and long-term storage (every word is saved to a local text file).
### 2. Prerequisites and Setup

    Ollama: Install from ollama.com and run ollama pull llama3.2 in your terminal.

    Python Libraries: Inside your virtual environment (venv), you must install the required tools: pip install ollama pymupdf

    The Book: You must place your own Monster_Manual.pdf directly into the Roll20_DM folder for the randomizer to work.

### 3. Session Persistence

    Live Memory: The AI remembers your current session as long as the terminal window stays open.

    Hard Copy: Every action, DM response, and dice roll is automatically saved to session_history.txt with a timestamp.

    To Continue a Story: Open your log file, copy the last paragraph of the previous session, and paste it as the starting location when you restart the script.

### 4. The Monster Manual (PDF Integration)

Each time you start a new session, the script performs the following:

    It randomly selects 4 pages from your Monster_Manual.pdf.

    It loads those specific stats into the AI brain for combat reference.

    It displays the page numbers in your terminal so you can refer to the artwork or lore in your own copy of the book.

### 5. Dice Rolling Mechanics

    Players: Players roll their own dice on Roll20. The DM simply enters the result into the prompt (Example: Fighter hits with a 15).

    Enemies: The AI handles enemy math. The DM triggers this by starting a line with the word roll followed by the dice and the action (Example: roll 1d20+2 The Orc attacks).

### 6. Privacy and Security

Your session_history.txt and Monster_Manual.pdf are automatically ignored by Git (via the .gitignore file). This means your code remains public on GitHub, but your personal game notes and copyrighted books stay private on your local machine.


