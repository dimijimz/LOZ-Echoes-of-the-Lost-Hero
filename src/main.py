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
        # Skips the intro
        if command.lower() == "skip":
            print("Skipping the intro... Prepare to enter the game directly!")
            link.obtain_echo_lens()  # Grant the Echo Lens instantly
            break  # Exit this loop and move to the main game loop

        elif command.lower() == "start":
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
        if first_move.lower() in ["forward", "w"]:
            print("\nYou take a trembling step forward. The silence is shattered by the sudden crunch beneath your foot.")
            time.sleep(5)
            print("Startled, you reach down and your hand closes around the object. It's been damaged, but faintly alive,")
            time.sleep(5)
            print("pulsing with warmth. Though you cannot see it, the sensation of its energy courses through your fingertips.")
            time.sleep(5)
            print("As you hold it, a faint yet familiar whisper drifts through the air.")
            time.sleep(5)
            print("The whisper grows, like an echo bouncing off unseen walls, until it becomes clear. It speaks a name:")
            time.sleep(5)  # Slight pause for effect
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
            time.sleep(4)
            print("\nThe voice is familiar, yet unknown, as if it has always been a part of you. You feel a connection to the object,")
            print("as if it holds the key to navigating this endless darkness. Not through sight, but through the echoes of sound and instinct.")
            print("This will guide you through the eternal darkness. Without it, the path ahead would be lost to you forever.")
            link.obtain_echo_lens()  # Link obtains the Echo Lens!
            break
        else:
            print("You cannot turn back. The only path is forward. Type 'forward' or 'w' to step ahead.")
        
    ## MAIN GAME LOOP ##
    while link.check_health() and current_room <= total_rooms:
        # Generate the room layout for the current room number
        room_data = generate_fixed_room(current_room)
        dungeon_size = {"width": room_data["width"], "height": room_data["height"]}
        room_objects = room_data["objects"]

        print(f"\nEntering Room {current_room}")

        # Room 5 Echo Lens Upgrade Cutscene
        if current_room == 5:
            print("\nYou feel an undeniable pull, as though the Echo Lens itself is urging you forward. The lens trembles in your hand, then slips free,")
            print("floating just beyond your reach. Darkness settles around you again, but a faint hum from the Lens pulses ahead.")
            time.sleep(2)

            # Prompting player input to move forward
            while True:
                advance = input("\nThe only way is forward. Type 'forward' or 'w' to step toward the unknown: ")
                if advance.lower() in ["forward", "w"]:
                    print("\nAs you step forward, the Lens begins to emit a low, resonant tone. Each step draws you closer, the air growing dense with a strange energy.")
                    print("Then, with a final pulse, the Echo Lens returns to your hand, settling with a newfound weight.")
                    time.sleep(3)
                    break
                else:
                    print("You feel the pull stronger than ever. Type 'forward' or 'w' to step into the unknown.")

            print("\nHolding the Echo Lens, you sense an undeniable power radiating from it, stronger than ever. As you activate the lens,")
            print("the surrounding darkness recedes, revealing not just outlines but the entire chamber with a surreal, crystalline clarity.")
    
            time.sleep(1.5)
            print("\nThis is no ordinary room. The Echo Lens reveals it as a Hall of Resonance, a place designed to amplify echoes and energy.")
            print("With each pulse of the lens, the chamber's walls seem to breathe, revealing shifting pathways and subtle inscriptions that whisper of ancient secrets.")
    
            link.upgrade_echo_lens()
            print("\nThe power of the Echo Lens has expanded; you sense the entire room as if each detail is woven into your mind. The lens feels")
            print("like a part of you now, attuned to reveal depths beyond sight. You move forward, guided by its amplified resonance.")
            continue  # Continue to the next loop iteration for interaction

        # Room interaction loop
        while True:
            options = ["move", "scan", "quit game"]
            # Check for objects directly under Link for interaction
            for obj, pos in link.nearby_objects.items():
                if obj == "Locked Door" and link.position == pos:
                    options.append("open door")
                elif obj == "Chest" and link.position == pos:
                    options.append("open chest")

            command = input(f"What would you like to do? {options}: ")

            if command == "quit" or command == "quit game":
                print("Thanks for playing!")
                return
        
            elif command == "scan":
                link.scan(room_objects, dungeon_size)

            elif command in ["w", "a", "s", "d"]:
                link.move(command, dungeon_size)
                link.nearby_objects = {}

            elif command.startswith("move "):
                direction = command.split(" ")[1]
                link.move(direction, dungeon_size)
                link.nearby_objects = {}

            elif command == "open door" and "Locked Door" in link.nearby_objects and link.position == link.nearby_objects["Locked Door"]:
                if link.unlock_door():
                    break

            elif command == "open chest" and "Chest" in link.nearby_objects and link.position == link.nearby_objects["Chest"]:
                print("You open the chest...")
                if not link.has_key:
                    link.obtain_key()
                else:
                    print("The chest is empty.")

            else:
                print("Invalid command or no object nearby to interact with.")

        current_room += 1

    print("\nCongratulations, you've completed the dungeon!")
    print("Thanks for playing Legend of Zelda: Echoes of the Lost Hero!")

if __name__ == "__main__":
    main()
