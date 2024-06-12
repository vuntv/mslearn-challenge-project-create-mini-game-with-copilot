import random

# Function to determine the winner
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "tie"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "scissors" and computer_choice == "paper") or \
         (player_choice == "paper" and computer_choice == "rock"):
        return "win"
    else:
        return "lose"

# Function to play the game
def play_game():
    options = ["rock", "paper", "scissors"]
    player_score = 0
    computer_score = 0

    while True:
        player_choice = input("Enter rock, paper, or scissors: ").lower()

        if player_choice not in options:
            print("Invalid option. Please choose rock, paper, or scissors.")
            continue

        computer_choice = random.choice(options)
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(player_choice, computer_choice)

        if result == "win":
            print("You win this round!")
            player_score += 1
        elif result == "lose":
            print("You lose this round!")
            computer_score += 1
        else:
            print("This round is a tie!")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

    print("\nFinal Scores:")
    print(f"Your score: {player_score}")
    print(f"Computer's score: {computer_score}")
    print("Thanks for playing!")

# Run the game
if __name__ == "__main__":
    play_game()
