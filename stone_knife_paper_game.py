import random

def generate_computer_choice():
    num = random.randint(0,2) #Randomly choose 0,1,2
    if num == 0:
        return "S" #stone
    elif num == 1:
        return "K" #knife
    else:
        return "P" #paper
#print(generate_computer_choice())

def play_stone_knife_paper_game():
    num_rounds = int(input("Enter the number of rounds to play: "))

    if num_rounds <= 0:
        print("Please enter a positive number of rounds.")
        return

    for round_num in range(1, num_rounds + 1):
        print(f"\n Round {round_num}/{num_rounds}")

        user_choice = input("Enter S(stone), or K(knife) or P(paper) to play the game: ").upper()
        if user_choice not in ["S", "K", "P"]:
            print("Invalid input! Please enter S, K, or P.")
            user_choice = input("Enter S(stone), K(knife) or P(paper): ").upper()

        computer_choice = generate_computer_choice()
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print( "It is a tie.")
        elif (user_choice == "S" and computer_choice == "K") or \
            (user_choice == "K" and computer_choice == "P") or \
            (user_choice == "P" and computer_choice == "S"):
            print("You win!")
        else: 
            print("You Lose!")
play_stone_knife_paper_game()
