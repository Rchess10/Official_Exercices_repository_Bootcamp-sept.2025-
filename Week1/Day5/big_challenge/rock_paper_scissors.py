from game import Game


def get_user_menu_choice():
    choice = input("Menu:\n(g) Play a new game\n(x) Show scores & exit\nEnter your choice: ").strip().lower()
    if choice in {"g", "x"}:
        return choice
    return None


def print_results(results):
    print("Game Results:")
    print(f"You won: {results.get('win', 0)} times")
    print(f"You lost: {results.get('loss', 0)} times")
    print(f"Draws: {results.get('draw', 0)} times")


def main():
    game = Game()
    results = {"win": 0, "loss": 0, "draw": 0}

    while True:
        choice = get_user_menu_choice()
        if choice is None:
            print("Invalid choice. Please try again.")
            continue
        if choice == "g":
            result = game.play()
            results[result] += 1
        elif choice == "x":
            print_results(results)
            break


if __name__ == "__main__":
    main()
import random

class Game:
    def __init__(self, items=None):
        if items is None:
            items = ["rock", "paper", "scissors"]
        self.items = list(items)

    def get_user_item(self):
        prompt = f"Choose one of {', '.join(self.items)}: "
        while True:
            choice = input(prompt).strip().lower()
            if choice in self.items:
                return choice
            print("Invalid choice, try again.")

    def get_computer_item(self):
        return random.choice(self.items)

    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            return "draw"
        wins = {("rock", "scissors"), ("scissors", "paper"), ("paper", "rock")}
        return "win" if (user_item, computer_item) in wins else "loss"

    def play(self):
        user = self.get_user_item()
        computer = self.get_computer_item()
        result = self.get_game_result(user, computer)
        if result == "win":
            outcome_msg = "You win!"
        elif result == "loss":
            outcome_msg = "You lose."
        else:
            outcome_msg = "It's a draw."
        print(f"You selected {user}. The computer selected {computer}. {outcome_msg}")
        return result
    
    