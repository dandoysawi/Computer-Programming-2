import random # Added this in case you want random cat reactions!

# --- Initial Setup (Global Variables) ---
player_name = input("Enter your name: ")
location = "Animal Shelter"
inventory = [] # You could track items like "Treat" or "Hat" here

# --- Game Functions ---

def skibidi_encounter():
    print("\n--- Skibidi Encounter ---")
    action = input("Food (f) or Shoo (s)? ").lower().strip()

    if action == 'f':
        item = input("Treat (t) or Hat (h)? ").lower().strip()
        if item == 't':
            print("Skibidi is happy!")
        elif item == 'h':
            print("Skibidi looks awesome!")
        else:
            print("Skibidi is confused.")
    else:
        print("Skibidi zooms away: 'Umalis ka dito, pusa!'")

def macy_encounter():
    print("\n--- Macy Encounter ---")
    action = input("Clothes (c) or Shoo (s)? ").lower().strip()

    if action == 'c':
        print("Macy feels safe in a blanket.")
    else:
        print("Macy hides: 'Umalis ka dito, pusa!'")

def update_location(new_place):
    global location
    location = new_place
    print(f"Location updated to: {location}")

# --- Main Game Flow ---
def start_game():
    print(f"\nNew owner of Skibidi & Macy: {player_name}")
    choice = input("Go home (h) or other day (d)? ").lower().strip()

    if choice == 'd':
        print("End: Cats will wait for you.")
        return # Stops the function here

    if choice == 'h':
        update_location("House")
        
        cat_choice = input("Choose cat - Skibidi (s) or Macy (m): ").lower().strip()
        
        if cat_choice == 's':
            skibidi_encounter()
        elif cat_choice == 'm':
            macy_encounter()
        else:
            print("Both cats are confused by your silence.")

    print("\n--- Game Over ---")

# --- Run the Program ---
start_game()