import time

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
        # Normalize input to full direction names
        direction_map = {
            "w": "forward",
            "s": "backward",
            "a": "left",
            "d": "right",
            "forward": "forward",
            "backward": "backward",
            "left": "left",
            "right": "right"
        }
        direction = direction_map.get(direction.lower())
        
        if direction is None:
            print("Invalid direction.")
            return
        
         # Apply the movement
        moves = {
            "forward": (0, 1),
            "backward": (0, -1),
            "left": (-1, 0),
            "right": (1, 0)
        }
        dx, dy = moves[direction]
        new_x, new_y = self.position["x"] + dx, self.position["y"] + dy


        # Ensure Link doesn’t move out of dungeon bounds
        if 0 <= new_x < dungeon_size["width"] and 0 <= new_y < dungeon_size["height"]:
            self.position["x"], self.position["y"] = new_x, new_y
            self.facing = direction
            print(f"Moved {self.facing}.")
        else:
            print("You walk straight into a wall. I guess we can't go that way!")


    def scan(self, room_objects, dungeon_size):
        # Check if Link has the Echo Lens
        if not self.has_echo_lens:
            print("You cannot scan without the Echo Lens.")
            return
        
        #Reset neaby objects before each scan
        self.nearby_objects = {}
        detected_objects = []

        # Set scan range based on echo lens strength
        scan_range = max(2, self.echo_lens_strength)  # Ensures a minimum range of 2 for early exploration     
        print("Echo Lens: ‘Scanning now...’")

        # Loop to detect objects within scan range
        for step in range(1, scan_range + 1):
            directions = {
                "forward": (self.position["x"], self.position["y"] + step),
                "backward": (self.position["x"], self.position["y"] - step),
                "left": (self.position["x"] - step, self.position["y"]),
                "right": (self.position["x"] + step, self.position["y"])
            }
            target_position = directions.get(self.facing)
            if not target_position:
                continue

            x, y = target_position
            if 0 <= x < dungeon_size["width"] and 0 <= y < dungeon_size["height"]:
                if target_position in room_objects:
                    obj = room_objects[target_position]
                    self.nearby_objects[obj] = target_position
                    print(f"Detected {obj} {step} step(s) {self.facing}.")
                    detected_objects.append(f"{obj} detected {step} step(s) {self.facing}.")
            else:
                detected_objects.append(f"Wall detected {step} step(s) {self.facing}.")

        # Print objects or wall info if detected
        if detected_objects:
            print("Objects detected:")
            for item in detected_objects:
                print(f"- {item}")
        else:
            print("No objects or walls are in front of you.")

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

    
    def check_health(self):
        """Check if Link's health is above zero."""
        return self.health > 0