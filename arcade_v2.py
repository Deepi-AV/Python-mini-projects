import sys
from rps import rps 
from guess_the_number import guess_Num

def play_arcade(name="Player"):

    welcome_back=False

    print(f"\n{name}, Welcome To The ARCADE!!\n")

    while True:

        if(welcome_back):
            print("\nWelcome Back to the Arcade Game Menu: \n")
        
        choice=input("Please Choose the game you would like to play:\n\n1 = Rock, Paper, and Scissors\n2 = Guess the Number\nOr Press x to Exit\n\nEnter: ")

        if choice=='1':
            play_rps=rps(name)
            play_rps()
            welcome_back=True
        elif choice=='2':
            play=guess_Num(name)
            play()
            welcome_back=True
        elif choice=='x':
            sys.exit(f"\nSee you soon, {name}!!\n")
        else:
            print("You entered the wrong input...Choose from 1,2 or x")


if __name__=="__main__":

    import argparse

    parser=argparse.ArgumentParser(
        description="Personalized game experience"
    )

    parser.add_argument(
        "-n","--name",metavar="name", required=True,help="Provide your name."
    )

    
    args=parser.parse_args()

    play=play_arcade(args.name)