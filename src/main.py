from Link import Link 
from game_logic import check_player_health, get_dungeon_size, get_room_objects
import time

def main():
    print("Welcome to Legend of Zelda: Echoes of the Lost Hero!")
    
    # Create a new instance of class: Link
    link = Link()

    # Retrieve dungeon size and room objects
    dungeon_size = get_dungeon_size()
    room_objects = get_room_objects()
## Start of the adventure
    while True:
        command = input("Type 'start' to begin the quest of the Lost Hero: ")
        if command.lower() == "start":
            print("\nThe void of The Depths envelops you. There is no light, no form, only an overwhelming sense of emptiness.")
            print("This isn't the mere absence of light; it's as though the very fabric of reality is pulling you into itself.")
            print("You try to blink, but there are no eyes to close. A chilling realization grips you— your sight has been stolen.")
            print("You stand alone in silence, the ground beneath your feet cold and unfamiliar, a twisted echo of a world lost to darkness.")
            print("And yet... something within compels you forward. As if moving is the only answer in a place that offers none.")
            break
        else:
            print("Invalid command. Please try typing 'start'.")

# First step and discovery of the Echo Lens
    while True:
        first_move = input("\nYour body feels stiff, hesitant, yet an invisible force drives you onward. Type 'forward' or 'w' to step ahead: ")
        if first_move.lower() == "forward" or first_move.lower() == "w":
            print("\nYou take a trembling step forward. The silence is shattered by the sudden crunch beneath your foot.")
            print("Startled, you reach down and your hand closes around the object. It's been damaged, but faintly alive,")
            print("pulsing with warmth. Though you cannot see it, the sensation of its energy courses through your fingertips.")
            print("As you hold it, a faint yet familiar whisper drifts through the air.")
            print("The whisper grows, like an echo bouncing off unseen walls, until it becomes clear. It speaks a name:")
             # Adding a pause for the reveal of the Echo Lens
            time.sleep(15) #15 is the best pause time for this part
            print("\n\t *** THE ECHO LENS ***")

            time.sleep(4) #slight 4 pause and new line for dramatic effect
            print("\nThe voice is familiar, yet unknown, as if it has always been a part of you. You feel a connection to the object,")
            print("as if it holds the key to navigating this endless darkness. Not through sight, but through the echoes of sound and instinct.")
            print("This will guide you through the eternal darkness. Without it, the path ahead would be lost to you forever.")
            link.obtain_echo_lens()  # Link obtains the Echo Lens!
            break
        else:
            print("You cannot turn back. The only path is forward. Type 'forward' or 'w' to step ahead.")
    
    
    #MAIN GAME LOOP
    while check_player_health(link):
        command = input("What would you like to do? [move, scan, quit game] ")

        if command == "quit" or command == "quit game":

            print("Thanks for playing!")
            break

        elif command == "scan":
            link.scan(room_objects)

        elif command == "move":
            direction = input("What direction? [forward(W),backward(S),left(A),right(D)]")
            link.move(direction, dungeon_size)

        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()