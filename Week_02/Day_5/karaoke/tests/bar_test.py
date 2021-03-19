import unittest

from src.bar import Bar
from src.song import Song
from src.guest import Guest
from src.room import Room

class TestBar(unittest.TestCase):
    def setUp(self):
        songs = {
            'Dark Side of the Moon' : 'Pink Floyd',
            'Beer' : 'Psychostick',
            'Black & White' : 'In Flames',
            'Hey Ya' : 'Outkast',
            'Firework' : 'Katy Perry',
            'Delete me' : 'ASAP'
            }
        room = Room(1, songs) #We are working with room 1, which has the songs above as default. The room also has an a guest list

        self.bar = Bar('Screeching Soul Tavern', room)

    def test_bar_has_name(self): #Pass
        self.assertEqual('Screeching Soul Tavern', self.bar.bar_name)

    def test_can_add_songs_to_room_song_list_using_Song(self): #Pass
        new_song_1 = Song('Paranoid', 'Ozzy Ozzy Ozzy')
        new_song_2 = Song('Walk', 'Pantera')
        self.bar.add_to_song_list(new_song_1)
        self.bar.add_to_song_list(new_song_2)
        self.assertEqual(8, len(self.bar.room.song_list))

    def test_can_remove_song_from_song_list_using_Song(self): #Pass
        unwanted_song_1 = Song('Firework', 'Katy Perry')
        unwanted_song_2 = Song('Delete me', 'ASAP')
        self.bar.remove_from_song_list(unwanted_song_1)
        self.bar.remove_from_song_list(unwanted_song_2)
        self.assertEqual(4, len(self.bar.room.song_list))

    def test_room_has_no_initial_guests(self): #Pass
        self.assertEqual([], self.bar.room.guest_list)

    def test_can_add__one_guest(self): #Pass
        guest = Guest('Cozza')
        self.bar.add_guest(guest)
        self.assertEqual(1, len(self.bar.room.guest_list))

    def test_can_add_upto_4_guests(self):
        guests = [Guest('Cozza'), Guest('Mozza'), Guest('Tozza'), Guest('Lozza')]
        for guest in guests:
            self.bar.add_guest(guest)
        self.assertEqual(4, len(self.bar.room.guest_list))
    
    def test_can_not_add_guests_if_full(self): #Pass
        guests = [Guest('Cozza'), Guest('Mozza'), Guest('Tozza'), Guest('Lozza'), Guest('Pozza')]
        for guest in guests:
            self.bar.add_guest(guest)
        self.assertEqual('Sorry, this room is at full capacity', self.bar.add_guest(guest))

    def test_can_remove_guest(self): #Pass
        guest = Guest('Cozza')
        self.bar.add_guest(guest) 
        self.bar.remove_guest(guest)
        self.assertEqual(0, len(self.bar.room.guest_list))
   