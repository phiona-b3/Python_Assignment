import random

def stone_knife_paper():
    while True:
        computer_choice = random.randint(0,2)
        user_choice = input("Enter your choice(S for stone, K for knife, P for paper): ")
        user_choice = user_choice.upper()


        if user_choice not in['S','K','P']:
            print("invalid input.please enter S,K or P.")

            continue

        if computer_choice == 0:
            computer_choice_str = 'S'
        elif computer_choice ==1:
            computer_choice_str = 'K'
        else:
            computer_choice_str = 'P'


        print(f"computer's choice: {computer_choice_str}")


        if user_choice == computer_choice_str:
            print("It's a tie!")

        elif (user_choice == 'S' and computer_choice_str == 'K')or\
             (user_choice == 'K' and computer_choice_str == 'P')or\
             (user_choice == 'P' and computer_choice_str == 'S'):
            print("Congratulation you win!")

        else:
            ("Computer wins!")


        play_again = input("Do you want to play again?(yes/no):")
        if play_again.lower() !='yes':
            break

stone_knife_paper()
