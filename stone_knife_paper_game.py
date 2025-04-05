import random

def play_game():
    choices = ['S', 'K', 'P']
    computer_choice = random.choice(choices)
    user_choice = input("Enter your choice (S for Stone, K for Knife, P for Paper): ").upper()

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'S' and computer_choice == 'K') or \
         (user_choice == 'K' and computer_choice == 'P') or \
         (user_choice == 'P' and computer_choice == 'S'):
        print("You win!")
    else:
        print("Computer wins!")

    print(f"Computer chose: {computer_choice}")

play_game()