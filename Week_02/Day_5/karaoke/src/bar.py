class Bar:
    def __init__(self, bar_name, room, till_cash):
        self.bar_name = bar_name
        self.room = room
        self.till_cash = till_cash

    def add_to_song_list(self, song):
        self.room.song_list[song.title] = song.artist

    def remove_from_song_list(self, song):
        self.room.song_list.pop(song.title)
  
    def add_guest(self, guest):
        if len(self.room.guest_list) <= self.room.room_capacity:
            self.room.guest_list.append(guest)
        else:
            return 'Sorry, this room is at full capacity'

    def remove_guest(self, guest):
        self.room.guest_list.remove(guest)

    def remove_cash_from_guest(self, guest):
        guest.remove_cash_from_wallet(self.room.room_cost)

    def add_cash_to_till_by_one_sale(self):
        self.till_cash += self.room.room_cost

    def remove_from_till(self, amount):
        self.till_cash -= amount

    def sell_to_group_of_guests(self, guests):
        for guest in guests:
            self.remove_cash_from_guest(guest)
            self.add_cash_to_till_by_one_sale()
            self.add_guest(guest)
