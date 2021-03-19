class Room:
    def __init__(self, room_number, song_list):
        self.room_number = room_number
        self.song_list = song_list #We have an initial song list assigned to the room. This is a dictionary
        self.guest_list = [] #There are no guests initially
        self.room_capacity = 4 # The room capcity of all rooms is 4

        
