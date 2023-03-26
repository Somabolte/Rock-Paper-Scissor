import random

# possible moves
moves = ["rock", "paper", "scissors"]

while True:
    # get player move
    player_move = input("Enter your move (rock, paper, scissors): ")

    # validate player move
    if player_move not in moves:
        print("Invalid move. Try again.")
        continue

    # get computer move
    computer_move = random.choice(moves)

    # print moves
    print(f"You played {player_move}, computer played {computer_move}.")

    # determine winner
    if player_move == computer_move:
        print("It's a tie!")
    elif player_move == "rock" and computer_move == "scissors":
        print("You win!")
    elif player_move == "paper" and computer_move == "rock":
        print("You win!")
    elif player_move == "scissors" and computer_move == "paper":
        print("You win!")
    else:
        print("Computer wins!")

    # ask if player wants to play again
    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() != "y":
        break
