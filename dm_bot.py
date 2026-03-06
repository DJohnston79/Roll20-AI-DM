import ollama
import random

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

# 1. Setting the Stage
SYSTEM_PROMPT = """
You are a professional D&D 5e Dungeon Master. 
- Keep responses atmospheric but concise (under 150 words).
- Use **bold** for emphasis.
- If an enemy attacks, specify the attack name and damage.
- Always end with 'What do you do?'
"""

print("--- Local AI Dungeon Master: Online ---")

# NEW: Dynamic Start
setting = input("Describe the starting location/scenario for today: ")
if not setting:
    setting = "A generic dark forest entrance."

chat_history = [{'role': 'system', 'content': SYSTEM_PROMPT}]
chat_history.append({'role': 'user', 'content': f"The session begins here: {setting}"})

# Get initial response
response = ollama.chat(model='llama3.2', messages=chat_history)
dm_text = response['message']['content']
print(f"\nDM: {dm_text}\n")
chat_history.append({'role': 'assistant', 'content': dm_text})

# 2. The Game Loop
while True:
    player_input = input("Player action (or 'roll 1d20+5'): ")
    
    if player_input.lower() == 'quit':
        break

    # Check if the DM needs to roll something manually
    dice_result = ""
    if "roll" in player_input.lower():
        dice_result = roll_dice(player_input.replace("roll ", ""))
        print(f"SYSTEM: {dice_result}")

    # Combine player action with any dice results
    full_input = f"{player_input} {dice_result}"
    chat_history.append({'role': 'user', 'content': full_input})

    response = ollama.chat(model='llama3.2', messages=chat_history)
    dm_response = response['message']['content']
    print(f"\nDM: {dm_response}\n")
    chat_history.append({'role': 'assistant', 'content': dm_response})