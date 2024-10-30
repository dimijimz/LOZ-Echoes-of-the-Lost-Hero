from Link import Link 
from game_logic import generate_fixed_room
import time

def main():
    print(r"""
            _
          .!=!.
          \===/
          |>X<|
          |>X<|
          |>X<|
          |>X<|
          |>X<|
          |>X<|
          |>X<|
         .-----.
     /\__:-----:__/\
   ./ ._. \.-./ ._. \.
 ./ ./  -.  V  .-  \. \.
/__/      \   /      \__\
          |! !|
          |! !|
         / . . \
        |!.V V.!|
         \\ V //
         ||   ||
         ||   ||
         ||   ||
         ||   ||
         ||   ||
         ||   ||
         ||   ||
         ||   ||        Welcome to Legend of Zelda: Echoes of the Lost Hero!
         ||   ||
         ||   ||
         ||   ||
         ||   ||
         ||   ||
         ||   ||
         ||   ||
         ||   ||
         ||   ||
         ||   ||
          \\ //
           \V/          A text-based adventure game created in Python fully developed by Dimitri Jimenez
          """)
    
    # Create a new instance of class: Link
    link = Link()

    # Define total number of rooms and initialize room tracking
    total_rooms = 10
    current_room = 1


## Start of the adventure
    while True:
        command = input("Type 'start' to begin the quest of the Lost Hero: ")
        if command.lower() == "start":
            print("\nThe void of The Depths envelops you. There is no light, no form, only an overwhelming sense of emptiness.")
            time.sleep(5)
            print("This isn't the mere absence of light; it's as though the very fabric of reality is pulling you into itself.")
            time.sleep(5)            
            print("You try to blink, but there are no eyes to close. A chilling realization grips you— your sight has been stolen.")
            time.sleep(5)            
            print("You stand alone in silence, the ground beneath your feet cold and unfamiliar, a twisted echo of a world lost to darkness.")
            time.sleep(5)            
            print("And yet... something within compels you forward. As if moving is the only answer in a place that offers nothing.")
            time.sleep(5)
            break
        elif command.lower() == "quit":
            print("Thanks for playing!")
            exit()
        else:
            print("Invalid command. Please try typing 'start'.")

# First step and discovery of the Echo Lens
    while True:
        first_move = input("\nYour body feels stiff, hesitant, yet an invisible force drives you onward. Type 'forward' or 'w' to step ahead: ")
        if first_move.lower() == "forward" or first_move.lower() == "w":
            print("\nYou take a trembling step forward. The silence is shattered by the sudden crunch beneath your foot.")
            time.sleep(5)
            print("Startled, you reach down and your hand closes around the object. It's been damaged, but faintly alive,")
            time.sleep(5)
            print("pulsing with warmth. Though you cannot see it, the sensation of its energy courses through your fingertips.")
            time.sleep(5)
            print("As you hold it, a faint yet familiar whisper drifts through the air.")
            time.sleep(5)
            print("The whisper grows, like an echo bouncing off unseen walls, until it becomes clear. It speaks a name:")
             # Adding a pause for the reveal of the Echo Lens
            time.sleep(5) #15 is the best pause time for this part
            print(r"""
    ███        ▄█    █▄       ▄████████          
▀█████████▄   ███    ███     ███    ███          
   ▀███▀▀██   ███    ███     ███    █▀           
    ███   ▀  ▄███▄▄▄▄███▄▄  ▄███▄▄▄              
    ███     ▀▀███▀▀▀▀███▀  ▀▀███▀▀▀              
    ███       ███    ███     ███    █▄           
    ███       ███    ███     ███    ███          
   ▄████▀     ███    █▀      ██████████          
                                                 
   ▄████████  ▄████████    ▄█    █▄     ▄██████▄ 
  ███    ███ ███    ███   ███    ███   ███    ███
  ███    █▀  ███    █▀    ███    ███   ███    ███
 ▄███▄▄▄     ███         ▄███▄▄▄▄███▄▄ ███    ███
▀▀███▀▀▀     ███        ▀▀███▀▀▀▀███▀  ███    ███
  ███    █▄  ███    █▄    ███    ███   ███    ███
  ███    ███ ███    ███   ███    ███   ███    ███
  ██████████ ████████▀    ███    █▀     ▀██████▀ 
                                                 
 ▄█          ▄████████ ███▄▄▄▄      ▄████████    
███         ███    ███ ███▀▀▀██▄   ███    ███    
███         ███    █▀  ███   ███   ███    █▀     
███        ▄███▄▄▄     ███   ███   ███           
███       ▀▀███▀▀▀     ███   ███ ▀███████████    
███         ███    █▄  ███   ███          ███    
███▌    ▄   ███    ███ ███   ███    ▄█    ███    
█████▄▄██   ██████████  ▀█   █▀   ▄████████▀     
▀                                                """)

            time.sleep(4) #slight 4 pause and new line for dramatic effect
            print("\nThe voice is familiar, yet unknown, as if it has always been a part of you. You feel a connection to the object,")
            print("as if it holds the key to navigating this endless darkness. Not through sight, but through the echoes of sound and instinct.")
            print("This will guide you through the eternal darkness. Without it, the path ahead would be lost to you forever.")
            
            link.obtain_echo_lens()  # Link obtains the Echo Lens!
            
            break
        else:
            print("You cannot turn back. The only path is forward. Type 'forward' or 'w' to step ahead.")
    
    
    #MAIN GAME LOOP (Checks the players health or alive)
      # Main game loop
    while link.check_health() and current_room <= total_rooms:
        # Generate the room layout for the current room number
        room_data = generate_fixed_room(current_room)
        dungeon_size = {"width": room_data["width"], "height": room_data["height"]}
        room_objects = room_data["objects"]

        print(f"\nEntering Room {current_room}")

        # Room 5 Echo Lens Upgrade Cutscene
        if current_room == 5:
            print("\nIn the center of the room lies an ornate chest, glimmering faintly in the darkness.")
            command = input("Would you like to approach the chest and open it? [yes/no]: ")
            if command.lower() == "yes":
                print("\nYou open the chest and find an upgraded Echo Lens. Its power seems to grow stronger!")
                link.upgrade_echo_lens()

        # Room interaction loop
        while True:
            options = ["move", "scan", "quit game"]
            for obj in link.nearby_objects:
                if obj == "Locked Door":
                    options.append("open door")
                elif obj == "Chest":
                    options.append("open chest")
                elif obj == "Torch Stand":
                    options.append("light torch")

            command = input(f"What would you like to do? {options}: ")

            if command == "quit" or command == "quit game":
                print("Thanks for playing!")
                return

            elif command == "scan":
                link.scan(room_objects, dungeon_size)

            elif command == "move":
                direction = input("What direction? [forward(W), backward(S), left(A), right(D)] ")
                link.move(direction, dungeon_size)
                link.nearby_objects = {}

            elif command == "open door" and "Locked Door" in link.nearby_objects:
                if link.unlock_door():  # Call the unlock_door method in Link
                    break  # Move to the next room if the door was unlocked

            elif command == "open chest" and "Chest" in link.nearby_objects:
                print("You open the chest...")
                if not link.has_key:
                    link.obtain_key()
                else:
                    print("The chest is empty.")

            elif command == "light torch" and "Torch Stand" in link.nearby_objects:
                print("You light the torch, illuminating part of the room.")

            else:
                print("Invalid command or no object nearby to interact with.")

        # Move to the next room
        current_room += 1

    print("\nCongratulations, you've completed the dungeon!")
    print("Thanks for playing Legend of Zelda: Echoes of the Lost Hero!")

if __name__ == "__main__":
    main()