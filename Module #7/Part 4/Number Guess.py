import random
import json
from pathlib import Path

class NumberGuesser:
    def __init__(self):
        self.stats_file = Path("guess_stats.json")
        self.load_stats()
    
    def load_stats(self):
        try:
            with open(self.stats_file) as f:
                self.stats = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.stats = {"games_played": 0, "total_guesses": 0}
    
    def save_stats(self):
        with open(self.stats_file, 'w') as f:
            json.dump(self.stats, f)
    
    def play_game(self):
        print("Think of a number between 1-1000")
        input("Press Enter when ready...")
        
        low, high = 1, 1000
        guesses = []
        
        while True:
            guess = (low + high) // 2
            print(f"My guess: {guess}")
            guesses.append(guess)
            
            feedback = input("Too (H)igh, (L)ow, or (C)orrect? ").lower()
            if feedback == 'c':
                break
            elif feedback == 'h':
                high = guess - 1
            elif feedback == 'l':
                low = guess + 1
            else:
                print("Invalid input! Use H/L/C")
        
        self.stats["games_played"] += 1
        self.stats["total_guesses"] += len(guesses)
        self.save_stats()
        
        print(f"\nGuessed in {len(guesses)} attempts!")
        print(f"Average guesses: {self.stats['total_guesses']/self.stats['games_played']:.1f}")

if __name__ == "__main__":
    game = NumberGuesser()
    game.play_game()
