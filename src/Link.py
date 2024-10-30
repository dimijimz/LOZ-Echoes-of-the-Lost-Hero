import time
from game_logic import get_room_objects, check_player_health

class Link:
    def __init__(self, health=3, start_x=0, start_y=0):
        # Initial attributes for Link
        self.health = health
        self.position = {"x": start_x, "y": start_y}
        self.facing = "forward"  # Link starts facing forward
        self.has_echo_lens = False  # Link starts without the Echo Lens
        self.echo_lens_strength = 0  # Echo Lens strength starts at 0
        self.has_key = False  # Link starts without a key
        self.nearby_objects = {} # Dictionary to store nearby interactable objects
    
    def obtain_key(self):
        self.has_key = True
        print("You have found a key! It may open a locked door somewhere.")

    def move(self, direction, dungeon_size):
        # Update Link's position based on movement direction
        if direction == "forward" or direction == "w":
            self.position["y"] += 1
            self.facing = "forward"
        elif direction == "backward" or direction == "s":
            self.position["y"] -= 1
            self.facing = "backward"
        elif direction == "left" or direction == "a":
            self.position["x"] -= 1
            self.facing = "left"
        elif direction == "right" or direction == "d":
            self.position["x"] += 1
            self.facing = "right"
        else:
            print("Invalid direction.")

        # Ensure Link doesn’t move out of dungeon bounds
        if self.position["x"] < 0 or self.position["x"] >= dungeon_size["width"] or \
           self.position["y"] < 0 or self.position["y"] >= dungeon_size["height"]:
            print("You walk straight into a wall. I guess we can't go that way!")
            # Move Link back to original position
            if direction == "forward":
                self.position["y"] -= 1
            elif direction == "backward":
                self.position["y"] += 1
            elif direction == "left":
                self.position["x"] += 1
            elif direction == "right":
                self.position["x"] -= 1
        else:
            print(f"Moved {self.facing}.")

    def scan(self, room_objects, dungeon_size):
        # Check if Link has the Echo Lens
        if not self.has_echo_lens:
            print("You cannot scan without the Echo Lens.")
            return
        
        #Reset neaby objects before each scan
        self.nearby_objects = {}        

        # Limited scan if Echo Lens strength is less than 2
        if self.echo_lens_strength < 2:
            print("Echo Lens Scan:")
            for step in range(1, self.echo_lens_strength + 1):
                # Determine target position based on Link's facing direction
                if self.facing == "forward":
                    target = (self.position["x"], self.position["y"] + step)
                elif self.facing == "backward":
                    target = (self.position["x"], self.position["y"] - step)
                elif self.facing == "left":
                    target = (self.position["x"] - step, self.position["y"])
                elif self.facing == "right":
                    target = (self.position["x"] + step, self.position["y"])

                # Check if there is an object in that direction
                if target in room_objects:
                    obj = room_objects[target]
                    self.nearby_objects[obj] = target # Stores nearby objects
                    print(f"- {obj} ahead at {step} step(s) away")
                else:
                    print("- Empty space ahead")
            return

        print("Echo Lens: ‘Scanning the room… the echoes reveal the unseen.’")
        detected_objects = []

    # Loop through each object in the room and calculate relative position, up to `echo_lens_strength`
        for pos, obj in room_objects.items():
            dx = pos[0] - self.position["x"]
            dy = pos[1] - self.position["y"]
        
            # Calculate the distance to each object
            distance = max(abs(dx), abs(dy))
        
            # Skip if object is out of range for the current echo lens strength
            if distance > self.echo_lens_strength:
                continue

        # Store interactable objects in front of Link as nearby
            if abs(dx) <= 1 and abs(dy) <= 1 and (
            (self.facing == "forward" and dy == 1) or
            (self.facing == "backward" and dy == -1) or
            (self.facing == "left" and dx == -1) or
            (self.facing == "right" and dx == 1)
        ):
                self.nearby_objects[obj] = pos
                print(f"You sense a {obj} in front of you.")

            # Determine directions based on relative position
            direction_fb = "forward" if dy > 0 else "backward"
            direction_lr = "right" if dx > 0 else "left"
        
            # Format the output for each detected object within lens strength
            detected_objects.append(f"{obj}: {abs(dy)} step(s) {direction_fb}, {abs(dx)} step(s) {direction_lr}")
    
        # Print all detected objects in the room
        print("Objects detected:")
        for item in detected_objects:
            print(f"- {item}")

    # Function to unlock the door
    def unlock_door(self):
        # Checks if there is a "Locked Door" nearby
        if "Locked Door" in self.nearby_objects:
            if self.has_key:
                print("You use the key to unlock the door. It swings open, granting you access to the next room.")
                self.has_key = False  # Consumes the key after use
                return True  # Door successfully unlocked
            else:
                print("You attempt to open the door, but it’s locked. A key is needed to unlock it.")
                return False  # Door remains locked
        else:
            print("There's no door here to unlock.")
            return False  # No door to unlock
        
    # Function to obtain the Echo Lens
    def obtain_echo_lens(self):
        self.has_echo_lens = True
        self.echo_lens_strength = 1  # Initial scan range of 1 step
        time.sleep(12)
        print("\nYou have discovered the Echo Lens, a mystical artifact with the power to reveal the unseen.")
        print("Though its form is damaged, it still hums with faint but familiar energy. It will be your guide through the darkness,")
        print("helping you sense what lies just beyond your reach. Its secrets, however, remain shrouded for now.")
        time.sleep(9)

    def upgrade_echo_lens(self):
        if self.echo_lens_strength < 2:  # Upgrade allows up to 2 steps of scanning
            self.echo_lens_strength += 1
            print(f"The Echo Lens has been upgraded! You can now scan {self.echo_lens_strength} steps away.")
        else:
            print("The Echo Lens is already at its maximum strength.")

    def unlock_door(self, room_objects):
        if self.has_key:
            print("You use the key to unlock the door.")
            #room_objects[door_position] = "Unlocked Door"
        else:
            print("You attempt to open the door and it won't budge. Maybe a key will help?")
