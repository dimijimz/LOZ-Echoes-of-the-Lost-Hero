# Define the size of the dungeon (room) and its objects
dungeon_size = {"width": 5, "height": 5}

# Objects in the room
room_objects = {
    (2, 1): "Chest",
    (2, 4): "Locked Door",
}
# Check players health (Alive or Dead)
def check_player_health(link):
    if link.health > 0:
        return True
    else:
        return False

def get_dungeon_size():
    return dungeon_size

def get_room_objects():
    return room_objects
