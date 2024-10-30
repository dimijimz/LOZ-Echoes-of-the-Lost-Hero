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
        # Move Link based on direction and update facing
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
    
        # Convert input to the full direction name
        if direction in direction_map:
            direction = direction_map[direction]
        else:
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
        self.position["x"] += dx
        self.position["y"] += dy
        self.facing = direction

        # Ensure Link doesn’t move out of dungeon bounds
        if not (0 <= self.position["x"] < dungeon_size["width"] and 0 <= self.position["y"] < dungeon_size["height"]):
            print("You walk straight into a wall. I guess we can't go that way!")
            self.position["x"] -= dx  # Undo move
            self.position["y"] -= dy
        else:
            print(f"Moved {self.facing}.")


    def scan(self, room_objects, dungeon_size):
        # Check if Link has the Echo Lens
        if not self.has_echo_lens:
            print("You cannot scan without the Echo Lens.")
            return
        
        #Reset neaby objects before each scan
        self.nearby_objects = {}
        detected_objects = []        

         # Scan logic based on Echo Lens strength
        print("Echo Lens: ‘Scanning the room… the echoes reveal the unseen.’")
        for pos, obj in room_objects.items():
            dx, dy = pos[0] - self.position["x"], pos[1] - self.position["y"]
            distance = max(abs(dx), abs(dy))
            
            # Skip objects out of range for current Echo Lens strength
            if distance > self.echo_lens_strength:
                continue

            # Store interactable objects in front of Link
            if self.is_in_front(dx, dy):
                self.nearby_objects[obj] = pos
                print(f"You sense a {obj} in front of you.")

            # Add details to detected objects
            direction_fb = "forward" if dy > 0 else "backward"
            direction_lr = "right" if dx > 0 else "left"
            detected_objects.append(f"{obj}: {abs(dy)} step(s) {direction_fb}, {abs(dx)} step(s) {direction_lr}")

        # Print detected objects or "No objects detected" if list is empty
        if detected_objects:
            print("Objects detected:")
        for item in detected_objects:
            print(f"- {item}")
        else:
            print("No objects or walls are in front of you.")

    def is_in_front(self, dx, dy):
        # Helper method to check if object is in front based on Link's facing direction
        facing_directions = {
            "forward": (0, 1),
            "backward": (0, -1),
            "left": (-1, 0),
            "right": (1, 0)
        }
        fx, fy = facing_directions[self.facing]
        return dx == fx and dy == fy

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