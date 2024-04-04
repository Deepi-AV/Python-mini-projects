import random
import sys
from enum import Enum
#Rock-Paper-Scissors


def rps(playerName="Player"):

    game_count=0
    player_score=0
    computer_score=0

    def play_rps():

        nonlocal game_count
        nonlocal player_score
        nonlocal computer_score

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
        
        print(playerName+" chose "+RPS(playerCh).name)
        print("Computer chose "+RPS(computerCh).name)

        def decide_winner(player,computer):
            nonlocal player_score
            nonlocal computer_score
            if player=='1' and computer=='3':
                player_score+=1
                return playerName+" win!!🎊\n"
            elif player=='2' and computer=='1':
                player_score+=1
                return playerName+" win!!🎊\n"
            elif player=='3' and computer=='2':
                player_score+=1
                return playerName+" win!!🎊\n"
            elif player==computer:
                return "Tie Game..😲\n"
            else:
                computer_score+=1
                return "Computer Wins..😏\n"
        
        game_count+=1
        game_result=decide_winner(playerCh,computerCh)
        print(game_result)

        while True:
            will=input("Would you like to continue ? ('Y' for yes 'Q' to quit): ")
            if will.lower() in ['y','q']:
                break
            else:
                continue
        if will.lower()=='y':
            return play_rps()
        else:

            if(player_score>computer_score):
                print("Overall Winner "+playerName+" with "+str(player_score)+"/"+str(game_count))
            elif(computer_score>player_score):
                print("Overall Winner -COMPUTER with "+str(computer_score)+"/"+str(game_count))
            else:
                print("Equal Score "+ playerName+"("+str(player_score)+") COMPUTER("+str(computer_score)+")")
            return


        
    return play_rps

name=input("Enter Player Name: ")
play=rps(name)

play()



