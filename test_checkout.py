import unittest

from checkout import Checkout


class CheckoutTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.checkout = Checkout()

    def tearDown(self):
        self.checkout.clear()

    def test_checkout_clear(self):
        self.checkout.calculate('A')
        self.assertNotEqual(self.checkout, Checkout())

        self.checkout.clear()
        self.assertEqual(self.checkout, Checkout())

    def test_checkout_for_invalid_item(self):
        total = self.checkout.calculate('A')
        self.assertEqual(total, 50)

        new_total = self.checkout.calculate('Z')
        self.assertEqual(new_total, total)

    def test_checkout_for_item_A(self):
        total = self.checkout.calculate('A')
        self.assertEqual(total, 50)

        total = self.checkout.calculate('A')
        self.assertEqual(total, 100)

        total = self.checkout.calculate('A')
        self.assertEqual(total, 130)

        total = self.checkout.calculate('A')
        self.assertEqual(total, 180)

    # TODO finish tests
