# Roll20-AI-DM
Here is the plain text version, organized into numbered sections as requested. You can copy and paste this directly into your GitHub README or save it as a text file for your records.


### 1. Overview

Roll20 AI Dungeon Master is a local, private D&D Dungeon Master tool powered by Llama 3.2 and Ollama. This script acts as a bridge between a local AI "brain" on your PC and your Roll20 tabletop sessions, allowing for private storytelling without subscriptions.

### 2. Prerequisites

Before you try to run the script, make sure these three things are installed and ready:

1. **Ollama:** Download and install from ollama.com. Make sure the application is running (look for the icon in your system tray).
2. **Llama 3.2:** Open a standard Command Prompt and run the command: `ollama pull llama3.2`. This downloads the AI model (approx 2.0GB).
3. **Python 3.12+:** Ensure Python is installed on your Windows machine and added to your PATH.

### 3. Setup and Installation

Follow these steps to get the folder ready on your computer:

1. Clone this repository or download the project folder to your Desktop.
2. Open a Command Prompt and navigate to the folder: `cd Desktop\Roll20_DM`
3. Create a virtual environment to keep things clean: `python -m venv venv`
4. Activate the virtual environment: `venv\Scripts\activate`
* (You should now see `(venv)` at the start of your command line).


5. Install the required communication library: `pip install ollama`

### 4. Session Prep (Do this before every game)

To ensure the game runs smoothly without technical lag, check these three items before your players log in:

1. **Check the Engine:** Click the Ollama icon in your Start Menu to ensure the background service is active.
2. **Check the Brain:** In a terminal, type `ollama list` to make sure `llama3.2` appears in the list.
3. **Verify the Script:** Open your `dm_bot.py` file in VS Code to make sure your latest changes are saved.

### 5. How to Play

1. **Launch the DM:** In your `(venv)` terminal, run `python dm_bot.py`.
2. **Set the Scene:** The script will ask for a starting location. Type in the current setting (e.g., "The party is inside a damp cave filled with glowing mushrooms").
3. **The Roll20 Bridge:** - Keep Roll20 open in your browser and the Python terminal open next to it.
* When a player types an action in Roll20, type it into the "Player action" prompt in your terminal.
* When the AI generates the DM's response, copy that text and paste it into the Roll20 chat for your friends to read.



### 6. Dice Rolling and Combat

The script includes a built-in dice roller for the DM.

* If you need to roll for a monster or a check, type `roll` followed by the dice notation (e.g., `roll 1d20+5`).
* The system will calculate the result and feed it directly to the AI so the narration reflects the outcome of the roll.

---

**Would you like me to show you how to add a "Save Game" feature to this script so it writes the story to a text file as you play?**
