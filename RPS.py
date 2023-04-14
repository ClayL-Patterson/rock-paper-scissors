import random

game_over = 3
player_wins = 0
computer_wins = 0
play_game = True
play_again = ""

print("Lets Play...")

#Rock
print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

while play_game:
    computer_pick = random.randint(0,2)
    
    computer_choice = ""

    if computer_pick == 0:
        computer_choice = "rock"
    elif computer_pick == 1:
        computer_choice = "paper"
    else:
        computer_choice = "scissors"

    

    player_choice = input("What is your choice: rock, paper, scissors: (q to quit) ")
    

    if player_choice == "q":
        break
    if player_choice == "rock" and computer_choice == "scissors":
        print("Player wins!")
        player_wins += 1
    elif player_choice == "paper"  and computer_choice == "rock":
        print("Player wins!")
        player_wins += 1
    elif player_choice == "scissors" and computer_choice == "paper":
        print("Player wins!")
        player_wins += 1
    elif player_choice == "scissors" and computer_choice == "rock":
        print("Computer wins!")
        computer_wins += 1
    elif player_choice == "rock" and computer_choice == "paper":
        print("Computer wins!")
        computer_wins += 1
    elif player_choice == "paper" and computer_choice == "scissors":
        print("Computer wins!")
        computer_wins += 1
    elif player_choice == computer_choice:
        print("Its a tie!")

    print(f"Total Score: \nPlayer = {player_wins} \nComputer = {computer_wins}")
    
    if player_wins >= game_over:
        print("Player wins!")
        play_again = input("Do you want to play again? (yes/no)")
    if computer_wins >= game_over:
        print("Computer wins!")
        play_again = input("Do you want to play again? (yes/no)")

    if play_again == "yes":
        play_game = True
    elif play_again == "no":
        play_game = False