import unittest

from src.guest import Guest

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest('Cozza', 18.50)

    def test_guest_has_name(self): #Pass
        self.assertEqual('Cozza', self.guest.name)

    def test_guest_has_wallet_balance(self): #Pass
        self.assertEqual(18.50, self.guest.wallet_balance)

    def test_guest_can_remove_cash_from_wallet(self): #Pass
        self.guest.remove_cash_from_wallet(10.00)
        self.assertEqual(8.50, self.guest.wallet_balance)
