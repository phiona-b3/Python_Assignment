import random

def get_computer_choice():
    choices = ["S", "K", "P"]
    return random.choice(choices)

def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == "S" and computer == "K") or \
         (player == "K" and computer == "P") or \
         (player == "P" and computer == "S"):
        return "You win!"
    else:
        return "Computer wins!"

# Get user choice
player_choice = input("Enter S for Stone, K for Knife, or P for Paper: ").upper()
computer_choice = get_computer_choice()

print(f"Computer chose: {computer_choice}")
print(determine_winner(player_choice, computer_choice))

