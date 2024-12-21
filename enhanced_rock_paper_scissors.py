import tkinter as tk
import random

class RockPaperScissorsGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")
        
        self.scores = {"User": 0, "Computer": 0}
        self.rounds = {"User": 0, "Computer": 0}
        self.best_of = 3
        
        # Create a frame for the title and score
        self.title_frame = tk.Frame(root)
        self.title_frame.pack()

        self.title_label = tk.Label(self.title_frame, text="Rock Paper Scissors", font=("Helvetica", 24))
        self.title_label.pack()

        self.score_label = tk.Label(self.title_frame, text="User: 0 | Computer: 0", font=("Helvetica", 18))
        self.score_label.pack()

        self.round_label = tk.Label(self.title_frame, text="Round: 0", font=("Helvetica", 16))
        self.round_label.pack()

        self.game_status_label = tk.Label(self.title_frame, text="Game in Progress", font=("Helvetica", 14))
        self.game_status_label.pack()

        # Create frame for buttons
        self.button_frame = tk.Frame(root)
        self.button_frame.pack()

        self.rock_button = tk.Button(self.button_frame, text="Rock", width=10, height=2, font=("Helvetica", 14), command=lambda: self.user_choice('rock'))
        self.rock_button.grid(row=0, column=0, padx=10)

        self.paper_button = tk.Button(self.button_frame, text="Paper", width=10, height=2, font=("Helvetica", 14), command=lambda: self.user_choice('paper'))
        self.paper_button.grid(row=0, column=1, padx=10)

        self.scissors_button = tk.Button(self.button_frame, text="Scissors", width=10, height=2, font=("Helvetica", 14), command=lambda: self.user_choice('scissors'))
        self.scissors_button.grid(row=0, column=2, padx=10)

        # Create frame for result display
        self.result_frame = tk.Frame(root)
        self.result_frame.pack()

        self.result_label = tk.Label(self.result_frame, text="Make your choice!", font=("Helvetica", 18))
        self.result_label.pack()

        # Reset button
        self.reset_button = tk.Button(root, text="Reset Game", width=20, height=2, font=("Helvetica", 14), command=self.reset_game)
        self.reset_button.pack()

    def user_choice(self, choice):
        if self.rounds["User"] == 2 or self.rounds["Computer"] == 2:
            self.game_status_label.config(text="Game Over!")
            return
        
        # User makes a choice, computer makes a random choice
        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        result = self.determine_winner(choice, computer_choice)
        
        # Update result and score
        self.result_label.config(text=f"You chose {choice.capitalize()} | Computer chose {computer_choice.capitalize()}. {result}")
        self.update_score(result)

        # Update round label
        self.round_label.config(text=f"Round: {self.rounds['User'] + self.rounds['Computer']}")

        # Check if anyone has won the Best of 3
        if self.rounds["User"] == 2 or self.rounds["Computer"] == 2:
            self.game_status_label.config(text=f"Game Over! {'You win!' if self.rounds['User'] == 2 else 'Computer wins!'}")
        
    def determine_winner(self, user, computer):
        if user == computer:
            return "It's a tie!"
        elif (user == 'rock' and computer == 'scissors') or (user == 'scissors' and computer == 'paper') or (user == 'paper' and computer == 'rock'):
            return "You win!"
        else:
            return "Computer wins!"

    def update_score(self, result):
        if result == "You win!":
            self.scores["User"] += 1
            self.rounds["User"] += 1
        elif result == "Computer wins!":
            self.scores["Computer"] += 1
            self.rounds["Computer"] += 1

        # Update score label
        self.score_label.config(text=f"User: {self.scores['User']} | Computer: {self.scores['Computer']}")

    def reset_game(self):
        self.scores = {"User": 0, "Computer": 0}
        self.rounds = {"User": 0, "Computer": 0}
        self.score_label.config(text="User: 0 | Computer: 0")
        self.round_label.config(text="Round: 0")
        self.game_status_label.config(text="Game in Progress")
        self.result_label.config(text="Make your choice!")
        self.game_status_label.config(text="Game in Progress")

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissorsGUI(root)
    root.mainloop()
import tkinter as tk
import random
from tkinter import messagebox
import os
from PIL import Image, ImageTk

class RockPaperScissorsGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")
        
        self.scores = {"User": 0, "Computer": 0}
        self.rounds = {"User": 0, "Computer": 0}
        self.best_of = 3

        self.game_status_label = None
        
        # Load images for choices
        self.rock_img = ImageTk.PhotoImage(Image.open("rock.png").resize((100, 100)))
        self.paper_img = ImageTk.PhotoImage(Image.open("paper.png").resize((100, 100)))
        self.scissors_img = ImageTk.PhotoImage(Image.open("scissors.png").resize((100, 100)))
        
        # Create a frame for the title and score
        self.title_frame = tk.Frame(root)
        self.title_frame.pack()

        self.title_label = tk.Label(self.title_frame, text="Rock Paper Scissors", font=("Helvetica", 24))
        self.title_label.pack()

        self.score_label = tk.Label(self.title_frame, text="User: 0 | Computer: 0", font=("Helvetica", 18))
        self.score_label.pack()

        self.round_label = tk.Label(self.title_frame, text="Round: 0", font=("Helvetica", 16))
        self.round_label.pack()

        self.game_status_label = tk.Label(self.title_frame, text="Game in Progress", font=("Helvetica", 14))
        self.game_status_label.pack()

        # Create frame for buttons
        self.button_frame = tk.Frame(root)
        self.button_frame.pack()

        self.rock_button = tk.Button(self.button_frame, image=self.rock_img, command=lambda: self.user_choice('rock'))
        self.rock_button.grid(row=0, column=0, padx=10)

        self.paper_button = tk.Button(self.button_frame, image=self.paper_img, command=lambda: self.user_choice('paper'))
        self.paper_button.grid(row=0, column=1, padx=10)

        self.scissors_button = tk.Button(self.button_frame, image=self.scissors_img, command=lambda: self.user_choice('scissors'))
        self.scissors_button.grid(row=0, column=2, padx=10)

        # Create frame for result display
        self.result_frame = tk.Frame(root)
        self.result_frame.pack()

        self.result_label = tk.Label(self.result_frame, text="Make your choice!", font=("Helvetica", 18))
        self.result_label.pack()

        # Reset button
        self.reset_button = tk.Button(root, text="Reset Game", width=20, height=2, font=("Helvetica", 14), command=self.reset_game)
        self.reset_button.pack()

    def user_choice(self, choice):
        if self.rounds["User"] == 2 or self.rounds["Computer"] == 2:
            self.game_status_label.config(text="Game Over!")
            return
        
        # User makes a choice, computer makes a random choice
        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        result = self.determine_winner(choice, computer_choice)
        
        # Update result and score
        self.result_label.config(text=f"You chose {choice.capitalize()} | Computer chose {computer_choice.capitalize()}. {result}")
        self.update_score(result)

        # Update round label
        self.round_label.config(text=f"Round: {self.rounds['User'] + self.rounds['Computer']}")

        # Check if anyone has won the Best of 3
        if self.rounds["User"] == 2 or self.rounds["Computer"] == 2:
            self.game_status_label.config(text=f"Game Over! {'You win!' if self.rounds['User'] == 2 else 'Computer wins!'}")
            self.show_winner_message()

    def determine_winner(self, user, computer):
        if user == computer:
            return "It's a tie!"
        elif (user == 'rock' and computer == 'scissors') or (user == 'scissors' and computer == 'paper') or (user == 'paper' and computer == 'rock'):
            return "You win!"
        else:
            return "Computer wins!"

    def update_score(self, result):
        if result == "You win!":
            self.scores["User"] += 1
            self.rounds["User"] += 1
        elif result == "Computer wins!":
            self.scores["Computer"] += 1
            self.rounds["Computer"] += 1

        # Update score label
        self.score_label.config(text=f"User: {self.scores['User']} | Computer: {self.scores['Computer']}")

    def show_winner_message(self):
        winner = "You win!" if self.rounds["User"] == 2 else "Computer wins!"
        messagebox.showinfo("Game Over", winner)

    def reset_game(self):
        self.scores = {"User": 0, "Computer": 0}
        self.rounds = {"User": 0, "Computer": 0}
        self.score_label.config(text="User: 0 | Computer: 0")
        self.round_label.config(text="Round: 0")
        self.game_status_label.config(text="Game in Progress")
        self.result_label.config(text="Make your choice!")
        self.game_status_label.config(text="Game in Progress")

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissorsGUI(root)
    root.mainloop()
