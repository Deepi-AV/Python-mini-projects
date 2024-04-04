import random
import sys
from enum import Enum
#Rock-Paper-Scissors

game_count=0
def play_rps():

    class RPS(Enum) :
        ROCK= '1'
        PAPER= '2'
        SCISSORS= '3'
   
    valid_inputs = ['1', '2', '3']
    playerCh=input("\nEnter 1 for Rock\n2 for Paper\n3 for Scissors\n\n")
    computerCh= random.choice("123")

    if playerCh not in valid_inputs:
        print("You entered a wrong input...need to choose from 1,2, or 3")
        return play_rps()
    else:

        global game_count
        game_count+=1
        print("Computer chose "+RPS(playerCh).name)
        print("Computer chose "+RPS(computerCh).name)

        if playerCh=='1' and computerCh=='3':
            print("You win!!🎊\n")
        elif playerCh=='2' and computerCh=='1':
            print("You win!!🎊\n")
        elif playerCh=='3' and computerCh=='2':
            print("You win!!🎊\n")
        elif playerCh==computerCh:
            print("Tie Game..😲\n")
        else:
            print("Computer Wins..😏\n")

    while True:
        will=input("Would you like to continue ? ('Y' for yes 'Q' to quit): ")
        if will.lower() in ['y','q']:
            break
        else:
            continue
    if will.lower()=='y':
        return play_rps()
    else:
        print("You played "+str(game_count)+" times")
        return


play_rps()


