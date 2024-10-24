import time
class Link:
    def __init__(self, health=3, start_x=0, start_y=0):
        # This is the constructor. It runs when we create an instance of Link.
        # `self.health = health` means we're giving Link an initial health value (default is 3).
        # `self.position` will track where Link is in the dungeon, starting at (0, 0).
        self.health = health
        self.position = {"x": start_x, "y": start_y}
        self.facing = "forward"  # Link starts by facing forward.
        self.has_echo_lens = False # Link starts without the Echo Lens
        self.echo_lens_strength = 0
        self.has_key = False
    
    def move(self, direction, dungeon_size):
        # Update Link's position based on the direction the player inputs.
        if direction == "forward" or direction == "w":
            self.position["y"] += 1  # Moving forward increases Y value (moves down)
            self.facing = "forward"
        elif direction == "backward" or direction == "s":
            self.position["y"] -= 1  # Moving backward decreases Y value (moves up)
            self.facing = "backward"
        elif direction == "left" or direction == "a":
            self.position["x"] -= 1  # Moving left decreases X value (moves left)
            self.facing = "left"
        elif direction == "right" or direction == "d":
            self.position["x"] += 1  # Moving right increases X value (moves right)
            self.facing = "right"
        else:
            print("Invalid direction.")
        
        # Ensure Link doesn't walk out of bounds (dungeon walls).
        if self.position["x"] < 0 or self.position["x"] >= dungeon_size["width"] or self.position["y"] < 0 or self.position["y"] >= dungeon_size["height"]:
            print("You walk straight into a wall. I guess we can't go that way!")
            # Move Link back to avoid going outside the dungeon
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
# Scan - Echo Lens
    def scan(self, room_objects):
        if not self.has_echo_lens:
            print("You cannot scan without the Echo Lens.")
            return

        # Determine scan range based on the Echo Lens' strength
        scan_range = self.echo_lens_strength
        scanned_objects = []

        for step in range(1, scan_range + 1):
            if self.facing == "forward":
                target = (self.position["x"], self.position["y"] + step)
            elif self.facing == "backward":
                target = (self.position["x"], self.position["y"] - step)
            elif self.facing == "left":
                target = (self.position["x"] - step, self.position["y"])
            elif self.facing == "right":
                target = (self.position["x"] + step, self.position["y"])

            # Check if there's something in that direction
            if target in room_objects:
                scanned_objects.append(room_objects[target])
            else:
                scanned_objects.append("Empty space")

        print(f"Echo Lens Scan: {', '.join(scanned_objects)}")
 # Obtain Echo Lens
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