# This will be the main app file
# This bar.py will choose to add/remove songs to a room, and check in/out guests from a room

class Bar:
    def __init__(self, bar_name, room):
        self.bar_name = bar_name
        self.room = room

    def add_to_song_list(self, song):
        self.room.song_list[song.title] = song.artist

    def remove_from_song_list(self, song):
        self.room.song_list.pop(song.title)
  
    def add_guest(self, guest):
        if len(self.room.guest_list) <= self.room.room_capacity:
            self.room.guest_list.append(guest)
            return f'The room currently contains {self.room.guest_list}'
        else:
            return 'Sorry, this room is at full capacity'

    def remove_guest(self, guest):
        self.room.guest_list.remove(guest)

        