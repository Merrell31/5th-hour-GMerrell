#Name:Gavin Merrell
#Class: 5th Hour
import random


P1ROCK = "Rock"
P1SCISSORS = "Scissors"
P1PAPER = "Paper"
P2ROCK = "Rock"
P2SCISSORS = "Scissors"
P2PAPER = "Paper"
player1choice = random.choice([P1ROCK, P2ROCK, P1SCISSORS])
player2choice = random.choice([P2ROCK, P2SCISSORS, P2PAPER])
print (player1choice, player2choice)

if player1choice == "Rock" and player2choice == "Paper":
    print ("Player 1 Wins paper beats rock")
elif player1choice == "Paper" and player2choice == "Rock":
    print ("Player 2 Wins paper beats rock")
elif player1choice == "Rock" and player2choice == "Scissors":
    print ("Player 1 Wins Rock beats Scissors")
elif player1choice == "Scissors" and player2choice == "Rock":
    print ("Player 2 Wins Rock beats Scissors")
elif player1choice == "Paper" and player2choice == "Scissors":
    print ("Player 1 Wins scissors beats paper")
elif player1choice == "Scissors" and player2choice == "Paper":
    print ("Player 2 Wins scissors beats paper")
else:
    print("Player 1 and player 2 chose the same play agin.")
