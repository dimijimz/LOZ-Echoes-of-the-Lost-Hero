from game_logic import check_player_health
def main():
    print("Welcome to Legend of Zelda: Echoes of the Lost Hero!")
    while True:
        player_command = input("Type start to jump in!")
        if player_command.lower() == "start":
            break
        else:
            print("Invalid command. Please try again.")

    while True:
        if check_player_health() == False:
            print("The hero has died. Game over.")
            break
        player_health = 3
        player_command = input("What would you like to do? [scan, move, quit] ")
        
        if player_command == "quit":
            return "Thanks for playing!"
            
        elif player_command == "scan":
            ### def scan():
            print("You activate the Echo Lens and scan the area.")
            

        elif player_command == "move":
            player_command = input("What direction? [forward, backward, left, right] ")
            if player_command == "forward":
                print("You move forward.")
                if wall():
                    print("You walked head first into a wall.. Ouch!")
            elif player_command == "backward":
                print("You move backward.")
            elif player_command == "left":
                print("You move left.")
            elif player_command == "right":
                print("You move right.")
            else:
                print("Invalid direction. Please try again.")

        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
