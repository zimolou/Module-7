import random
from enum import Enum, auto

class Gesture(Enum):
    ROCK = auto()
    PAPER = auto()
    SCISSORS = auto()
    LIZARD = auto()
    SPOCK = auto()

WIN_RULES = {
    Gesture.ROCK: [Gesture.SCISSORS, Gesture.LIZARD],
    Gesture.PAPER: [Gesture.ROCK, Gesture.SPOCK],
    Gesture.SCISSORS: [Gesture.PAPER, Gesture.LIZARD],
    Gesture.LIZARD: [Gesture.PAPER, Gesture.SPOCK],
    Gesture.SPOCK: [Gesture.ROCK, Gesture.SCISSORS]
}

GESTURE_NAMES = {
    'r': Gesture.ROCK,
    'p': Gesture.PAPER,
    's': Gesture.SCISSORS,
    'l': Gesture.LIZARD,
    'k': Gesture.SPOCK
}

def get_player_choice():
    while True:
        choice = input("\nChoose (R)ock, (P)aper, (S)cissors, (L)izard, Spoc(K): ").lower()
        if choice in GESTURE_NAMES:
            return GESTURE_NAMES[choice]
        print("Invalid input! Please use R/P/S/L/K")

def determine_round_winner(player, computer):
    if player == computer:
        return "tie"
    return "player" if computer in WIN_RULES[player] else "computer"

def print_match_status(scores):
    print(f"\n=== SCORE: Player {scores['player']} - {scores['computer']} Computer ===")

def main():
    print("Rock-Paper-Scissors-Lizard-Spock (Best of 3)")
    scores = {"player": 0, "computer": 0}
    
    while max(scores.values()) < 2:
        player_choice = get_player_choice()
        computer_choice = random.choice(list(Gesture))
        
        print(f"\nPlayer: {player_choice.name} vs Computer: {computer_choice.name}")
        
        result = determine_round_winner(player_choice, computer_choice)
        if result != "tie":
            scores[result] += 1
            print(f"{result.capitalize()} wins this round!")
        else:
            print("It's a tie!")
        
        print_match_status(scores)
    
    winner = max(scores, key=scores.get)
    print(f"\n{winner.capitalize()} wins the match!")

if __name__ == "__main__":
    main()


