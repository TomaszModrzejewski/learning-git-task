import sys


def mainhall(swordpick):
    roomdir=input("\nEnter the way you want to go : Left, Right, or Front:\n")

    if ((roomdir=="left")or(roomdir=="Left")):
        left(swordpick)
    elif ((roomdir=='right')or(roomdir=="Right")):
        right(swordpick)
    elif ((roomdir=='front')or(roomdir=="Front")):
        front(swordpick)
    else:
        print("Wrong direction, You have stepped on a Magic Cirlce.\nYou are DEAD !!!\n")
        print("\t\t\t\t\t***GAME OVER***")
        sys.exit(1)


def left(swordpick):
    print("Sword found in this room.")
    swordpick = int(input("\nPress '0' to pickup Enchanted Sword\n"))

    if (swordpick == 0) :
        print("You are back to main Hall with Enchanted Sword.\n")
        mainhall(swordpick)
    else:
        print("There was nothing else in the Sword room.\n")
        print("You are back in main Hall.\n")
        mainhall(swordpick)


def right(swordpick):
    print("You are in the Reading room.\n")
    print("To your left is the Book shelf.")
    print("To your right is the Secret Exit.")
    print("To your front lies the Fireplace.")
    right_roomdir=input("\nEnter the way you want to go : Left, Right, or Front:\n")

    if ((right_roomdir=="left")or(right_roomdir=="Left")):
        bookshelf(swordpick)
    elif ((right_roomdir=="right")or(right_roomdir=="Right")):
        print("You exit through the Dungeon.\n")
        print("\t\t\t\t\t***GAME OVER***")
        sys.exit(0)
    elif ((right_roomdir=="front")or(right_roomdir=="Front")):
        print("The Fireplace was the entrance to HELL.\n")
        hell(swordpick)
    else:
        print("Wrong direction, You have stepped on a Magic Cirlce.\nYou are DEAD !!!\n")
        print("\t\t\t\t\t***GAME OVER***")
        sys.exit(1)

def front(swordpick):
    print("You have entered the Treasure room.")
    print("Infront of you lies an old Golden Box.")
    toward_box=input("\nTo go towards the box, Type 'Go front':\n")

    if ((toward_box=="go front")or(toward_box=="Go front")):
        print("OH No, You stepped on a TRAP, and it transports you somewhere !!!!\n")
        hell(swordpick)
    else:
        print("Wrong direction, You have stepped on a Magic Cirlce.\nYou are DEAD !!!\n")
        print("\t\t\t\t\t***GAME OVER***")
        sys.exit(1)


def bookshelf(swordpick):
    print("You are at the book shelf.")
    print("And, you see some books on the shelf.")
    print("There is also a note that says:\n")
    print("** DO NOT READ THESE BOOKS, THESE WILL BE THE DEATH OF YOU **\n")
    read_books=input("To read the books, Type 'Read books'.\nTo go back, Type 'Back off' :\n")

    if ((read_books=="Read books")or(read_books=="read books")):
        print("You were warned !!!!!")
        print("You are DEAD")
        print("\t\t\t\t\t***GAME OVER***")
        sys.exit(1)
    elif ((read_books=="back off")or(read_books=="Back off")):
        print("You go back to the Entrance of the Reading Room.\n")
        right(swordpick)
    else:
        print("You Touched something CuRsEd !!!!")
        print("You are DEAD")
        print("\t\t\t\t\t***GAME OVER***")
        sys.exit(1)


def  hell(swordpick):
    print("You have reached HELL !!!!")
    print("Infront of you, stands a DRAGON.")
    print("KILL HIM, to pass through this hurdle.\n")
    if (swordpick == 0):
        attack=int(input("Enter enough attack power to kill the beast (10 < attack power < 500) :\n"))

        if (attack < 10):
            print("Attack power was TOO LOW....")
            print("The DRAGON kills YOU.")
            print("\t\t\t\t\t***GAME OVER***")
            sys.exit(1)
        elif(10 <= attack <= 500):
            print("You do your signature MAGMA ICE MAGIC SLASH !!!!")
            print("This kills the dragon, and you are awarded the title 'THE DRAGON SLAYER KNIGHT'.")
            print("You see Two Portals open....\nThe portals show the destination, you want to go to.")
            go_back=input("\nTo go to the Treasure Room, Type 'Treasure room'\nTo go to the Reading Room, Type 'Reading room' :\n")
            if ((go_back=="Treasure room")or(go_back=="treasure room")):
                treasure_room(swordpick)
            elif ((go_back=="Reading Room")or(go_back=="reading room")):
                right(swordpick)
            else:
                print("You got lost in the Portals !!!!")
                print("You are DEAD NOW")
                print("\t\t\t\t\t***GAME OVER***")
                sys.exit(1)
        else:
            print("WoW, You did your most powerful move 'TIME LIFE BREAKER' !!!!")
            print("This kills the DRAGON, but you also lost all your health by using this move....")
            print("With your dying breath, you are awarded the title 'DRAGON LIFE DESTROYER' !!!")
            print("You are DEAD.\nWell Played.\nTRY AGAIN LATER\n")
            print("\t\t\t\t\t***GAME OVER***")
            sys.exit(1)
    else:
        print("Oh NO !!!!")
        print("You don't have a SWORD !!!!\n")
        print("The DRAGON kills YOU.\n")
        print("\t\t\t\t\t***GAME OVER***")
        sys.exit(1)

def treasure_room(swordpick):
    print("You are back the Treasure room.\n")
    print("Infront of you lies the old Golden Box.\n")
    open_box=input("\nTo open the box, Type 'Open box':\n")

    if ((open_box=="Open box")or(open_box=="open box")):
        print("You opened the box, and there lies a note saying : \n")
        print("YOU SHOULD NOT BE GREEDY, BE CONTENT WITH WHAT YOU HAVE :)\n")
        room_change=input("To leave the room, Type 'Main hall' or Type 'Reading room':\n")
        if ((room_change=="Main hall") or (room_change=="main hall")):
            print("\nYou are back in the main hall.")
            mainhall(swordpick)
        elif ((room_change=="Reading room")or(room_change=="reading room")):
            right(swordpick)
        else:
            print("Wrong Move.\nYou are DEAD !!!\n")
            print("\t\t\t\t\t***GAME OVER***")
            sys.exit(1)
    else:
        print("Wrong Move.\nYou are DEAD !!!\n")
        print("\t\t\t\t\t***GAME OVER***")
        sys.exit(1)

def main():
    print("Welcome, Warrior !!!!\nYou have entered the Dragon's Treasure Dungeon !!!")
    print("You are in the Main Hall.")
    print("This place was once the Hall of the Great Heroes.")
    print("Now all are DEAD !!!!\n")
    print("To the left is the Sword room.")
    print("To the right is the castle reading room, with back entrance.")
    print("To the front lies the Treasure room.")
    print("Choose your rooms wisely.\nBecause you can not go back now !!\n")
    swordpick = 1
    mainhall(swordpick)

main()
