import random

class Game: 
    def __init__(self, items = None):
        if items is None:
            items = ["rock","paper","scissors"]
        self.items = list(items)
    
    def get_user_item(self):
        prompt = f"Choose one of {', '.join(self.items)}: "
        while True:
            choice = input(prompt).strip().lower()
            if choice in self.items:
                print(choice)
                return choice
            print("Choix invalide, réessaie.")
    
    def get_computer_item(self):
        return random.choice(self.items)

    def get_game_result(self,user_item,computer_item):
        if computer_item == user_item:
            return "draw"
        wins = {("rocks","scissors"),("scissors","paper"),("paper","rock")}
        if (user_item,computer_item) in wins:
            return "win" if (user_item,computer_item) in wins else "lose"
        return "lose"
    

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

game = Game()
game.get_user_item()
game.get_computer_item()
game.get_game_result(1,"rock")