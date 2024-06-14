import random
import unittest

# The options for the game
options = ['rock', 'paper', 'scissors']

def get_computer_choice():
    """This function returns the choice of the computer."""
    return random.choice(options)

def determine_winner(user_choice, computer_choice):
    """This function determines the winner of the game."""
    if user_choice not in options or computer_choice not in options:
        raise ValueError("Invalid choice")
    if user_choice == computer_choice:
        return 'tie'
    if (user_choice == 'rock' and computer_choice == 'scissors') or \
       (user_choice == 'scissors' and computer_choice == 'paper') or \
       (user_choice == 'paper' and computer_choice == 'rock'):
        return 'user'
    else:
        return 'computer'

def play_game():
    """This function runs the game."""
    while True:
        user_choice = input("Enter your choice (rock, paper, scissors) or 'exit' to quit: ").lower()
        if user_choice == 'exit':
            break
        elif user_choice not in options:
            print("Invalid choice. Please try again.")
            continue
        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)
        if winner == 'tie':
            print(f"It's a tie! Both you and the computer chose {user_choice}.")
        elif winner == 'user':
            print(f"You win! You chose {user_choice} and the computer chose {computer_choice}.")
        else:
            print(f"You lose! You chose {user_choice} and the computer chose {computer_choice}.")

if __name__ == "__main__":
    play_game()
