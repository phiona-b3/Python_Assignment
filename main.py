import random

def get_computer_choice():
    choices = ["S", "K", "P"]
    return random.choice(choices)

print(f"Computer chose: {computer_choice}")

