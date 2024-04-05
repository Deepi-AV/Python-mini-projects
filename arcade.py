import rps
import guess_the_number as gn 
import sys

def arcade_game(name="Player"):
     
    print(f"\nWelcome to the arcade game..{name}!!\n")

    def play_arcade():
        nonlocal name
        choice=input("Please Choose the game you would like to play:\n1 = Rock, Paper, and Scissors\n2 = Guess the Number\nOr Press x to Exit\n\nEnter: ")

        def decide_game():
            nonlocal name
            if choice=='1':
                play_rps=rps.rps(name)
                play_rps()
                print(f"{name}, Welcome Back to the Arcade Menu..\n")
                return play_arcade()
            elif choice=='2':
                play=gn.guess_Num(name)
                play()
                print(f"{name}, Welcome Back to the Arcade Menu..\n")
                return play_arcade()
            elif choice=='x':
                sys.exit(f"\nSee you soon, {name}!!\n")
            else:
                print("You entered the wrong input...Choose from 1,2 or x")
                return play_arcade()

        decide_game()

    return play_arcade


if __name__=="__main__":

    import argparse

    parser=argparse.ArgumentParser(
        description="Personalized game experience"
    )

    parser.add_argument(
        "-n","--name",metavar="name", required=True,help="Provide your name."
    )

    args=parser.parse_args()

    play=arcade_game(args.name)
    play()
