# Function to print Tic Tac Toe
def printblock(values):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[0], values[1], values[2]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[3], values[4], values[5]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
 
    print("\t  {}  |  {}  |  {}".format(values[6], values[7], values[8]))
    print("\t     |     |")
    print("\n")

# Function to print the score-board
def printresults(score):
    print("\t--------------------------------")
    print("\t\t    ScoreBoard")
    print("\t--------------------------------")
    for key,value in score.items():
        print("\t   ", key, "\t    ", value)
    print("\t--------------------------------")
    pass

# Function to check if any player has won
def checkwin(playerpos,curplayer):
    # All possible winning combinations
    soln=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    # Loop to check if any winning combination is satisfied
    for i in soln:
        if all(y in playerpos[curplayer] for y in i):
            # Return True if any winning combination satisfies
            return True
    # Return False if no combination is satisfied       
    return False


# Function to check if the game is drawn
def checkdraw(playerpos):
    if(len(playerpos['X']+playerpos['O'])==9):
        return True
    return False

# Function for a single game of Tic Tac Toe
def singlegame(curplayer):
    # Represents the Tic Tac Toe
    values=[' ' for i in range(9)]
    # Stores the positions occupied by X and O
    playerpos={'X':[],'O':[]}

    # Game Loop for a single game of Tic Tac Toe
    while True:
        printblock(values)
        # Try exception block for MOVE input
        try:
            move=int(input(f"Player  {curplayer}  turn. Which box?"))
        except ValueError:
            print("Wrong Input Try Again")
            continue
        # Sanity check for MOVE inout
        if move<1 and move>9:
            print("Wrong input try again")
            continue
        # Check if the box is not occupied already
        if values[move-1]!=' ':
            print("Place filled Try Different Number")
            continue
        # Update game information
 
        # Updating grid status
        values[move-1]=curplayer
        
        # Updating player positions
        playerpos[curplayer].append(move)

        # Function call for checking win
        if checkwin(playerpos,curplayer):
            printblock(values)
            print("Player ", curplayer, " has won the game!!")     
            print("\n")
            return curplayer

        # Function call for checking draw game
        if checkdraw(playerpos):
            printblock(values)
            print("Match Drawn")     
            print("\n")
            return 'D'
        
        # Switch player moves
        if curplayer == 'X':
            curplayer = 'O'
        else:
            curplayer = 'X'

if __name__ == '__main__':

    print("Player 1")
    player1=input("Enter Player Name 1 : ")
    print("\nPlayer 2")
    player2=input("Enter Player Name 2 : ")
    print("\n")
    
    # Stores the player who chooses X and O
    curplayer=player1
    
    # Stores the choice of players
    playerchoice={"X":"","O":""}

    # Stores the scoreboard
    score={player1:0,player2:0}
    printresults(score)
    
    # Stores the options
    options = ['X', 'O']

    # Game Loop for a series of Tic Tac Toe
    # The loop runs until the players quit 
    while True:
        
         # Player choice Menu
        print('''
    Turn to choose for hruthik
    Enter 1 for X
    Enter 2 for O
    Enter 3 to Quit\n''')

        # Try exception for CHOICE input
        try:
            choice=int(input())
        except ValueError:
            print("Error in choosing choice! try again")
            continue
        # Conditions for player choice
        if choice>=1 and choice<=3:
            print("Error in choosing choice! try again")
            if choice==1:
                playerchoice["X"]=curplayer
                if playerchoice["X"]==player1:
                    playerchoice["O"]==player2
                else:
                    playerchoice["X"]==player1
            elif choice==2:
                playerchoice["O"]=curplayer
                if playerchoice["O"]==player1:
                    playerchoice["O"]==player2
                else:
                    playerchoice["O"]==player1
            else:
                print("\tFinal Score Board")
                printresults(score)
                break
        else:
            print("Wrong Choice Try Again")    
            continue

        # Stores the winner in a single game of Tic Tac Toe
        winner=singlegame(options[choice-1])

        # Edits the scoreboard according to the winner
        if winner!='D':
            playerwon=playerchoice[winner]
            score[playerwon]+=1
        printresults(score)

        # Switch player who chooses X or O
        if curplayer == player1:
            curplayer = player2
        else:
            curplayer = player1