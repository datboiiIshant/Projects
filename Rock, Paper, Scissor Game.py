import random

def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissor): ")
    Options = ["rock", "Paper", "scissors"] #List
    computer_choice = random.choice(Options)
    choices = {"computer" : computer_choice, "player" : player_choice} #Dictionary with Key Value Pairs
    return choices

def check_win(player, computer):
    print(f"You chose {player}, computer chose {computer}") #F-Strings
    if player == computer:
        return "It's a tie !"
    elif player == "rock": #Refactoring and Nested If
        if computer == "scissors":
            return "Rock Smashes Scissors! You win!"
        else:
            return "Paper covers Rock! You lose."
    elif player == "paper": 
        if computer == "rock":
            return "Paper cover rock! You win!"
        else:
            return "Scissors cuts paper! You lose."
    elif player == "Scissor":
        if computer == "Paper":
            return "Scissors cuts paper! You win!"
        else:
            return "Rock breaks Scissors! You lose."

# check_win("rock","paper")
choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)