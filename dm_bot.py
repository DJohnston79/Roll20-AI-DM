import ollama
import random
from datetime import datetime

def roll_dice(dice_query):
    """Simple helper to simulate DM rolls like '1d20+3'"""
    try:
        # Example: '1d20+5' -> parts = ['1', '20+5']
        num_dice, rest = dice_query.lower().split('d')
        if '+' in rest:
            sides, bonus = map(int, rest.split('+'))
        else:
            sides, bonus = int(rest), 0
        
        rolls = [random.randint(1, sides) for _ in range(int(num_dice))]
        total = sum(rolls) + bonus
        return f"(Roll: {rolls} + {bonus} = {total})"
    except:
        return ""

def save_to_log(entry):
    """Saves every line of the story to a text file locally"""
    with open("session_history.txt", "a", encoding="utf-8") as f:
        f.write(entry + "\n")

# 1. Initialization & Setting the Stage
SYSTEM_PROMPT = """
You are a professional D&D 5e Dungeon Master. 
- Keep responses atmospheric but concise (under 150 words).
- Use **bold** for emphasis.
- If an enemy attacks, specify the attack name and damage.
- Always end with 'What do you do?'
"""

print("--- Local AI Dungeon Master: Online (Session Logging Active) ---")

setting = input("Describe the starting location/scenario for today: ")
if not setting:
    setting = "A generic dark forest entrance."

# Start the log with a timestamp for this session
save_to_log(f"\n--- New Session: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ---")
save_to_log(f"Setting: {setting}")

chat_history = [{'role': 'system', 'content': SYSTEM_PROMPT}]
chat_history.append({'role': 'user', 'content': f"The session begins here: {setting}"})

# Get initial response from AI
response = ollama.chat(model='llama3.2', messages=chat_history)
dm_text = response['message']['content']
print(f"\nDM: {dm_text}\n")
save_to_log(f"DM: {dm_text}")
chat_history.append({'role': 'assistant', 'content': dm_text})

# 2. The Game Loop
while True:
    player_input = input("Player action (or 'roll 1d20+5'): ")
    
    if player_input.lower() == 'quit':
        save_to_log("--- Session Ended ---\n")
        break

    # Handle Dice Rolls
    dice_result = ""
    if "roll" in player_input.lower():
        dice_result = roll_dice(player_input.replace("roll ", ""))
        print(f"SYSTEM: {dice_result}")

    # Combine player action with any dice results for the AI
    full_input = f"{player_input} {dice_result}"
    save_to_log(f"PLAYER: {full_input}")
    chat_history.append({'role': 'user', 'content': full_input})

    # Get DM response
    response = ollama.chat(model='llama3.2', messages=chat_history)
    dm_response = response['message']['content']
    print(f"\nDM: {dm_response}\n")
    save_to_log(f"DM: {dm_response}")
    chat_history.append({'role': 'assistant', 'content': dm_response})