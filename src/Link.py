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

    def scan(self, room_objects):
        # Check if Link has the Echo Lens
        if not self.has_echo_lens:
            print("You cannot scan without the Echo Lens.")
            return

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
                    print(f"- {room_objects[target]} ahead")
                else:
                    print("- Empty space ahead")
            return

        # Full-room scan if Echo Lens strength is 2 or more
        print("Echo Lens: ‘Scanning the room… the echoes reveal the unseen.’")
        detected_objects = []

        # Loop through each object in the room and calculate relative position
        for pos, obj in room_objects.items():
            dx = pos[0] - self.position["x"]
            dy = pos[1] - self.position["y"]

            # Skip Link's current position
            if dx == 0 and dy == 0:
                continue
            
            # Determine directions based on relative position
            direction_fb = "forward" if dy > 0 else "backward"
            direction_lr = "right" if dx > 0 else "left"
            
            # Format the output for each detected object
            detected_objects.append(f"{obj}: {abs(dy)} step(s) {direction_fb}, {abs(dx)} step(s) {direction_lr}")
        
        # Print all detected objects in the room
        print("Objects detected:")
        for item in detected_objects:
            print(f"- {item}")

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
