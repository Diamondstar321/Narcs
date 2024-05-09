from unittest.mock import patch, mock_open, call
import unittest
from order import Order
from shopping_cart import ShoppingCart

#TEST (in shell): python -m unittest unit_test_order.py

'''
Test suite for verifying the Order class's functionality related to saving orders to a CSV-based database.
'''

class TestOrder(unittest.TestCase):
    def setUp(self):
        """
        Set up test fixtures for each test method.
        Initializes an Order instance with a predefined set of attributes and a ShoppingCart object.
        """
        self.order = Order(
            name="John Doe", 
            orderNumber=123, 
            shoppingCart=ShoppingCart(), 
            deliveryDate="2024-04-26", 
            shippingAddress="123 Elm St", 
            status="Pending"
        )

    @patch('csv.DictWriter')
    @patch('builtins.open', new_callable=mock_open)
    def test_save_to_order_database(self, mocked_file, mock_writer):
        """
        Test the saving of an order to the order database.
        Verifies that the file is opened correctly for both reading and appending,
        checks the appropriate write operations are performed,
        and ensures headers and row data are correctly written to the file.
        """
        self.order.save_to_order_database()
        calls = [
            call('order_database.csv', 'r', newline=''),
            call('order_database.csv', 'a', newline='')
        ]
        mocked_file.assert_has_calls(calls, any_order=True)
        self.assertTrue(mock_writer.return_value.writeheader.called)
        self.assertTrue(mock_writer.return_value.writerow.called)

if __name__ == "__main__":
    unittest.main()
