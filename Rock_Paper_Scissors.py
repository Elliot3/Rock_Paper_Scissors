from random import randint
import sys

wins = 0
losses = 0
ties = 0

def game(wins, losses, ties):
    print "Make your choice! Rock, Paper or Scissors?"
    player_choice = raw_input("=> ")
    computer_choice = randint(0,2)
    
    if player_choice.lower() == "rock":
        if computer_choice == 0:
            print "The computer played Rock, its a tie!"
            ties += 1
            return end(wins, losses, ties)
        elif computer_choice == 1:
            print "The computer played Paper, you lose!"
            losses += 1
            return end(wins, losses, ties)
        elif computer_choice == 2:
            print "The computer played Scissors, you win!"
            wins += 1
            return end(wins, losses, ties)

    if player_choice.lower() == "paper":
        if computer_choice == 0:
            print "The computer played Rock, you win!"
            wins += 1
            return end(wins, losses, ties)
        elif computer_choice == 1:
            print "The computer played Paper, its a tie!"
            ties += 1
            return end(wins, losses, ties)
        elif computer_choice == 2:
            print "The computer played Scissors, you lose!"
            losses += 1
            return end(wins, losses, ties)
        
    if player_choice.lower() == "scissors":
        if computer_choice == 0:
            print "The computer played Rock, you lose"
            losses += 1
            return end(wins, losses, ties)
        elif computer_choice == 1:
            print "The computer played Paper, you win!"
            wins += 1
            return end(wins, losses, ties)
        elif computer_choice == 2:
            print "The computer played Scissors, its a tie!"
            ties += 1
            return end(wins, losses, ties)
    else:
        print "Invalid choice! Try again."
        return game(wins, losses, ties)
            
def end(wins, losses, ties):
    print "Player wins: %d" % wins
    print "Computer wins: %d" % losses
    print "Games tied: %d" % ties
    print "------------------"
    print "Play again...?"
    answer = raw_input("=> ")
    
    if answer.lower() in ('yes','y'):
        game(wins, losses, ties)
    else:
        sys.exit()

print "Let's play Rock, Paper, Scissors!"
print "---------------------------------"
game(wins, losses, ties)