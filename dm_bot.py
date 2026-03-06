import ollama
import random
import fitz  # PyMuPDF
from datetime import datetime
import os

def get_random_monsters(pdf_filename, count=4):
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        pdf_path = os.path.join(script_dir, pdf_filename)
        if not os.path.exists(pdf_path):
            return "No specific monster stats loaded.", []
        doc = fitz.open(pdf_path)
        random_pages = random.sample(range(12, doc.page_count), count)
        monster_data = ""
        page_list = []
        for pg_num in random_pages:
            monster_data += f"\n--- REF PAGE {pg_num} ---\n" + doc.load_page(pg_num).get_text()
            page_list.append(pg_num)
        return monster_data, page_list
    except Exception as e:
        return f"Error reading PDF: {e}", []

def roll_dice(dice_query):
    """Internal tool for DM to roll for enemies"""
    try:
        num_dice, rest = dice_query.lower().split('d')
        if '+' in rest:
            sides, bonus = map(int, rest.split('+'))
        else:
            sides, bonus = int(rest), 0
        rolls = [random.randint(1, sides) for _ in range(int(num_dice))]
        return f"(Enemy Roll Result: {sum(rolls) + bonus})"
    except:
        return ""

def save_to_log(entry):
    with open("session_history.txt", "a", encoding="utf-8") as f:
        f.write(entry + "\n")

# --- START SESSION ---
PDF_FILE = "Monster_Manual.pdf"
session_monsters, loaded_pages = get_random_monsters(PDF_FILE)

SYSTEM_PROMPT = f"""
You are a professional D&D 5e Dungeon Master. 
- PLAYERS: They roll their own dice on Roll20. Accept their results as fact.
- ENEMIES: Use these stats for combat: {session_monsters}
- NARRATION: Describe the results of player hits and enemy attacks. 
- Keep it atmospheric and concise. End with 'What do you do?'
"""

print("--- AI DM: Enemy-Only Rolling Mode ---")
print(f"SYSTEM: Random Monster Pages Loaded: {loaded_pages}")

setting = input("Describe the scene: ") or "A cold dungeon room."
save_to_log(f"\n--- Session: {datetime.now()} ---\nSetting: {setting}")

chat_history = [{'role': 'system', 'content': SYSTEM_PROMPT}]
chat_history.append({'role': 'user', 'content': f"The session begins: {setting}"})

response = ollama.chat(model='llama3.2', messages=chat_history)
dm_text = response['message']['content']
print(f"\nDM: {dm_text}\n")
save_to_log(f"DM: {dm_text}")
chat_history.append({'role': 'assistant', 'content': dm_text})

while True:
    player_input = input("Action/Result: ")
    if player_input.lower() == 'quit':
        break

    # The 'roll' command is now strictly for your Enemy/DM use
    dice_result = ""
    if player_input.lower().startswith("roll "):
        # Only parse the math part, e.g., 'roll 1d20+4'
        parts = player_input.split(" ", 2)
        dice_result = roll_dice(parts[1])
        print(f"SYSTEM {dice_result}")

    full_input = f"{player_input} {dice_result}"
    save_to_log(f"PLAYER/DM: {full_input}")
    chat_history.append({'role': 'user', 'content': full_input})

    response = ollama.chat(model='llama3.2', messages=chat_history)
    dm_response = response['message']['content']
    print(f"\nDM: {dm_response}\n")
    save_to_log(f"DM: {dm_response}")
    chat_history.append({'role': 'assistant', 'content': dm_response})