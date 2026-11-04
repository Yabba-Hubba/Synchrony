
import random
#welcome message
print("Welcome to Rock, Paper, Scissors!")

choices = ["rock", "paper", "scissors"]

while True:
    player = input("Choose rock, paper, or scissors: ").lower()
    computer = random.choice(choices)

    if player not in choices:
        print("Invalid choice!")
        continue

    print("Computer chose:", computer)

    if player == computer:
        print("It's a tie!")
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        print("You win!")
    else:
        print("You lose!")

    again = input("Play again? (yes/no): ").lower()
    if again != "yes":
        print("Thanks for playing!")
        break
