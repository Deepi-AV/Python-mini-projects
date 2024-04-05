import random
import sys
import argparse


def guess_Num(name="Player"):

    game_count=0
    player_score=0

    def play_game():
        nonlocal game_count
        nonlocal player_score
        actual_number=random.choice("123")
        guess=input(f"\n{name}, guess what number I must be thinking of from- 1, 2 or 3: ")

        if guess not in ['1','2','3']:
            print(f"\n{name}, you entered wrong input..choose from 1, 2 or 3!")
            return guess_Num()
        
        print(f"\n{name}, you chose {guess}")

        def decide_winner():
            nonlocal player_score
            if(guess==actual_number):
                player_score+=1
                return f"{name}, Great Job! I was thinking of {actual_number} only."
            else:
                return f"{name}, Oh NO it was not the one!!\nBetter Luck next time..!\nI was thinking of {actual_number}"
            
        
        game_result=decide_winner()
        print(game_result)
        game_count+=1   
        
        print(f"\nGame Count: {game_count}")
        print(f"{name} wins: {player_score}")
        print(f"Winning Percentage: {player_score/game_count:.2%}\n")
        print("Play Again?\n")

        while True:
            continue_game=input("Type Y to continue and Q to exit...")
            if continue_game.lower() not in ['y','q']:
                continue
            else:
                break            


        if continue_game.lower()=='y':
            return guess_Num()
        else:
            print("\nThanks for Playing!!..")
            sys.exit("BYE!\n")

    return play_game
    
if __name__=="__main__":
    parser= argparse.ArgumentParser(
    description="Personalized Experience with Name of the Player"
    )

    parser.add_argument(
        "-n","--name",metavar="name",
        required=True,help="Your name or any name you wish."
    )

    args=parser.parse_args()
    guess_Num(args.name)
    