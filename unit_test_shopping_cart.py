import unittest
from unittest.mock import patch, MagicMock, call
from shopping_cart import ShoppingCart

#TEST (in shell): python -m unittest unit_test_shopping_cart.py

'''
Test suite for the ShoppingCart class to verify correct functionality of
adding, removing, and printing the contents of the shopping cart.
'''

class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        """
        Set up the ShoppingCart instance before each test.
        Initializes a shopping cart and sets up a default item (prescription).
        """
        self.cart = ShoppingCart()
        self.prescription = {'Name': 'Aspirin', 'Price': '19.99'}

    def test_add_item_new(self):
        """
        Test adding a new item to the cart.
        Verifies that a new item is added correctly with the specified quantity and price.
        """
        self.cart.add_item(self.prescription, 2)
        self.assertIn('Aspirin', self.cart.items)
        self.assertEqual(self.cart.items['Aspirin']['quantity'], 2)
        self.assertEqual(self.cart.items['Aspirin']['price'], 19.99)

    def test_add_item_existing(self):
        """
        Test adding quantity to an existing item in the cart.
        Verifies that adding more of an existing item updates the quantity appropriately.
        """
        self.cart.add_item(self.prescription, 1)
        self.cart.add_item(self.prescription, 3)
        self.assertEqual(self.cart.items['Aspirin']['quantity'], 4)

    @patch('builtins.print')
    def test_print_receipt(self, mock_print):
        """
        Test the receipt printing functionality.
        Verifies that the receipt is printed correctly, including item details and totals.
        """
        self.cart.add_item(self.prescription, 1)
        self.cart.print_receipt()
        calls = [
            call('Receipt:'),
            call('========================================'),
            call('1 x Aspirin at $19.99 each: $19.99'),
            call('========================================'),
            call('Subtotal: $19.99'),
            call('Tax (8%): $1.60'),
            call('Total: $21.59')
        ]
        mock_print.assert_has_calls(calls, any_order=True)

    def test_remove_item(self):
        """
        Test removing an item or a quantity from the cart.
        Verifies that the specified quantity of an item is removed from the cart.
        """
        self.cart.add_item(self.prescription, 3)
        self.cart.remove_item(self.prescription, 1)
        self.assertEqual(self.cart.items['Aspirin']['quantity'], 2)

    def test_remove_item_entirely(self):
        """
        Test completely removing an item when its quantity goes to zero.
        Verifies that the item is completely removed from the cart if its quantity reaches zero.
        """
        self.cart.add_item(self.prescription, 1)
        self.cart.remove_item(self.prescription, 1)
        self.assertNotIn('Aspirin', self.cart.items)

    @patch('builtins.print')
    def test_remove_item_not_present(self, mock_print):
        """
        Test attempt to remove an item not in the cart.
        Verifies that attempting to remove a non-existent item triggers an appropriate error message.
        """
        self.cart.remove_item({'Name': 'Non-existent', 'Price': '10'}, 1)
        mock_print.assert_called_with("No Non-existent in the cart to remove.")

if __name__ == '__main__':
    unittest.main()