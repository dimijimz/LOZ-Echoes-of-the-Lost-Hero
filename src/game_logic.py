# Define the size and objects of each fixed room
def generate_fixed_room(room_number):
    # Predefined rooms for initial levels with only chest and door
    rooms = {
    1: {"width": 4, "height": 4, "objects": {(1, 1): "Chest", (3, 3): "Locked Door"}},
    2: {"width": 4, "height": 4, "objects": {(2, 2): "Chest", (2, 3): "Locked Door"}},
    3: {"width": 5, "height": 5, "objects": {(3, 3): "Chest", (2, 4): "Locked Door"}},
    4: {"width": 5, "height": 5, "objects": {(2, 2): "Chest", (4, 4): "Locked Door"}},
    5: {"width": 6, "height": 6, "objects": {(3, 3): "Chest", (5, 5): "Locked Door"}},  # Room 5 with Echo Lens upgrade
    6: {"width": 6, "height": 6, "objects": {(1, 1): "Chest", (5, 5): "Locked Door"}},
    7: {"width": 7, "height": 7, "objects": {(1, 1): "Chest", (6, 6): "Locked Door"}},
    8: {"width": 8, "height": 8, "objects": {(1, 1): "Chest", (7, 7): "Locked Door"}},
    9: {"width": 9, "height": 9, "objects": {(1, 1): "Chest", (8, 8): "Locked Door"}},
    10: {"width": 10, "height": 10, "objects": {(1, 1): "Chest", (9, 9): "Locked Door"}},
}

    
    # Return the selected room layout based on room number
    room = rooms.get(room_number, {"width": 6, "height": 6, "objects": {}})
    return {"width": room["width"], "height": room["height"], "objects": room["objects"]}
