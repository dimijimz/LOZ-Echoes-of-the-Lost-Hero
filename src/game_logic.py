import random

# Define the minimum size of the rooms
MIN_ROOM_SIZE = 10

# Define the size of the dungeon (room) and its objects
def generate_room():
    width = random.randint(MIN_ROOM_SIZE, MIN_ROOM_SIZE + 5)
    height = random.randint(MIN_ROOM_SIZE, MIN_ROOM_SIZE + 5)

# Initial room size dictionary
    room_size = {"width": width, "height": height}

# Dictionary to store room objects with their positions
    room_objects = {}

# Use a set to track used positions for objects
    used_positions = set()


 # Place a door on one of the walls (left, right, top, or bottom wall)
    wall_side = random.choice(["left", "right", "top", "bottom"])
    if wall_side == "left":
        door_position = (0, random.randint(1, height - 2))  # Left wall, avoid corners
    elif wall_side == "right":
        door_position = (width - 1, random.randint(1, height - 2))  # Right wall
    elif wall_side == "top":
        door_position = (random.randint(1, width - 2), 0)  # Top wall
    else:
        door_position = (random.randint(1, width - 2), height - 1)  # Bottom wall

    room_objects[door_position] = "Locked Door"
    used_positions.add(door_position)  # Mark door position as used

    # Define the types of objects to be placed in various rooms
    object_types = ["Chest", "Torch Stand", "Cracked Wall"]

    # Randomly determine the number of objects to place (between 3 and 6 for variety)
    num_objects = random.randint(3, 6)

    # Place each object randomly within room boundaries, ensuring unique positions
    for _ in range(num_objects):
        obj_type = random.choice(object_types)

        # Generate unique position within room boundaries, avoiding the door location
        while True:
            x = random.randint(1, width - 2)  # Avoid wall edges for regular objects
            y = random.randint(1, height - 2)
            position = (x, y)
            if position not in used_positions:  # Ensure no overlap
                used_positions.add(position)
                room_objects[position] = obj_type
                break

    return room_size, room_objects