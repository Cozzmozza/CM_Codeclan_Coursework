import unittest

from src.guest import Guest

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest('Cozza')

    def test_guest_has_name(self): #Pass
        self.assertEqual('Cozza', self.guest.name)

# Tests We Want:
    # Test the guest has a name