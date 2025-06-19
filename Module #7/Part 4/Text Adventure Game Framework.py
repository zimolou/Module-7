import time
import random

def start_game():
    print("Welcome to the Mysterious Island Adventure!")
    time.sleep(1)
    print("You wake up on an unfamiliar beach...")
    time.sleep(1)
    player_name = input("First, tell me your name: ")
    print(f"Alright {player_name}, let's begin your adventure!\n")
    
    # Initialize player status
    inventory = []
    health = 100
    score = 0
    
    # Start first scene
    beach_scene(player_name, inventory, health, score)

def beach_scene(player_name, inventory, health, score):
    print("\nYou stand on a golden beach facing a dense jungle.")
    print("To the east you see a cave entrance.")
    print("To the west there's a shipwreck on the shore.")
    
    while True:
        print(f"\nHealth: {health} | Score: {score} | Inventory: {inventory}")
        choice = input("\nWhat will you do? (E)ast to cave, (W)est to shipwreck, (S)earch sand: ").upper()
        
        if choice == "E":
            cave_scene(player_name, inventory, health, score)
            break
        elif choice == "W":
            shipwreck_scene(player_name, inventory, health, score)
            break
        elif choice == "S":
            if "compass" not in inventory:
                print("\nYou find a rusty compass buried in the sand!")
                inventory.append("compass")
                score += 10
            else:
                print("\nYou find nothing new.")
        else:
            print("\nInvalid choice. Try again.")

def cave_scene(player_name, inventory, health, score):
    print("\nYou enter the dark cave. It's damp and cold.")
    print("There's a faint glowing light deeper inside.")
    print("You also notice some strange markings on the walls.")
    
    while True:
        print(f"\nHealth: {health} | Score: {score} | Inventory: {inventory}")
        choice = input("\nWhat will you do? (G)o toward light, (S)tudy markings, (L)eave cave: ").upper()
        
        if choice == "G":
            print("\nAs you approach the light, the floor collapses!")
            health -= random.randint(10, 30)
            if health <= 0:
                game_over(player_name, score)
                return
            else:
                print(f"You survive with {health} health remaining.")
                treasure_room(player_name, inventory, health, score)
                break
        elif choice == "S":
            print("\nThe markings appear to be an ancient language.")
            if "notebook" in inventory:
                print("Using your notebook, you decipher a warning about traps!")
                score += 20
            else:
                print("You can't understand them without reference materials.")
        elif choice == "L":
            beach_scene(player_name, inventory, health, score)
            return
        else:
            print("\nInvalid choice. Try again.")

def shipwreck_scene(player_name, inventory, health, score):
    print("\nThe old ship creaks as you board it.")
    print("There's a locked chest on the deck and a hatch leading below.")
    
    while True:
        print(f"\nHealth: {health} | Score: {score} | Inventory: {inventory}")
        choice = input("\nWhat will you do? (O)pen chest, (G)o below deck, (L)eave ship: ").upper()
        
        if choice == "O":
            if "key" in inventory:
                print("\nYou open the chest and find a treasure map!")
                inventory.append("map")
                score += 50
            else:
                print("\nThe chest is locked. You need a key.")
        elif choice == "G":
            print("\nBelow deck you find a skeleton with a key in its hand!")
            inventory.append("key")
            score += 15
        elif choice == "L":
            beach_scene(player_name, inventory, health, score)
            return
        else:
            print("\nInvalid choice. Try again.")

def treasure_room(player_name, inventory, health, score):
    print("\nYou land in a hidden treasure chamber!")
    print("Gold coins and jewels glitter everywhere.")
    
    if "map" in inventory:
        print("\nUsing your map, you find the legendary Ruby of the Seas!")
        score += 100
        inventory.append("ruby")
    else:
        print("\nWithout guidance, you only grab some coins.")
        score += 30
    
    print("\nA secret passage leads back to the beach.")
    input("Press Enter to exit with your treasures...")
    beach_scene(player_name, inventory, health, score)

def game_over(player_name, score):
    print(f"\nOh no {player_name}! Your adventure ends here.")
    print(f"Final Score: {score}")
    print("\nGAME OVER\n")
    play_again()

def play_again():
    choice = input("Would you like to play again? (Y/N): ").upper()
    if choice == "Y":
        start_game()
    else:
        print("\nThanks for playing!")

# Start the game
if __name__ == "__main__":
    start_game()
